from typing import Iterable

from aiogram import Dispatcher
from dishka.integrations.aiogram import setup_dishka
from dishka import make_async_container, Provider

from gym_bro.setup.config import config, Config


def create_dishka(providers: Iterable[Provider], dp: Dispatcher) -> None:
    container = make_async_container(
        *providers,
        context={Config: config},
    )
    setup_dishka(
        container=container,
        router=dp,
        auto_inject=True,
    )
