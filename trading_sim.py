import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CornixBot.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



import tzlocal,random
import time,telebot,json
from telebot.types import *
from django.db.models import Q
from django.conf import settings
from ratelimiter import RateLimiter
from django.shortcuts import render,redirect
from Cornix.models import User,MyClient,MyOrder
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler(timezone=str(tzlocal.get_localzone()))



@sched.scheduled_job('interval', minutes=1)
def Simulate_Trading():
	print("Stating now")

	while 1:
		UserClients = MyClient.objects.all().exclude(has_funds=False)

		for client in UserClients:
			print(client,"hhhhhhh")
			my_trades = MyOrder.objects.filter(client=client)
			if my_trades.exists():
				last_trade = my_trades.order_by('-date_placed').first()
				recommend_trade = random.choice(["Buy","Sell"])

				print(recommend_trade,"GVBNJKIUYGVBNKJIJHBN")
				print(last_trade.order_type,"YGHBJIUYGHBJIUHBN")

				if recommend_trade == 'Buy' and last_trade.order_type == 'sell':
					order = MyOrder(client=client,coin_pair="BTC/USDT",order_type="buy",amount=500)
					order.save()

				elif recommend_trade == 'Sell' and last_trade.order_type == 'buy':
					order = MyOrder(client=client,coin_pair="BTC/USDT",order_type="sell",amount=500)
					order.save()

					client.balance += random.choice([2,4,6])
					client.save()
				else:
					pass
			else:
				order = MyOrder(client=client,coin_pair="BTC/USDT",order_type="buy",amount=500)
				order.save()

		time.sleep(30)



sched.start()


