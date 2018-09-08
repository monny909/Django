from django import forms
from .models import Report, News, Cases, Institution, Profile, Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('title', 'uploaded_file1','uploaded_file2','uploaded_file3', 'description',)

class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'thumbnail', 'description',)


class AddCasesForm(forms.ModelForm):

    class Meta:
        model = Cases
        fields = ('title', 'uploaded_file1','uploaded_file2','uploaded_file3', 'description',)

class AddSchoolForm(forms.ModelForm):

    class Meta:
        model = Institution
        fields = ('name', 'bio',)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','password',]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'institution',]

class loginForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ( )


class AddActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['title', 'description',]
