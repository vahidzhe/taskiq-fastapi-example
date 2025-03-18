from contextlib import asynccontextmanager
from fastapi import FastAPI
from .tq import broker
from .routes import router


# Define the application lifespan, ensuring the broker is started and stopped
# only in the main process, not in worker processes.
@asynccontextmanager
async def lifespan(app: FastAPI):

    if not broker.is_worker_process:
        await broker.startup()

    yield

    if not broker.is_worker_process:
        await broker.shutdown()

app = FastAPI(lifespan=lifespan)
app.include_router(router)



