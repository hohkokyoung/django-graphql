import graphene
from project.api.graphql.types import BaseObjectType

from ..models import *

class ProductNode(BaseObjectType):
    class Meta:
        model = Product