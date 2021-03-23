
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# from ingredients.schema import schema

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql$', GraphQLView.as_view(graphiql=True)),

    # path('admin/', admin.site.urls),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    # path('', include('books.urls')),
    # path('', include('quiz.urls'))
    # path('', include('contacts.urls'))
]
