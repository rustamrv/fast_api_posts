from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.main import api_router  # Assuming this is the correct attribute name
from app.models import Base
from app.database import engine

fastApp = FastAPI()

# CORS middleware
fastApp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
Base.metadata.create_all(bind=engine)

fastApp.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(fastApp, host="127.0.0.1", port=8000)