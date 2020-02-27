from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_donation = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username

    # def get_absolute_url_detail(self):
    #     """ Returns a fully-qualified path for a page (/my-new-value-page). """
    #     path_components = {'slug': self.slug}
    #     return reverse('detail_profile', kwargs=path_components)
    
    # def get_absolute_url_update(self):
    #     """ Returns a fully-qualified path for a page (/my-new-value-page). """
    #     path_components = {'slug': self.slug}
    #     return reverse('update_profile', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(User.username, allow_unicode=True)
        # Call save on the superclass.
        return super(Profile, self).save(*args, **kwargs)

class Value(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=100)


    def __str__(self):
            return self.title

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(Value.title, allow_unicode=True)
        return super(Value, self).save(*args, **kwargs)

    


@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



