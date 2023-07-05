from django.db import models
from django.contrib.auth.models import User

class Retailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="retailer")
    phone = models.PositiveBigIntegerField(default=0, blank=True)
    address = models.TextField(max_length=512, default="", blank=True)
    google_map = models.URLField(max_length=1024, default="", blank=True)

    def __str__(self) -> str:
        return self.user.username
