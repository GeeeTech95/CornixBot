from django.core.management.base import BaseCommand
from django.core.management.commands import loaddata
from django.core import management
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'sets up all necessary credentials for the app to work'

    def add_arguments(self, parser):

        # Optional argument
        parser.add_argument(
            '--test',
            action='store_true',
            help='load test data as well for test purposes',
        )
        #parser.add_argument('-en', '--env_name', type=str,help = "indicates the environmenntal name")
        #parser.add_argument('-wd_id','--webhook_id',type=str,help = "webhook id to be deleted")

  

    def handle(self, *args, **options):
        self.is_test = options.get("test", False)
        self.stdout.write("simulating trading  ...")
        with open("simulate_trading.py") as f :
            exec(f.read())
       

   
