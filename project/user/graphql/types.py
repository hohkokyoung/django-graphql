import graphene
from django.contrib.auth import get_user_model
from project.api.graphql.types import BaseObjectType

User = get_user_model()

class UserNode(BaseObjectType):
    class Meta:
        model = User