# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_game', '0003_auto_20140721_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='book_value',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='change',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dividend_per_share',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dividend_yield',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='earnings_per_share',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ebitda',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fifty_day_moving_avg',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fifty_two_week_high',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fifty_two_week_low',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_book_ratio',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_earnings_growth_ratio',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_earnings_ratio',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_sales_ratio',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='short_ratio',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='two_hundred_day_moving_avg',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=4),
        ),
    ]
