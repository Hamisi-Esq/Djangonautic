from django.urls import path
from djangonautic import views


urlpatterns = [
    path("", views.article_list),
]
