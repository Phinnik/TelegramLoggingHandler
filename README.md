# Telegram logging handler

## Installation
```bash
pip3 install git+https://github.com/Phinnik/telegram_logging_handler.git
```

## Usage
```python
import logging
from telegram_logging_handler import TelegramHandler

handler = TelegramHandler(bot_token, chat_id)
formatter = logging.Formatter(
    fmt="<strong>%(levelname)s</strong>\n<i>%(name)s</i>\n\n%(message)s"
)
handler.setFormatter(formatter)

logger = logging.getLogger("LoggerName")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
```


## How to get chat ID?
1. Send some message to your bot
2.
    ```bash
    get_tg_chat_id <bot_token> <your_username>
    ```