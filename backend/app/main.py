from fastapi import FastAPI

app = FastAPI(title="SHANKS API")

@app.get("/")
def read_root():
    return {"Hello": "World", "version": "1.0.0"}

# Include routers here
# from app.api.v1.routes import missions
# app.include_router(missions.router, prefix="/api/v1/missions", tags=["missions"])
