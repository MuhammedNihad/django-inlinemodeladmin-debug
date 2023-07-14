from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django_reverse_admin import ReverseModelAdmin, ReverseInlineModelAdmin

from .models import Retailer


class CustomReverseInlineModelAdmin(ReverseInlineModelAdmin):
    """    
    By overriding ReverseInlineModelAdmin and setting can_delete to False in the formset, the delete
    checkbox is hidden, preventing the deletion of the Retailer object and its parent object in the User
    model when using the UserCreationForm as the form in inline_reverse attribute of RetailerAdmin class.
   
    Otherwise, If an attempt is made to delete the retailer model object by checking the checkbox and
    hitting save button without providing a new password in both the password and password confirmation fields
    (similar to when creating new user, which can be inconvenient in this case), a validation ValueError will
    be raised by UserCreationForm with the message "The User could not be changed because the data didn't validate".
    """

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.can_delete = False
        return formset


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

    def get_inline_instances(self, request, obj=None):
        """
        Overrides the get_inline_instances method to use CustomReverseInlineModelAdmin class for reverse inline instances.
        """
        inline_instances = super().get_inline_instances(request, obj)
        for inline in inline_instances:
            if isinstance(inline, ReverseInlineModelAdmin):
                inline.__class__ = CustomReverseInlineModelAdmin
        return inline_instances
