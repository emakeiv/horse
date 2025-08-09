
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.endpoints import health

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
    
    return server

#TODO: db mappers ?
app = create_server()