# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode


class ActiveManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(is_active=True)


class Quote(models.Model):
    quote = models.TextField("Replik")
    picture = models.ImageField(u"Arkaplan imajı", upload_to="uploads")
    is_active = models.BooleanField("Aktif/Pasif", default=False)

    objects = ActiveManager()

    def __unicode__(self):
        return smart_unicode(self.quote)

    @models.permalink
    def get_absolute_url(self):
        return 'quote', [self.id, ]
