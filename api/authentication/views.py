from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.authentication.models import YaUser

USER_ERROR = {
    'error': 'User with given email already exists'
}
CODE_INFO = {
    'email': 'The confirmation code was sent to your email'
}
CODE_ERROR = {
    'error': 'Invalid confirmation code'
}


def get_tokens_for_user(user):
    """Create new refresh and access tokens for the given user."""
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    """Provide confirmation code to user for given email."""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        user = YaUser.objects.filter(email=email).exists()
        if user:
            return Response(
                USER_ERROR, status=status.HTTP_400_BAD_REQUEST
            )
        user = YaUser.objects.create_user(email=email, password=None)
        user.confirmation_code = get_random_string(length=11)
        user.save()
        send_mail(
            'Your confirmation code is here!',
            user.confirmation_code,
            'YaMDb@yamdb.com',
            (email,),
        )
        return Response(CODE_INFO, status=status.HTTP_200_OK)


class JWTTokenView(APIView):
    """Provide token to user for given email and confirmation_code."""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']
        confirmation_code = request.data['confirmation_code']
        user = get_object_or_404(YaUser, email=email)
        if user.confirmation_code != confirmation_code:
            return Response(
                CODE_ERROR, status=status.HTTP_400_BAD_REQUEST
            )
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_200_OK)
