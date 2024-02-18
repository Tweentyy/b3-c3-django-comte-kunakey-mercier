from django import forms
from .models import Site
import re

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url', 'username', 'password']

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

    def clean_url(self):
        url = self.cleaned_data['url']
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not re.match(regex, url):
            raise forms.ValidationError('L\'URL doit commencer par http ou https et suivre le format standard d\'une URL.')
        return url