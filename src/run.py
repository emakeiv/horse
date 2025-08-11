import sys
import os
import uvicorn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

#TODO: args ? external conf

def _start(config: dict) -> None:
    uvicorn.run(
        "api.v1.server:app", 
        host="0.0.0.0", 
        port=8080, 
        reload=True
    )

if __name__ == "__main__":
    _start()