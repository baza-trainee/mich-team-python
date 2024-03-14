from django.shortcuts import redirect
import requests
import os
import dotenv

from rest_framework.views import APIView


class UserActivationView(APIView):
    def get(self, request, uid, token):
        return redirect(os.getenv("SUCCESS_REGISTER_URL") + "?uid=" + uid + "&token=" + token + "&activation=true")


def password_reset(request, uid, token):
    return redirect(os.getenv("SUCCESS_REGISTER_URL") + "?uid=" + uid + "&token=" + token + "&password_reset=true")
