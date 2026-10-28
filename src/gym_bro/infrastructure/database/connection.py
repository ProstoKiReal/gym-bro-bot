from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from gym_bro.setup.config import config


engine = create_async_engine(
    config.db.url,
    pool_pre_ping=True,
    echo=config.app.debug,
    pool_size=config.db.POOL_SIZE,
    max_overflow=config.db.POOL_MAX_OVERFLOW,
)

session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=True,
)
