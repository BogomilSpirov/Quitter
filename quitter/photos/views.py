from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from . import forms


# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddPhotoView(views.CreateView):
	template_name = 'photos/add_photo.html'
	form_class = forms.PhotosForm
	success_url = reverse_lazy('profile_details')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditPhotoView(views.UpdateView):
	model = models.Photos
	template_name = 'photos/edit_photo.html'
	form_class = forms.PhotosForm
	success_url = reverse_lazy('profile_details')
	pk_url_kwarg = "pk"

	def form_valid(self, form):
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.user = self.request.user
			self.object.save()
			return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DeletePhotoView(views.DeleteView):
	model = models.Photos
	template_name = 'photos/delete_photo.html'
	success_url = reverse_lazy('profile_details')
	pk_url_kwarg = "pk"
