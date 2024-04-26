from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router
from router import router_number

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB dropped")
    await create_tables()
    print("DB init")
    yield
    print("Closing...")
    

app = FastAPI(lifespan=lifespan)
app.include_router(router=tasks_router)
app.include_router(router=router_number)

