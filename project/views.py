from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from graphene_file_upload.django import FileUploadGraphQLView
from .jwt import get_user_from_request

User = get_user_model()

# --- credit ---
# author: abaskov
# reference: https://github.com/graphql-python/graphene-django/issues/345

# note that this view only handles JWT exceptions if it is found in the request headers
# however authorization should be handled at the resolver level instead
class ProtectedGraphQLView(FileUploadGraphQLView):
    # get user object from db, create new account if not found
    # then add it to request context
    def dispatch(self, request, *args, **kwargs):
        user = get_user_from_request(request)

        if isinstance(user, type(None)):
            user = AnonymousUser()

        # check if error is returned as user
        if isinstance(user, Exception):
            return JsonResponse({"error":"Authorization Error.", "status":401}, status=401)

        # add user info to request context
        request.user = user

        return super().dispatch(request, *args, **kwargs)

