
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.endpoints import health, core

def create_server() -> FastAPI:
    server = FastAPI(
        title="Heuristic router API for LLM's", 
        debug=True
    )
    
    # server.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],  # TODO:(dynamic change for prod)
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )


    server.include_router(health.router, prefix="/api/v1")
    server.include_router(core.router, prefix="/api/v1")
    return server

app = create_server()