from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        credential = request.data.get('credential')
        password = request.data.get('password')

        if not credential:
            return Response({
                'error': 'Credential is required!',
            }, status=status.HTTP_400_BAD_REQUEST)

        {
            "credential": "admin",
            "password": "Admin123#"
        }
        try:
            user = User.objects.get(username=credential)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=credential)
            except User.DoesNotExist:
                return Response({
                    'error': 'User not found!'
                }, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            token = RefreshToken.for_user(user)
            return Response({
                'message': 'Login Successful',
                'access_token': str(token.access_token),
                'refresh_token': str(token),
            })

        return Response({
            'error': 'Invalid password!'
        }, status=status.HTTP_400_BAD_REQUEST)
