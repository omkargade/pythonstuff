#buy and sell stocks of ADANIPORTS using Kite api

from kiteconnect import KiteConnect
from kiteconnect import WebSocket
import requests

tp_b = 359.15
tp_s = 358.85
l_b = 359.20
l_s = 358.80
a=0
check = 1

api_key = ""
api_secret = ""
#print(api_key+" "+api_secret)

kite = KiteConnect(api_key=api_key,timeout=15)

print(kite.login_url()+"\nLogin on url and copy & enter request token\n")

req_token = input("Enter request token: ")

acc_list = (kite.request_access_token(req_token,api_secret))
acc_token = acc_list["access_token"]
pub_token = acc_list["public_token"]

def start():
    kws = WebSocket(api_key, pub_token, "DM4592")

    while True:
        kws.on_tick = on_tick
        kws.on_connect = on_connect
        kws.connect()

def on_tick(tick, ws):
    global acc_token, pub_token, once, z, c, d, b, sl1, sl2, check,a
    print("\n", tick)
    for j in tick:
        print("ltp: ", j['last_price'])
        ltp = j['last_price']

    if a == 0:
        if ltp>l_s:
            print(kite.order_place(tradingsymbol="ADANIPORTS", quantity=1, exchange="NSE", transaction_type="SELL",
                             price=l_s, trigger_price=tp_s, order_type="SL", product="MIS"))
            a=1
    if a==1:
        if ltp<l_s:
            print(kite.order_place(tradingsymbol="ADANIPORTS", quantity=1, exchange="NSE", transaction_type="BUY",
                                           price=l_b, trigger_price=tp_b, order_type="SL", product="MIS"))
            a=3
    if a==3:
        if ltp>l_b:
            print(kite.order_place(tradingsymbol="ADANIPORTS", quantity=1, exchange="NSE", transaction_type="SELL",
                                           price=l_s, trigger_price=tp_s, order_type="SL", product="MIS"))
            a=1


def on_connect(ws):
    ws.subscribe([3861249])
    ws.set_mode(ws.MODE_LTP, [3861249])

###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################

def can_order(oid):
    response = kite.order_cancel(oid,"regular")
    print(response)

def get_id(oid, a_token):
    global a_price  # if a_price error then remove this line
    response = requests.get("https://api.kite.trade/orders/" + oid + "?api_key=" + api_key + "&access_token=" + a_token)
    book = response.json()
    for i in book["data"]:
        if (i["average_price"] != 0.0):
            a_price = i["average_price"]

    return a_price

start()
