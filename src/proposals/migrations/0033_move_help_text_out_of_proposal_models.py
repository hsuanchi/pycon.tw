# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 08:31
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0032_auto_20170209_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkproposal',
            name='objective',
            field=core.models.EAWTextField(max_length=1000, verbose_name='objective'),
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='outline',
            field=models.TextField(blank=True, verbose_name='outline'),
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='supplementary',
            field=models.TextField(blank=True, default='', verbose_name='supplementary'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='objective',
            field=core.models.EAWTextField(max_length=1000, verbose_name='objective'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='outline',
            field=models.TextField(blank=True, verbose_name='outline'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='supplementary',
            field=models.TextField(blank=True, default='', verbose_name='supplementary'),
        ),
    ]
