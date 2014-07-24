# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_game', '0004_auto_20140721_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
    ]
