from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django_reverse_admin import ReverseModelAdmin

from .models import Retailer


@admin.register(Retailer)
class RetailerAdmin(ReverseModelAdmin):
    inline_type = "stacked"
    inline_reverse = [
        ("user", {"form": UserCreationForm, "fields": ["username", "password1", "password2"]}, ),
    ]
    fieldsets = (
        (
            None,
            {"fields": ("phone", "address", "google_map")},
        ),
    )
    list_display = [
        "user",
        "phone",
    ]
