from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, AnonymousUser
from django.db.models.signals import post_save
from copy import deepcopy
import pickle
import django

from settings import AUDITED_MODELS

from middleware import threadlocals

def update_record(sender, instance, created, **kwargs):
    registered = []
    for app, mdl in AUDITED_MODELS:
        registered.append(django.db.models.get_model(app, mdl))
    if sender in registered:
        userid = None
        ut = None
        details = ''
        requestuser = threadlocals.get_current_user()
        if isinstance(instance, User):
            user = instance
        else:
            try:
                user = instance.user
            except:
                user = None
        if requestuser != None:
            userid = requestuser.id
        details += 'model %s;' % sender.__name__
        if created == True:
            ut = UpdateType.objects.get(name = "joined")
            details += "new;"
        else:
            details += "edited;"
        if ut == None:
            ut = UpdateType.objects.get(name = "update")
        try:
            state = pickle.dumps(instance, protocol=0)
        except:
            state = None
        url = threadlocals.get_url()
        result = isinstance(user, AnonymousUser)
        if result:
            user = None
            details += "AnonymousUser, new account or a login.;"
        log = Log.objects.create(
            user = user, 
            update_type = ut,
            by_user_id = userid,
            url = url,
            details = details,
            state = state
            )

post_save.connect(update_record)

class UpdateType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Log(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    by_user_id = models.IntegerField(max_length=150, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    update_type = models.ForeignKey(UpdateType)
    update_date = models.DateTimeField(auto_now_add=True, blank=False, null=False, db_index=True)
    state = models.TextField(blank=True, null=True, default=None)
    def __unicode__(self):
        return "%s %s %s" % (self.update_type.name, self.update_date, self.details)
    
    class Meta:
        ordering = ['-update_date']