import argparse

import requests


def get_chat_id(bot_token: str, username: str) -> int:
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url, timeout=5).json()
    for update in response["result"]:
        if "message" not in update:
            continue
        if update["message"]["from"]["username"] == username:
            return update["message"]["chat"]["id"]
    raise RuntimeError(f'Could not find user "{username}"')


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("bot_token", type=str)
    argument_parser.add_argument("username", type=str)
    args = argument_parser.parse_args()

    bot_token: str = args.bot_token
    username: str = args.username

    if (bot_token is None) or (username is None):
        raise RuntimeError("bot_token and username are required")

    chat_id = get_chat_id(bot_token, username)
    print(f"\nYour chat id is:\t{chat_id}")


if __name__ == "__main__":
    main()
