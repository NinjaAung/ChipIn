from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Value(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    value = models.CharField(max_length=100)


    def __str__(self):
            return self.value

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(Value.value, allow_unicode=True)
        return super(Value, self).save(*args, **kwargs)
