from django.contrib import admin
from django.urls import path

from djangonautic import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", views.about), 
    path("", views.homepage),
]
