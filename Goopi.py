  
import json
import os
import string
import sys
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import base64
import re
from datetime import datetime
import time
import urllib.parse as urllib
  
product_name = 'Wall of Sound - 7:37/“MOTE” Mesh-Mix Snow Pants'
Color = 'Black'
size = 'L'
count = 2
info_username = '張某某'
info_email = 'aabb@gmail.com'
info_phone = '0966123432'
info_LineId = '@aery'
info_msg = '盡快出貨'
info_card_number = '4532115598843071'
info_card_name = '張某某'
info_card_date = '10/27'
info_card_cvc = '171'
params = {
    'storeid': '263713',
    'storename': '新大慶門市',
    'storeaddress': '基隆市中山區中和路168巷7弄13號15號1樓',
    'outside': '0',
    'ship': '1111111',
    'TempVar': '',
    'isSameTab': 'true' }
expiry_date_str = '2024-07-01 11:30:00'

 
def myprint(str):
    currentDateAndTime = datetime.now() 
    print(f"{currentDateAndTime} {str}")

def GetNumInStr(str):
    matches = re.search(r'\d+', str)
    num = -1
    if matches:
        num = int(matches[0])
    else:
        num = -1
    return num

def WaitObjId(browser,id):
    wait = WebDriverWait(browser, 5)
    try:
        element = wait.until(EC.presence_of_element_located((By.ID, f"{id}")))
        return True
    except TimeoutException:
        return False

#讀取設定
def read_info_from_json(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def check_date(expiry_date_str):
    # 指定日期格式
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # 取得當前日期
    current_date = datetime.now()
    
    # 解析指定的過期日期
    expiry_date = datetime.strptime(expiry_date_str, date_format)
    
    # 比較當前日期和過期日期
    if current_date > expiry_date:
        #print("超過指定日期，程式將退出。")
        exit(-1)
    else:
        print("pass")
#字符轉換
def replace_symbols_with_space(text):
     
    translator = str.maketrans(string.punctuation, ',' * len(string.punctuation))
 
    return text.translate(translator)
#選信用卡
def select_cvc_card(driver:uc.Chrome):
   
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@id, 'number')]")))
    card_number_iframe = driver.find_element(By.XPATH, "//iframe[contains(@id, 'number')]")
    driver.switch_to.frame(card_number_iframe)
 
    card_number_input = driver.find_element(By.TAG_NAME, "input")
    card_number_input.send_keys(info_card_number)  

   
    driver.switch_to.default_content()

    
    card_name_iframe = driver.find_element(By.XPATH, "//iframe[contains(@id, 'firstName')]")
    driver.switch_to.frame(card_name_iframe)
   
    card_name_input = driver.find_element(By.TAG_NAME, "input")
    card_name_input.send_keys(info_card_name)  

   
    driver.switch_to.default_content()

  
    expiry_date_iframe = driver.find_element(By.XPATH, "//iframe[contains(@id, 'expDate')]")
    driver.switch_to.frame(expiry_date_iframe)
   
    expiry_date_input = driver.find_element(By.TAG_NAME, "input")
    expiry_date_input.send_keys(info_card_date)   

    driver.switch_to.default_content()
 
    cvc_iframe = driver.find_element(By.XPATH, "//iframe[contains(@id, 'cvc')]")
    driver.switch_to.frame(cvc_iframe)
    
    cvc_input = driver.find_element(By.TAG_NAME, "input")
    cvc_input.send_keys(info_card_cvc)   

   
    driver.switch_to.default_content()
 

def Util():
    #sys.stderr = open('null', 'w')
    myprint("version: 2")
    check_date(expiry_date_str)
    setting = read_info_from_json('D:/buy.json')
    product_name = setting['product_info']['product_name']
    Color = setting['product_info']['Color']
    size = setting['product_info']['size']
    count = setting['product_info']['count']

    #個人資訊
    info_username = setting['personal_info']['info_username']
    info_email = setting['personal_info']['info_email']
    info_phone = setting['personal_info']['info_phone']
    info_LineId = setting['personal_info']['info_LineId']
    info_msg = setting['personal_info']['info_msg']
    #信用卡
    info_card_number = setting['card_info']['card_number']
    info_card_name = setting['card_info']['card_name']
    info_card_date = setting['card_info']['card_date']
    info_card_cvc = setting['card_info']['card_cvc']
    #門市
    params = {
    "storeid": setting['store_info']['id'],
    "storename": setting['store_info']['name'],
    "storeaddress": setting['store_info']['address'],
    "outside": "0",
    "ship": "1111111",
    "TempVar": "",
    "isSameTab": "true"
    } 

    # 設定ChromeDriver選項
    uc_options = uc.ChromeOptions()
    uc_options.add_argument('--mute-audio') 
    myprint("6")
    # 啟動WebDriver
    driver = uc.Chrome(options=uc_options,driver_executable_path="D:/bbc.exe")

    # 加載目標URL
    driver.delete_all_cookies()

    #driver.get("https://www.goopi.co/users/sign_in") 
    #print("請先登入帳號 在案任意鍵繼續")
    #os.system("pause")

    driver.get("https://www.goopi.co") 
    # 查找所有包含產品的元素
    #productList__product product-list__product
   
    myprint("start")
    #尋找所有連結  
    while 1:
        firstProduct  = driver.find_elements(By.CLASS_NAME,'product-list__product')  
        for product in firstProduct:
            #try:
            #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "./following-sibling::div[contains(@class, 'product-list__product')]")))
            #except TimeoutException:
            #    break
            #next_element = current_element.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'product-list__product')]")
            #current_element = product
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'quick-cart-item')))
            except TimeoutException:
                myprint("定位不到產品資訊")
            product_link_element = product.find_element(By.CLASS_NAME, 'quick-cart-item')
            product_link = product_link_element.get_attribute('href')
            product_link = urllib.parse.unquote(product_link)#轉換原始字符而不是百分比
            if product_link == '':
                continue
            ga_product = product_link_element.get_attribute('ga-product')
            if ga_product == '':
                continue

            if 'products' in product_link: #確保抓取的網址是產品 
                title = json.loads(ga_product)['title']
                if title.lower().find(product_name.lower()) > -1:#wariunnnnnnnnnnnn title.lower().find(product_name.lower()  混色TEST
                    myprint("購物中...")
                    #兩種版本 一種顏色在名稱 一種顏色在選單
                    if title.find('Colors') > -1: 
                        #driver.get(linkurl)  
                        #快速購買
                        product_a_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'a[href="{product_link}"]')))
                        quick_cart_button = product_a_element.find_element(By.CSS_SELECTOR, '.js-btn-add-to-cart')
                        quick_cart_button.click()

                        #選顏色
                        product_a_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,f"[data-original-title='{Color}']")))
                        driver.find_element(By.CSS_SELECTOR,f"[data-original-title='{Color}']").click()
                    else: 
                        new_linkurl = product_link
                        # 找到最後一個'-'的位置
                        if Color != '':
                            last_hyphen_index = product_link.rfind('-')
                            if last_hyphen_index != -1:
                                new_linkurl = product_link[:last_hyphen_index]
                            new_linkurl = new_linkurl + '-' + replace_symbols_with_space(Color).replace(',','').replace(' ','-').lower() #Color.replace(' ','-').lower()
                            print(new_linkurl) 
                        #快速購買 
                        product_a_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'a[href="{product_link}"]')))
                        quick_cart_button = product_a_element.find_element(By.CSS_SELECTOR, '.js-btn-add-to-cart')
                        quick_cart_button.click()
                        #driver.get(new_linkurl)  

                    #選尺寸
                    if size != '':
                        try:
                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'js-selectpicker')))
                            select = Select(driver.find_element(By.CLASS_NAME,'js-selectpicker'))
                            select.select_by_value(f'string:{size}')
                        except TimeoutException:
                            print('failed find size')

                    #選數量
                    try:
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control.form-control-xs.form-control-inline")))
                        count_html = driver.find_element(By.CSS_SELECTOR,"input.form-control.form-control-xs.form-control-inline")
                        count_html.clear()
                        count_html.send_keys(f'{count}')
                    except TimeoutException:
                            print('failed find count')

                    #加入購物車
                    try:
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"js-btn-quick-cart-add-to-cart")))
                        #buy = driver.find_element(By.ID,"btn-main-checkout").click() #網址版本加入購物車
                        buy = driver.find_element(By.CLASS_NAME,"js-btn-quick-cart-add-to-cart").click()#快速購物確認
                    except TimeoutException:
                            print('failed find js-btn-quick-cart-add-to-cart')

                    time.sleep(0.4)
                    #等待跳出購物車清單
                    while 1:
                        try:
                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'js-selectpicker')))
                            #driver.refresh()
                            break
                        except TimeoutException:
                            driver.refresh()

                    #結帳 
                    time.sleep(0.4)
                    # 7-11 info callback
                    buy_url = "https://www.goopi.co/callback?storeid={storeid}&storename={storename}&storeaddress={storeaddress}&outside={outside}&ship={ship}&TempVar={TempVar}&isSameTab={isSameTab}&"
                    buy_url = buy_url.format(**params)
                    driver.get(buy_url)
                    #確認門市有選到
                    while 1:
                        if driver.find_element(By.CSS_SELECTOR, '.btn.btn-color-primary.btn-block.btn-pick-store').text != '更改':
                            myprint("門市選擇失敗,重新選擇中...")
                            driver.get(buy_url)
                        else:
                            myprint("門市選擇成功")
                            break
                    
                    driver.find_element(By.ID,"order-customer-phone").clear()#清除手機
                    driver.find_element(By.ID,"order-customer-phone").send_keys(info_phone)#填寫手機
                    driver.find_element(By.NAME,"order[order_remarks]").send_keys(info_msg)#填入給客服的訊息
                    #填寫非會員資料
                    if 1 == 0:
                        driver.find_element(By.ID,"order-customer-name").send_keys(info_username)#名稱
                        driver.find_element(By.ID,"order-customer-email").send_keys(info_email)#信箱

                        driver.find_element(By.ID,"user-field-598198f2d4e395db79000a21").send_keys(info_LineId)#LineId
                        

                        #填入信用卡
                        select_cvc_card(driver)

                    #勾選同步個人資料
                    script = '''
                    var checkbox = document.querySelector('label.control-label input[type="checkbox"][name="order[delivery_data][recipient_is_customer]"]');
                    if (checkbox) { checkbox.click(); }
                    '''
                    driver.execute_script(script)

                    #勾選同意網站服務條款及隱私權政策
                    script = '''
                    var checkbox = document.querySelector('label.control-label input[type="checkbox"][data-e2e-id="checkout-policy_checkbox"]');
                    if (checkbox) { checkbox.click(); }
                    '''
                    driver.execute_script(script) 

                    #time.sleep(1.4)#防止偵測機器人
                    driver.find_element(By.CSS_SELECTOR,f"[data-e2e-id='place-order_button']").click_safe()#driver.find_element(By.CLASS_NAME,"g-recaptcha").click_safe()
                    myprint("end")
                    WebDriverWait(driver, 60*30).until(EC.url_contains("unknown"))  
                    exit(-1)     
                    driver = 0 
                    break      
        print("商品未上架 重新搜尋中....")
        driver.refresh()
        time.sleep(1)
    return 