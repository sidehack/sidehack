from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .hackers.models import Hacker
from .orgs.models import Organization


@python_2_unicode_compatible  # only if you need to support Python 2
class Hack(models.Model):   # hack is an object in the sidehack world
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    creator_id = models.ForeignKey(Hacker, on_delete=models.CASCADE)
    github_repo_id = models.ForeignKey(
        'GithubRepository', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.id


@python_2_unicode_compatible  # only if you need to support Python 2
class GithubRepository(models.Model):   # github repo connected to the sidehack
    repo_name = models.CharField(max_length=200)
    repo_creator_id = models.ForeignKey(Hacker, on_delete=models.CASCADE)
    repo_org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
