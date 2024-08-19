import addresses, apr, holdings, calculator, prices

	
def calculations(wallets):
    print (wallets)
    addresses_list = addresses.collector(wallets)
    apr_list = apr.collector()
    holdings_list = holdings.collector(addresses_list)

    tokens_earned = calculator.tokens_income(holdings_list)

    prices_list = prices.collector ()
    passive_income = calculator.tokens_to_dollars(tokens_earned, prices_list)
    return passive_income

# # tokens = float(input("How many tokens you got?"))
# # Yearly = tokens * apr / 100
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