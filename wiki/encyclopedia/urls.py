from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:content>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create", views.new_page, name="create")
]
