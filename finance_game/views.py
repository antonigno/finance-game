from django.shortcuts import render
from django.http import HttpResponse
from finance_game.models import User, Stock, HistoricStockPrice
from django.template import RequestContext, loader
import ystockquote
from urllib2 import HTTPError
import urllib

import urllib2
import lxml.html

def user_details(request, username):
    user = User.objects.filter(name=username).first()
    money = user.wallet.money
    stock_option_list = user.portfolio.stocks_options.all()
    template = loader.get_template('finance_game/dashboard.html')
    context = RequestContext(request, {
        'user': username,
        'money': money,
        'stock_option_list': stock_option_list,
    })
    return HttpResponse(template.render(context))
    # response = "details for user {0}: money: {1}\n".format(username, user.wallet.money)
    # response += "stock_options: " + "\n".join(["{0} {1}".format(so.quantity, so.stock.name) for so in stock_option_list])

    # return HttpResponse(response)
#
# def update_symbols(request):
#     from finance_game.models import Stock
#     def get_countries():
#         url = "http://www.myinvestorshub.com/yahoo_stock_list.php"
#         countries_html = urllib2.urlopen(url).read()
#         index_root = lxml.html.fromstring(countries_html)
#         for country in index_root.cssselect("option"):
#             yield country.text
#     symbol_url_base = "http://www.myinvestorshub.com/yahoo_list.php"
#     for country in get_countries():
#         if country == "United Kingdom":
#             data = urllib.urlencode({"cnt": country})
#             binary_data = data.encode('utf-8')
#             request = urllib2.Request(symbol_url_base, binary_data)
#             response = urllib2.urlopen(request)
#             index_root = lxml.html.fromstring(response.read().decode('utf-8'))
#             table = index_root.cssselect("table")[3]
#             stock_rows = table.cssselect("tr")
#             for stock_row in stock_rows[1:]:
#                 _, company_name, symbol, exchange, country = list(map(lambda s: s.text, stock_row.cssselect("td")))
#                 if company_name and symbol and exchange and country:
#                     print(company_name, symbol, exchange, country)
#                     stock = Stock(name=company_name, symbol=symbol, exchange=exchange, country=country)
#                     stock.update_values()
#                     stock.save()
#     return HttpResponse("Done.")
#
# def update_stocks(request):
#     from finance_game.models import Stock
#     for stock in Stock.objects.all():
#         stock.update_values()
#     return HttpResponse("Done.")
#
# def update_prices(request):
#     from finance_game.models import Stock
#     for stock in Stock.objects.all():
#         stock.price = ystockquote.get_all(stock.symbol)["price"]
#         stock.save()
#     return HttpResponse("Done.")

def update_historics(request, start_date, end_date):
    for stock in Stock.objects.all():
        try:
            historical_prices = ystockquote.get_historical_prices(stock.symbol, start_date, end_date)
            for date in historical_prices:
                historical_price = historical_prices[date]
                hsp = HistoricStockPrice(date=date,
                                         adj_close=float(historical_price["Adj Close"]),
                                         close=float(historical_price["Close"]),
                                         high=float(historical_price["High"]),
                                         low=float(historical_price["Low"]),
                                         open=float(historical_price["Open"]),
                                         volume=int(historical_price["Volume"]),
                                         stock=stock)
                hsp.save()
        except HTTPError as err:
            if err.code == 404:
                continue
            else:
                raise(err)
    return HttpResponse("done")
