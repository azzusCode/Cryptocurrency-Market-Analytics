from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

columns = ["Name", "Price", "1h", "24h","7d", "Market Cap", "Volume (24h)", "Circulating Supply"]

def get_crypto_details(row):
    details = row.text.split('\n')
    contents = {}
    if len(details) < 9:
        return None
    contents["Name"] = details[1]
    contents["Price"] = details[3].replace('$','').replace(',','')
    contents["1h"] = details[4].split(' ')[0].replace('%','')
    contents["24h"] = details[4].split(' ')[1].strip().replace('%','')
    contents["7d"] = details[4].split(' ')[2].strip().replace('%','')
    contents["Market Cap"] = details[5].replace('$','').replace(',','')
    contents["Volume (24h)"] = details[6].replace('$','').replace(',','')
    contents["Circulating Supply"] = details[8].split(' ')[0].replace(',','')
    return contents   
    
def main():
    
    data = []   
    for page_id in range(1,109):
        
        url = f"https://coinmarketcap.com/?page={page_id}"
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)
        [driver.execute_script(f"window.scrollBy(0, {step});") or time.sleep(delay) for step in [300] * (driver.execute_script("return document.body.scrollHeight") // 300) for delay in [0.5]]
        
        table = driver.find_element(By.CLASS_NAME, "sc-936354b2-3")
        print(table)
        rows = table.find_elements(By.TAG_NAME, "tr")
    
        for id, row in enumerate(rows):
            if (id > 0):
                data.append(get_crypto_details(row))
        driver.close()  
      
    data = [d for d in data if d is not None]
    print(len(data))    
    df = pd.DataFrame(data=data, columns=columns)
    df.to_csv("crypto_data.csv", index=False)
    
    return
    
if __name__ == "__main__":
    main()