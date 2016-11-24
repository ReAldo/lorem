from __future__ import unicode_literals

from django.db import models


class Phrase(models.Model):
    text = models.CharField(max_length=512)

    def __unicode__(self):
        return self.text
