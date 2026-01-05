from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from atomic_habits.models import Habits
from atomic_habits.validators import validate_execution_time, validate_frequency, validate_pleasant_habit, validate_no_both_addition_and_award


class HabitsSerializer(ModelSerializer):
    """ Класс сериализатора для модели привычки """
    time = serializers.TimeField(validators=[validate_execution_time])
    period = serializers.IntegerField(validators=[validate_frequency])

    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, attrs):
        """ Валидируем приятные привычки """
        validate_pleasant_habit(attrs)

        """ Валидируем, что нельзя одновременно указывать и награду, и связанную привычку """
        validate_no_both_addition_and_award(attrs)

        return attrs