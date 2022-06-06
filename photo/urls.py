from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('new_image/', views.new_image, name='new_image'),
    path('comments/<int:image_id>/', views.comments, name='comments'),
    path('like/<int:post_id>/', views.like_post, name='like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)