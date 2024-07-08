from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from accounts.permissions import IsSelfOrReadonly


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

# class UserList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSelfOrReadonly,)


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSelfOrReadonly, )
