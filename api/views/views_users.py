
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models.user import YaUser
from api.serializers.serializers_users import YaUserSerializer


class YaUserViewSet(ModelViewSet):
    queryset = YaUser.objects.all()
    serializer_class = YaUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    @action(detail=False, methods=['get', 'patch'])
    def me(self, request):
        user = self.request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_403_FORBIDDEN)
