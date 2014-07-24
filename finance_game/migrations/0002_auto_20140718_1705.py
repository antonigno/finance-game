# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ebitda',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.CharField(max_length=30),
        ),
    ]
