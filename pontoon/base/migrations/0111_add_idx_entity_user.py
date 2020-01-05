# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-31 13:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0110_permissionchangelog"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="translation",
            index_together=set(
                [
                    ("entity", "locale", "approved"),
                    ("entity", "user"),
                    ("entity", "locale", "fuzzy"),
                ]
            ),
        ),
    ]
