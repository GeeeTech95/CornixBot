from .config import *
from telebot.types import *


def tech_support():
	keyboard = InlineKeyboardMarkup()
	support = InlineKeyboardButton(f"Support 🙋",url="https://t.me/CornixTradingTechSupport_bot")
	keyboard.add(support)
	return(keyboard)

def home_key():
	keyboard = InlineKeyboardMarkup()
	new_client = InlineKeyboardButton("Add Another Client",callback_data=f"new_client")
	my_portfolio = InlineKeyboardButton("Portfolio",callback_data=f"my_portfolio")
	# configs = InlineKeyboardButton("📈 Optimized Configs",callback_data=f"configs")
	# auto_trading = InlineKeyboardButton("🔥 Auto Trading",callback_data=f"return_to_menu")
	# signals = InlineKeyboardButton("Signals",callback_data=f"return_to_menu")
	Trades = InlineKeyboardButton("Trades",callback_data=f"my_trades")
	bot_configs = InlineKeyboardButton("⚙️ Bot Configuration",callback_data=f"bot_configs")
	# misc = InlineKeyboardButton("Misc.",callback_data=f"misc")
	# subscription = InlineKeyboardButton("📝Subscription",callback_data=f"my_subscription")
	about_cornix = InlineKeyboardButton(f"ℹ️ Help",callback_data=f"about_cornix")
	support = InlineKeyboardButton(f"Support 🙋",url="http://t.me/CornixTradingTechSupport_bot")
	widthdrawal = InlineKeyboardButton(f"♻️ widthdraw",callback_data=f"widthdrawal")

	keyboard.add(new_client)
	keyboard.add(my_portfolio,Trades)
	keyboard.add(bot_configs)
	keyboard.add(widthdrawal)
	keyboard.add(support,about_cornix)
	return(keyboard)

def Main_Menu():
	keyboard = InlineKeyboardMarkup()
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")
	keyboard.add(main_menu)
	return(keyboard)

def my_portfolios_info_btn():
	keyboard = InlineKeyboardMarkup()
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:my_portfolio")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")
	keyboard.add(main_menu,back)
	return(keyboard)

def my_portfolios_btn():
	keyboard = InlineKeyboardMarkup()
	faq = InlineKeyboardButton("✋ How it Works",callback_data=f"my_portfolio_faq")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")
	keyboard.add(faq)
	keyboard.add(main_menu)
	return(keyboard)

def new_client_step_1_of_3(show_menu):
	keyboard = InlineKeyboardMarkup()

	Binance_client = InlineKeyboardButton(f"Binance",callback_data=f"Binance@client")
	FTX_client = InlineKeyboardButton(f"FTX",callback_data=f"FTX@client")
	ByBit_client = InlineKeyboardButton(f"ByBit",callback_data=f"ByBit@client")
	BitMEX_client = InlineKeyboardButton(f"KuCoin",callback_data=f"BitMEX@client")
	Huobipro_client = InlineKeyboardButton(f"Huobi.pro",callback_data=f"Huobi.pro@client")
	coinex_client = InlineKeyboardButton(f"Coinex",callback_data=f"Coinex@client")
	support = InlineKeyboardButton(f"Support 🙋",url="http://t.me/cornixautotradingsupport")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")

	
	
	keyboard.add(Binance_client,FTX_client)
	keyboard.add(ByBit_client,BitMEX_client)
	keyboard.add(Huobipro_client,coinex_client)
	keyboard.add(support) #temporarily disabling support
	if show_menu == True:
		keyboard.add(main_menu)
	else:
		pass

	return(keyboard)
	

def new_client_step_1_2_of_3(exchange,show_menu):
	keyboard = InlineKeyboardMarkup()
	if exchange == "Binance":
		binance_futures = InlineKeyboardButton(f"Binance Futures",callback_data=f"option_binance_futures:{exchange}")
		binance_coins_futures = InlineKeyboardButton(f"Binance Coins-Futures",callback_data=f"option_binance_coins_futures:{exchange}")
		binance_spot = InlineKeyboardButton(f"Binance Spot (Regular)",callback_data=f"option_binance_spot:{exchange}")

		keyboard.add(binance_futures)
		keyboard.add(binance_coins_futures)
		keyboard.add(binance_spot)

	elif exchange == "Coinex":
		coinex_futures = InlineKeyboardButton(f"Coinex Futures",callback_data=f"option_coinex_futures:{exchange}")
		coinex_spot = InlineKeyboardButton(f"Coinex Spot (Regular)",callback_data=f"option_coinex_spot:{exchange}")
		coinex_margin = InlineKeyboardButton(f"Coinex Margin",callback_data=f"option_coinex_margin:{exchange}")
		coinex_finacial = InlineKeyboardButton(f"Coinex Financial",callback_data=f"option_coinex_financial:{exchange}")
		keyboard.add(coinex_futures)
		keyboard.add(coinex_spot)
		keyboard.add(coinex_margin)
		keyboard.add(coinex_finacial)


	else:
		bybit_inverse = InlineKeyboardButton(f"ByBit Inverse ",callback_data=f"option_bybit_inverse:{exchange}")
		bybit_linear = InlineKeyboardButton(f"ByBit Linear",callback_data=f"option_bybit_linear:{exchange}")

		keyboard.add(bybit_inverse)
		keyboard.add(bybit_linear)

	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")

	

	about_cornix = InlineKeyboardButton(f"About Cornix",callback_data=f"about_cornix")
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:1")
	support = InlineKeyboardButton(f"Support 🙋",url="http://t.me/CornixTradingTechSupport_bot")
	
	
	keyboard.add(about_cornix,support)
	if show_menu == True:
		keyboard.add(main_menu)
	else:
		pass
	keyboard.add(back)
	return(keyboard)


def new_client_step_2_of_3(exchange,show_menu):
	keyboard = InlineKeyboardMarkup()

	client_name = InlineKeyboardButton(f"My-{exchange}",callback_data=f"set_name:My-{exchange}")
	about_cornix = InlineKeyboardButton(f"About Cornix",callback_data=f"about_cornix")
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:1_2")
	support = InlineKeyboardButton(f"Support 🙋",url="http://t.me/CornixTradingTechSupport_bot")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")

	
	
	keyboard.add(client_name)
	keyboard.add(about_cornix,support)
	if show_menu == True:
		keyboard.add(main_menu)
	else:
		pass
	keyboard.add(back)
	
	return(keyboard)

def new_client_step_3_of_3(exchange,show_menu):
	keyboard = InlineKeyboardMarkup()

	about_cornix = InlineKeyboardButton(f"About Cornix",callback_data=f"about_cornix")
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:2")
	support = InlineKeyboardButton(f"Support 🙋",url="http://t.me/CornixTradingTechSupport_bot")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")

	keyboard.add(about_cornix,support)
	if show_menu == True:
		keyboard.add(main_menu)
	else:
		pass
	keyboard.add(back)
	return(keyboard)


def about_cornix(step="home"):
	keyboard = InlineKeyboardMarkup()

	about_cornix_E = InlineKeyboardButton("Tell me about Cornix",callback_data=f"about_cornix_E")
	cornix_can_do = InlineKeyboardButton("What can Cornix do for me?",callback_data=f"cornix_can_do")
	made_for = InlineKeyboardButton("Who is Cornix made for?",callback_data=f"made_for")
	trade_for = InlineKeyboardButton("How does Cornix trade for me?",callback_data=f"trade_for")
	cornix_features = InlineKeyboardButton("What trading features does Cornix offer?",callback_data=f"cornix_features")

	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:{step}")
	support = InlineKeyboardButton(f"Support 🙋",url="http://t.me/CornixTradingTechSupport_bot")
	
	keyboard.add(about_cornix_E)
	keyboard.add(cornix_can_do)
	keyboard.add(made_for)
	keyboard.add(trade_for)
	keyboard.add(cornix_features)
	keyboard.add(back,support)
	return(keyboard)


def about_cornix_back():
	keyboard = InlineKeyboardMarkup()

	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:about")
	keyboard.add(back)
	return(keyboard)


def client_creation_success():
	keyboard = InlineKeyboardMarkup()
	start_trading = InlineKeyboardButton("Yes",callback_data=f"start_trading")
	main_menu = InlineKeyboardButton("No",callback_data=f"return_to_menu")
	keyboard.add(start_trading,main_menu)
	return(keyboard)


def deposit_options():
	keyboard = InlineKeyboardMarkup()

	key_1 = InlineKeyboardButton(f"$1,000 USDT",callback_data=f"deposit:1000")
	key_2 = InlineKeyboardButton(f"$3,000 USDT",callback_data=f"deposit:3000")
	key_3 = InlineKeyboardButton(f"$5,000 USDT",callback_data=f"deposit:5000")
	key_4 = InlineKeyboardButton(f"$10,000 USDT",callback_data=f"deposit:10000")
	key_5 = InlineKeyboardButton(f"$25,000 USDT",callback_data=f"deposit:25000")
	# key_4 = InlineKeyboardButton(f"$2,600  USDT",callback_data=f"deposit:2600")
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:2")
	
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	keyboard.add(key_5)
	keyboard.add(back)
	return(keyboard)


def payment_method():
	keyboard = InlineKeyboardMarkup()
	usdt_pay = InlineKeyboardButton("⚡ USDT.TRC20 (Tether USD(Tron/TRC20))",callback_data=f"pay_with:USDT")
	sol_pay = InlineKeyboardButton("⚡ Solana (SOL)",callback_data=f"pay_with:SOL")
	btc_pay = InlineKeyboardButton("⚡ Bitcoin (BTC)",callback_data=f"pay_with:BTC")
	eth_pay = InlineKeyboardButton("⚡ Ethereum (ETH)",callback_data=f"pay_with:ETH")
	xrp_pay = InlineKeyboardButton("⚡ Ripple (XRP)",callback_data=f"pay_with:XRP")
	dot_pay = InlineKeyboardButton("⚡ Polkadot (DOT)",callback_data=f"pay_with:DOT")
	dodge_pay = InlineKeyboardButton("⚡ Dodge",callback_data=f"pay_with:DODGE")
	back = InlineKeyboardButton("↵ Back",callback_data=f"return_to_menu")
	keyboard.add(usdt_pay)
	keyboard.add(sol_pay)
	keyboard.add(btc_pay)
	keyboard.add(eth_pay)
	keyboard.add(xrp_pay)
	keyboard.add(dot_pay)
	keyboard.add(dodge_pay)
	keyboard.add(back)
	return(keyboard)


def confirm_payment():
	keyboard = InlineKeyboardMarkup()
	i_paid = InlineKeyboardButton("💳 I've made deposit",callback_data=f"i_paid")
	back = InlineKeyboardButton("↵ Back",callback_data=f"return_to_menu")
	keyboard.add(i_paid)
	keyboard.add(back)
	return(keyboard)



def bot_configs():
	keyboard = InlineKeyboardMarkup()
	clients = InlineKeyboardButton("Clients",callback_data=f"my_clients")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")
	keyboard.add(clients)
	keyboard.add(main_menu)
	return(keyboard)


def bot_configs_clients(my_clients):
	keyboard = InlineKeyboardMarkup()
	for client in my_clients:
		client_id = hex(int(client.client_id.time_low))[2:]
		keyboard.add(InlineKeyboardButton(f"{client.client_name}",callback_data=f"my_client:{client_id}"))

	new_client = InlineKeyboardButton("➕ Add New Client",callback_data=f"new_client")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:bot_configs")
	keyboard.add(new_client)
	keyboard.add(main_menu,back)
	return(keyboard)

def configs_clients(client_id):
	keyboard = InlineKeyboardMarkup()
	delete_client = InlineKeyboardButton("❌ Delete",callback_data=f"delete_client:{client_id}")
	main_menu = InlineKeyboardButton("⇱ Main Menu",callback_data=f"return_to_menu")
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:bot_configs")
	keyboard.add(delete_client)
	keyboard.add(main_menu,back)
	return(keyboard)


def back_to_configs():
	keyboard = InlineKeyboardMarkup()
	back = InlineKeyboardButton(f"↵ Back",callback_data=f"back_to_step:bot_configs")
	keyboard.add(back)
	return(keyboard)

def Cancel_btn():
	keyboard = ReplyKeyboardMarkup(True)
	keyboard.row("❌ Cancel",)
	return(keyboard)


def admin_approval(user,client_id):
	keyboard = InlineKeyboardMarkup()
	approve = InlineKeyboardButton("✅ Approve",callback_data=f"add_user:{user},{client_id}")
	reject = InlineKeyboardButton("❌ Reject",callback_data=f"reject_user:{user}")
	keyboard.add(approve,reject)
	return(keyboard)


# This is for withdrawals

def withdrawal_currency_opt():
	keyboard = InlineKeyboardMarkup()
	usdt_pay = InlineKeyboardButton("⚡ TETHER USD/Tron (TRC20)",callback_data=f"withdraw_with:USDT")
	btc_pay = InlineKeyboardButton("⚡ BITCOIN (BTC)",callback_data=f"withdraw_with:SOL")
	eth_pay = InlineKeyboardButton("⚡ ETHEREUM (ETH)",callback_data=f"withdraw_with:BTC")
	sol_pay = InlineKeyboardButton("⚡ SOLANA (SOL)",callback_data=f"withdraw_with:ETH")
	xrp_pay = InlineKeyboardButton("⚡ RIPPLE (XRP)",callback_data=f"withdraw_with:XRP")
	dot_pay = InlineKeyboardButton("⚡ POLKADOT (DOT)",callback_data=f"withdraw_with:DOT")
	dodge_pay = InlineKeyboardButton("⚡ DODGE",callback_data=f"withdraw_with:DODGE")
	back = InlineKeyboardButton("↵ Back",callback_data=f"return_to_menu")
	keyboard.add(usdt_pay)
	keyboard.add(btc_pay)
	keyboard.add(eth_pay)
	keyboard.add(sol_pay)
	keyboard.add(xrp_pay)
	keyboard.add(dot_pay)
	keyboard.add(dodge_pay)
	keyboard.add(back)
	return(keyboard)


def confirm_withdrawal():
	keyboard = InlineKeyboardMarkup()
	approve = InlineKeyboardButton("✅ Confirm",callback_data=f"confirm_withdrawal")
	reject = InlineKeyboardButton("❌ Cancel",callback_data=f"cancel_withdrawal")
	keyboard.add(approve,reject)
	return(keyboard)


def admin_approve_withdrawal(client_id,withdrawal_amount):
	keyboard = InlineKeyboardMarkup()
	approve = InlineKeyboardButton("✅ Approve Withdrawal",callback_data=f"approve_withdrawal:{client_id},{withdrawal_amount}")
	reject = InlineKeyboardButton("❌ Reject Withdrawal",callback_data=f"reject_withdrawal:{client_id}")
	keyboard.add(approve,reject)
	return(keyboard)
