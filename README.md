# lifedata manager

medical data manager for devs to track their health and their families.

## what it does
- manage multiple people (family profiles)
- store lab results
- track medications and supplements
- upload and tag health documents
- export data as csv/json

## quickstart (local)

if you prefer a different venv path, just activate that instead of .venv.

requirements: python 3.12+ and a running postgres (or docker)

start postgres + create env (terminal)

```bash
cp manager/.env.example manager/.env
docker compose up -d db
```
run migrations + server (terminal)
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip -r manager/requirements.txt
cd manager
alembic upgrade head
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
open the api docs (browser)
- http://localhost:8000/docs

test the health endpoint (browser)
- http://localhost:8000/api/v1/health

note: the root url (`http://localhost:8000/`) may return 404. that’s expected unless a root route is added.

leave this terminal running while you use the browser links.

## status
active development. current state:
- api boots locally
- api docs available at `/docs`
- health endpoint available at `/api/v1/health`
- people endpoints available at `/api/v1/people` (create/list)

next:
- auth + roles (accounts, memberships)
- lab results model + endpoints (create/list)
- export (csv/json)

## license
mit
