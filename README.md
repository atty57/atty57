<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:00d4ff&height=190&section=header&text=ATHARVA%20VICHARE&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=agents%20%C2%B7%20LLMs%20%C2%B7%20open%20source&descAlignY=58&descSize=16" width="100%" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=2800&pause=700&color=00D4FF&center=true&vCenter=true&width=640&lines=%3E+booting+atharva.exe+...;%3E+loading+agents+%2F+RAG+%2F+LLMs+...;%3E+shipping+fixes+to+microsoft%2Fagent-framework" alt="typing intro" />

</div>

### 👋 Hi, I'm Atharva Vichare!
I'm a software developer with a passion for building efficient, scalable solutions. My expertise spans backend engineering, cloud computing, and AI-driven technologies. I enjoy tackling complex problems and continually learning new skills to build impactful software.

---

## 🛰️ Open Source // Transmission Log

```text
> target   : microsoft/agent-framework   (Microsoft's SDK for AI agents & multi-agent workflows)
> runtime  : Python + .NET
> status   : 5 merged  ·  6 in review
> focus    : human-in-the-loop tool approval · AG-UI / A2A protocol interop · memory · observability
```

I work where agents meet the real world: the approval loops, protocol adapters and state handoffs where things quietly break.

### ✅ Merged into `main`

| PR | Stack | Anomaly detected → resolution |
|---|---|---|
| [#7271](https://github.com/microsoft/agent-framework/pull/7271) |  Python | **Double execution on approval.** After a human approved a tool call, the round-trip ran the function a second time. Fixed so an approved call runs exactly once. |
| [#7474](https://github.com/microsoft/agent-framework/pull/7474) |  .NET | **Unbounded auto-approval loop.** Put a hard bound on the tool-approval auto-approval loop so an agent can't spin without limit. |
| [#7635](https://github.com/microsoft/agent-framework/pull/7635) |  Python | **Broken memory provider.** The Cosmos DB memory provider was still calling a renamed `add_cosmos` toolkit API; rewired it to the current one. |
| [#7655](https://github.com/microsoft/agent-framework/pull/7655) |  Python | **Lost attachments over AG-UI.** File attachments were silently dropped when the URL arrived in `source.value`; they now make it through. |
| [#7951](https://github.com/microsoft/agent-framework/pull/7951) |  Python | **Crash on shutdown.** `A2AAgent` threw an `AttributeError` on exit when the caller supplied their own `http_client`; fixed the teardown path. |

### 🔄 In orbit (open for review)

| PR | Stack | Mission |
|---|---|---|
| [#8665](https://github.com/microsoft/agent-framework/pull/8665) |  Python | Correct tool-argument validation for `datetime`, `set` and `tuple` parameters |
| [#8465](https://github.com/microsoft/agent-framework/pull/8465) |  .NET | Fix AG-UI `Unknown chat role: reasoning` error on follow-up turns |
| [#8265](https://github.com/microsoft/agent-framework/pull/8265) |  .NET | Preserve the agent continuation token when wrapped with `UseOpenTelemetry` |
| [#8018](https://github.com/microsoft/agent-framework/pull/8018) |  .NET | Surface the real workflow exception instead of a JSON serialization error |
| [#7920](https://github.com/microsoft/agent-framework/pull/7920) |  .NET | Stop AG-UI SSE events from being written with explicit `null`s |

<p align="left">
<a href="https://github.com/microsoft/agent-framework/pulls?q=is%3Apr+author%3Aatty57+is%3Amerged"><img src="https://img.shields.io/badge/view_merged_PRs-00D4FF?style=for-the-badge&logo=github&logoColor=black" /></a>
<a href="https://github.com/microsoft/agent-framework/pulls?q=is%3Apr+author%3Aatty57"><img src="https://img.shields.io/badge/all_contributions-302B63?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

## 🛠️ Skills & Tools
### 💻 Languages & Frameworks
<p align="left"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" /> <img src="https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" /> <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white" /> </p>

### ☁️ Cloud & Infrastructure
<p align="left"> <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" /> <img src="https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" /> <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" /> <img src="https://img.shields.io/badge/Azure%20DevOps-0078D7?style=for-the-badge" /> <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" /> <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" /> </p>

### 🧠 Machine Learning & AI
<p align="left"> <img src="https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=mlflow&logoColor=white" /> <img src="https://img.shields.io/badge/Deep%20Learning-FF0000?style=for-the-badge&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" /> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white" /> <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" /> <img src="https://img.shields.io/badge/QLoRA%20%2F%20Unsloth-6E40C9?style=for-the-badge" /> <img src="https://img.shields.io/badge/Reinforcement%20Learning-8A2BE2?style=for-the-badge" /> <img src="https://img.shields.io/badge/Unity-000000?style=for-the-badge&logo=unity&logoColor=white" /> </p>

### 🤖 GenAI & Agentic Systems
<p align="left"> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/Microsoft%20Agent%20Framework-5E5E5E?style=for-the-badge" /> <img src="https://img.shields.io/badge/Google%20ADK-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" /> <img src="https://img.shields.io/badge/Vertex%20AI-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" /> <img src="https://img.shields.io/badge/AWS%20Bedrock-FF9900?style=for-the-badge" /> <img src="https://img.shields.io/badge/LiteLLM-2B2B2B?style=for-the-badge" /> <img src="https://img.shields.io/badge/RAG-0A66C2?style=for-the-badge" /> <img src="https://img.shields.io/badge/Qdrant-DC244C?style=for-the-badge&logo=qdrant&logoColor=white" /> <img src="https://img.shields.io/badge/ChromaDB-FF6446?style=for-the-badge" /> <img src="https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white" /> </p>

### 📚 Familiar with LLMs
<p align="left"> <img src="https://img.shields.io/badge/GPT-005571?style=for-the-badge&logo=openai&logoColor=white" /> <img src="https://img.shields.io/badge/BERT-1F425F?style=for-the-badge&logo=google&logoColor=white" /> <img src="https://img.shields.io/badge/LLaMA-FF4500?style=for-the-badge&logo=meta&logoColor=white" /> <img src="https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white" /> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" /> <img src="https://img.shields.io/badge/Qwen-615CED?style=for-the-badge" /> </p>

---

## 🚀 Interests
- Building scalable backend systems.
- Developing cloud-native applications.
- Exploring Large Language Models (LLMs) and their applications.

---

## 📫 Connect With Me!
Feel free to connect - I'm always excited to collaborate or discuss interesting projects!

<a href="https://www.linkedin.com/in/atharva-vichare-68739a213"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>

Linkedin - https://www.linkedin.com/in/atharva-vichare-68739a213

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,50:302b63,100:0f0c29&height=110&section=footer" width="100%" />
