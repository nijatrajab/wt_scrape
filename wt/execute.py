import json
import csv
import time
import urllib.request

from utils.scrape import items_array
from utils.constants import wt_slug, wt_sub_cat, wt_cat

print("Connecting Selenium Firefox ...")

response_status = 0
while response_status != 200:
    try:
        response = urllib.request.urlopen('http://selenium:4444/wd/hub/status')
        response_status = response.status
        response.close()
        time.sleep(2)
    except Exception as e:
        print("The Selenium Firefox is NOT ready! - " + str(e))
        time.sleep(2)
        pass

print("The Selenium Firefox is ready!")

wt_dict = {k: {'category': v1, 'subcategory': v2} for k, v1, v2 in zip(wt_slug, wt_cat, wt_sub_cat)}
all_products = []

start = time.time()

for i in wt_slug[:1]:
    all_products += items_array(i, wt_dict)

end = time.time()
elapsed = end - start

print(f'Scraping took {elapsed} seconds!')
print(f'{len(all_products)} products has been found!')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)

data_file = open('data.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in all_products:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
data_file.close()
