from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    profile_pic = models.ImageField(upload_to="profiles/", default="profiles/default.jpeg")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return "Username: "+ self.full_name
    


