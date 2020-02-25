from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_donation = models.DecimalField(max_digits=8, decimal_places=2, default=5.00)
    onboarded = models.CharField(max_length=128, default='False')

    def __str__(self):
        return self.user.username

    def get_absolute_url_detail(self):
        """ Returns a fully-qualified path for a page (/my-new-value-page). """
        path_components = {'slug': self.slug}
        return reverse('detail_profile', kwargs=path_components)
    
    def get_absolute_url_update(self):
        """ Returns a fully-qualified path for a page (/my-new-value-page). """
        path_components = {'slug': self.slug}
        return reverse('update_profile', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.username, allow_unicode=True)

        # Call save on the superclass.
        return super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

