import graphene
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from graphene_permissions.mixins import AuthMutation
from graphene_permissions.permissions import AllowAuthenticated
from project.api.graphql.utils import decode_global_id, safe_get

from ..models import Product

class CreateProduct(AuthMutation, graphene.relay.ClientIDMutation):
    permission_classes = (AllowAuthenticated,)

    class Input:
        name = graphene.String(required=True, description="Name of the product")
        description = graphene.String(required=True, description="Description of the product")

    ok = graphene.String()
    error = graphene.String()

    @classmethod
    def mutate_and_get_payload(self, root, info, **kwargs):

        # # fail permission check
        # if not self.has_permission(root, info, kwargs):
        #     return CreateProduct(ok=None, error=APIError.insufficient_permission.value)

        try:
            product = Product(name=safe_get(kwargs, "name"), description=safe_get(kwargs, "description"))
            product.save()
        except:
            return CreateProduct(ok=None, error="Error creating product")

        return CreateProduct(ok="yes", error=None)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()