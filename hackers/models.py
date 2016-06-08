from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from orgs.models import Organization


@python_2_unicode_compatible  # only if you need to support Python 2
class Hacker(models.Model):     # sidehack creator, same as repo creator
    login = models.CharField(max_length=200)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
