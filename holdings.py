import yaml
import requests
   


staked_assets = "/cosmos/staking/v1beta1/delegations/"

def collector(addresses): 
    with open('config.yaml', 'r') as file:
            data = yaml.safe_load(file) 
    holdings = {}
    for address in addresses:    
        index = address.find("1")
        network = str(address[:index])
        url_list = data.get('supported_networks', {}).get(network, {}).get('APIs', [])
        for url in url_list:
            url = url + staked_assets + address
            response = requests.get(url)
            if response.status_code == 200: 
                print (f"Using {url}")
                responses = response.json()["delegation_responses"]
                validators = len(responses) 
                for i in range (0, validators):
                    stake = float(responses[i]['balance']['amount'])/1000000
                    if network in holdings:
                        holdings [network] += stake 
                    else: 
                        holdings [network] = stake 
                break
            elif url == url_list[-1]: 
                print (f"All APIs were used for {network} and none of them works!")       
                holdings [network] = 0               
        
    return (holdings)



# collector(['saga1qnsxa5chxj87mvm9jxqnyr9pdlp324mp0zc5m6','cosmos1n8wrmsa58765ck0phxq93etk3g0wtzwqzjgl2s','osmo1qnsxa5chxj87mvm9jxqnyr9pdlp324mpe2jk2w','cosmos1qnsxa5chxj87mvm9jxqnyr9pdlp324mp33pxuu'])


