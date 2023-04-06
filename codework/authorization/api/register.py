import traceback
import sys

from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet

from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from authorization.models import Account
from authorization.functions import get_token, post_register


@api_view(['POST',])
@permission_classes([AllowAny,])
def register_user(request):
    data = request.data
    output = {}
    try:
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']
        email = data['email']
        try:
            user = Account.objects.get(email=email)
            output['status'] = 'failed'
            output['status_text'] = 'Email with this account already exists'
            return Response(output, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            pass
        try:
            user = Account.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_active=True
            )
            user.set_password(password)
            user.save()
            post_data = post_register(email)
            redirect_uri = 'http://127.0.0.1:8000/'
            username = email
            token = get_token(username, password, redirect_uri)
            output['status'] = 'success'
            output['status_text'] = 'successfully registered the user'
            output['user_data'] = post_data
            output.update(token)
            return Response(output, status=status.HTTP_200_OK)
        except EmptyResultSet:
            traceback.print_exc(file=sys.stdout)
            output['status'] = 'failed'
            output['status_text'] = 'Failed to register the user'
            return Response(output, status=status.HTTP_400_BAD_REQUEST)
    except KeyError as e:
        traceback.print_exc(file=sys.stdout)
        output['status'] = 'failed'
        output['status_text'] = f'Key Error: {e}'
        return Response(output, status=status.HTTP_400_BAD_REQUEST)
