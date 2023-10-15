import logging
from typing import Dict

import requests


class TelegramHandler(logging.Handler):
    def __init__(
        self,
        bot_token: str,
        chat_identifier: int | str,
        level_silence: Dict[int, bool] | None = None,
        level: int = 0,
    ) -> None:
        super().__init__(level)
        self._bot_token = bot_token
        self._chat_identifier = chat_identifier
        if level_silence is None:
            level_silence = {
                logging.DEBUG: True,
                logging.INFO: True,
                logging.WARNING: False,
                logging.ERROR: False,
            }
        self._level_silence = level_silence

    @property
    def _api_url(self) -> str:
        return f"https://api.telegram.org/bot{self._bot_token}"

    def emit(self, record: logging.LogRecord) -> None:
        message_text = self.format(record)

        url = self._api_url + "/sendMessage"

        silent = self._level_silence.get(record.levelno, True)
        params = {
            "chat_id": self._chat_identifier,
            "text": message_text,
            "disable_web_page_preview": True,
            "disable_notification": silent,
            "parse_mode": "html",
        }
        requests.get(url=url, params=params, timeout=60)
