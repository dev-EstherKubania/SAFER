from django.urls import path
from . import views

urlpatterns = [
    path('',views.community_home, name = 'community-home'),
    path('new_forum', views.create_forum, name = 'create_forum'),
    path('forum/<str:forum_id>',views.forum, name = 'forum'),
    path('upload_media/',views.upload_media, name = 'upload_media'),
]