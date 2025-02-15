from operator import truediv
from ks_api_client import ks_api 
import time 
import sys
import math

#Client Security credentials
access_token = "4a83250c-6245-30ca-920d-b6610f5b0982"
user_id = "MS1041996"
consumer_key = "HAmCjJ7Q5psDiXK_MzAIxOLPkS4a"
consumer_secret = "adUuNB3Vjlg136XE2BLmuClDxFoa"
client_password = "M@n@n_1"
bid_percent_lower = 3
sell_percent_higher = 5
# instrument_token = 10069
instrument_token_list = [2210,2071,10070] #If you are adding a new value in this list so add one more False in the order_status_list
order_status_list = [False,False,False]
stock_opening_price_list = [] #don't change this 
order_id_list = [] #don't change this 
quantity = 1
order_executed = True

#Initialize client and authorize
client = ks_api.KSTradeApi(access_token = access_token, userid = user_id, consumer_key = consumer_key,ip = "127.0.0.1", app_id = "ksec_fetch", host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = consumer_secret)
client.login(password = client_password)
client.session_2fa()

#Get stock's day opening price
def stock_price(instrument_token):
    open_price = float(client.quote(instrument_token = instrument_token)['success'][0]['open_price'])
    return open_price

#Place a BUY order
def place_buy_order(stock_opening_price, instrument_token, quantity):
    bid_price = math.floor((100 - bid_percent_lower)/100 * float(stock_opening_price))
    response = client.place_order(order_type = "N", instrument_token = instrument_token, transaction_type = "BUY", quantity = quantity, price = bid_price, disclosed_quantity = 0, trigger_price = 0, validity = "GFD", variety = "REGULAR", tag = 
"string")
    if "NSE" in response.keys():
        order_id = response["Success"]["NSE"]["orderId"]
    else:
        order_id = response["Success"]["BSE"]["orderId"]
    print("Bid placed at: ", bid_price)
    return order_id

#Check order status
def check_order_status(order_id):
    response = client.order_report(order_id = 2220526081044)
    order_executed = any(order['status'] == "TRAD" for order in response['success'])
    return order_executed

#Place a SELL order
def place_sell_order(buy_price, instrument_token, quantity):
    sell_price = math.ceil((100 + sell_percent_higher)/100 * float(buy_price))
    response = client.place_order(order_type = "N", instrument_token = instrument_token, transaction_type = "SELL", quantity = quantity, price = sell_price, disclosed_quantity = 0, trigger_price = 0, validity = "GFD", variety = "REGULAR", tag = 
"string")
    if "NSE" in response.keys():
        order_id = response["Success"]["NSE"]["orderId"]
    else:
        order_id = response["Success"]["BSE"]["orderId"]
    print("Sell order placed at: ", sell_price)
    return order_id

for instrument_token in instrument_token_list:
    stock_opening_price = stock_price(instrument_token)
    print("Opening price for instrument token", instrument_token, "is:", stock_opening_price)
    order_id = place_buy_order(stock_opening_price, instrument_token, quantity)
    print("Order ID: ", order_id)
    order_id_list.append(order_id)
    stock_opening_price_list.append(stock_opening_price)
    time.sleep(0.2) #these are added to make the preogram free from glitches

while True:
    for i in range(len(instrument_token_list)):
        if order_executed == check_order_status(order_id_list[i]):
            print(f"Order placed for ID:{order_id_list[i]}   for instrument token : {instrument_token_list[i]}")
            print("Now placing Sell order")
            sell_order_id = place_sell_order(stock_opening_price_list[i], instrument_token_list[i], quantity)
        time.sleep(0.1) #these are added to make the preogram free from glitches

    # Old code 
    # while order_executed != check_order_status(order_id):
    #     print("Checking order status.......!!")
    #     time.sleep(10)
    #     check_order_status(order_id)

    # sell_order_id = place_sell_order(stock_opening_price, instrument_token, quantity)
