# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formfactory', '0012_auto_20170703_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='paragraph',
            field=simplemde.fields.SimpleMDEField(blank=True, help_text=b'To add form specific content.', null=True),
        ),
    ]
