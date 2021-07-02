from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager,BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.


'''

class CustomUser(AbstractUser):
    #username = None
    phno = models.CharField(unique=True,null=False,blank=False,max_length=13)

    objects = UserManager()

    USERNAME_FIELD = phno        
    REQUIRED_FIELDS=[]        

'''           


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phn, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phn:
            raise ValueError('The given phone must be set')
        
        user = self.model(phn=phn, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phn, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phn, password, **extra_fields)

    def create_superuser(self, phn, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phn, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^(0|91|\+91)?-?[789]\d{9}$', message="Phone number must be entered in the format: '+919999999999'. Up to 10 digits allowed.")
    phn = models.CharField(_('phone number'), validators=[phone_regex], max_length=17, unique=True) # validators should be a list
    


    USERNAME_FIELD = 'phn'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
 
 