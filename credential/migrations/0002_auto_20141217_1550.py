# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='certify',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='credential',
            name='course',
            field=models.CharField(default='Karel the Robot', max_length=100, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='issue_date',
            field=models.DateField(verbose_name='Issue Date'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Skill Level'),
        ),
    ]
