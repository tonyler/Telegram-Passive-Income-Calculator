import telebot
from calc_core import calculations


bot = telebot.TeleBot("SECRET", parse_mode='Markdown') # You can set parse_mode by default.HTML or MARKDOWN	

user_started = {}
wallets_list = {}

@bot.message_handler(commands=['start'])
def send_stats(message):
    user_id = message.from_user.id
    user_started[user_id] = True
    wallets_list[user_id] = []
    print (f'Bot initiated by {user_id}')
    bot.reply_to(message, "Type your cosmos addresses (one from each derivation path)\n Type 'calc' to begin calculations.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    if message.chat.type == 'private' and user_started.get(user_id):
        if len(message.text) > 44:
            if message in wallets_list[user_id]: 
                bot.reply_to(message, "This address has been added already!")
            else: 
                print (f"Wallet added!")
                wallets_list[user_id].append(message.text)
                bot.reply_to(message, "Wallet added\n Add more wallets or send 'calc' to calculate") 
        
        elif message.text == "calc": 
            bot.reply_to(message, "Give me a minute...")
            try:
                passive_income = calculations(wallets_list[user_id])
                bot.reply_to(message, f"""
Passive Income
Daily --> {round(passive_income["daily"],2)}
Monthly --> {round(passive_income["monthly"],2)}
Yearly --> {round(passive_income["yearly"],2)}
""")

            except Exception as e: 
                bot.reply_to(message,"Something went wrong :S.\n No passive income calculations for you :P")
                print (e)


            


bot.infinity_polling()

# def calculations(wallets):
#     addresses_list = addresses.collector(wallets)
#     apr_list = apr.collector()
#     holdings_list = holdings.collector(addresses_list)

#     tokens_earned = calculator.tokens_income(holdings_list, apr_list)
#     print (tokens_earned)

#     prices_list = prices.collector ()
#     passive_income = calculator.tokens_to_dollars(tokens_earned, prices_list)
# # tokens = float(input("How many tokens you got?"))
# Yearly = tokens * apr / 100
# Monthly = Yearly / 12 
# Daily = Monthly / 30


# osmosis_url = 'https://api-osmosis.imperator.co/tokens/v2/saga'
# response = requests.get(osmosis_url)
# price = response.json()[0]['price']
# print (price)
# Yearly = Yearly * price
# Monthly = Monthly * price
# Daily = Daily * price

# print (Daily)


# cosmos1qnsxa5chxj87mvm9jxqnyr9pdlp324mp33pxuu
# archway1n8wrmsa58765ck0phxq93etk3g0wtzwqhe5mq8
# cosmos1z23gy5wmhmeq2v349hzfy7ndq9jfq3k05hpms7
# cosmos159k45unpajxzmjttreggecy02ymte4perl9zmm
# cosmos1ehgxjv8hz7y5kxq4zczfmlrjrpflghpjup6d0p