from django.db import models

from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True) # опциональное поле

    avatar = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    bio = models.TextField()
    phone = models.CharField(max_length=13)
    # last_join = models.DateField(auto_now = True) ***post save signal

    def __str__(self):
        return f'Profile of {self.user.username}'