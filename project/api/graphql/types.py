from lib2to3.pytree import Base
from tracemalloc import BaseFilter
import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class CountableConnection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    # note: we can change the way we count results by modifying the code here!
    def resolve_total_count(root, info, **kwargs):
        return len(root.iterable)


class BaseObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model,
        interfaces=(relay.Node,),
        filter_fields=["id"],
        connection_class=CountableConnection,
        **options,
    ):
        return super().__init_subclass_with_meta__(
            model=model,
            interfaces=interfaces,
            filter_fields=filter_fields,
            connection_class=connection_class,
            **options,
        )

class BaseFilterConnectionField(DjangoFilterConnectionField):
    @classmethod
    def default_resolver(self, args, info, iterable):
        return iterable

    @classmethod
    def resolve_queryset(
        self, connection, iterable, info, args, filtering_args, filterset_class
    ):
        # get queryset back from default resolver
        iterable = self.default_resolver(args=args, info=info, iterable=iterable)

        # return error if no queryset is found
        # otherwise proceed to return the result from the queryset
        if iterable is None:
            raise Exception(f"{connection.__name__} matching query does not exist.")

        return super(BaseFilterConnectionField, self).resolve_queryset(
            **{
                "connection": connection,
                "iterable": iterable,
                "info": info,
                "args": args,
                "filtering_args": filtering_args,
                "filterset_class": filterset_class,
            }
        )
        
class MyFilterConnectionField(BaseFilterConnectionField):
    @classmethod
    def resolve_queryset(
        self, connection, iterable, info, args, filtering_args, filterset_class
    ):
        try:
            iterable = iterable.filter(user=info.context.user)
        except:
            raise Exception(f"{connection.__name__} Only for logged-in users.")

        return super(MyFilterConnectionField, self).resolve_queryset(
            **{
                "connection": connection,
                "iterable": iterable,
                "info": info,
                "args": args,
                "filtering_args": filtering_args,
                "filterset_class": filterset_class,
            }
        )