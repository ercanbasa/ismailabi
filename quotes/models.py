from django.db import models
from django.utils.encoding import smart_unicode

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="static/uploads")

    @models.permalink
    def get_absolute_url(self):
        return 'quote', [self.id, ]

    def __unicode__(self):
        return smart_unicode(self.quote)