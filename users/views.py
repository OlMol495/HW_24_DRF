from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer, UserProfileSerializer, UserPublicProfileSerializer



class UserViewSet(viewsets.ModelViewSet):
    """ Вывод данных по юзерам с кастомизированной вьюшкой на детали юзера """
    queryset = User.objects.all()
    default_serializer = UserSerializer  # Дефолтный сериалайзер
    serializers = {
        'retrieve': UserProfileSerializer  # Детали юзера выводятся по UserProfileSerializer
    }

    def get_serializer_class(self):
        """ Return appropriate serializer """
        if self.action == 'retrieve':
            if self.request.user == self.get_object():
                return UserProfileSerializer
            return UserPublicProfileSerializer
        return self.default_serializer


