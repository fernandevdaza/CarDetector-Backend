from fastapi import FastAPI
from app.routers import inference
from app.routers import car
from contextlib import asynccontextmanager
from app.controllers.yolo_model_controller import init_yolo_model
import torch, gc
from app.core.state import state
from app.core.db import engine
import app.models.db.models as models
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    state.yolo_model = init_yolo_model()
    yield
    del state.yolo_model
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.synchronize()
        torch.cuda.empty_cache()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inference.router)
app.include_router(car.router)
