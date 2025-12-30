# OrbitOps – NOAA Space Weather Ingestion

OrbitOps is a production-style DevOps project that ingests real-time NOAA
space weather data on an edge device (Jetson Nano / ARM), using
Linux RBAC, systemd timers, containers, and CI/CD.

This project is designed as a **real-world DevOps portfolio project**
aligned with how infrastructure and automation work in production
environments.

---

## 🚀 What This Project Demonstrates

- Linux system administration (users, groups, permissions)
- Least-privilege security model (DevOps / App / ITSec separation)
- systemd oneshot services with systemd timers (cron-free scheduling)
- Containerized data ingestion (non-root, stateless containers)
- Real NOAA space weather data ingestion
- GitHub Actions CI pipeline
- Edge-device friendly architecture (Jetson / ARM-ready)

---

## 🛰️ Data Source

**NOAA Space Weather Prediction Center (SWPC)**  

Endpoint:
```
https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json
```

The ingestion job extracts the most recent solar wind measurements
and stores them as structured JSON.

---

## 🧱 Architecture Overview

```
Jetson Nano (Linux)
│
├── /srv/orbitops
│   ├── apps/        → application output (DevOps + App)
│   ├── ops/         → operational scripts
│   └── secrets/     → restricted (ITSec only)
│
├── systemd
│   ├── orbitops-noaa.service  → oneshot ingestion job
│   └── orbitops-noaa.timer    → scheduled execution (every 5 min)
│
├── Docker
│   └── Non-root container running ingestion code
│
└── GitHub Actions
    └── CI pipeline builds container on every push
```

---

## 👥 Linux Security Model (RBAC)

| Role    | Group   | Access |
|--------|---------|--------|
| DevOps | devops  | /srv/orbitops/apps, ops |
| App    | app     | Application code & output |
| ITSec  | itsec   | secrets only |
| SRE    | sre     | Observability / runtime |

Secrets directory is **fully isolated** from DevOps and App users.

---

## 🐳 Container Usage

### Build Image
```bash
docker build -t orbitops-noaa:latest -f docker/Dockerfile .
```

### Run Container (Production Style)
```bash
docker run --rm   -e NOAA_OUTPUT=/data/latest.json   -v /srv/orbitops/apps/noaa:/data   orbitops-noaa:latest
```

---

## ⏱️ Scheduling (systemd Timer)

- systemd **oneshot** service
- systemd **timer** triggers ingestion every 5 minutes
- No cron
- Fully observable via `journalctl`

```bash
systemctl list-timers | grep orbitops
journalctl -u orbitops-noaa.service
```

---

## 🔁 CI/CD

- GitHub Actions pipeline
- Runs on every push to `main`
- Builds container image
- Ready for extension (lint, tests, push to registry)

Workflow location:
```
.github/workflows/ci.yml
```

---

## 🎯 Why This Project Matters

This repository mirrors how **real DevOps teams** operate:

- Clear ownership boundaries
- Secure filesystem layout
- Infrastructure-first thinking
- Automation without shortcuts
- Cloud & edge compatible

This is not a demo — it is a **production mindset project**.
