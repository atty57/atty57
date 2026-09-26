<p align="center">
  <img src="assets/hero.svg" width="100%" alt="Atharva Vichare, GenAI / ML Engineer: agents, RAG and open source" />
</p>

<p align="center">
  <a href="https://github.com/atty57/moonlight"><img src="https://img.shields.io/badge/☾_moonlight-v0.1-7C5CFF?style=flat-square&labelColor=0A0B10" /></a>
  <a href="https://www.linkedin.com/in/atharva-vichare-68739a213"><img src="https://img.shields.io/badge/LinkedIn-connect-0A66C2?style=flat-square&labelColor=0A0B10&logo=linkedin" /></a>
  <a href="https://portfolio-atty57s-projects.vercel.app"><img src="https://img.shields.io/badge/portfolio-visit-22D3EE?style=flat-square&labelColor=0A0B10&logo=vercel" /></a>
</p>

### 👋 Hi, I'm Atharva Vichare!
I'm a software developer with a passion for building efficient, scalable solutions. My expertise spans backend engineering, cloud computing, and AI-driven technologies. I enjoy tackling complex problems and continually learning new skills to build impactful software.

<br />

## 🌙 Moonlight

<a href="https://github.com/atty57/moonlight"><img src="assets/moonlight.svg" width="100%" alt="Moonlight: give your leftover AI usage a night job" /></a>

Your weekly Claude usage resets on a fixed day, and whatever you haven't used is gone. **Moonlight** is a Claude Code plugin that spends it on your backlog: on the last night before the reset, a cloud agent works through your task queue while you sleep and leaves **draft pull requests** for the morning.

| | |
|---|---|
| **Queue anything** | `/moonlight:add <task>` for code, or research and writing with `repo: none` |
| **Runs in the cloud** | Scheduled as cloud routines inside your sleep window, so your laptop can be off |
| **Safe by default** | Works on its own branches, opens draft PRs only, never merges |
| **Loses nothing** | Pushes after every step, so hitting the usage limit never loses work |

```text
/plugin marketplace add atty57/moonlight
/plugin install moonlight@moonlight
/moonlight:setup
```


<br />

## 🛰️ Open Source · `microsoft/agent-framework`

Microsoft's SDK for building AI agents and multi-agent workflows in **Python** and **.NET**. I work where agents meet the real world: the approval loops, protocol adapters and state handoffs where things quietly break.

> [!NOTE]
> **Focus:** human-in-the-loop tool approval · AG-UI / A2A protocol interop · memory · observability

#### ✅ Merged

| PR | Stack | What broke → what I fixed |
|---|---|---|
| [#7271](https://github.com/microsoft/agent-framework/pull/7271) | Python | **Double execution on approval.** After a human approved a tool call, the round-trip ran the function a second time. Now an approved call runs exactly once. |
| [#7474](https://github.com/microsoft/agent-framework/pull/7474) | .NET | **Unbounded auto-approval loop.** Put a hard bound on the tool-approval auto-approval loop so an agent can't spin without limit. |
| [#7635](https://github.com/microsoft/agent-framework/pull/7635) | Python | **Broken memory provider.** The Cosmos DB memory provider was still calling a renamed `add_cosmos` toolkit API; rewired it to the current one. |
| [#7655](https://github.com/microsoft/agent-framework/pull/7655) | Python | **Lost attachments over AG-UI.** File attachments were silently dropped when the URL arrived in `source.value`; they now make it through. |
| [#7951](https://github.com/microsoft/agent-framework/pull/7951) | Python | **Crash on shutdown.** `A2AAgent` threw an `AttributeError` on exit when the caller supplied their own `http_client`; fixed the teardown path. |

#### 🔄 In review

| PR | Stack | Change |
|---|---|---|
| [#8665](https://github.com/microsoft/agent-framework/pull/8665) | Python | Correct tool-argument validation for `datetime`, `set` and `tuple` parameters |
| [#8465](https://github.com/microsoft/agent-framework/pull/8465) | .NET | Fix AG-UI `Unknown chat role: reasoning` error on follow-up turns |
| [#8265](https://github.com/microsoft/agent-framework/pull/8265) | .NET | Preserve the agent continuation token when wrapped with `UseOpenTelemetry` |
| [#8018](https://github.com/microsoft/agent-framework/pull/8018) | .NET | Surface the real workflow exception instead of a JSON serialization error |
| [#7920](https://github.com/microsoft/agent-framework/pull/7920) | .NET | Stop AG-UI SSE events from being written with explicit `null`s |

<a href="https://github.com/microsoft/agent-framework/pulls?q=is%3Apr+author%3Aatty57"><img src="https://img.shields.io/badge/all_my_PRs_→-7C5CFF?style=flat-square&logo=github&labelColor=0A0B10" /></a>

<br />

## 🛠️ Skills & Tools

**💻 Languages & Frameworks**
<p align="left"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" /> <img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white" /> </p>

**☁️ Cloud & Infrastructure**
<p align="left"> <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white" /> <img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=google-cloud&logoColor=white" /> <img src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" /> <img src="https://img.shields.io/badge/Azure%20DevOps-0078D7?style=flat-square" /> <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" /> <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" /> </p>

**🧠 Machine Learning & AI**
<p align="left"> <img src="https://img.shields.io/badge/Machine%20Learning-FF6F00?style=flat-square&logo=mlflow&logoColor=white" /> <img src="https://img.shields.io/badge/Deep%20Learning-FF0000?style=flat-square&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" /> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" /> <img src="https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white" /> <img src="https://img.shields.io/badge/QLoRA%20%2F%20Unsloth-6E40C9?style=flat-square" /> <img src="https://img.shields.io/badge/Reinforcement%20Learning-8A2BE2?style=flat-square" /> <img src="https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white" /> </p>

**🤖 GenAI & Agentic Systems**
<p align="left"> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/Microsoft%20Agent%20Framework-5E5E5E?style=flat-square" /> <img src="https://img.shields.io/badge/Google%20ADK-4285F4?style=flat-square&logo=googlecloud&logoColor=white" /> <img src="https://img.shields.io/badge/Vertex%20AI-4285F4?style=flat-square&logo=googlecloud&logoColor=white" /> <img src="https://img.shields.io/badge/AWS%20Bedrock-FF9900?style=flat-square" /> <img src="https://img.shields.io/badge/LiteLLM-2B2B2B?style=flat-square" /> <img src="https://img.shields.io/badge/RAG-0A66C2?style=flat-square" /> <img src="https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white" /> <img src="https://img.shields.io/badge/ChromaDB-FF6446?style=flat-square" /> <img src="https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white" /> </p>

**📚 Familiar with LLMs**
<p align="left"> <img src="https://img.shields.io/badge/GPT-005571?style=flat-square&logo=openai&logoColor=white" /> <img src="https://img.shields.io/badge/BERT-1F425F?style=flat-square&logo=google&logoColor=white" /> <img src="https://img.shields.io/badge/LLaMA-FF4500?style=flat-square&logo=meta&logoColor=white" /> <img src="https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=claude&logoColor=white" /> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" /> <img src="https://img.shields.io/badge/Qwen-615CED?style=flat-square" /> </p>

<br />

## 🚀 Interests
- Building scalable backend systems.
- Developing cloud-native applications.
- Exploring Large Language Models (LLMs) and their applications.

## 📫 Connect With Me!
Feel free to connect - I'm always excited to collaborate or discuss interesting projects!

Linkedin - https://www.linkedin.com/in/atharva-vichare-68739a213

<br />

<p align="center"><sub>☾ built by day · shipped by night</sub></p>
