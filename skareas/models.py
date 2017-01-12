from django.db import models

import django.db.models as ddm

class SkiArea(ddm.Model):
    uid = models.CharField(max_length=32)
    name = models.TextField()
# Create your models here.
