# Exit Ahead

A drive-safe food ordering app. Drivers see restaurants along their route, order ahead for pickup, and the food is ready when they arrive. Built as a hands-on project to learn full stack development and AI/ML.

> **Status:** early prototype. The UI works with sample data. The backend, map and ML features are in progress (see the roadmap).

## Why this project

Ordering food while driving is a safety problem as much as a product problem. The design follows three rules:

- **Driving mode** allows only voice ordering and one-tap "usual" orders. Full menus unlock when parked.
- **Order ahead for pickup**, not delivery. Nothing has to be done at the restaurant.
- **Timed to arrival**, so the kitchen starts preparing based on how far away the driver is.

## Features

- [x] Driving / Parked modes with large tap targets
- [x] Voice ordering (browser speech recognition, keyword matching)
- [x] One-tap usual orders and a confirmation step
- [x] Restaurants along the route with exit, detour time and ready-by time
- [ ] Interactive map with route, restaurants, distance and offers
- [ ] Backend API and database
- [ ] Order status tracking
- [ ] Payments (test mode)
- [ ] ML: prep-time and arrival prediction
- [ ] ML: LLM-based order parsing with evaluation

## Tech stack

| Layer | Current | Planned |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | Next.js, TypeScript, Leaflet |
| Backend | none | FastAPI (Python) |
| Data | hardcoded sample data | PostgreSQL + PostGIS, Redis |
| ML | none | scikit-learn / XGBoost, Whisper, LLM API |
| DevOps | none | Docker, GitHub Actions, cloud deploy |

## Getting started

```bash
git clone https://github.com/SravanABC/HF.git
cd HF
```

Open `roadside-order.html` in your browser. No build step is needed yet.

## Roadmap

1. **Map view:** Leaflet map with route, nearby restaurants, distance and offers
2. **Backend:** FastAPI + Postgres, order state machine, tests
3. **Full stack:** connect the UI to the API, add auth, containerize, deploy
4. **ML:** prep-time predictor with a baseline and evaluation, then LLM order parsing
5. **Write-up:** design decisions, results and lessons learned

## Data note

All restaurants, menus and prices are sample data. Any ML results will be reported with the dataset used and how it was generated.

## What I'm learning

Python and FastAPI, SQL and PostGIS, React/Next.js, Docker and CI, and applied ML. Coming from 10 years of ServiceNow development, I'm applying enterprise workflow and integration experience to a consumer product.

## License

MIT (add a `LICENSE` file to the repo)
