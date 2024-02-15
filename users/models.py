from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from common.utils import generate_unique_id


class UserManager(BaseUserManager):
  def create_superuser(self, email, password):
    user = self.model(
      email=self.normalize_email(email),
      username=email[:email.index('@')],
    )
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.password = make_password(password)
    user.save(using=self._db)


    return user


class User(AbstractUser):
  id = models.BigIntegerField(primary_key=True, blank=True)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  first_name = models.CharField(max_length=50, blank=True)
  last_name = models.CharField(max_length=50, blank=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  last_login = models.DateTimeField(auto_now=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return True

  def save(self, *args, **kwargs):
    if not self.id:
      self.id = generate_unique_id(self, 111)

    super().save(*args, **kwargs)
