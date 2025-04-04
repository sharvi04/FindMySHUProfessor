from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import MemberProfile, StudentProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Automatically create a profile for Members or Students based on the group. """
    if created:
        if instance.groups.filter(name="Member").exists():  # Check if user is in the 'Member' group
            MemberProfile.objects.create(user=instance)
        elif instance.groups.filter(name="User").exists():  # Check if user is in the 'User' group
            StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ Save the related profile whenever the user model is updated. """
    if hasattr(instance, 'member_profile'):  # Save MemberProfile if it exists
        instance.member_profile.save()
    elif hasattr(instance, 'student_profile'):  # Save StudentProfile if it exists
        instance.student_profile.save()
