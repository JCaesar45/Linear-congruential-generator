# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LCG Engine API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LCGRequest(BaseModel):
    r0: int
    a: int
    c: int
    m: int
    n: int

@app.post("/api/lcg")
def generate_lcg(request: LCGRequest):
    r = request.r0
    for _ in range(request.n):
        r = (request.a * r + request.c) % request.m
    return {"result": r}
