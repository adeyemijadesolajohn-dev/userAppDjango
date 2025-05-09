from django.db import models
from django.contrib.auth.models import User


# Create your models here.
GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    image = models.ImageField(
        upload_to="profile",
        null=True,
        blank=True,
        default="https://w7.pngwing.com/pngs/84/165/png-transparent-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper-united-states-thumbnail.png",
    )
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.fullname
