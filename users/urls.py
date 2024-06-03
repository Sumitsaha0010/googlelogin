from django.urls import path
from users.views.home import home
from users.views.logout import logout_view

urlpatterns = [
    path("",home),
    path("logout", logout_view),
]
