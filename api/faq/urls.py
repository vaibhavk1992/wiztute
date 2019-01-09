from django.urls import path
from .views import ListFaqView
from . import views


urlpatterns = [
    path('', ListFaqView.as_view(), name="something1"),
    path('create',views.setUp, name="something")
]