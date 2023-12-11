from django.shortcuts import redirect
import requests
import os
import dotenv

from rest_framework.views import APIView


class UserActivationView(APIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/user_auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data = post_data)
        return redirect(os.getenv("SUCCESS_REGISTER_URL"))

def password_reset(request, uid, token):
    password_reset_url = os.getenv("PASSWORD_RESET_URL")
    redirect_url = f"{password_reset_url}?uid={uid}&token={token}"
    return redirect(redirect_url)