from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput()
    )
    email = forms.CharField(
        max_length=50,
        widget=forms.EmailInput()
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password'
            }
        )
    )
    username.widget.attrs.update({'autocomplete': 'off'})
    email.widget.attrs.update({'autocomplete': 'off'})
    password1.widget.attrs.update({'autocomplete': 'off'})
    password2.widget.attrs.update({'autocomplete': 'off'})


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(),
        error_messages={
            'required': 'Please provide your username.',
            'invalid': 'Invalid username.',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password'
            }
        ),
    )
    username.widget.attrs.update({'autocomplete': 'off'})
    password.widget.attrs.update({'autocomplete': 'off'})
