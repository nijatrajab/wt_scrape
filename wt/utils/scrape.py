import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.color import convert_rgb_to_names


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

    price_list = []
    name_list = []
    link_list = []
    brand_list = []
    color_list = []
    img_list = []
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
    driver.quit()
    div_grid = doc.find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-7 MuiGrid-grid-lg-8")

    if div_grid is not None:
        children_price = div_grid.findChildren('p', class_=re.compile('Card_price_', re.I))
        children_image_div = div_grid.findChildren('div', class_=re.compile('Card_imageContainer', re.I))
        children_name_div = div_grid.findChildren('div', class_=re.compile('Card_name', re.I))

        price_list += [lnk.text for lnk in children_price]
        name_list += [chn.findChild('h3').text for chn in children_name_div]
        brand_list += [chn.findChild('a', href=re.compile('/mehsullar/', re.I))['href'].split('brands')[1][1:] for chn
                       in children_name_div]
        link_list += [chn.findChild('a', href=re.compile('/mehsul/', re.I))['href'] for chn in children_name_div]
        color_list += [[convert_rgb_to_names(
            cc.findChild('div', class_=re.compile('Card_color_', re.I))['style']) if cc.findChild(
            'div', class_=re.compile('Card_color_', re.I)) is not None and cc.findChild(
            'div', class_=re.compile('Card_color_', re.I)).has_attr('style') else None for cc in chi.findChildren(
            'div', class_=re.compile('Card_colorContainer_', re.I))] for chi in children_image_div]
        img_list += [chc.findChild('img')['src'] for chc in children_image_div]

        if len(price_list) != 0:
            for i in range(len(price_list)):
                product_list += [{'brand': brand_list[i], 'title': name_list[i], 'price': price_list[i],
                                  'link': "https://www.w-t.az/" + link_list[i], 'color': color_list[i],
                                  'img': img_list[i],
                                  'category': wt_dict[ctg]['category'], 'subcategory': wt_dict[ctg]['subcategory']}]
        else:
            print('No product found!')

        print(f'Found {len(name_list)} product{"s" if len(name_list) > 1 else ""} '
              f'for {wt_dict[ctg]["subcategory"]} subcategory')
    else:
        print('Something bad happened!')

    return product_list
