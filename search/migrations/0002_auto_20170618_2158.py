# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='page_numbers',
            new_name='page_chapter',
        ),
        migrations.AddField(
            model_name='page',
            name='page_number',
            field=models.IntegerField(default=234),
            preserve_default=False,
        ),
    ]
