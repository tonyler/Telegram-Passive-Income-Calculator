import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Disable sandboxing (necessary in some environments)
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

def store_data(network, apr, website, line, file_path='apr.txt'):
    with open(file_path, 'r') as file:
        old_content = file.readlines()

    # Ensure the list has enough lines
    while len(old_content) <= line:
        old_content.append("\n")

    # Update the specific line with the new data
    old_content[line] = f"{network} {apr} {website}\n"

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(old_content)


       
def collector():
    supported_networks = list(data['supported_networks'].keys())
    line = 0 
    staking_dict = {}

    for network in supported_networks:

        network_details = data['supported_networks'].get(network, {})
        websites_used = network_details.get('Websites', {})  
        for website in websites_used:
                selector = websites_used[website].get('selector')  # Accessing 'selector' under each website
                url = websites_used[website].get('url')
                try:
                    driver.get(url)
                except Exception as e: 
                     print (e)
                
                try:
                    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                    print(f"Successfully located APR for {network} via {website}. ✅ , {element.text}")
                except Exception as e:
                    print(f"Data fetched from {website} for {network} failed: {e} 🫤...")
                if website == list(websites_used.keys())[-1]: 
                        print ("-----------------------------------------")
                        print (f"!!!!!  All Websites failed for {network}. You gotta check this. !!!!")
                        print ("-----------------------------------------")
                        line += 1
                        continue
                try:
                    staking_dict[network] = float(element.text[:-1])
                    store_data (network, float(element.text[:-1]), website, line)
                    line+=1 
                    break
                except Exception as e: 
                    print (e)
                

    driver.quit()
    return(staking_dict)


