from fastapi import FastAPI
from db import get_all_logs, get_log_by_user

app = FastAPI()

@app.get("/logs")
def get_logs():
    return get_all_logs()

@app.get("/logs/{user_id}")
def get_logs_by_user(user_id):
    return get_log_by_user(user_id)