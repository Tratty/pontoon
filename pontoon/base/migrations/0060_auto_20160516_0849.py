# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0059_add_abstract_aggregated_stats_class"),
    ]

    operations = [
        migrations.AlterField(
            model_name="repository",
            name="type",
            field=models.CharField(
                choices=[
                    (b"file", b"File"),
                    (b"git", b"Git"),
                    (b"hg", b"HG"),
                    (b"svn", b"SVN"),
                ],
                default=b"file",
                max_length=255,
            ),
        ),
    ]
