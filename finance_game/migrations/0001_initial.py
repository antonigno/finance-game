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
            name='APIKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apikey', models.CharField(max_length=32)),
                ('api_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricStockPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adj_close', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('open', models.FloatField()),
                ('volume', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'creation date')),
                ('last_operation_date', models.DateTimeField(auto_now=True, verbose_name=b'last operation date', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('symbol', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('exchange', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('avg_daily_volume', models.IntegerField(default=0)),
                ('book_value', models.FloatField(default=0)),
                ('change', models.FloatField(default=0)),
                ('dividend_per_share', models.FloatField(default=0)),
                ('dividend_yield', models.FloatField(default=0)),
                ('earnings_per_share', models.FloatField(default=0)),
                ('ebitda', models.FloatField(default=0)),
                ('fifty_day_moving_avg', models.FloatField(default=0)),
                ('fifty_two_week_high', models.FloatField(default=0)),
                ('fifty_two_week_low', models.FloatField(default=0)),
                ('market_cap', models.FloatField(default=0)),
                ('price_book_ratio', models.FloatField(default=0)),
                ('price_earnings_growth_ratio', models.FloatField(default=0)),
                ('price_earnings_ratio', models.FloatField(default=0)),
                ('price_sales_ratio', models.FloatField(default=0)),
                ('short_ratio', models.FloatField(default=0)),
                ('two_hundred_day_moving_avg', models.FloatField(default=0)),
                ('volume', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='historicstockprice',
            name='stock',
            field=models.ForeignKey(to='finance_game.Stock'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='StockOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('portfolio', models.ForeignKey(to='finance_game.Portfolio')),
                ('stock', models.ForeignKey(to='finance_game.Stock')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('money', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'unnamed wallet', max_length=30)),
                ('currency', models.ForeignKey(to='finance_game.Currency')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
