# OrbitOps – NOAA Space Weather Ingestion

OrbitOps is a production-style DevOps project that ingests real-time NOAA space weather data on an edge device (Jetson), using Linux RBAC, systemd timers, containers, and CI.

## 🚀 What This Project Demonstrates

- Real-world Linux administration (users, groups, permissions)
- Least-privilege security model (DevOps / App / ITSec separation)
- systemd oneshot services with systemd timers (cron-free scheduling)
- Containerized ingestion (non-root, stateless containers)
- Real NOAA space weather data ingestion
- CI pipeline with GitHub Actions
- Edge-device friendly design (Jetson / ARM-ready)

## 🛰️ Data Source

NOAA Space Weather Prediction Center  
Endpoint:https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json





## 🧱 Architecture Overview

- **Linux RBAC**: Dedicated users and groups for DevOps, App, and Security
- **Ingestion Job**: Python-based NOAA data ingestion
- **Scheduling**: systemd timer (every 5 minutes)
- **Container Runtime**: Docker, non-root execution
- **CI**: GitHub Actions builds the container image on every push

## 🐳 Container Usage

### Build
```bash
docker build -t orbitops-noaa -f docker/Dockerfile .


docker run --rm orbitops-noaa
