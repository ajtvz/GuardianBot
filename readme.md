GuardianBot – PC Performance & AI‑Powered Game Optimization
GuardianBot is a lightweight system monitoring agent built for gamers who want real insight into how their PC performs while they play. It tracks essential hardware metrics in real time — CPU, memory, disk, network, and system information — and pairs them with AI‑driven anomaly detection to help identify issues that might be causing lag, stutters, high latency, or unexpected performance drops.

The goal is simple:
Give gamers a clear view of what their PC is doing and help them fix problems before they ruin the experience.

GuardianBot collects metrics locally and sends them to a backend service for analysis. The long‑term vision is a full dashboard where players can view performance history, get AI explanations for unusual behavior, and receive practical suggestions to improve gameplay smoothness and system stability.

Features (Current)
Real‑time metric collection

CPU usage

Memory usage

Disk usage

Network throughput

System information (OS, hostname, boot time, core count)

Persistent device ID

Timestamped payloads

Clean, modular Python architecture

Project Roadmap
Phase 1 — Core Agent (Completed)
[x] Build agent structure

[x] Add CPU, memory, disk, network, and system metrics

[x] Add timestamps

[x] Add persistent device ID

[x] Prepare payload format for backend ingestion

Phase 2 — Backend API (In Progress)
[ ] FastAPI backend

[ ] /ingest endpoint for receiving metrics

[ ] Pydantic validation

[ ] PostgreSQL database setup

[ ] Store device + metric records

[ ] Basic authentication for agents

Phase 3 — AI Analysis
[ ] Anomaly detection (Isolation Forest / PyOD)

[ ] AI explanations for performance spikes

[ ] Suggestions for fixing latency, stutters, and bottlenecks

Phase 4 — Dashboard
[ ] Web UI for real‑time metrics

[ ] Historical charts

[ ] Device overview page

[ ] AI insights panel

[ ] User accounts & login

Phase 5 — Quality of Life
[ ] Windows + Linux installers

[ ] Auto‑update system

[ ] Run agent as a background service

[ ] Config file support

[ ] Logging & error reporting

Who This Is For
GuardianBot is built for:

Gamers who want to understand why their FPS drops

Players dealing with random lag spikes or high latency

Anyone who wants a simple way to monitor PC health

People who want AI‑powered explanations instead of digging through logs

Developers interested in system monitoring, backend design, and anomaly detection