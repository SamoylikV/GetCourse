from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, TeacherProfile
from django.contrib.auth.forms import AuthenticationForm



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('user_type',)


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['first_name', 'last_name', 'description', 'avatar', 'pdf_file']
