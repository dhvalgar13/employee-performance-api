from fastapi import FastAPI
from controllers import router

app = FastAPI(title="Employee Performance Review API")
app.include_router(router)
