from django.db import models
from django.conf import settings


class Retailer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="retailer")
    phone = models.PositiveBigIntegerField(default=0, blank=True)
    address = models.TextField(max_length=512, default="", blank=True)
    google_map = models.URLField(max_length=1024, default="", blank=True)

    def __str__(self) -> str:
        return str(self.user.name)
