from fbchat import Client
from fbchat.models import *
from time import sleep

EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
MESSAGE = 'Merry Christmas  ☃!🎁🎁'

exclude_ids = []
client = Client(EMAIL, PASSWORD)


def login():
    if not client.isLoggedIn():
        client.login(EMAIL, PASSWORD)


def get_receivers():
    output = []
    for user in users:
        is_friend = user.is_friend

        if user.uid not in exclude_ids and is_friend:
            output.append(user)

    return output


def send_message_to_receivers():
    for receiver in receivers:
        client.send(Message(text=MESSAGE), thread_id=receiver.uid)
        print(f'Sent to {receiver.first_name} {receiver.last_name}.')
        sleep(2)


if __name__ == '__main__':
    login()
    users = client.fetchAllUsers()
    receivers = get_receivers()
    print(f'Receivers count: {len(receivers)}.\n')

    send_message_to_receivers()

    print('Done!')
