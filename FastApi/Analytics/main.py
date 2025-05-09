from fastapi import FastAPI
from .database import engine
from . import models
from .router import Analytics
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Allow requests from your frontend
origins = [
    "http://localhost:3000",  # React dev server
    # Add more origins if needed, e.g., for deployment
]

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all headers
)


app.include_router(Analytics.router)

models.Base.metadata.create_all(engine)
