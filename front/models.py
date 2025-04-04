from django.db import models
from django.contrib.auth.models import Group
from auditlog.registry import auditlog


# Create your models here.
def create_groups():
    Group.objects.get_or_create(name='User')
    Group.objects.get_or_create(name='Member')

create_groups()
