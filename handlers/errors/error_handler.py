import logging
from typing import Any

from aiogram import Router
from aiogram.exceptions import (TelegramAPIError,
                                TelegramUnauthorizedError,
                                TelegramBadRequest,
                                TelegramNetworkError,
                                TelegramNotFound,
                                TelegramConflictError,
                                TelegramForbiddenError,
                                RestartingTelegram,
                                CallbackAnswerException,
                                TelegramEntityTooLarge,
                                TelegramRetryAfter,
                                TelegramMigrateToChat,
                                TelegramServerError)
from aiogram.handlers import ErrorHandler


router = Router()


@router.errors()
class MyErrorHandler(ErrorHandler):
    async def handle(self, ) -> Any:
        """
        Exceptions handler. Catches all exceptions within task factory tasks.
        :param dispatcher:
        :param update:
        :param exception:
        :return: stdout logging
        """
        if isinstance(self.exception_name, TelegramUnauthorizedError):
            """
            Когда токен бота недействителен, возникает ошибка.
            """
            logging.info(f'Unauthorized: {self.exception_message}')
            return True

        if isinstance(self.exception_name, TelegramNetworkError):
            """
            Ошибка организована для всех ошибок в сети Telegram.
            """
            logging.exception(f'NetworkError: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramNotFound):
            """
            Если чат, сообщение, пользователь и т. д. не найдены, ошибка организована.
            """
            logging.exception(f'NotFound: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramConflictError):
            """
            Ошибка возникает, когда токен бота используется повторно.
            """
            logging.exception(f'ConflictError: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramForbiddenError):
            """
            Ошибка возникает в таких случаях, как исключение бота из чата.
            """
            logging.exception(f'ForbiddenError: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, CallbackAnswerException):
            """
            Ошибка организована в таких ситуациях, как отсутствие ответа.
            """
            logging.exception(f'CallbackAnswerException: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramMigrateToChat):
            """
            Ошибка возникает, когда чат перемещается в супергруппу.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramServerError):
            """
            Ошибка организована, когда сервер Telegram возвращает ошибку 5xx.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramAPIError):
            """
            Ошибка организована для всех ошибок Telegram API.
            """
            logging.exception(f'EntityTooLarge: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramRetryAfter):
            """
            Ошибка организуется, когда запросов становится слишком много.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramEntityTooLarge):
            """
            Ошибка возникает, когда данные превышают лимит во время запроса.
            """
            logging.exception(f'EntityTooLarge: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramBadRequest):
            """
            Ошибка возникает, когда запрос имеет неправильный формат.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, RestartingTelegram):
            """
            Ошибка возникает при перезапуске сервера Telegram.
            """
            logging.exception(f'RestartingTelegram: {self.exception_message} \nUpdate: {self.update}')
            return True

        logging.exception(f'Update: {self.update} \n{self.exception_name}')