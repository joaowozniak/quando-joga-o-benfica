import asyncio
import time
from asyncio import ensure_future
from functools import wraps


class SchedulerService:
    @staticmethod
    def scheduler(refresh_rate_in_seconds: float, execution_hour: str):
        def decorator(func):
            @wraps(func)
            async def wrapped() -> None:
                async def loop() -> None:
                    while True:
                        current_time = time.strftime("%H:%M", time.localtime())
                        if (
                                current_time == execution_hour
                        ):
                            try:
                                await func()
                            except Exception as exc:
                                raise exc
                        await asyncio.sleep(refresh_rate_in_seconds)

                ensure_future(loop())

            return wrapped

        return decorator
