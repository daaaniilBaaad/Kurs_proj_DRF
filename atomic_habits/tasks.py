from datetime import datetime, timedelta

from celery import shared_task

from atomic_habits.models import Habits
from atomic_habits.services import send_telegram_message


@shared_task
def task():
    """ Задача переодической отправки уведомлений в телеграм за 10 минут до выполнения привычки """
    wonts = Habits.objects.filter.all()
    for wont in wonts:
        if wont.user.chat_id and wont.time <= datetime.now().time() - timedelta(minutes=10):
            text = f"Я буду {wont.action} в {wont.time} в {wont.place}"
            send_telegram_message(text, wont.user.tg_chat_id)

