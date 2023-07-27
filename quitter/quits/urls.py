from django.urls import path
from . import views as views


urlpatterns = [
	path('add_quit/', views.AddQuitView.as_view(), name='add_quit'),
	path('edit_quit/<int:pk>/', views.EditQuitView.as_view(), name='edit_quit'),
	path('delete_quit/<int:pk>/', views.DeleteQuitView.as_view(), name='delete_quit'),
	path('preview_quit/<int:pk>/', views.PreviewQuitView.as_view(), name='preview_quit'),
]

