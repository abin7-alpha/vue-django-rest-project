from django.urls import path
from authorization.api.login import login_user
from authorization.api.register import register_user
from views import CreateAccount

app_name = 'users'

urlpatterns = [
   path('create/', CreateAccount.as_view(), name="create_user"),
   path('login-user', login_user, name='login_user'),
   path('register-user',  register_user, name='register_user'),
]
