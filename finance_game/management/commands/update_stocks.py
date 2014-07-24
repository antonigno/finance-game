from django.core.management.base import BaseCommand, CommandError
from finance_game.models import Stock


class Command(BaseCommand):
    help = 'Update all stock data'

    def handle(self, *args, **options):
        for stock in Stock.objects.all():
            stock.update_values()
            self.stdout.write('Successfully updated stock {0}'.format(stock.symbol))