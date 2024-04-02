from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.EvlonPostsView.as_view(), name="evlon-posts"),
]