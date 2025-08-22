from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "blog"

# DRF router for api endpoints
router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")
router.register(r"comments", views.CommentViewSet, basename="comment")

urlpatterns = [
    # Frontend pages
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # API
    path("api/", include(router.urls)),
]
