from sqlalchemy.ext.asyncio import AsyncSession

from gym_bro.application.interfaces.tx_manager import TXManager


class AlchemyTXManager(TXManager):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc, tb):
        try:
            await super().__aexit__(exc_type, exc, tb)
        finally:
            await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
