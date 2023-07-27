from django.contrib.auth import get_user_model
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from pyperclip import copy
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from quitter.quits.models import Quit
from . import forms
from quitter.photos.models import Photos
from . import models

# Create your views here.

UserModel = get_user_model()


class Index(views.ListView):
    template_name = 'common/base.html'
    model = Quit
    context_object_name = 'quits'
    paginate_by = 5

    def get_queryset(self):
        return Quit.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = forms.AddCommentForm()
        context['search_form'] = forms.SearchForm()
        search_text = self.request.GET.get('search_text')
        if search_text:
            context['quits'] = Quit.objects.filter(title__icontains=search_text)
        if self.request.user.is_authenticated:
            for quit in context['quits']:
                quit.already_liked = quit.like_set.filter(user=self.request.user).exists()
        return context


@method_decorator(login_required, name='dispatch')
class ProfileDetailsView(views.TemplateView):
    template_name = 'common/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['photos'] = Photos.objects.filter(user=user)
        context['quits'] = Quit.objects.filter(user=user)
        return context


@method_decorator(login_required, name='dispatch')
class EditProfileView(views.UpdateView):
    model = UserModel
    template_name = 'common/edit_profile.html'
    form_class = forms.EditProfileForm
    success_url = reverse_lazy('profile_details')
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DeleteProfileView(views.DeleteView):
    model = UserModel
    template_name = 'common/delete_profile.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['age'] = date.today().year - user.date_of_birth.year
        return context

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.photos_set.all().delete()
        user.quits_set.all().delete()
        return super().delete(request, *args, **kwargs)


class ProfilePreviewView(views.DetailView):
    model = UserModel
    template_name = 'common/preview_profile.html'
    context_object_name = 'user'
    pk_url_kwarg = "pk"


@login_required
def like_functionality(request, pk):
    quit = Quit.objects.get(id=pk)
    kwargs = {
        'for_quit': quit,
        'user': request.user
    }
    like_object = models.Like.objects.filter(**kwargs).first()
    if like_object:
        like_object.delete()
    else:
        new_like_object = models.Like(**kwargs)
        new_like_object.save()
    return redirect('index')


@login_required
def share_functionality(request, pk):
    copy(request.META['HTTP_REFERER'] + f"quits/preview_quit/{pk}")
    return redirect('index')


@login_required
def follow_functionality(request, pk):
    user = UserModel.objects.get(id=pk)
    kwargs = {
        'for_user': user,
        'user': request.user
    }
    follow_object = models.Follow.objects.filter(**kwargs).first()
    if follow_object:
        follow_object.delete()
    else:
        new_follow_object = models.Follow(**kwargs)
        new_follow_object.save()
    return redirect('profile_preview', pk=pk)


@login_required
def comment_functionality(request, pk):
    quit = Quit.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.for_quit = quit
            new_comment.user = request.user
            new_comment.save()
    return redirect('index')
