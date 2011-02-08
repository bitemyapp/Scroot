from django import forms
from audit.models import *

# Muy complejo.
class LogForm(forms.ModelForm):
    class Meta:
        model = Log
