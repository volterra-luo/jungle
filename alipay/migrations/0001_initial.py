# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=20, verbose_name=b'Username')),
                ('out_trade_no', models.CharField(default=None, help_text=b'An unique numbered transaction ID in merchant system', max_length=64)),
                ('trade_no', models.CharField(default=b'0', help_text=b'The transaction ID in alipay system', max_length=28)),
                ('course_id', models.IntegerField()),
                ('subject', models.CharField(help_text=b'A short description for the product.', max_length=200)),
                ('total_fee', models.DecimalField(max_digits=6, decimal_places=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('payment_status', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['payment_date', 'trade_no'],
            },
        ),
    ]
