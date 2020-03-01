from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Cause(models.Model):
    organization_name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)









    def get_absolute_url(self):
        return reverse('cause_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.organization_name}'