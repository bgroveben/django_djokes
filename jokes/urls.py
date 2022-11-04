from django.urls import path

from .views import JokeListView

app_name = 'jokes'
urlpatterns = [
    # Remember that only URL paths that begin with '/jokes/' will be handed
    # off to the URLConf of the jokes app, so '' will actually be '/jokes/'.
    path('', JokeListView.as_view(), name='list'),
    # The second argument of the path() function must be a view function (as
    # opposed to a class-based view), which is why you have to pass
    # JokeListView.as_view(). The as_view() method of class-based views
    # returns a view function.
]
