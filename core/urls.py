from django.urls import path
from . import views # Import the views from our current app (core)

app_name = 'core' # This is important! It gives a namespace to our app's URLs.

# This list maps specific web addresses (paths) to our view functions.
urlpatterns = [
    # When someone visits the empty path '' (meaning just /),
    # Django will call the 'index' function from our views.py.
    # We also give it a name='index' so we can refer to it easily later.
    path('', views.index, name='index'),
]
