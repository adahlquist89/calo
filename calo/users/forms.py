from django import forms
from users.models import CaloUser, Profile
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#class RegisterForm(forms.Form):
#	username = forms.Charfield(max_length=45, label='Username')
#	password = forms.Charfield(max_length=30, label='Password', widget=forms.PasswordInput)
#	first_name = forms.Charfield(max_length=30, label='First name')
#	last_name = forms.Charfield(max_length=30, label='Last name')
#	birth_date = forms.DateField()
#
#class LoginForm(forms.Form):
#	username = forms.Charfield(max_length=45, label='Username')
#	password = forms.Charfield(max_length=30, label='Password', widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	
    class Meta:
        model = CaloUser
        fields = ('email', 'first_name','last_name', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user