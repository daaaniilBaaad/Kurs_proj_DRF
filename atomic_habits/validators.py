from django.core.exceptions import ValidationError


def validate_execution_time(execution_time):
    """ Валидатор времени выполнения задачи. """
    total_seconds = execution_time.hour * 3600 + execution_time.minute * 60 + execution_time.second
    if total_seconds > 120:
        raise ValidationError('Время выполнения задачи не может превышать 2 минуты.')


def validate_frequency(frequency_days):
    """ Валидатор частоты выполнения задачи. """
    if frequency_days > 7:
        raise ValidationError('Частота выполнения задачи не может превышать 7 дней.')


def validate_pleasant_habit(attrs):
    """ Валидатор приятной привычки. """
    addition_habit = attrs.get('addition_habit')
    award = attrs.get('award')
    reward_action = attrs.get('reward_action')
    if addition_habit and not addition_habit.reward_action:
        raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')
    if reward_action and (addition_habit or award):
        raise ValidationError('У приятной привычки не может быть связанной привычки или награды.')


def validate_no_both_addition_and_award(attrs):
    """ Валидатор отсутствия одновременно связанной привычки и награды. """
    addition_habit = attrs.get('addition_habit')
    award = attrs.get('award')
    if addition_habit and award:
        raise ValidationError('У привычки не может быть одновременно связанной привычки и награды.')
