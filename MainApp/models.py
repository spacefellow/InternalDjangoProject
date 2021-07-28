from django.db import models
from django.urls import reverse


class BlockInfo(models.Model):
    height = models.IntegerField(default=0, unique=True)
    hash = models.CharField('Хэш блока', max_length=200)
    timestamp = models.IntegerField(default=0)
    miner = models.CharField('Адрес майнера', max_length=200)
    transactionCount = models.IntegerField(default=0)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return str(self.height)

    def get_absolute_url(self):
        return reverse('post', kwargs={'block_slug': self.slug})

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

