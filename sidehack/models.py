from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Organization(models.Model):
    org_name = models.CharField(max_length=200)

    def __str__(self):
        return self.org_name


@python_2_unicode_compatible
class Hacker(models.Model):     # sidehack creator, same as repo creator
    login = models.CharField(max_length=200)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.login


@python_2_unicode_compatible
class Hack(models.Model):   # hack is an object in the sidehack world
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    creator = models.ForeignKey(Hacker, on_delete=models.CASCADE)
    github_repo = models.ForeignKey(
        'GithubRepository', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class GithubRepository(models.Model):   # github repo connected to the sidehack
    repo_name = models.CharField(max_length=200)
    repo_creator = models.ForeignKey(Hacker, on_delete=models.CASCADE)
    repo_org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.repo_name
