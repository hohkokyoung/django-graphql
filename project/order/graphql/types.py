import graphene
from project.api.graphql.types import BaseObjectType
from project.user.graphql.types import UserNode

from ..models import *

class OrderNode(BaseObjectType):
    class Meta:
        model = Order

    user = graphene.Field(lambda: UserNode)

class OrderProductNode(BaseObjectType):
    class Meta:
        model = OrderProduct