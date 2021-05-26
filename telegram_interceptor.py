from telegram.client import Telegram

import config


if __name__ == '__main__':

    tg = Telegram(
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        phone=config.PHONE_NUMBER,
        database_encryption_key=config.DB_ENCRYPTION_KEY,
    )

    # you must call login method before others
    tg.login()

    def new_message_handler(update):
        print(update)
        message_content = update['message']['content']
        message_text = message_content.get('text', {}).get('text', '').lower()

        if message_content['@type'] == 'messageText' and message_text == 'ping':
            chat_id = update['message']['chat_id']
            print(f'Ping has been received from {chat_id}')
            tg.send_message(
                chat_id=chat_id,
                text='pong',
            )

    tg.add_message_handler(new_message_handler)
    tg.idle()  # blocking waiting for CTRL+C
