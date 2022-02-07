import json
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.color_v2 import convert_rgb_to_names


def items_array(ctg, wt_dict):
    url = f"https://www.w-t.az/mehsullar/{ctg}"

    options = Options()
    options.headless = True

    driver = webdriver.Remote(
        command_executor='http://selenium:4444',
        desired_capabilities=DesiredCapabilities.FIREFOX, options=options)

    try:
        # driver.set_page_load_timeout(60)
        driver.get(url)
    except TimeoutError as te:
        print("Exception has been thrown: " + str(te))
        driver.close()
        driver.quit()

    previous_height = driver.execute_script("return document.body.scrollHeight")

    name_list = []
    link_list = []
    product_list = []

    print(f'Starting scrape for: {wt_dict[ctg]["subcategory"]}')

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            WebDriverWait(driver, 5).until(
                lambda driver: driver.execute_script("return document.body.scrollHeight;") > previous_height)
            previous_height = driver.execute_script("return document.body.scrollHeight;")
        except:
            break

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_elements(By.CLASS_NAME, re.compile(
                '(?=.*Card_price_)(?=.*Card_name)(?=.*MuiGrid-root MuiGrid-item '
                'MuiGrid-grid-xs-12 MuiGrid-grid-md-7 MuiGrid-grid-lg-8)', re.I)))
    except:
        pass

    doc = BeautifulSoup(driver.page_source, 'html.parser')
    div_grid = doc.find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-7 MuiGrid-grid-lg-8")

    if div_grid is not None:
        children_name_div = div_grid.findChildren('div', class_=re.compile('Card_name', re.I))
        link_list += ["https://www.w-t.az" + chn.findChild('a', href=re.compile('/mehsul/', re.I))['href'] for chn in children_name_div]

        if len(link_list) != 0:
            for url in link_list:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(url)

                prod_doc = BeautifulSoup(driver.page_source, 'html.parser')
                prod_html = prod_doc.find('script', id=re.compile('__NEXT_DATA__', re.I))
                prod_data = json.loads(prod_html.text)['props']['pageProps']['product']

                for i in range(len(prod_data['options'])):
                    brand = prod_data['options'][i]['parameters'][0]['value'].strip() if prod_data['options'][i]['parameters'][0]['value'] is not None else None
                    model = prod_data['model'].strip() if prod_data['model'] is not None else None
                    identificator = prod_data['options'][i]['identificator'].strip() if prod_data['options'][i]['identificator'] is not None else None
                    title = (brand if brand is not None else '') + ' ' + (model if brand is not None else '')
                    full_title = (title if brand is not None else '') + ' ' + (identificator if brand is not None else '')
                    memory = ''.join(prod_data['options'][i]['memory'].strip().split(' ')) if prod_data['options'][i]['memory'] is not None else None
                    color = convert_rgb_to_names(prod_data['options'][i]['color'].strip()) if prod_data['options'][i]['color'] is not None else None
                    price = prod_data['options'][i]['price']
                    discount_price = prod_data['options'][i]['discount']['price']
                    image = prod_data['options'][i]['images'][0] if len(prod_data['options'][i]['images']) > 0 else None
                    link = f'https://www.w-t.az/mehsul/{prod_data["options"][i]["productId"]}/{prod_data["options"][i]["slug"]}'

                    product_list += [{
                        'brand': brand,
                        'model': model,
                        'identification': identificator,
                        'title': title,
                        'full_title': full_title,
                        'memory': memory,
                        'color': color,
                        'price': price,
                        'discount_price': discount_price if discount_price != 0 else None,
                        'image': image,
                        'link': link,
                        'category': wt_dict[ctg]['category'],
                        'subcategory': wt_dict[ctg]['subcategory']
                    }]

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        else:
            print('No product found!')

        print(f'Found {len(product_list)} product{"s" if len(product_list) > 1 else ""} '
              f'for {wt_dict[ctg]["subcategory"]} subcategory')
    else:
        print('Something bad happened!')
    driver.quit()
    return product_list
