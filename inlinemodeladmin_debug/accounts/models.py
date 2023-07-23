import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with email and without username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Default custom user model.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = None  # type: ignore
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    name = models.CharField(_("Name of User"), max_length=150)
    email = models.EmailField(_("Email address of User"), unique=True, blank=False)
    date_modified = models.DateTimeField(auto_now=True)

    # Flags for user types
    is_retailer = models.BooleanField(
        _("Retailer status"),
        default=False,
        help_text=_("Designates whether the user should treated as retailer"),
    )
    is_shop_owner = models.BooleanField(
        _("Shop owner status"),
        default=False,
        help_text=_("Designates whether the user should treated as shop owner"),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()
