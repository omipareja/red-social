from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.forms import model_to_dict
from .managers import UserManager


class Category(models.Model):

    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = (
        ('M','Masculio'),
        ('F','Femenino'),
        ('O','Otros'),
    )
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    categoria = models.ManyToManyField(Category,blank=True)
    full_name = models.CharField('Nombres',max_length=100)
    genero = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    date_birth = models.DateField('Fecha Nacimiento',blank=True,null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name','email',]

    objects = UserManager()

    '''
    def get_image(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        return '{}{}'.format(STATIC_URL, 'img/noimage.png')
    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions','last_login','groups','date_birth'])
        item['genero'] = {'id':self.genero,'name':self.get_genero_display()}
        item['avatar'] = self.get_image()
        return item
        
    '''
    def __str__(self):
        return str(self.pk) + '-' +self.full_name