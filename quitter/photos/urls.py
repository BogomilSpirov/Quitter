from django.urls import path
from . import views as views

urlpatterns = [
	path('add_photo/', views.AddPhotoView.as_view(), name='add_photo'),
	path('edit_photo/<int:pk>/', views.EditPhotoView.as_view(), name='edit_photo'),
	path('delete_photo/<int:pk>/', views.DeletePhotoView.as_view(), name='delete_photo'),
]
