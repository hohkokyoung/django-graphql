import graphene
from project.api.graphql.types import BaseFilterConnectionField

from .types import *

class Query(graphene.ObjectType):
    all_products = BaseFilterConnectionField(ProductNode)