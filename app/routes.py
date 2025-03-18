from datetime import datetime, timedelta
from fastapi import APIRouter
from app.tasks import send_email_task
from .tq import redis_source
router = APIRouter()

@router.get("/")
async def health():
    return {"status": "ok"}


@router.get("/send-email")
async def send_email(
    email_to: str = "",
    subject: str = "Test Email",
    body: str = "<h1>Hello World!</h1>"
):
    
    
    
    
    # classic way
    # await send_email_task.kiq(
    #     email_to=email_to,
    #     subject=subject,
    #     body=body,
    # )

    # schedule by time
    await send_email_task.schedule_by_time(
        source=redis_source,
        time=datetime.now() + timedelta(seconds=10), # run in 10 seconds
        email_to=email_to,
        subject=subject,
        body=body,
    )
    return {"message": "Email queued for sending"}