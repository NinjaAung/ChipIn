from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(User.username, allow_unicode=True)
        return super(Profile, self).save(*args, **kwargs)

class MonthlyDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_donation')
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.amount)
    
    
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(MonthlyDonation.amount, allow_unicode=True)
        return super(MonthlyDonation, self).save(*args, **kwargs)
    
@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



