from django.conf.urls import patterns, include, url
from django.contrib import admin

from finance_game import views as finance_views
from finance_game_api import views as api_views
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_details/(?P<username>\S+)', finance_views.user_details, name="user_details"),
    # url(r'^update_symbols/', finance_views.update_symbols, name="update_symbols"),
    # url(r'^update_prices/', finance_views.update_prices, name="update_prices"),
    # url(r'^update_stocks/', finance_views.update_stocks, name="update_stocks"),
    url(r'^update_historics/(?P<start_date>\S+)/(?P<end_date>\S+)', finance_views.update_historics, name="update_historics"),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'finance_game/login.html'}),
    # API
    url(r'^api/stock/(?P<symbol>\S+)', api_views.stock, name="stock_details"),
    url(r'^api/exchange/(?P<exchange_name>\S+)', api_views.exchange, name="exchange stocks"),
    url(r'^api/user/(?P<username>\S+)$', api_views.user, name="user"),
    url(r'^api/(?P<username>\S+)/portfolio', api_views.portfolio, name="portfolio"),
    url(r'^api/(?P<username>\S+)/wallet', api_views.portfolio, name="wallet"),
#update_historics
)
