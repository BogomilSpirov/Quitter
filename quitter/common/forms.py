from django import forms
from quitter.accounts import models
from .models import Comment


class EditProfileForm(forms.ModelForm):
	GENDER_CHOICES = [
		('male', 'Male'),
		('female', 'Female'),
		('do_not_show', 'Do Not Show'),
	]

	class Meta:
		model = models.QuitterUser
		fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'profile_picture']

	first_name = forms.CharField(
		max_length=50,
		widget=forms.TextInput()
	)
	last_name = forms.CharField(
		max_length=50,
		widget=forms.TextInput()
	)
	email = forms.EmailField(
		widget=forms.EmailInput()
	)
	date_of_birth = forms.DateField(
		widget=forms.DateInput()
	)
	gender = forms.ChoiceField(
		choices=GENDER_CHOICES,
		widget=forms.Select(),
	)
	profile_picture = forms.URLField(
		max_length=1000,
		widget=forms.URLInput()
	)
	first_name.widget.attrs.update({'autocomplete': 'off'})
	last_name.widget.attrs.update({'autocomplete': 'off'})
	email.widget.attrs.update({'autocomplete': 'off'})
	gender.widget.attrs.update({'autocomplete': 'off'})
	profile_picture.widget.attrs.update({'autocomplete': 'off'})


class AddCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text']

	comment_text = forms.CharField(
		max_length=780,
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Comment...'
			}
		)
	)


class SearchForm(forms.Form):
	search_text = forms.CharField(
		max_length=50,
		required=False,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Search...'
			}
		)
	)
