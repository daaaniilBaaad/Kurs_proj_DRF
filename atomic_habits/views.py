from rest_framework import generics
from atomic_habits.models import Habits
from atomic_habits.serializers import HabitsSerializer
from atomic_habits.paginators import CustomPagination
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    """ Класс для создания привычек """
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        """ Присваивание привычки пользователю """
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsListAPIView(generics.ListAPIView):
    """ Класс для получения списка привычек """
    serializer_class = HabitsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        """ Пользователь может видеть свои и публичные привычки """
        user = self.request.user
        user_habits = Habits.objects.filter(owner=user)
        public_habits = Habits.objects.filter(is_published=True)

        return user_habits | public_habits


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс для вывода привычки """
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """ Класс для обновления привычки """
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """ Класс для удаления привычки """
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)
