# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='customer_name',
            field=models.CharField(max_length=255, verbose_name='Deliver to name', blank=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='detail_address',
            field=models.CharField(help_text='\u5efa\u8bae\u60a8\u5982\u5b9e\u586b\u5199\u8be6\u7ec6\u6536\u8d27\u5730\u5740\uff0c\u4f8b\u5982\u8857\u9053\u540d\u79f0\uff0c\u95e8\u724c\u53f7\u7801\uff0c\u697c\u5c42\u548c\u623f\u95f4\u53f7\u7b49\u4fe1\u606f', max_length=255, verbose_name='Shipping address:', blank=True),
        ),
    ]
