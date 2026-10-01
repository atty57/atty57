#!/usr/bin/env python3
"""Draw a GitHub contribution calendar as an isometric night skyline.

One building per day of the last year: taller and brighter for busier days, an
empty plot for a day with nothing. The palette, fonts and motifs follow the
profile's other assets (assets/hero.svg, assets/moonlight.svg).

Data comes from the GitHub GraphQL API, which needs a token in GH_TOKEN or
GITHUB_TOKEN. Any token reads public contributions; a personal access token
with the read:user scope also picks up private ones, provided "Include private
contributions on my profile" is enabled in your GitHub profile settings.

  python contribution_city.py --login atty57 --out assets/contribution-city.svg
  python contribution_city.py --sample --out /tmp/preview.svg   # offline preview

Standard library only, so the workflow needs no pip install.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone

# ---------------------------------------------------------------- palette ----
# Lifted from assets/hero.svg and assets/moonlight.svg so the city sits in the
# same night as the rest of the README.
BG_TOP = "#0B0A18"
BG_BOTTOM = "#09080F"
PURPLE = "#7C5CFF"
CYAN = "#22D3EE"
LAVENDER = "#B9A8FF"
MOON_LIGHT = "#F4F1FF"
TEXT_DIM = "#A9A6C4"
TEXT_FAINT = "#5F5B82"
PLOT_FILL = "#101026"
PLOT_EDGE = "#211D3D"

# roof / left face / right face, from quietest to busiest day
TIERS = [
    ("#3A2F7A", "#261D56", "#1B1440"),
    ("#4F3CAE", "#352782", "#241A61"),
    ("#6A4FE0", "#4A34AC", "#33247F"),
    ("#8E72FF", "#6248D6", "#4631A3"),
]
PEAK = ("#22D3EE", "#1799B4", "#0E6B82")

# ---------------------------------------------------------------- geometry ---
WIDTH = 1200
HEIGHT = 600
HALF_H = 4          # tile half-depth: a flattened isometric, so 53 weeks fit
BASE_Y = 300        # screen y of the back corner of the grid; the header's
                    # stat pill ends at y=166, and the tallest tower on the
                    # back corner reaches BASE_Y - HALF_H - H_MAX, so keep
                    # BASE_Y above 166 + H_MAX + HALF_H or they collide
H_MIN = 7           # a one-contribution day still gets a shed
H_MAX = 118
H_GAMMA = 0.62      # compresses the tallest towers so the rest stay readable

GRAPHQL_URL = "https://api.github.com/graphql"
QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_calendar(login: str, token: str) -> list[tuple[date, int]]:
    """Return [(day, count)] for the last 365 days, oldest first."""
    to_dt = datetime.now(timezone.utc)
    from_dt = to_dt - timedelta(days=364)
    body = json.dumps(
        {
            "query": QUERY,
            "variables": {
                "login": login,
                "from": from_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "to": to_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
            },
        }
    ).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "contribution-city",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:400]
        raise RuntimeError(f"GitHub API returned HTTP {exc.code}: {detail}") from exc

    if payload.get("errors"):
        raise RuntimeError("GitHub API errors: " + json.dumps(payload["errors"]))
    user = (payload.get("data") or {}).get("user")
    if not user:
        raise RuntimeError(
            f"no contribution calendar came back for login {login!r} — check the "
            "login and that the token is valid"
        )

    days: list[tuple[date, int]] = []
    for week in user["contributionsCollection"]["contributionCalendar"]["weeks"]:
        for day in week["contributionDays"]:
            days.append((date.fromisoformat(day["date"]), int(day["contributionCount"])))
    days.sort()
    return days


def sample_calendar() -> list[tuple[date, int]]:
    """A synthetic year, for checking the drawing without network access."""
    today = date.today()
    start = today - timedelta(days=364)
    days = []
    for i in range(365):
        day = start + timedelta(days=i)
        r = _noise(day.isoformat(), 3)
        weekend = day.isoweekday() >= 6
        base = 2.0 + 9.0 * (i / 364.0)            # busier towards the present
        if weekend:
            base *= 0.35
        count = 0 if r[0] < (0.34 if weekend else 0.16) else int(base * (0.2 + 2.4 * r[1] ** 2))
        if r[2] > 0.995:
            count += 28                            # the occasional all-nighter
        days.append((day, count))
    return days


# ------------------------------------------------------------------ helpers --
def _noise(seed: str, n: int) -> list[float]:
    """Deterministic pseudo-randomness, so a redraw of the same data is byte
    identical and the daily commit only moves what actually changed."""
    h = 2166136261
    for ch in seed:
        h = ((h ^ ord(ch)) * 16777619) & 0xFFFFFFFF
    out = []
    for _ in range(n):
        h = (h * 1664525 + 1013904223) & 0xFFFFFFFF
        out.append(h / 0xFFFFFFFF)
    return out


def num(value: float) -> str:
    """Short coordinate: drop the decimal when it buys nothing."""
    r = round(value, 1)
    return str(int(r)) if r == int(r) else str(r)


def quartiles(counts: list[int]) -> tuple[int, int, int]:
    s = sorted(counts)
    if not s:
        return 0, 0, 0

    def at(p: float) -> int:
        return s[min(len(s) - 1, max(0, round(p * (len(s) - 1))))]

    return at(0.25), at(0.50), at(0.75)


def streaks(days: list[tuple[date, int]]) -> tuple[int, int]:
    """(current, longest) run of consecutive days with at least one contribution."""
    longest = run = 0
    for _, count in days:
        run = run + 1 if count else 0
        longest = max(longest, run)

    current = 0
    today = days[-1][0]
    for day, count in reversed(days):
        if count == 0:
            # today may simply not have happened yet; anything older breaks it
            if day == today:
                continue
            break
        current += 1
    return current, longest


# ------------------------------------------------------------------ drawing --
def face(points: list[tuple[float, float]], fill: str) -> str:
    pts = " ".join(f"{num(x)},{num(y)}" for x, y in points)
    return f'<polygon points="{pts}" fill="{fill}"/>'


def building(cx: float, cy: float, half_w: float, height: float, tier) -> str:
    """Three faces of an isometric box standing on the tile at (cx, cy)."""
    roof, left, right = tier
    hw, hh, h = half_w, HALF_H, height
    out = [
        # left face, then right, then the roof on top of both
        face([(cx - hw, cy), (cx, cy + hh), (cx, cy + hh - h), (cx - hw, cy - h)], left),
        face([(cx, cy + hh), (cx + hw, cy), (cx + hw, cy - h), (cx, cy + hh - h)], right),
        face(
            [(cx, cy - hh - h), (cx + hw, cy - h), (cx, cy + hh - h), (cx - hw, cy - h)],
            roof,
        ),
    ]
    return "".join(out)


def windows(cx: float, cy: float, half_w: float, height: float, seed: str) -> list[str]:
    """Lit windows down the left face, so the skyline reads as a city at night."""
    if height < 26:
        return []
    floors = min(3, int(height // 26))
    rolls = _noise(seed + "w", floors * 3)
    out = []
    for f in range(floors):
        if rolls[f * 3] < 0.32:
            continue  # a dark floor
        # v runs 0 at street level to 1 at the roof
        v0 = 0.18 + f * (0.62 / max(1, floors))
        vh = min(0.12, 9.0 / height)
        u0 = 0.18 + 0.46 * rolls[f * 3 + 1]
        uw = 0.26
        warm = rolls[f * 3 + 2] > 0.3
        fill = "#FFE3A3" if warm else CYAN
        op = ".55" if warm else ".45"
        pts = []
        for u, v in ((u0, v0), (u0 + uw, v0), (u0 + uw, v0 + vh), (u0, v0 + vh)):
            pts.append((cx - half_w + u * half_w, cy + u * HALF_H - v * height))
        joined = " ".join(f"{num(x)},{num(y)}" for x, y in pts)
        out.append(f'<polygon points="{joined}" fill="{fill}" fill-opacity="{op}"/>')
    return out


def render(days: list[tuple[date, int]], login: str) -> str:
    total = sum(c for _, c in days)
    nonzero = [c for _, c in days if c]
    active = len(nonzero)
    peak_day, peak_count = max(days, key=lambda d: (d[1], d[0]))
    q1, q2, q3 = quartiles(nonzero)
    current, longest = streaks(days)

    first = days[0][0]
    origin = first - timedelta(days=first.isoweekday() % 7)  # the Sunday column starts
    cols = (days[-1][0] - origin).days // 7 + 1

    # widest tile that still leaves a margin: the diamond spans (cols-1)+6 steps
    half_w = max(6, min(19, 1096 // (cols + 5)))
    span = (cols - 1 + 6) * half_w
    origin_x = (WIDTH - span) / 2 + 6 * half_w

    def place(day: date) -> tuple[float, float]:
        col = (day - origin).days // 7
        row = day.isoweekday() % 7
        return origin_x + (col - row) * half_w, BASE_Y + (col + row) * HALF_H

    def tier_of(day: date, count: int):
        # exactly one building wears the accent, even if other days tie on count
        if day == peak_day:
            return PEAK
        if count <= q1:
            return TIERS[0]
        if count <= q2:
            return TIERS[1]
        if count <= q3:
            return TIERS[2]
        return TIERS[3]

    # painter's algorithm: far tiles (small col+row) first, near ones last
    plots: list[str] = []
    towers: list[str] = []
    lights: list[str] = []
    beacon = ""
    for day, count in sorted(days, key=lambda d: ((d[0] - origin).days // 7) + d[0].isoweekday() % 7):
        cx, cy = place(day)
        if count == 0:
            pts = [(cx, cy - HALF_H), (cx + half_w, cy), (cx, cy + HALF_H), (cx - half_w, cy)]
            joined = " ".join(f"{num(x)},{num(y)}" for x, y in pts)
            plots.append(
                f'<polygon points="{joined}" fill="{PLOT_FILL}" stroke="{PLOT_EDGE}" stroke-width=".6"/>'
            )
            continue
        # heights are relative to the busiest day, with a floor on the
        # reference so a near-empty year doesn't grow skyscrapers off a peak of 1
        height = H_MIN + (count / max(peak_count, 8)) ** H_GAMMA * (H_MAX - H_MIN)
        towers.append(building(cx, cy, half_w, height, tier_of(day, count)))
        lights.extend(windows(cx, cy, half_w, height, day.isoformat()))
        if day == peak_day:
            top = cy - HALF_H - height
            beacon = (
                f'<g><line x1="{num(cx)}" y1="{num(top)}" x2="{num(cx)}" y2="{num(top - 20)}" '
                f'stroke="{CYAN}" stroke-width="1" stroke-opacity=".5"/>'
                f'<circle class="beacon" cx="{num(cx)}" cy="{num(top - 24)}" r="2.6" fill="{CYAN}"/></g>'
            )

    pill = (
        f"peak {peak_count} on {peak_day:%b} {peak_day.day} · streak {current}d"
        f" · longest {longest}d · active {active} days"
    )
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # bottom left, in the open ground the diagonal band leaves behind
    legend = "".join(
        building(126 + i * 26, 554, 9, 6 + i * 7, tier) for i, tier in enumerate(TIERS)
    )

    css = """
    .sans { font-family: ui-sans-serif, -apple-system, "Segoe UI", Inter, Roboto, Helvetica, Arial, sans-serif; }
    .mono { font-family: ui-monospace, SFMono-Regular, "JetBrains Mono", Menlo, Consolas, monospace; }
    .star { animation: twinkle 3s ease-in-out infinite; }
    .s2 { animation-delay: .7s; } .s3 { animation-delay: 1.4s; } .s4 { animation-delay: 2.1s; }
    .halo { animation: breathe 6s ease-in-out infinite; transform-origin: 1086px 84px; }
    .beacon { animation: pulse 2.2s ease-in-out infinite; }
    @keyframes twinkle { 0%,100% { opacity: .2; } 50% { opacity: 1; } }
    @keyframes breathe { 0%,100% { opacity: .3; transform: scale(1); } 50% { opacity: .55; transform: scale(1.07); } }
    @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: .25; } }
    @media (prefers-reduced-motion: reduce) {
      .star, .halo, .beacon { animation: none; }
    }
    """

    desc = (
        f"An isometric night skyline built from {login}'s GitHub contributions: one "
        f"building per day of the last year, taller and brighter for busier days. "
        f"{total:,} contributions across {active} active days, busiest on "
        f"{peak_day.isoformat()} with {peak_count}."
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" role="img" aria-labelledby="cc-title cc-desc">
<title id="cc-title">Contribution city</title>
<desc id="cc-desc">{desc}</desc>
<style>{css}</style>
<defs>
  <clipPath id="cc-card"><rect width="{WIDTH}" height="{HEIGHT}" rx="24"/></clipPath>
  <linearGradient id="cc-sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{BG_TOP}"/><stop offset="1" stop-color="{BG_BOTTOM}"/>
  </linearGradient>
  <linearGradient id="cc-name" x1="0" x2="1">
    <stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="{LAVENDER}"/>
  </linearGradient>
  <pattern id="cc-grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".05"/>
  </pattern>
  <radialGradient id="cc-fade" cx="50%" cy="20%" r="75%">
    <stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <mask id="cc-gridmask"><rect width="{WIDTH}" height="{HEIGHT}" fill="url(#cc-fade)"/></mask>
  <filter id="cc-blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <mask id="cc-crescent">
    <circle cx="1086" cy="84" r="30" fill="#fff"/>
    <circle cx="1100" cy="74" r="26" fill="#000"/>
  </mask>
  <linearGradient id="cc-moon" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{MOON_LIGHT}"/><stop offset="1" stop-color="{LAVENDER}"/>
  </linearGradient>
</defs>

<g clip-path="url(#cc-card)">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#cc-sky)"/>
  <circle cx="200" cy="40" r="180" fill="{PURPLE}" fill-opacity=".5" filter="url(#cc-blur)"/>
  <circle cx="1060" cy="600" r="170" fill="{CYAN}" fill-opacity=".3" filter="url(#cc-blur)"/>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#cc-grid)" mask="url(#cc-gridmask)"/>

  <circle class="halo" cx="1086" cy="84" r="66" fill="{PURPLE}" filter="url(#cc-blur)"/>
  <rect x="1020" y="18" width="132" height="132" fill="url(#cc-moon)" mask="url(#cc-crescent)"/>
  <g fill="#fff">
    <circle class="star" cx="880" cy="44" r="1.8"/>
    <circle class="star s2" cx="968" cy="106" r="1.4"/>
    <circle class="star s3" cx="1162" cy="52" r="1.6"/>
    <circle class="star s4" cx="820" cy="96" r="1.3"/>
    <circle class="star s2" cx="1150" cy="132" r="1.5"/>
    <circle class="star s3" cx="744" cy="40" r="1.4"/>
  </g>

  <text x="64" y="54" class="mono" font-size="14" letter-spacing="2.5" fill="{LAVENDER}">CONTRIBUTION CITY · LAST 365 DAYS</text>
  <text x="62" y="108" class="sans" fill="url(#cc-name)"><tspan font-size="52" font-weight="700" letter-spacing="-1">{total:,}</tspan><tspan font-size="22" font-weight="400" fill="{TEXT_DIM}"> contributions</tspan></text>

  <rect x="52" y="128" width="624" height="38" rx="19" fill="#fff" fill-opacity=".05" stroke="#fff" stroke-opacity=".1"/>
  <circle cx="72" cy="147" r="4" fill="{PURPLE}"/>
  <text x="88" y="152" class="mono" font-size="14" fill="#D6D8E1">{pill}</text>

  <ellipse cx="620" cy="548" rx="450" ry="40" fill="{PURPLE}" fill-opacity=".1" filter="url(#cc-blur)"/>

  <g>{"".join(plots)}</g>
  <g>{"".join(towers)}</g>
  <g>{"".join(lights)}</g>
  {beacon}

  <text x="64" y="552" class="mono" font-size="12" fill="{TEXT_FAINT}">quiet</text>
  <g>{legend}</g>
  <text x="236" y="552" class="mono" font-size="12" fill="{TEXT_FAINT}">busy</text>
  <text x="64" y="578" class="mono" font-size="12" fill="{TEXT_FAINT}">one building per day · height and colour track that day's contributions · redrawn {stamp}</text>
</g>
</svg>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--login", default=os.environ.get("GITHUB_LOGIN", ""))
    ap.add_argument("--out", required=True)
    ap.add_argument("--sample", action="store_true", help="draw synthetic data, no network")
    args = ap.parse_args()

    if args.sample:
        days = sample_calendar()
        login = args.login or "sample"
    else:
        if not args.login:
            print("error: pass --login or set GITHUB_LOGIN", file=sys.stderr)
            return 2
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token:
            print("error: set GH_TOKEN or GITHUB_TOKEN", file=sys.stderr)
            return 2
        days = fetch_calendar(args.login, token)
        login = args.login

    if not days:
        print("error: the calendar came back empty", file=sys.stderr)
        return 1

    svg = render(days, login)
    directory = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(directory, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(svg)

    total = sum(c for _, c in days)
    print(f"{args.out}: {len(days)} days, {total:,} contributions, {len(svg):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
