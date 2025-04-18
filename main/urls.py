from django.urls import path
from main import views


app_name = "main"
urlpatterns = [
    path("", views.home, name="home"),
    path("statistics/", views.statistics, name="statistics"),
    path("support/", views.support, name="support"),
    path("favourites/", views.favourites, name="favourites"),
    path("history/", views.history, name="history"),
]
