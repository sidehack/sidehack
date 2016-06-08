# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-06 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.Organization')),
            ],
        ),
    ]