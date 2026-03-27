GuardianBot is a lightweight, modular system‑monitoring agent designed to collect machine metrics and send them to a central AI‑powered incident assistant.
The goal is to build a real SRE‑style monitoring agent with:

Clean, scalable architecture

Modular metric collectors

A simple agent loop

JSON payload output

Future cloud deployment (Docker → Kubernetes → Terraform)

AI‑assisted analysis and alerting

This project is intentionally built step‑by‑step, with full awareness of every decision.

📂 Project Structure
Code
guardianbot/
│
├── agent/
│   ├── __init__.py
│   ├── main.py                # Agent entry point (to be created)
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── cpu.py             # CPU metric collector (completed)
│   │   ├── memory.py          # Memory collector (planned)
│   │   ├── disk.py            # Disk collector (planned)
│   │   ├── network.py         # Network collector (planned)
│   │   └── system.py          # System info collector (planned)
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py          # Logging utilities (planned)
│   │   └── helpers.py         # Shared helper functions (planned)
│   └── config.py              # Configuration settings (planned)
│
├── tests/
│   ├── test_cpu.py            # Unit tests (planned)
│   ├── test_memory.py
│   └── ...
│
├── requirements.txt
└── README.md
This structure mirrors real monitoring agents (Datadog, New Relic, Prometheus exporters).

🧩 Current Implementation
✔ CPU Metric Collector
File: agent/metrics/cpu.py

python
from psutil import cpu_percent

def collect_cpu():
    return cpu_percent(interval=1)
Uses psutil.cpu_percent(interval=1)

Returns a float

Designed to plug directly into the agent’s JSON payload

This is the template for all future metric collectors.

🔄 Agent Loop (Planned)
The agent will:

Collect metrics from each module

Assemble them into a JSON payload

Print or send the payload

Sleep for 2 seconds

Repeat

This logic will live in main.py.

📊 Metrics to Implement Next
Each metric will follow the same pattern as CPU:

Memory
RAM usage

Swap usage

Disk
Disk usage

Disk I/O

Network
Upload / download bytes

Network I/O

System
Hostname

Uptime

OS info

Each will be implemented in its own file under agent/metrics/.

🧠 Design Philosophy
GuardianBot is built with:

Modularity
Each metric lives in its own file.
Easy to test, easy to extend.

Simplicity
Each collector returns a single value or dictionary.
No unnecessary complexity.

Scalability
The architecture is ready for:

Docker

Kubernetes

Terraform

Remote ingestion endpoints

AI‑Friendliness
All metrics will be assembled into a clean JSON payload for analysis.

🚀 Roadmap
Phase 1 — Local Agent (Current Phase)
[x] CPU metric

[ ] Memory metric

[ ] Disk metric

[ ] Network metric

[ ] System info metric

[ ] JSON payload builder

[ ] Agent loop

[ ] Logging utilities

[ ] Config file

Phase 2 — Local Docker Deployment
Dockerfile

docker‑compose.yml

Local testing

Phase 3 — Cloud Deployment
Kubernetes manifests

Terraform provisioning

Remote ingestion endpoint

Phase 4 — AI Incident Assistant
LLM‑powered analysis

Alerting

Recommendations

Automated incident summaries

🧭 Current Status
You have completed:

The CPU metric collector

The architectural direction

The project structure plan

The development roadmap

Next step:
Create the full folder + file skeleton so we can start filling in the remaining metric collectors.