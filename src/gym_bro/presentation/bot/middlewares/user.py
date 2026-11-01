from collections.abc import Awaitable, Callable
from typing import TypeVar

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

MiddlewareEvent = TypeVar("MiddlewareEvent", bound=TelegramObject)
HandlerResult = TypeVar("HandlerResult")


class RequireUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[
            [MiddlewareEvent, dict[str, object]], Awaitable[HandlerResult]
        ],
        event: MiddlewareEvent,
        data: dict[str, object],
    ) -> HandlerResult | None:
        if not isinstance(event, Message):
            return await handler(event, data)

        user = event.from_user
        if user is None:
            return None

        data["user"] = user
        return await handler(event, data)
