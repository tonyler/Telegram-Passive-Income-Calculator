




def tokens_income(holdings):
    passive_dict = {} 
    with open("apr.txt", 'r') as file:
        saved_aprs = file.readlines()
        print (saved_aprs)

    for network in holdings: 
        for line in saved_aprs: 
            elements = line.split()
            if elements[0] == network:
                apr = float(elements[1])
                income = holdings[network] * apr/100
                print (f"income from {network} is {income} tokens per year")
                passive_dict[network] = income #in tokens, not 
                break
    return (passive_dict)

def tokens_to_dollars(tokens_earned, prices): 
    total = 0
    passive_income_dict = {}
    for network in tokens_earned: 
        income = tokens_earned[network] * prices[network]
        total+=income
        print (f"Yearly Income from {network} is {income}")
    
    print (f"Yearly Income in total: {total}")
    monthly = total / 12 
    print (f"Monthly Income in total: {monthly}")
    daily = monthly/30 
    print (f"Daily Income in total: {daily}")

    passive_income_dict["yearly"] = total
    passive_income_dict["monthly"] = monthly
    passive_income_dict["daily"] = daily

    return passive_income_dict


