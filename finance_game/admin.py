from django.contrib import admin
from finance_game.models import Stock
from finance_game.models import StockOption
from finance_game.models import Portfolio
from finance_game.models import Wallet
from finance_game.models import Currency
from finance_game.models import HistoricStockPrice
from finance_game.models import APIKey

class WalletInline(admin.StackedInline):
    model = Wallet
    extra = 1
    # fieldsets = [
    #     (None, {'fields': ['name']}),
    #     ('Wallet details', {'fields': ['money', 'currency']}),
    # ]


class StockOptionInline(admin.StackedInline):
    model = StockOption
    extra = 1

class StockOptionInline(admin.StackedInline):
    model = StockOption
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [StockOptionInline]

class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'email']
    inlines = [WalletInline, ]


admin.site.register(Stock)
admin.site.register(StockOption)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(HistoricStockPrice)
admin.site.register(APIKey)
