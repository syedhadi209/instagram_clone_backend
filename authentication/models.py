from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,username, first_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, first_name, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    


class CustomUser(AbstractUser):
    profile_picture = models.CharField(max_length=500,null=True, default=None)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['password', 'first_name', 'email']


