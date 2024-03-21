import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time


vk_session = vk_api.VkApi(token='')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
chat_id =
file_path = "messages.txt"


def write_message_to_file(message):
    with open(file_path, "a") as file:
        file.write(message + "\n")

def read_messages_from_file():
    with open(file_path, "r") as file:
        messages = file.readlines()
        return [message.strip() for message in messages]

def send_message(message):
    vk.messages.send(peer_id=2000000000 + chat_id, message=message, random_id=random.getrandbits(64))
def process_messages():
    new_message_counter = 0
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    if event.text:
                        write_message_to_file(event.text)
                        new_message_counter += 1
                        if new_message_counter == 3:
                            return True
        except Exception as e:
            print("Ошибка при получении сообщений:", e)


def send_random_message():
    while True:
        try:
            if process_messages():
                messages = read_messages_from_file()
                if len(messages) >= 1:
                    random_message = random.choice(messages)
                    send_message(random_message)
            time.sleep(10)
        except Exception as e:
            print("Ошибка при отправке сообщения:", e)


import threading

thread2 = threading.Thread(target=send_random_message)

thread2.start()
