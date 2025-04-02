
from taskiq import TaskiqScheduler
import taskiq_fastapi
from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend, RedisScheduleSource
from taskiq.schedule_sources import LabelScheduleSource
from .config import settings


broker = ListQueueBroker(url=settings.REDIS_URL,).with_result_backend(
    RedisAsyncResultBackend(redis_url=settings.REDIS_URL,result_ex_time=3600))
        
        
redis_source = RedisScheduleSource(settings.REDIS_URL,)

scheduler = TaskiqScheduler(
            broker,
            [
                redis_source,
                LabelScheduleSource(broker),
            ],
            )

taskiq_fastapi.init(broker, 'app.main:app')

# from app import tasks      