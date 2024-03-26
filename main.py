from schemas import STaskAdd
from fastapi import FastAPI, Depends
from typing import Optional, Annotated
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова')
    yield
    print('Выключение')
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)




