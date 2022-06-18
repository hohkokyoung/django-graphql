import graphene

import project.auth.graphql.schema as auth_schema
import project.product.graphql.schema as product_schema
import project.order.graphql.schema as order_schema
import project.user.graphql.schema as user_schema

class Query(
    auth_schema.Query,
    product_schema.Query,
    order_schema.Query,
    user_schema.Query,
    graphene.ObjectType,
):
    pass

class Mutation(
    auth_schema.Mutation,
    product_schema.Mutation,
    order_schema.Mutation,
    user_schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)