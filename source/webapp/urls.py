from django.contrib import admin
from django.urls import path

from webapp.views import sum_calc

urlpatterns = [
    path("", sum_calc),
]
