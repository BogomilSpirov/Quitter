from django import forms
from . import models
from ..photos.models import Photos


class QuitForm(forms.ModelForm):
    class Meta:
        model = models.Quit
        fields = ['title', 'photo', 'description', 'tagged_people']

    title = forms.CharField(
        max_length=780,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title...'
            }
        )
    )
    description = forms.CharField(
        max_length=780,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Description...'
            }
        )
    )
    title.widget.attrs.update({'autocomplete': 'off'})
    description.widget.attrs.update({'autocomplete': 'off'})

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].queryset = Photos.objects.filter(user=user)
