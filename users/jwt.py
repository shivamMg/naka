from datetime import datetime
from calendar import timegm

from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    """
    `jwt_payload_handler` from `rest_framework_jwt.utils` requires user
    email and therefore could not be used.
    """
    payload = {
        'user_id': user.pk,
        'username': user.username,
        'is_staff': user.is_staff,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    # if isinstance(user.pk, uuid.UUID):
    #     payload['user_id'] = str(user.pk)

    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    return payload
