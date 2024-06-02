from django.urls import path
from . import views

urlpatterns = [
    path('',views.community_home, name = 'community-home'),
    path('forum/<str:forum_id>',views.forum, name = 'forum'),
    path('upload_media/',views.upload_media, name = 'upload_media'),
]