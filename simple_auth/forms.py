from django import forms

from .models import Password


class PasswordAdminForm(forms.ModelForm):
    """
    Form class for administering passwords in the admin
    """
    class Meta:
        model = Password
        fields = '__all__'


class PasswordForm(forms.Form):
    """
    Form class for inputting shared passwords
    """
    password = forms.CharField(widget=forms.PasswordInput)
    url = forms.CharField(widget=forms.HiddenInput, required=False)
