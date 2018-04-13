from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from benutzerverwaltung import settings

class Profile(models.Model):                    #Erweiterung des UserModels
    user = models.OneToOneField(User)
    salutation = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=30, default='')
    phone = PhoneNumberField(default='')
    fax = PhoneNumberField(default='')
    mobile = PhoneNumberField(default='')
    birthday = models.DateField(default='')
    departement = models.CharField(max_length=50, default='')
    rank = models.CharField(max_length=80, default='')
    activity = models.CharField(max_length=50, default='')
    institute = models.CharField(max_length=50, default='')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):       #Bei Registrierung das ProfilModel akutalisieren
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
