from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,email,first_name,  middle_name,last_name,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email = self.normalize_email(email),
            password=password,
            middle_name = middle_name,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    
    
    def create_staffuser(self,email,password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
        )
        user.save(using = self._db)
        return user
    def create_superuser(self,email,first_name,middle_name,last_name,password=None,):
        user = self.create_user(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        user.save(using = self._db)
        return user


class  User(AbstractBaseUser,PermissionsMixin):
    email =  models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','middle_name','last_name']
    objects = UserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.first_name + " " + self.middle_name
    def get_short_name(self):
        return self.first_name


    # @property
    # def is_staff(self):
    #     return self.is_staff
    
    # @property
    # def is_admin(self):
    #     return self.is_admin
    
    # @property
    # def is_active(self):
    #     return self.is_active
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    
     