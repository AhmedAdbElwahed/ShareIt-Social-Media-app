from django.contrib.auth.models import User
from django.http import HttpRequest

from . import models

from typing import Optional


class EmailAuthBackend:
    """
        Authenticate using an e-mail address.
    """

    def authenticate(self, request: HttpRequest, username=None, password=None) -> Optional[User]:
        try:
            user: User = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id) -> Optional[User]:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    :param backend: The social auth backend used for the user authentication
    :param user: The new or existing user authenticated
    :param args:
    :param kwargs:
    :return: None
    """
    models.Profile.objects.get_or_create(user=user)
