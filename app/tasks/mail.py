from fastapi_mail import FastMail, MessageSchema
from app.tq import broker
from app.utils import log_on_completion,mail_conf
from logging import getLogger

logger = getLogger(__name__)

@broker.task
@log_on_completion
async def send_email_task(email_to: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype="html"
    )
    
    fm = FastMail(mail_conf)
    await fm.send_message(message)
    