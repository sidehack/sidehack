# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-23 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='hacker',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidehack.Organization'),
        ),
        migrations.AddField(
            model_name='hack',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidehack.Hacker'),
        ),
        migrations.AddField(
            model_name='hack',
            name='github_repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidehack.GithubRepository'),
        ),
        migrations.AddField(
            model_name='githubrepository',
            name='repo_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidehack.Hacker'),
        ),
        migrations.AddField(
            model_name='githubrepository',
            name='repo_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidehack.Organization'),
        ),
    ]
