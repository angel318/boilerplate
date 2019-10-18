import os
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext as _
from ...common.models import FieldDefaultsAbstracts

def path_and_rename(obj, filename):
    ext = filename.split('.')[-1]
    path = 'examples/'

    filename = '{}.{}'.format(uuid4().hex, ext)

    # return the whole path to the file
    return os.path.join(path, filename)

class Object(FieldDefaultsAbstracts):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=path_and_rename,
        blank=True,
        default=''
    )

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None
        super(Object, self).save(*args, **kw)
        if old and old.image != self.image:
            if old.image != '':
                print('Cambios detectados en ImageField')
                print('Eliminando archivo', old.image)
                old.image.delete(save=False)
        else:
            print('No se cambio la imagen')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Object'
        verbose_name_plural = 'Objects'
