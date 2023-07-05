from django.contrib import admin
from django.contrib.auth.models import User

from .models import Retailer


class UserInline(admin.StackedInline):
    model = User
    fields = ["username", "password1", "password2"]
    fk_name = "user"


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    inlines = [UserInline]
    fieldsets = (
        (
            None,
            {"fields": ("user", "phone", "address", "google_map")},
        ),
    )
    list_display = [
        "user",
        "phone",
    ]
