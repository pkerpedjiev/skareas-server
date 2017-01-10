from django.db import models

import django.db.models as ddm

class SkiArea(ddm.Model):
    uid = models.CharField(max_length=32)
    name = models.TextField()
    edited_by = models.ForeignKey('auth.User', related_name="ski_areas", on_delete=models.CASCADE)
# Create your models here.
