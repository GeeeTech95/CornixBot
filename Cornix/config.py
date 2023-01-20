# from .models import Subcriptions
from datetime import datetime, timedelta
from dateutil.relativedelta import *


USDT = "TP2twCcFRzcqXBb8AeerGzXYZdknGnjGGV"
ETH = "0xAb7f95B706548928A08d0c26AB08ca5b359eCC02"
BTC = "bc1qecx3fvxw98n46nl9sthhd2ctzcqh7mjpmwsknj"
TRX = "TTLt2GSvrZy4dLHUJJFgiAMekHoKBj2VYr"
DOT = "13CZNdspezSRqx6TvDRdYVmbNMTeCiT7aaXEPfc4Gwr1vxvX"
XRP = "rPtugswQVNiZYDgdFNJDF5JGWhMrbrd5HL"
DODGE = "DGee8VSkYzyYwnR9uoEWY3ftHuyDmuL59Z"
SOL = "Hrd6gsgU8btwsAAPd99T5L24DfPwJwaEGyUBTeJv1R1j"


def is_active(user):
	try:
		sub = Subcriptions.objects.get(subscriber=user)
		if sub.active == True:
			if (sub.date_expired.replace(tzinfo=None) - datetime.utcnow().replace(tzinfo=None)) < timedelta(1):
				# Check if the user's subscription has expired
				Subcriptions.objects.filter(subscriber=user).update(active = False,paid=False)
				return(False)
			else:
				return(True)
			return
		else:
			return(False)
	except Subcriptions.DoesNotExist:
		return(False)
