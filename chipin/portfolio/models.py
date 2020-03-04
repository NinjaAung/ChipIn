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
    

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(Cause.organization_name, allow_unicode=True)
        return super(Cause, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-value-page). """
        path_components = {'slug': self.slug}
        return reverse('cause_detail', kwargs=path_components)










    def get_absolute_url(self):
        return reverse('cause_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.organization_name}' + ' ' + self.category