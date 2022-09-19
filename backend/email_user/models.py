from django.contrib.auth.models import (
  AbstractBaseUser,
  BaseUserManager,
  PermissionsMixin,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class EmailUserManager(BaseUserManager):

  def create_user(self, email, username, password=None):
    if not email:
      raise ValueError("email required")

    email = self.normalize_email(email)
    user = self.model(email=email, username=username)

    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, username, password):
    user = self.create_user(email, username, password)
    user.is_superuser = True
    user.is_staff = True

    user.save(using=self._db)

    return user

username_validators = UnicodeUsernameValidator()

class EmailUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField("email address", unique=True)
  username = models.CharField(
      "username",
      max_length=20,
      unique=True,
      validators = [username_validators],
  )

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'

  is_staff = models.BooleanField(
      'is staff',
      default=False,
  )
  is_active = models.BooleanField(
      'is active',
      default=True,
  )
  date_joined = models.DateTimeField(
    'date joined',
    auto_now_add=True,
  )

  objects = EmailUserManager()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username',]

  def __str__(self):
    return self.email

  @property
  def is_authenticated(self):
    return True

  @property
  def is_anonymous(self):
    return False
