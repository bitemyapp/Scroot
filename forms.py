from django import forms
from audit.models import *

class LogForm(forms.ModelForm):
    class Meta:
        model = Log