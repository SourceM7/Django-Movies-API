from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerilizer
from rest_framework.authtoken.models import Token
from user_app import models
from rest_framework import status


@api_view(["POST"])
def logout_view(request):
    if request.method == "POST":
        request.user.auth.token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(
    [
        "POST",
    ]
)
def registeration_view(request):
    if request.method == "POST":
        serilizer = RegistrationSerilizer(data=request.data)

        data = {}

        if serilizer.is_valid():
            account = serilizer.save()
            data["response"] = "registeration success"
            data["username"] = account.username
            data["email"] = account.email

            token = Token.objects.get(user=account).key
            data["token"] = token

        else:
            data = serilizer.errors

        return Response(data)
