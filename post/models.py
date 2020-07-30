from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi', auto_now_add=True)
    #verbose_name ekranda görünmesini istediğin yazıyı yazar.

    #Bu işlem başlığın post ismi olarak görünmesini sağlar.
    def __str__(self):
        return self.title

    #URL adreslerinin dinamik bi şekilde isimlenmesini ve gezinmeyi sağlar.
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id':self.id})
