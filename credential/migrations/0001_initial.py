# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(default=b'Karel the Robot', max_length=100, verbose_name=b'Course Name')),
                ('level', models.IntegerField(default=1, verbose_name=b'Skill Level')),
                ('issue_date', models.DateField(verbose_name=b'Issue Date')),
                ('certify', models.ImageField(upload_to=b'')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
