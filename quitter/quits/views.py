from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.utils.decorators import method_decorator
from django.views import generic as views
from . import forms
from .models import Quit


# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddQuitView(views.CreateView):
    template_name = 'quits/add_quit.html'
    form_class = forms.QuitForm
    success_url = reverse_lazy('profile_details')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditQuitView(views.UpdateView):
    model = models.Quit
    template_name = 'quits/edit_quit.html'
    form_class = forms.QuitForm
    success_url = reverse_lazy('profile_details')
    pk_url_kwarg = "pk"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DeleteQuitView(views.DeleteView):
    model = models.Quit
    template_name = 'quits/delete_quit.html'
    success_url = reverse_lazy('profile_details')
    pk_url_kwarg = "pk"


class PreviewQuitView(views.DetailView):
    model = Quit
    template_name = 'quits/preview_quit.html'
    context_object_name = 'quit'
    pk_url_kwarg = "pk"
