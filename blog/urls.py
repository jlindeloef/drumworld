from . import views
from django.urls import path
from .views import CommentUpdateView, CatListView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('<slug:slug>', CommentUpdateView.as_view(), name='edit_comment'),
]