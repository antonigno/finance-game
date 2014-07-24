from django.db import models
import ystockquote
from django.contrib.auth.models import User
import uuid
from decimal import *


class Stock(models.Model):
    """
    a model representing a Stock object
    """
    symbol = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    exchange = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    avg_daily_volume = models.IntegerField(default=0)
    book_value = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    change = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    dividend_per_share = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    dividend_yield = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    earnings_per_share = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    ebitda = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    fifty_day_moving_avg = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    fifty_two_week_high = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    fifty_two_week_low = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    market_cap = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    price_book_ratio = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    price_earnings_growth_ratio = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    price_earnings_ratio = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    price_sales_ratio = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    short_ratio = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    two_hundred_day_moving_avg = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    volume = models.IntegerField(default=0)

    def update_values(self):
        """
        update stock's fields calling yahoo finance
        """
        data = ystockquote.get_all(self.symbol)
        print data
        for field in data:
            try:
                field_type = type(getattr(self, field))
                print field, field_type
            except AttributeError:
                continue
            if field_type == float:
                if data[field] == "N/A":
                    data[field] = 0.0
                setattr(self, field, float(data[field]))
            elif field_type == unicode:
                setattr(self, field, str(data[field]))
            elif field_type == long:
                if data[field] == "N/A":
                    data[field] = 0
                setattr(self, field, int(data[field]))
            elif field_type == Decimal:
                if data[field] == "N/A":
                    data[field] = 0.0
                elif data[field].endswith("K"):
                    data[field] = Decimal(data[field][:-1]) * 1000
                elif data[field].endswith("M"):
                    data[field] = Decimal(data[field][:-1]) * 1000000
                elif data[field].endswith("B"):
                    data[field] = Decimal(data[field][:-1]) * 1000000000
                elif data[field].endswith("T"):
                    data[field] = Decimal(data[field][:-1]) * 1000000000000
                setattr(self, field, Decimal(data[field]))
            else:
                print("field {0} NOT SAVED".format(field))
        self.save()

    def __str__(self):
        return "Name: {0}({1}), Price: {2}".format(self.name, self.symbol, self.price)


class HistoricStockPrice(models.Model):
    """
    historic stock's price
    """
    adj_close = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    volume = models.IntegerField()
    date = models.DateField()
    stock = models.ForeignKey(Stock)
    def __str__(self):
        return "Stock: {0}({1}), Day: {2}".format(self.stock.name, self.stock.symbol, self.date)


class APIKey(models.Model):
    """
    used to access the public api
    """
    apikey = models.CharField(max_length=32)
    api_user = models.ForeignKey(User)
    def create_key(self):
        self.apikey = uuid.uuid4().hex


class Portfolio(models.Model):
    """
    it's where a user's stock options are held
    """
    name = models.CharField(max_length=30)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    last_operation_date = models.DateTimeField('last operation date', null=True, blank=True, auto_now=True)
    user = models.ForeignKey(User)

    def get_total_value(self):
        return sum(map(lambda so: so.get_total_value(), self.stockoption_set.all()))

    def __str__(self):
        return "{0}'s portfolio {1}, Total value: {2}".format(self.user.username, self.name, self.get_total_value())


class StockOption(models.Model):
    """
    represents a quantity of stocks
    """
    stock = models.ForeignKey(Stock)
    quantity = models.IntegerField(default=0)
    portfolio = models.ForeignKey(Portfolio)

    def buy(self, quantity):
        """
        buy quantity stocks
        """
        self.stock.update_values()
        self.quantity += quantity

    def sell(self, quantity):
        """
        sell quantity stock
        """
        self.stock.update_values()
        if self.quantity <= quantity:
            raise Exception("You don't have enough money!!!")
        else:
            self.quantity -= quantity
            return quantity * self.stock.price

    def get_total_value(self):
        """
        get the total value in money of the stock option
        """
        return self.stock.price * self.quantity

    def __str__(self):
        return "Name: {0}, Quantity: {1}, Total value: {2}".format(self.stock.name, self.quantity,
                                                                   self.get_total_value())


class Currency(models.Model):
    """
    currency name and symbol
    """
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=3)
    def __str__(self):
        return "{0} ({1})".format(self.name, self.symbol)


class Wallet(models.Model):
    """
    contains money
    """
    money = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30, default="unnamed wallet")
    def __str__(self):
        return "{0}'s wallet, Money: {1}, Currency: {2}".format(self.user.username, self.money, self.currency)
