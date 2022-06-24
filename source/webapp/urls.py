from django.contrib import admin
from django.urls import path

# from webapp.views import index_view, create_article
from webapp.views import sum_calc

urlpatterns = [
    # path("", index_view),
    # path("articles/add/", create_article)
      path("", sum_calc),
]
