import traceback
import sys

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist, FieldError

from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from authorization.models import Account
from authorization.functions import get_token, serialized_user


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def login_user(request):
    data = request.data
    output = {}

    email = data['email']
    password = data['password']

    try:
        user = Account.objects.get(email=email)
    except ObjectDoesNotExist:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = "Account not exists"
        return Response(output, status=status.HTTP_401_UNAUTHORIZED)
    try:
        if user.is_active:
            pass
        else:
            raise Exception
    except FieldError:
        output['status'] = "failed"
        output['status_text'] = "Your account has been inactive, contact admin"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)
    try:
        try:
            authorized_user = authenticate(
                request,
                email=email,
                password=password
            )
            if authorized_user is None:
                raise Exception
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print(e)
            output['status'] = "failed"
            output['status_text'] = "Incorrect password"
            return Response(output, status=status.HTTP_401_UNAUTHORIZED)
        redirect_uri = 'http://127.0.0.1:7000/'
        username = email
        data = serialized_user(email)
        token = get_token(username, password, redirect_uri)
        output['status'] = 'success'
        output["status_text"] = "Succesfully Auntheticated"
        output["email"] = user.email
        output['user_data'] = data
        output.update(token)
        return Response(output, status=status.HTTP_200_OK)
    except Exception as error:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = "Failed to login"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)
