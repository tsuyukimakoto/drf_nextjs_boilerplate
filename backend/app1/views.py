import os
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloView(APIView):
    def get(self, request):  # pylint: disable=unused-argument
        return Response(
            {
                "hello": "world",
            }
        )
