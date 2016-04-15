from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from main.models import Case, Update, CustomUser

class SignUpForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

	class Meta:
		model = CustomUser
		fields = ('email',)

class LoginForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())


class CreateCaseForm(forms.ModelForm):
	class Meta:
		model = Case
		exclude = ['user']

class CreateUpdateForm(forms.ModelForm):
	image = forms.ImageField(required=False)
	image_text = forms.CharField(required=False)

	class Meta:
		model = Update
		exclude = ['case']
