# from .models import Subcriptions
from datetime import datetime, timedelta
from dateutil.relativedelta import *


USDT = "TMkLBRBWDRg5N4MWnyNQzy7X6aUHujcNAF"  #"TP2twCcFRzcqXBb8AeerGzXYZdknGnjGGV"
ETH = "0x424A3598FE297187613aBeaed5a2816Feb1014Fa"     
BTC = "bc1qa5yrhkqxuyzhqzd48k6kn8uz979yp778x7r76n"
TRX = "TTLt2GSvrZy4dLHUJJFgiAMekHoKBj2VYr"
DOT = "13CZNdspezSRqx6TvDRdYVmbNMTeCiT7aaXEPfc4Gwr1vxvX"
XRP = "rPtugswQVNiZYDgdFNJDF5JGWhMrbrd5HL"
DODGE = "DF3BWS6PawfZjYV4Q3ETNLttJSTkqH6ztP"
SOL = "E1uKruYRjhafgkJpet7hNDrqmuAzrW9dQDmak9d1ky2W"
MATIC = "0x424A3598FE297187613aBeaed5a2816Feb1014Fa"


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
