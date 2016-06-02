from __future__ import unicode_literals
from django.db import models


class Hack(models.Model):   # hack is an object in the sidehack world
    hack_title = models.CharField(max_length=200)
    hack_description = models.CharField(max_length=1000)
    hack_pub_date = models.DateTimeField('date published')
    hack_creator_login = models.ForeignKey('Hacker', on_delete=models.CASCADE)
    hack_github_repo = models.ForeignKey(
        'GithubRepository', on_delete=models.CASCADE
    )


class GithubRepository(models.Model):   # github repo connected to the sidehack
    github_repo_name = models.CharField(max_length=200)
    github_repo_creator_id = models.ForeignKey(
        'Hacker', on_delete=models.CASCADE
    )
    github_repo_creator_login = models.CharField(max_length=100)
    github_repo_parent_org = models.ForeignKey(
        'Organization', on_delete=models.CASCADE
    )


class Hacker(models.Model):     # sidehack creator, same as repo creator
    hacker_login = models.CharField(max_length=200)
    hacker_org_id = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE
    )


class Organization(models.Model):
    org_name = models.CharField(max_length=200)
