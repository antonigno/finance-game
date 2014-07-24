from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from finance_game.models import Stock
from finance_game.models import Portfolio
from finance_game.models import StockOption
from finance_game.models import User
from finance_game.models import APIKey
from utils import check_apikey

def stocks(request, symbol_list):
    result_stocks = []
    for symbol in symbol_list:
        result_stocks.append(serializers.serialize("json", Stock.objects.filter(symbol=symbol).first()))
    return HttpReponse(json.dumps(result_stocks), mimetype='application/json')

def stock(request, symbol):
    stock_model = Stock.objects.filter(symbol=symbol).first()
    if not stock_model:
        return HttpResponse("No stock found for symbol {0}".format(symbol))
    else:
        return HttpResponse(serializers.serialize("json", [stock_model]),
                            content_type='application/json')

def exchange(request, exchange_name):
    stock_models = Stock.objects.filter(exchange=exchange_name).all()
    if not stock_models:
        return HttpResponse("No stock found for exchange {0}".format(exchange_name))
    else:
        return HttpResponse(serializers.serialize("json", stock_models),
                            content_type='application/json')

@check_apikey
def portfolio(request, username):
    returned_json = []
    portfolios = Portfolio.objects.filter(user__username=username).all()
    for portfolio in portfolios:
        portfolio_json = {"type": "portfolio",
                          "id": portfolio.id,
                          "name": portfolio.name,
                          "creation_date": str(portfolio.creation_date),
                          "last_operation_date": str(portfolio.last_operation_date),
                          "stock_options": [],
                          "total_value": portfolio.get_total_value()}
        stock_options = StockOption.objects.filter(portfolio__id=portfolio.id).all()
        for stock_option in stock_options:
            stock_option_json = {"type": "stock_option",
                                 "stock_id": stock_option.stock_id,
                                 "quantity": stock_option.quantity,
                                 "value": stock_option.get_total_value(),
                                 }
            portfolio_json["stock_options"].append(stock_option_json)
        returned_json.append(portfolio_json)
    return HttpResponse(json.dumps(returned_json), content_type='application/json')

@check_apikey
def user(request, username):
    returned_json = {}
    user = User.objects.get(username=username)
    returned_json["username"] = user.username
    returned_json["first_name"] = user.first_name
    returned_json["last_name"] = user.last_name
    returned_json["email"] = user.email
    returned_json["date_joined"] = str(user.date_joined)
    return HttpResponse(json.dumps(returned_json), content_type='application/json')

@check_apikey
def wallet(request, username):
    return HttpResponse("diocane")