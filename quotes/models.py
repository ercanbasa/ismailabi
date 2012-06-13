# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode

class ActiveManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(is_active=True)

class Quote(models.Model):
    quote = models.TextField("Replik")
    author = models.CharField("Replik sahibi", max_length=50)
    picture = models.ImageField(u"Arkaplan imajı", upload_to="uploads")
    is_active = models.BooleanField("Aktif/Pasif", default=False)
    submitter_name = models.CharField("Ekleyen", max_length=255, null=True, blank=True)
    submitter_link = models.CharField("Profil linki", max_length=255, null=True, blank=True,
             help_text="Twitter ya da başka bir sosyal ağ adresinizi yazabilirsiniz.")

    objects = ActiveManager()

    def __unicode__(self):
        return smart_unicode(self.quote)

    @models.permalink
    def get_absolute_url(self):
        return 'quote', [self.id, ]
