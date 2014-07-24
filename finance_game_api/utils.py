"""
set of utility classes for finance_game_api application
"""

from finance_game.models import User
from finance_game.models import APIKey

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

def check_apikey(view):
    """
    decorator to check validity of an apikey
    """
    def wrapped_view(request, username, *args, **kwargs):
        api_key = request.GET.get("key", None)
        print username
        if not api_key:
            return HttpResponse("Please pass an api key as argument")
        try:
            user_api_key = APIKey.objects.get(api_user__username=username).apikey
        except ObjectDoesNotExist:
            return HttpResponse("Api key {0} is not recognized or access to this resource is denied".format(
                api_key))
        if api_key != user_api_key:
            print(api_key)
            print(user_api_key)
            return HttpResponse("Api key is not recognized or access to this resource is denied")
        return view(request, username, *args, **kwargs)
    return wrapped_view

