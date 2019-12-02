from django import forms
from .models import Url


class UrlForm(forms.ModelForm):
    long_url = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-url',
            'placeholder': 'Enter long URL'
        }),
        label='',
    )

    class Meta:
        model = Url
        fields = ('long_url',)
