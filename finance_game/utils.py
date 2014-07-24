from models import User, Stock, HistoricStockPrice
from django.template import RequestContext, loader
import ystockquote
import urllib

import urllib2
import lxml.html

def update_symbols():
    """
    update the symbol list calling myinvestorshub.com
    """
    from finance_game.models import Stock

    def get_countries():
        url = "http://www.myinvestorshub.com/yahoo_stock_list.php"
        countries_html = urllib2.urlopen(url).read()
        index_root = lxml.html.fromstring(countries_html)
        for country in index_root.cssselect("option"):
            yield country.text

    symbol_url_base = "http://www.myinvestorshub.com/yahoo_list.php"
    for country in get_countries():
        if country == "United Kingdom":
            data = urllib.urlencode({"cnt": country})
            binary_data = data.encode('utf-8')
            request = urllib2.Request(symbol_url_base, binary_data)
            response = urllib2.urlopen(request)
            index_root = lxml.html.fromstring(response.read().decode('utf-8'))
            table = index_root.cssselect("table")[3]
            stock_rows = table.cssselect("tr")
            for stock_row in stock_rows[1:]:
                _, company_name, symbol, exchange, country = list(map(lambda s: s.text, stock_row.cssselect("td")))
                if company_name and symbol and exchange and country:
                    print(company_name, symbol, exchange, country)
                    stock = Stock(name=company_name, symbol=symbol, exchange=exchange, country=country)
                    # stock.update_values()
                    stock.save()

def update_stocks():
    """
    update all stock data
    """
    from finance_game.models import Stock
    for stock in Stock.objects.all():
        stock.update_values()
        stock.save()

def update_prices():
    """
    update stock prices calling ystockquote
    """
    from finance_game.models import Stock
    for stock in Stock.objects.all():
        stock.price = ystockquote.get_price(stock.symbol)
        stock.save()

