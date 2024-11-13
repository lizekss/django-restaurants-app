from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    cover_photo = models.ImageField(upload_to='restaurant_covers/')

    def __str__(self):
        return self.name
