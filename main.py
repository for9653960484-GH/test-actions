from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Time API")


@app.get("/")
def read_root() -> dict:
    return {"status": "ok", "message": "Use /time to get server time"}


@app.get("/time")
def get_server_time() -> dict:
    now = datetime.now(timezone.utc)
    return {"server_time": now.isoformat()}


@app.get("/date")
def get_server_date() -> dict:
    today = datetime.now().date()
    return {"date": today.isoformat()}


@app.get("/date/utc")
def get_server_date_utc() -> dict:
    today_utc = datetime.now(timezone.utc).date()
    return {"date_utc": today_utc.isoformat()}
