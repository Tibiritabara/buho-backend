"""
Graphene schema definition
"""
import graphene

import compras.mutations
import compras.queries


class Query(
    compras.queries.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    compras.mutations.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
