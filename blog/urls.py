from . import views
from django.urls import path
from .views import CommentUpdateView, CatListView, CommentDeleteView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('edit/<int:pk>/', CommentUpdateView.as_view(), name='edit_comment'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(),name='delete_comment'),
]