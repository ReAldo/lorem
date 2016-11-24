from django.db import models


class Save(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text[:25]

    @models.permalink
    def get_absolute_url(self):
        return 'saves:save_detail', [self.pk]
