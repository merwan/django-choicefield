from django.db import models


class TopLevelDomain(models.Model):
    name = models.TextField(default='')
    depth = models.IntegerField(default=1)
    policy = models.TextField(null=True, default=None)
    public = models.BooleanField(default=False)
