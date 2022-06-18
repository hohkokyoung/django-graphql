import graphene
from project.api.graphql.types import BaseFilterConnectionField, MyFilterConnectionField

from .types import *

class Query(graphene.ObjectType):
    all_orders = BaseFilterConnectionField(OrderNode)
    
    my_orders = MyFilterConnectionField(OrderNode)

    pass