"""Simple VK auto-sale bot.

This script posts car sale messages to a VK group wall using the official
VK API. Provide your group token and group id via environment variables
`VK_TOKEN` and `VK_GROUP_ID` before running.
"""

import os
import time
import vk_api

POST_DELAY = 60  # seconds between posts


def post_message(vk, group_id: str, message: str, attachments: str | None = None) -> None:
    params = {
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'message': message,
    }
    if attachments:
        params['attachments'] = attachments
    vk.wall.post(**params)


def main() -> None:
    token = os.environ.get('VK_TOKEN')
    group_id = os.environ.get('VK_GROUP_ID')

    if not token or not group_id:
        raise SystemExit('Set VK_TOKEN and VK_GROUP_ID environment variables')

    vk = vk_api.VkApi(token=token).get_api()

    posts = [
        {
            'message': 'Продается автомобиль Ford Focus 2010, цена 500000₽.',
            'attachments': None,
        },
        # Добавьте свои посты при необходимости
    ]

    for post in posts:
        post_message(vk, group_id, post['message'], post['attachments'])
        print('Published:', post['message'])
        time.sleep(POST_DELAY)


if __name__ == '__main__':
    main()
