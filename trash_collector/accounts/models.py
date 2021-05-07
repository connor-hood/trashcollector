from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class AccountsManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_employee = True
        user.is_superuser = True
        user.is_customer = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Our custom user model that adds a new field to the default django user model"""
    is_employee = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    is_customer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    loginuser = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountsManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_employee

    def has_module_perms(self, app_label):
        return True
