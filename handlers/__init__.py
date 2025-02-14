from aiogram import Router, F
from aiogram.enums import ChatType

def setup_routers() -> Router:
    from .users import (
        start,
        admin,
        help,
        )
    from .errors import error_handler

    router = Router()
    start.router.message.filter(F.chat.type == ChatType.PRIVATE)

    router.include_routers(
        start.router,
        admin.router,
        help.router,
        error_handler.router,
        )

    return router