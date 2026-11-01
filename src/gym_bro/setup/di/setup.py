from collections.abc import Iterable

from aiogram import Dispatcher
from dishka import Provider, make_async_container
from dishka.integrations.aiogram import setup_dishka

from gym_bro.setup.config import Config, config


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
