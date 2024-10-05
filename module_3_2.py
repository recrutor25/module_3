#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def send_email(message, recipient, sender="university.help@gmail.com"):
    if not ('@' in recipient and ('.com' in recipient or '.net' in recipient or
        '.ru' in recipient) and '@' in sender and('.com' in sender or '.net'
        in sender or '.ru' in sender)):
    # Проверка на корректность e-mail отправителя и получателя
        print(f"Невозможно отправить с адреса {sender} на адрес {recipient}")

    # Проверка на отправку самому себе
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    # Проверка на отправителя по умолчанию.
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес"
              f" {recipient}.")

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           'urban.teacher@mail.ru')
