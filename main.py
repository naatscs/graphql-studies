import graphene
from fastapi import FastAPI, Query
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from schemas import PostSchema


app = FastAPI()

class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, content):
        post = PostSchema(title=title, content=content)

class PostMutations(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()

app.mount("/graphql",GraphQLApp(schema=graphene.Schema(mutation=PostMutations),on_get=make_graphiql_handler()))