from django.conf import settings
from django.contrib.auth import get_user_model
from graphql_jwt.utils import jwt_decode
from project.api.graphql.utils import handle_error, safe_get

User = get_user_model()

@handle_error(return_if_error=Exception())
def get_user_from_request(request):
    user = None

    # get token from request headers
    auth_header = request.META.get("HTTP_AUTHORIZATION")

    # get user object only if the auth header is found in headers
    if auth_header is not None:
        # check if auth header prefix follows the correct format:
        # <prefix specified in the settings.py> + a trailing space
        prefix = settings.GRAPHQL_JWT.get("JWT_AUTH_HEADER_PREFIX") + " "

        if auth_header.startswith(prefix) is not True:
            raise Exception("Auth header is invalid.")

        # verify & decode token
        token = auth_header[len(prefix) :]
        payload = jwt_decode(token)

        user = User.objects.get(username=safe_get(payload, "username"))

    return user