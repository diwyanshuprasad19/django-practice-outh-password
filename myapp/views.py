import json
import requests
from django.urls import reverse  # Import reverse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Login(APIView):

    def post(self, request):
        auth = ('s5zCPgwj0eO4FpEXP3Lpi9GhTUVAkitiK5ZXr7lC', 'pYoZcfKcRIXRtHouO6pfkzowBOhyZWaKqboOM8jIi9jtirTmXq39yqEFmhWjA3VH1muNINjEmeYSkCGj8IG127FDgc105ETAdT12LcfEC4jmPnZMYIYQ460R7YiMw1b8')

        username = request.data.get('username')  # Retrieve username from request data
        password = request.data.get('password')  # Retrieve password from request data

        if username and password:
            try:
                response = requests.post(reverse('oauth2_provider:token'), data={'username': username, 'password': password, 'grant_type': 'password'}, auth=auth)
                if response.status_code == status.HTTP_200_OK:
                    result = response.json()
                    data = {
                        "access_token": result['access_token'],
                    }
                    return Response(data=data, status=status.HTTP_200_OK)
                else:
                    return Response(data={"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data={"error": "Missing username or password"}, status=status.HTTP_400_BAD_REQUEST)
