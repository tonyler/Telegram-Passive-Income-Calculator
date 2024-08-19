import yaml
import bech32

with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)
addresses__list = []

supported_networks = list(data['supported_networks'].keys())


def convert_prefix(addresses_: list, new_prefix: str) -> str:
    new_addresses_ = []
    for address in addresses_:
        try:
            # Decode the bech32 address
            hrp, data = bech32.bech32_decode(address)
            if not hrp or not data:
                raise ValueError("Invalid bech32 address")
            
            # Re-encode with the new prefix
            new_addresses_.append(bech32.bech32_encode(new_prefix, data))
        except Exception as e:
            return f"Error converting bech32 address: {e}"

    return new_addresses_

def collector(addresses_):
        for network in supported_networks:
            new_address = convert_prefix(addresses_, network)
            addresses__list.extend(new_address)
            print(f"Converted address for {network}: {new_address}")
        return addresses__list