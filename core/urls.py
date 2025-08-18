from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("profile", views.profile, name="profile"),
    path("profile/<str:user>/", views.profile, name="profile"),
    path("post", views.create_post, name="post"),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('post/<str:user>/<int:post_id>', views.post_detail, name="post"),
    path('post/<int:post_id>/edit/', views.edit_post, name='post_edit'),
    path('del/<int:post_id>/', views.del_post, name='delete_post'),
    path("follow/<str:username>", views.follow_user, name="follow")

]