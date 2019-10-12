from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from django.contrib.auth.models import UserManager
# from django import forms
# from django.forms import ModelForm
# from django.contrib.auth.models import User


# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20,null=False)
#     company = models.CharField(max_length=30, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
# Create your models here.
class myUserManager(BaseUserManager):
	def create_user(self, email, password, **kwargs):
		user = self.model(email=self.normalize_email(email), is_active=True, **kwargs)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email,password, **kwargs):
		user = self.model(email=self.normalize_email(email), is_superuser=True, is_active=True, **kwargs)
		user.set_password(password)
		user.save()
		return user



# ############### Before #################################### 
class myUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=30, unique=True)
	phone = models.CharField(max_length=15,null=False)
	created = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['phone', 'is_staff']

	objects = myUserManager()

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def get_username(self):
		return self.email
	
	def __str__(self):
		return self.email

# ############### Before #################################### 

# 	def has_perm(self, perm, obj=None):
# 		"Does the user have a specific permission?"
# 		return True

# 	def has_module_perms(self, app_label):
# 		"Does the user have permissions to view the app `app_label`?"
# 		return True

# 	@property
# 	def is_staff(self):
# 		"Is the user a member of staff?"
# 		return self.is_admin

	



# 	# def set_password(self, raw_password):
#  #        # whatever logic you need to set the password for your user or maybe
# 	# 	self.user.set_password(raw_password)
# 	# def save(self, commit=True):
# 	# 	user = super(RegisterForm, self).save(commit=False)
#  #        first_name, last_name = self.cleaned_data["username"].split()
#  #        user.first_name = first_name
#  #        user.last_name = last_name
#  #        user.email = self.cleaned_data["email"]
#  #        if commit:
#  #            user.save()
# 	# 	return user

# 	def __str__(self):
# 		return self.email