from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Resume

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'placeholder': 'you@example.com',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Choose a username',
            'password1': 'Create a password',
            'password2': 'Confirm your password',
        }
        for name, field in self.fields.items():
            field.widget.attrs.setdefault('placeholder', placeholders.get(name, field.label))
            field.widget.attrs.setdefault('autocomplete', 'new-password' if name.startswith('password') else name)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
