from django.urls import path
from . import views as views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profile_details/', views.ProfileDetailsView.as_view(), name='profile_details'),
    path('profile_edit/<int:pk>/', views.EditProfileView.as_view(), name='profile_edit'),
    path('profile_delete/<int:pk>/', views.DeleteProfileView.as_view(), name='profile_delete'),
    path('profile_preview/<int:pk>/', views.ProfilePreviewView.as_view(), name='profile_preview'),
    path('like/<int:pk>/', views.like_functionality, name='like'),
    path('share/<int:pk>/', views.share_functionality, name='share'),
    path('follow/<int:pk>/', views.follow_functionality, name='follow'),
    path('comment/<int:pk>/', views.comment_functionality, name='comment'),
]
