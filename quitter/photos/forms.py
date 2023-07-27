from . import models as models
from django import forms


class PhotosForm(forms.ModelForm):
	class Meta:
		model = models.Photos
		fields = ['name', 'about', 'url']

	name = forms.CharField(
		max_length=50,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Name...'
			}
		)
	)
	about = forms.CharField(
		max_length=780,
		widget=forms.Textarea(
			attrs={
				'placeholder': 'About It...'
			}
		)
	)
	url = forms.URLField(
		max_length=1000,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Image Address...'
			}
		)
	)
	name.widget.attrs.update({'autocomplete': 'off'})
	about.widget.attrs.update({'autocomplete': 'off'})
	url.widget.attrs.update({'autocomplete': 'off'})
