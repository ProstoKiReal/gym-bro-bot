from aiogram import Router

from gym_bro.bot.handlers.profile import router as profile_router


router = Router()
router.include_routers(
    profile_router,
)
