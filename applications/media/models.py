from django.db import models
from model_utils.models import TimeStampedModel
from applications.users.models import User


class Album(TimeStampedModel):


    titulo = models.CharField(max_length=30,unique=True)
    descripcion = models.CharField(max_length=300)
    likes = models.ManyToManyField(User,blank=True)
    portada = models.ImageField(upload_to='portadas',blank=True,null=True)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,related_name= 'album_user'
    )

    def __str__(self):
        return str(self.pk)+ '-' +self.titulo

class Multimedia(TimeStampedModel):

    Type_Fields = (
        ('I','Imagen'),
        ('V','Video'),
    )

    descripcion = models.CharField(max_length=300)
    titulo = models.CharField(max_length=100,null=True,blank=True)
    likes = models.IntegerField(default=0)
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="album_image"
    )
    contenido = models.FileField(upload_to='contenido', blank=True, null=True)
    tipo = models.CharField(max_length=1,choices=Type_Fields,blank=True,null=True)

    def __str__(self):
        return str(self.pk) + '-'  + self.descripcion

'''
class VideoFile(Multimedia):
    video = models.FileField(upload_to='videos', blank=True, null=True)

    def __str__(self):
        return self.pk

class ImageFile(Multimedia):
    imagen = models.ImageField(upload_to='imagenes', blank=True, null=True)

    def __str__(self):
        return self.pk
'''


