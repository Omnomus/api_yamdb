# from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import (RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api.models.user import YaUser
from api.serializers.serializers_users import YaUserSerializer


class YaUserViewSet(ModelViewSet):
    queryset = YaUser.objects.all()
    serializer_class = YaUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'


class RetrieveUpdateViewSet(RetrieveModelMixin,
                            UpdateModelMixin,
                            GenericViewSet):
    pass


class YaUserRetrieveUpdateViewSet(RetrieveUpdateViewSet):
    queryset = YaUser.objects.all()
    serializer_class = YaUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        # pk = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
