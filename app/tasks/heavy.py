from datetime import datetime
from app.tq import broker
from app.utils import log_on_completion
from logging import getLogger

logger = getLogger(__name__)

@log_on_completion
@broker.task(schedule=[{"cron": "* * * * *"}]) # task ever 1 minute execute
async def heavy_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Scheduled task executed at: {now}")
    print(f"Hello from cron job! Time: {now}")
 
