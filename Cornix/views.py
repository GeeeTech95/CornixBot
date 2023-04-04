from locale import currency
import random
import requests,urllib
from .messages import *
from .Keyboards import *
import time,telebot,json
from telebot.types import *
from django.db.models import Q
from django.conf import settings
from ratelimiter import RateLimiter
from pycoingecko import CoinGeckoAPI
from django.http import HttpResponse
# from .wrappers import *
from .models import User,MyOrder,MyClient,STEP
from django.views.decorators.http import require_http_methods



NEW_CLIENT = {}
coin_gecko = CoinGeckoAPI()
bot = telebot.TeleBot(settings.WEBHOOK_TOKEN,parse_mode='HTML') #Telegram Bot API
bot.enable_save_next_step_handlers(filename="handlers-saves/step.save",delay=2)



def return_trade_history(user):
	my_order_history = "\n"
	MyUser = User.objects.get(user_id=user)
	my_portfolio = MyClient.objects.filter(myclient = MyUser).exclude(has_funds=False)

	if my_portfolio.exists():
		for client in my_portfolio:
			my_trades = MyOrder.objects.filter(client=client).order_by('-date_placed')[:9]

			for trade in my_trades:
				if trade.order_type == "buy":
					my_order_history += f"Buying <b>BTC</b> for {trade.client.client_name} @ {trade.date_placed.strftime('%b-%d-%y %I:%M %p')}\n\n"
				else:
					my_order_history += f"Buying <b>BTC</b> for {trade.client.client_name} @ {trade.date_placed.strftime('%b-%d-%y %I:%M %p')}\n\n"
		return(my_order_history)
	else:
		return("No trades yet")

def usdt_to_btc(amount):
	btc = float(coin_gecko.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd'])
	result =  round(float(amount/btc),3)
	return(result)

def get_user_portfolio(userID):
	MyUser = User.objects.get(user_id=userID)
	my_portfolio = MyClient.objects.filter(myclient = MyUser).exclude(has_funds=False)

	usdt_balance = 0

	for my_balance in my_portfolio:
		usdt_balance += my_balance.balance

	return(usdt_balance)

def return_client_name(name):
	if "spot" in name or "linear" in name:
		return(True)
	else:
		return(False)

def user_details(message):
	detail = {}
	detail["chat_id"] = message.chat.id
	detail["msg_type"] = message.chat.type
	detail["user_id"] = message.from_user.id
	detail["username"] = message.from_user.username
	return(detail)

def return_state(user):
	""" Returns the current state of a user """
	MY_STEP = STEP.objects.get(user=user)
	MY_STATE = MY_STEP.state.replace("'",'"')
	MY_STATE = json.loads(MY_STATE)
	return(MY_STATE)

def return_exchange_and_step(userID):
	MY_STATE = return_state(userID)
	try:
		step = MY_STATE["previuos_step"]
	except:
		step = "1"
	try:
		exchange = MY_STATE["client_name"]

		if exchange.split("-")[1].lower() == MY_STATE["exchange"].lower():
			exchange = MY_STATE["exchange"]
		else:pass
	except:
		try:
			exchange = MY_STATE["exchange"]
		except:
			exchange = None

	return(step,exchange)

def set_my_client_name(message):
	user_detail =  user_details(message)
	MY_STATE = return_state(user_detail["user_id"])

	MY_STATE["client_name"] = message.text
	MY_STATE["previuos_step"] = "2"
	STEP.objects.filter(user = user_detail["user_id"]).update(state = MY_STATE)

	try:
		my_option = MY_STATE["option"]
	except:
		my_option = ""
	
	if MY_STATE['exchange'] == "MarginedScheme":
		bot.send_message(chat_id=user_detail["chat_id"],text="Select the amount you want to invest:",reply_markup=deposit_options())
	else:
		bot.send_message(chat_id=user_detail["chat_id"], text="Select the currency you want to invest:",reply_markup=payment_method())


def set_invest_amount(message):
	user_detail =  user_details(message)
	MY_STATE = return_state(user_detail["user_id"])
	user = User.objects.get(user_id=user_detail["user_id"])

	try:
		amount = float(message.text)
		q = MY_STATE['payment_method']

		if q == "USDT":
			detail = payment_detail.format(amount,"USDT",USDT)

		elif q == "SOL":
			detail = payment_detail.format(amount,"Sol",SOL)

		elif q == "BTC":
			detail = payment_detail.format(amount,"BTC",BTC)

		elif q == "ETH":
			detail = payment_detail.format(amount,"ETH",ETH)

		elif q == "XRP":
			detail = payment_detail.format(amount,"XRP",XRP)

		elif q == "DOT":
			detail = payment_detail.format(amount,"DOT",DOT)

		elif q == "DODGE":
			detail = payment_detail.format(amount,"DODGE",DODGE)
		
		elif q == "BCH":
			detail = payment_detail.format(amount,"BCH",BCH)
		
		elif q == "BNB":
			detail = payment_detail.format(amount,"BNB",BNB)
		
		elif q == "BSC":
			detail = payment_detail.format(amount,"BSC",BSC)
		
		elif q == "LTC":
			detail = payment_detail.format(amount,"LTC",LTC)
		
		elif q == "Polygon":
			detail = payment_detail.format(amount,"MATIC",Polygon)
		
		elif q == "XLM":
			detail = payment_detail.format(amount,"XLM",XLM)
		
		elif q == "Atom":
			detail = payment_detail.format(amount,"Atom",Atom)
		
		elif q == "VET":
			detail = payment_detail.format(amount,"VET",VET)
		
		elif q == "DASH":
			detail = payment_detail.format(amount,"DASH",DASH)
		
		elif q == "NEAR":
			detail = payment_detail.format(amount,"NEAR",NEAR)
		
		elif q == "FTM":
			detail = payment_detail.format(amount,"FTM",FTM)
		
		elif q == "ZEC":
			detail = payment_detail.format(amount,"ZEC",ZEC)
		
		elif q == "ETC":
			detail = payment_detail.format(amount,"ETC",ETC)
		
		elif q == "FIL":
			detail = payment_detail.format(amount,"FIL",FIL)
		
		elif q == "ALGO":
			detail = payment_detail.format(amount,"ALGO",ALGO)
		
		elif q == "WAVES":
			detail = payment_detail.format(amount,"WAVES",WAVES)
		
		elif q == "RUNE":
			detail = payment_detail.format(amount,"RUNE",RUNE)
		
		elif q == "KAVA":
			detail = payment_detail.format(amount,"KAVA",KAVA)
		
		elif q == "THETA":
			detail = payment_detail.format(amount,"THETA",THETA)
		
		elif q == "ZIL":
			detail = payment_detail.format(amount,"ZIL",ZIL)
		
		elif q == "TOMO":
			detail = payment_detail.format(amount,"TOMO",TOMO)
		
		elif q == "TFUEL":
			detail = payment_detail.format(amount,"TFUEL",TFUEL)
		
		elif q == "QTUM":
			detail = payment_detail.format(amount,"QTUM",QTUM)
		
		elif q == "RVN":
			detail = payment_detail.format(amount,"RVN",RVN)
		else:
			pass

		bot.send_message(chat_id=user_detail["chat_id"], text=detail,reply_markup=confirm_payment())
		MY_STATE["deposit_amount"] = amount
		STEP.objects.filter(user = user).update(state = MY_STATE)
		STEP.objects.filter(user = user).update(next_step="")

	except:
		msg = bot.send_message(user_detail["chat_id"],"Please enter a number",reply_markup=Cancel_btn())
		#REPEAT STEP
		STEP.objects.filter(user = user).update(next_step="GET_INVEST_AMOUNT")


def process_transaction_hash(message):
	user_detail =  user_details(message)
	MY_STATE = return_state(user_detail["user_id"])
	MyUser = User.objects.get(user_id=user_detail["user_id"])

	# print(MY_STATE,"UGHBJUYTGHBJKUYGHBNJUHGB")


	if message.text == "❌ Cancel":
		STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")
		bot.send_message(user_detail["chat_id"],"Action terminated use the /start command to begin",reply_markup=ReplyKeyboardRemove(selective=False))#Main_Menu())
	else:
		msg = "Hello you transaction is being processed. Please wait"

		try:
			amount = MY_STATE["deposit_amount"]
			payment_method = MY_STATE['payment_method']
			# payment_method = MY_STATE["payment_method"]
			# result = check_transaction(message.text,MY_STATE["deposit_amount"])
			if 'option' in MY_STATE:
				my_exchange = f"{MY_STATE['exchange']} - {MY_STATE['option']}"
			else:
				my_exchange = f"{MY_STATE['exchange']}"

			# if result == True:
			myclient = MyClient(myclient=MyUser,balance=MY_STATE["deposit_amount"],exchange=my_exchange,client_name=MY_STATE["client_name"],investment_currency=payment_method,has_funds=False,start_trading=False)
			myclient.save()

			bot.send_message(user_detail["chat_id"],msg,reply_markup=ReplyKeyboardRemove(selective=False))#Main_Menu())
			bot.send_message(user_detail["chat_id"],"Once your deposit is confirmed the bot will start trading",reply_markup=ReplyKeyboardRemove(selective=False))#reply_markup=Main_Menu())
			STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")

			notify_admin_payment(myclient,payment_method,message.text)


			
			# elif result == False:
			# 	bot.send_message(user_detail["chat_id"],"There appears to be some incorrect details in your transaction.",reply_markup=ReplyKeyboardRemove(selective=False))
			# 	bot.send_message(user_detail["chat_id"],"Please contact support to rectify this.",reply_markup=tech_support())
				
			# 	STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")
			# else:
			# 	msgs = bot.send_message(user_detail["chat_id"],"Invalid transaction hash, please check you transaction ID and try again")#Main_Menu())
			# 	STEP.objects.filter(user = user_detail["user_id"]).update(next_step="PROC_TXN_HASH")

		except Exception as e:
			print(e)


def process_withdrawal_amount(message):
	user_detail =  user_details(message)
	MY_STATE = return_state(user_detail["user_id"])
	MyUser = User.objects.get(user_id=user_detail["user_id"])

	if message.text == "❌ Cancel":
		STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")
		bot.send_message(user_detail["chat_id"],"Action terminated use the /start command to begin",reply_markup=ReplyKeyboardRemove(selective=False))
	else:

		try:
			withdrawal_amount = float(message.text)
			my_clients = MyClient.objects.filter(myclient=MyUser).filter(balance__gte=withdrawal_amount)


			if my_clients.exists():
				msg = "Please enter the address to withdraw to:"
				MY_STATE["WITHDRAWAL"]["withdrawal_amount"] = withdrawal_amount

				bot.send_message(chat_id=user_detail["chat_id"],text=msg,reply_markup=Cancel_btn())
				STEP.objects.filter(user = MyUser).update(state = MY_STATE,next_step="GET_WITHDRAWAL_ADDRESS")

			else:
				msg = "Sorry but you don't have upto that amount yet"
				bot.send_message(chat_id=user_detail["chat_id"],text=msg,reply_markup=Main_Menu())

		except Exception as e:

			print(e,"sdfgdewqerfdgfdsfghfds")
			msg = "Please enter the amount you want to withdraw in USDT:(Don't include any alphabets just the digit)"
			bot.send_message(chat_id=user_detail["chat_id"], text=msg,reply_markup=Cancel_btn())


def process_withdrawal_address(message):
	user_detail =  user_details(message)
	MY_STATE = return_state(user_detail["user_id"])
	MyUser = User.objects.get(user_id=user_detail["user_id"])

	if message.text == "❌ Cancel":
		STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")
		bot.send_message(user_detail["chat_id"],"Action terminated use the /start command to begin",reply_markup=ReplyKeyboardRemove(selective=False))
	else:
		withdrawal_address = message.text
		withdrawal_amount = MY_STATE["WITHDRAWAL"]["withdrawal_amount"]
		withdrawal_currency = MY_STATE["WITHDRAWAL"]["withdrawal_currency"]


		MY_STATE["WITHDRAWAL"]["withdrawal_address"] = withdrawal_address
		STEP.objects.filter(user = MyUser).update(state = MY_STATE,next_step="")



		msg = f"""

		You are sending ${withdrawal_amount} of {withdrawal_currency}
		To: {withdrawal_address}


		<i>⚠️please note: daily maximum withdrawal is $25,000,000⚠️

		⚠️also note: there is a 15% fee for every withdrawal⚠️</i>
		"""
		bot.send_message(chat_id=user_detail["chat_id"],text=msg,reply_markup=confirm_withdrawal())
		STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")


def notify_admin(user):
	""" This is used to broadcast a new member subscription """
	admins = User.objects.filter(is_admin=True)
	user = User.objects.get(user_id=user)

	for admin in admins:

		if user.user_name == None:
			message_from = f"#{user.user_id}"
		else:
			message_from = f"@{user.user_name}"


		msg = f""" {message_from} started the bot for the first time
		"""
		bot.send_message(admin.chat_id,msg)


def notify_admin_payment(client,coin,txn_hash):
	""" This is used to broadcast a new member subscription """
	admins = User.objects.filter(is_admin=True)
	# client = MyClient.objects.get(client_id=client_id)

	for admin in admins:
		msg = f"""@{client.myclient.user_name} invested  {client.balance} {coin}  for <b>{client.exchange}</b>
		\n\n TXN HASH: <code>{txn_hash}</code>"""
		try:
			client_id = hex(int(client.client_id.time_low))[2:]
			bot.send_message(admin.chat_id,msg,reply_markup=admin_approval(client.myclient,client_id))
		except Exception as e:
			print(e,"uytdghjio98uydghjkioi7duyhgbn")


def notify_admin_withdrawal(client_id,withdrawal_amount,withdrawal_currency,withdrawal_address):
	""" This is used to broadcast a new member subscription """
	admins = User.objects.filter(is_admin=True)
	client = MyClient.objects.get(client_id=client_id)

	for admin in admins:
		msg = f"""@{client.myclient.user_name} initiated a withdrawal request for  ${withdrawal_amount} 
		worth of <b>{withdrawal_currency}</b> To the address: <code>{withdrawal_address}</code>"""

		try:
			client_id = hex(int(client.client_id.time_low))[2:]
			bot.send_message(admin.chat_id,msg,reply_markup=admin_approve_withdrawal(client_id,withdrawal_amount))
		except Exception as e:
			print(e,"iuytrgfgvbbhjkio87u6ytredfxcvbnhjmkio8u7y6tredf")
# CALLBACK QUERY HANDLING OCCURS HERE

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	try:
		show_menu = False
		userID = call.from_user.id
		chat_id = call.message.chat.id
		user = User.objects.get(user_id=userID)
		STEP.objects.filter(user = user).update(next_step="")

		userportfolio = MyClient.objects.filter(myclient = user)
		if userportfolio.exists():
			show_menu = True
		else:
			show_menu = False

		MY_STATE = return_state(userID)

		if call.data.endswith("@client"):
			q = call.data.split("@")[0]

			MY_STATE["exchange"] = q
			MY_STATE["previuos_step"] = "1"
			STEP.objects.filter(user = user).update(state = MY_STATE)

			if q == "Binance" or q == "ByBit" or q == "Coinex" or q == 'BULLIGON':
				bot.edit_message_text(chat_id=chat_id, text=step_1_2_of_3.format(q), message_id=call.message.message_id,reply_markup=new_client_step_1_2_of_3(q,show_menu))
			
			elif q == "MarginedScheme":
				bot.edit_message_text(chat_id=chat_id, text=margined_scheme, message_id=call.message.message_id,reply_markup=margin_payment_step_1(q,show_menu))


			else:
				bot.edit_message_text(chat_id=chat_id, text=step_2_of_3, message_id=call.message.message_id,reply_markup=new_client_step_2_of_3(q,show_menu))

		elif call.data.startswith("option_"):
			MY_STATE["previuos_step"] = "1_2"
			q = call.data.split(":")[1]
			option = call.data.split(":")[0].split("option_")[1]
			MY_STATE["option"] = option.replace("_"," ").replace(q.lower(),"").title()
			STEP.objects.filter(user = user).update(state = MY_STATE,next_step="SET_NAME")


			if return_client_name(call.data) == False:
				q = option.replace("_","-").upper()
			else:
				pass

			bot.edit_message_text(chat_id=chat_id, text=step_2_of_3, message_id=call.message.message_id,reply_markup=new_client_step_2_of_3(q,show_menu))

		elif call.data.startswith("set_name:"):
			q = call.data.split(":")[1]
			MY_STATE["client_name"] = q
			MY_STATE["previuos_step"] = "2"
			STEP.objects.filter(user = user).update(state = MY_STATE)

			try:
				my_option = MY_STATE["option"]
			except:
				my_option = ""
			
			if MY_STATE['exchange'] == "MarginedScheme":
				bot.edit_message_text(chat_id=chat_id, text="Select the amount you want to invest:", message_id=call.message.message_id,reply_markup=deposit_options())
			else:
				bot.edit_message_text(chat_id=chat_id, text="Select the currency you want to invest:", message_id=call.message.message_id,reply_markup=payment_method())
		
		elif call.data.startswith("step_margin:"):
			step = call.data.split(":")[1]
			client_exchange = MY_STATE["exchange"]
			STEP.objects.filter(user = user).update(state = MY_STATE,next_step="SET_NAME")

			bot.edit_message_text(chat_id=chat_id, text=step_2_of_3, message_id=call.message.message_id,reply_markup=new_client_step_2_of_3(client_exchange,show_menu))

		elif call.data.startswith("back_to_step:"):
			q = call.data.split(":")[1]
			step,exchange = return_exchange_and_step(userID)


			if q == "home":
				msg = """<b>Main Menu:</b>
				Choose an option"""
				bot.edit_message_text(chat_id=chat_id, text=msg, message_id=call.message.message_id,reply_markup=home_key())
			
			elif q == "about":
				bot.edit_message_text(chat_id=chat_id, text=about_cornix_auto, message_id=call.message.message_id,reply_markup=about_cornix(step))
			
			elif q == "my_portfolio":
				my_user_clients = MyClient.objects.filter(myclient = user).exclude(has_funds=False)
				bot.edit_message_text(chat_id=chat_id, text=my_portfolio_msg, message_id=call.message.message_id,reply_markup=my_portfolios_btn(my_user_clients))

			elif q == "1":
				bot.edit_message_text(chat_id=chat_id, text=step_1_of_3, message_id=call.message.message_id,reply_markup=new_client_step_1_of_3(show_menu))
			
			elif q == "2":
				STEP.objects.filter(user = user).update(next_step="SET_NAME")
				try:exchange = exchange.split('My-')[1]
				except:pass
				bot.edit_message_text(chat_id=chat_id, text=step_2_of_3, message_id=call.message.message_id,reply_markup=new_client_step_2_of_3(exchange,show_menu))

			elif q == "1_2":
				if exchange == 'MarginedScheme':
					bot.edit_message_text(chat_id=chat_id, text=margined_scheme, message_id=call.message.message_id,reply_markup=margin_payment_step_1(exchange,show_menu))
				else:
					client_exchange = MY_STATE["exchange"]
					bot.edit_message_text(chat_id=chat_id, text=step_1_2_of_3.format(MY_STATE["exchange"]), message_id=call.message.message_id,reply_markup=new_client_step_1_2_of_3(client_exchange,show_menu))

			elif q == "bot_configs":
				bot.edit_message_text(chat_id=chat_id, text=bot_config, message_id=call.message.message_id,reply_markup=bot_configs())
			else:
				pass

		#THE BILLING PROGRAM STARTS HERE
		
		elif call.data.startswith("deposit:"):
			amount = call.data.split(":")[1]
			detail = payment_detail.format(amount,"USDT",USDT)

			bot.send_message(chat_id=chat_id, text=detail,reply_markup=confirm_payment())
			
			MY_STATE["deposit_amount"] = amount
			MY_STATE["payment_method"] = "USDT"
			STEP.objects.filter(user = user).update(state = MY_STATE)
			STEP.objects.filter(user = user).update(next_step="")

		elif call.data.startswith("pay_with:"):
			q = call.data.split(":")[1]
			MY_STATE["payment_method"] = q
			STEP.objects.filter(user = user).update(state = MY_STATE)

			detail = f"Please Enter amount of {q} you want to invest"
			bot.send_message(chat_id=chat_id, text=detail,reply_markup=Cancel_btn())
			STEP.objects.filter(user = user).update(next_step="GET_INVEST_AMOUNT")

		elif call.data == "i_paid":
			user = User.objects.get(user_id=userID)
			detail = "Please send transaction ID/Hash as proof\nThis will be processed by the Bot Automatically"
			bot.send_message(chat_id=chat_id, text=detail,reply_markup=Cancel_btn())
			STEP.objects.filter(user = user).update(next_step="PROC_TXN_HASH")

		# BOT CONFIGS
		elif call.data == "bot_configs":
			bot.edit_message_text(chat_id=chat_id, text=bot_config, message_id=call.message.message_id,reply_markup=bot_configs())
			
		elif call.data == "my_clients":
			my_clients = MyClient.objects.filter(myclient = user)
			bot.edit_message_text(chat_id=chat_id, text=client_config, message_id=call.message.message_id,reply_markup=bot_configs_clients(my_clients))

		elif call.data.startswith("my_client:"):
			q = call.data.split(":")[1]
			my_client = MyClient.objects.filter(Q(client_id__icontains=q)).first()# This is for a users client method
			client_id = hex(int(my_client.client_id.time_low))[2:]
			bot.edit_message_text(chat_id=chat_id, text=configure_a_client, message_id=call.message.message_id,reply_markup=configs_clients(client_id))

		elif call.data.startswith("delete_client:"):
			q = call.data.split(":")[1]
			my_client = MyClient.objects.filter(Q(client_id__icontains=q)).first().delete()# This is for a users client method
			bot.edit_message_text(chat_id=chat_id, text="Client has been deleted", message_id=call.message.message_id,reply_markup=back_to_configs())

		# MAIN MENU CALLBACK ACTION
		elif call.data == "return_to_menu":
			msg = """<b>Main Menu:</b>
			Choose an option"""
			bot.edit_message_text(chat_id=chat_id, text=msg, message_id=call.message.message_id,reply_markup=home_key())

		elif call.data == "my_portfolio":
			my_user_clients = MyClient.objects.filter(myclient = user).exclude(has_funds=False)
			bot.edit_message_text(chat_id=chat_id, text=my_portfolio_msg, message_id=call.message.message_id,reply_markup=my_portfolios_btn(my_user_clients))
		
		elif call.data.startswith("portfolio:"):
			client_id = call.data.split(':')[1]
			my_client = MyClient.objects.filter(Q(client_id__icontains=client_id)).first()

			client_name =  my_client.client_name
			balance = my_client.balance
			currency = my_client.investment_currency
			exchange = my_client.exchange

			client_detail = my_client_detail.format(client_name,balance,currency,exchange)

			bot.edit_message_text(chat_id=chat_id, text=client_detail, message_id=call.message.message_id,reply_markup=my_portfolios_details_btn(my_client.client_id))
		
		elif call.data == 'stop_loss':
			bot.edit_message_text(chat_id=chat_id, text=stop_loss_msg, message_id=call.message.message_id,reply_markup=toggle_stop_loss_btn())
		
		elif call.data == 'stop_loss_enabled':
			bot.edit_message_text(chat_id=chat_id, text="automatic stop loss activated.", message_id=call.message.message_id,reply_markup=back_to_my_portfolio_btn())
		
		elif call.data == 'stop_loss_disabled':
			bot.edit_message_text(chat_id=chat_id, text="automatic stop loss de-activated.", message_id=call.message.message_id,reply_markup=back_to_my_portfolio_btn())
		
		
		elif call.data == "my_trades":
			my_trades = return_trade_history(user)
			bot.edit_message_text(chat_id=chat_id, text=f"{trade_history}{my_trades}", message_id=call.message.message_id,reply_markup=Main_Menu())

		elif call.data == "my_portfolio_faq":
			bot.edit_message_text(chat_id=chat_id, text=portfolio_info, message_id=call.message.message_id,reply_markup=my_portfolios_info_btn())

		elif call.data == "new_client":
			STEP.objects.filter(user = user).update(next_step="")
			bot.edit_message_text(chat_id=chat_id, text=step_1_of_3, message_id=call.message.message_id,reply_markup=new_client_step_1_of_3(show_menu))


		elif call.data.startswith("add_user:"):
			user,client_id = call.data.split(":")[1].split(",")
			subscriber = User.objects.get(user_id=user)

			MyClient.objects.filter(myclient=subscriber).update(has_funds = True,start_trading=True)
			bot.send_message(subscriber.chat_id,"Congratulations You deposit is successful the bot will start trading now.",reply_markup=Main_Menu())

			my_client = MyClient.objects.filter(Q(client_id__icontains=client_id)).first()# This is for a users client method

			msg = f"{call.message.text}\n\n Payment Approved ✅✅✅"
			bot.edit_message_text(chat_id=chat_id, text=msg, message_id=call.message.message_id,reply_markup=admin_approval(my_client.myclient,client_id))

		elif call.data.startswith("reject_user:"):
			# q = call.data.split(":")[1]
			user,client_id = call.data.split(":")[1].split(",")
			subscriber = User.objects.get(user_id=user)
			msg = """Sorry but we could'nt process your payment there go the bot will not start trading.
			"""
			MyClient.objects.filter(myclient=subscriber).update(has_funds = False,start_trading = False)
			my_client = MyClient.objects.filter(Q(client_id__icontains=client_id)).first()# This is for a users client method
			
			my_client.delete()
			bot.send_message(subscriber.chat_id,msg)
			bot.delete_message(chat_id=chat_id,message_id=call.message.message_id)
			
		#ABOUT CORNIX CALLBACK DATA
		elif call.data == "about_cornix":
			bot.edit_message_text(chat_id=chat_id, text=about_cornix_auto, message_id=call.message.message_id,reply_markup=about_cornix())

		elif call.data == "about_cornix_E":
			bot.edit_message_text(chat_id=chat_id, text=about_cornix_E, message_id=call.message.message_id,reply_markup=about_cornix_back())

		elif call.data == "cornix_can_do":
			bot.edit_message_text(chat_id=chat_id, text=cornix_can_do, message_id=call.message.message_id,reply_markup=about_cornix_back())

		elif call.data == "made_for":
			bot.edit_message_text(chat_id=chat_id, text=made_for, message_id=call.message.message_id,reply_markup=about_cornix_back())

		elif call.data == "trade_for":
			bot.edit_message_text(chat_id=chat_id, text=trade_for, message_id=call.message.message_id,reply_markup=about_cornix_back())

		elif call.data == "cornix_features":
			bot.edit_message_text(chat_id=chat_id, text=cornix_features, message_id=call.message.message_id,reply_markup=about_cornix_back())

		

		#WITHDRAWAL FUNTION BEGINS

		elif call.data.startswith("widthdrawal:"):

			client_id = call.data.split(':')[1]
			my_client = MyClient.objects.filter(Q(client_id__icontains=client_id)).first()

			MY_STATE["WITHDRAWAL"] = {}
			STEP.objects.filter(user = user).update(state = MY_STATE)

			MY_STATE["WITHDRAWAL"]["withdrawal_currency"] = my_client.investment_currency
			MY_STATE["WITHDRAWAL"]["withdrawal_client"] = client_id 
			msg = "Please enter the amount you want to withdraw in USDT:"
			STEP.objects.filter(user = user).update(state = MY_STATE,next_step="GET_WITHDRAWAL_AMOUNT")
			bot.send_message(chat_id=chat_id, text=msg,reply_markup=Cancel_btn())
	


		elif call.data == "confirm_withdrawal":

			withdrawal_amount = MY_STATE["WITHDRAWAL"]["withdrawal_amount"]
			client_id = MY_STATE["WITHDRAWAL"]["withdrawal_client"] 
			my_client = MyClient.objects.filter(Q(client_id__icontains=client_id))

			if my_client.exists():

				client = my_client.first()

				withdrawal_amount = MY_STATE["WITHDRAWAL"]["withdrawal_amount"]
				withdrawal_address = MY_STATE["WITHDRAWAL"]["withdrawal_address"]
				withdrawal_currency = MY_STATE["WITHDRAWAL"]["withdrawal_currency"]


				bot.send_message(chat_id=chat_id, text="Withdrawal in progress please wait...",reply_markup=Main_Menu())
				notify_admin_withdrawal(client.client_id,withdrawal_amount,withdrawal_currency,withdrawal_address)
			else:
				bot.send_message(chat_id=chat_id, text="Sorry not enough balance",reply_markup=Main_Menu())


		elif call.data == "cancel_withdrawal":
			bot.send_message(chat_id=chat_id, text="Withdrawal has been canceled",reply_markup=Main_Menu())


		elif call.data.startswith("approve_withdrawal:"):
			client_id,withdrawal_amount = call.data.split(":")[1].split(",")
			my_client = MyClient.objects.filter(Q(client_id__icontains=client_id)).first()# This is for a users client method

			balance = float(my_client.balance)-float(withdrawal_amount)
			my_client.balance = balance 
			my_client.save()

			if int(my_client.balance) <= 0:
				my_client.delete()# delete the users client
			else:
				pass


			client_id = hex(int(my_client.client_id.time_low))[2:]
			msg = f"{call.message.text}\n\nWidthdrawal Approved ✅✅✅"
			bot.edit_message_text(chat_id=chat_id, text=msg, message_id=call.message.message_id,reply_markup=admin_approve_withdrawal(client_id,withdrawal_amount))


		elif call.data.startswith("reject_withdrawal:"):
			# client_id = call.data.split(":")[1]
			# my_client = MyClient.objects.filter(Q(client_id__icontains=client_id)).first()# This is for a users client method
			bot.delete_message(chat_id=chat_id,message_id=call.message.message_id)
			
		else:
			pass

	except Exception as e:
		print(type(e).__name__,e,"CALLBACK ERROR")
		# bot.send_message(chat_id,step_1_of_3,reply_markup=new_client_step_1_of_3())



@bot.message_handler(commands=['start'])
def start(message):
	report = None
	user_detail = user_details(message)

	if user_detail["msg_type"] == "private":
		try:
			user = User.objects.get(user_id=user_detail["user_id"])
		except User.DoesNotExist:
			user = User(user_name=user_detail["username"],chat_id=user_detail["chat_id"],user_id=user_detail["user_id"])
			user.save()
			notify_admin(user)


		# save our user's state instance
		my_state, created = STEP.objects.get_or_create(user = user)
		try:
			NEW_CLIENT[user_detail["user_id"]]
		except KeyError:
			NEW_CLIENT[user_detail["user_id"]] = {}
		my_state.state = NEW_CLIENT[user_detail["user_id"]]
		my_state.save()
		#it ends here
		#Clear next step handler
		STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")

		my_portfolio = MyClient.objects.filter(myclient = user)
		if my_portfolio.exists():
			show_menu = True
		else:
			show_menu = False

		bot.send_message(user_detail["chat_id"],step_1_of_3,reply_markup=new_client_step_1_of_3(show_menu))
	else:
		pass

	
@bot.message_handler(content_types=['text'])
def reply_msg(message):
	user_detail = user_details(message)
	user = User.objects.get(user_id=user_detail['user_id'])
	my_state = STEP.objects.get(user = user)
	
	if user_detail["msg_type"] == "private":
		if message.text == "❌ Cancel":
			STEP.objects.filter(user = user_detail["user_id"]).update(next_step="")
			bot.send_message(user_detail["chat_id"],"Action terminated use the /start command to begin",reply_markup=ReplyKeyboardRemove(selective=False))
		
		elif my_state.next_step == "SET_NAME":
			set_my_client_name(message)
		elif my_state.next_step == "PROC_TXN_HASH":
			process_transaction_hash(message)
		elif my_state.next_step == "GET_INVEST_AMOUNT":
			set_invest_amount(message)
		elif my_state.next_step == "GET_WITHDRAWAL_AMOUNT":
			process_withdrawal_amount(message)

		elif my_state.next_step == "GET_WITHDRAWAL_ADDRESS":
			process_withdrawal_address(message)

		else:
			bot.send_message(user_detail["chat_id"],message.text)


	else:
		pass


@require_http_methods(["GET","POST"])
# @RateLimiter(max_calls=100, period=1)
def WebConnect(request):
	# Listens only for GET and POST requests
	# returns django.http.HttpResponseNotAllowed for other requests
	# Handle the event appropriately

	if request.method == 'POST':
		jsondata = request.body
		data = json.loads(jsondata)
		update = telebot.types.Update.de_json(data)
		bot.process_new_updates([update])
		return HttpResponse(status=201)
	else:
		bot.remove_webhook() #trying to find the reason for the too many requests
		time.sleep(1)
		bot.set_webhook(url=settings.WEBHOOK_URL+settings.WEBHOOK_TOKEN)
		print("Done")
		return HttpResponse(status=201)


# bot.load_next_step_handlers(filename="handlers-saves/step.save")
# try:
# 	bot.remove_webhook()
# 	bot.infinity_polling(timeout=10, long_polling_timeout = 5)
# except Exception as e:
# 	print(e,"ERORR FROM POLLING")
