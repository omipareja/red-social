from django.db import models
from django.forms import model_to_dict

from applications.users.models import User
from applications.media.models import Multimedia
from model_utils.models import TimeStampedModel
# Create your models here.

class Comentarios(TimeStampedModel):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    publicacion = models.ForeignKey(
        Multimedia,
        on_delete=models.CASCADE
    )
    comentario = models.CharField(max_length=250)

    def toJSON(self):
        item = model_to_dict(self,exclude=['id','modified'])
        item['usuario'] = self.usuario.username
        item['created'] = self.created.strftime('%Y-%m-%d')
        return item
    def __str__(self):
        return  str(self.pk) + '-'+self.usuario.username