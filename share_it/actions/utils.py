from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action

import datetime


def create_action(user, verb, target=None):
    """
    Creates create actions that optionally include a target object. You can use this function anywhere in your code
    as a shortcut to add new actions to the activity stream.
    :param user:
    :param verb:
    :param target:
    """
    # Check for any similar action made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)

    if not similar_actions:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
