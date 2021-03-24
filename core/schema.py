import graphene

import ingredients.schema
import contacts.schema


class Query(ingredients.schema.Query, contacts.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(contacts.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)