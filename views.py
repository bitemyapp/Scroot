from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_detail
from audit.models import *
from audit.forms import LogForm
from django.contrib import admin
from django import forms

import pickle

# Straight-up: this should be in Django core if it isn't already.
def form_factory(inst):
    # class of the unpickled object
    object_model = inst.__class__
    class _GenericMF(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(_GenericMF, self).__init__(*args, **kwargs)
            for label in self.fields:
                self.fields[label].help_text = None
                if self.fields[label].__class__ == forms.ModelChoiceField:
                    lab = self.fields[label].label.lower()
                    backflip = getattr(self.instance, lab)
                    self.fields[label] = forms.CharField(max_length=200)
        class Meta:
            model = object_model
    f = _GenericMF(instance=inst)
    for label in f.fields:
        if f.fields[label].__class__ == forms.ModelChoiceField:
            # you'd think I'd be able to eliminate this in either __init__ or
            # here eh?
            f.fields[label] = forms.CharField(max_length=200)
    return f

def log(request, object_id):
    isuser = False
    log = Log.objects.get(id = object_id)
    state = pickle.loads(str(log.state))
    stateform = form_factory(state)
    if isinstance(state, User):
        isuser = True
    return object_detail(
        request,
        queryset = Log.objects.all(),
        object_id = object_id,
        template_name = 'audit/detail.html',
        extra_context = {'stateform':stateform, 'isuser':isuser}
    )
