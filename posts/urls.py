from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView, PostDetailView,PostUpdateView


urlpatterns = [
    path("list/", PostListView.as_view(),name="list"),
    path("list/new", PostCreateView.as_view(),name="new"),
    path("list/<int:pk>/", PostDetailView.as_view(),name="detail"),
    path("list/<int:pk>/delete/", PostDeleteView.as_view(),name="delete"),
    path("list/<int:pk>/update/", PostUpdateView.as_view(),name="update"),
]



