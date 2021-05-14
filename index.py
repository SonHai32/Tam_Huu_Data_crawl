from selenium import webdriver
import time
import json

# driver = webdriver.Chrome()

# driver.get('https://www.pharmacity.vn/danh-muc-san-pham/cham-soc-sac-dep/')
# # time.sleep(2)
# # driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/a[1]').click()
# # time.sleep(1)

# item_containers = driver.find_elements_by_class_name('product-small')
list_item = []

with open('data.json', 'r') as file:
    list_item = list(json.load(file))

# for item in item_containers:
#     product_name = item.find_element_by_class_name('product-title').text
#     product_img = item.find_element_by_tag_name('img').get_attribute('src')
#     product_price = item.find_element_by_class_name('woocommerce-Price-amount').text
#     product_unit = item.find_element_by_class_name('uom').text

#     list_item.append(
#         {
#             'product_name': product_name,
#             'product_img': product_img,
#             'product_price': product_price,
#             'product_unit': product_unit,
#             'cate': {
#                 'cate_id': 'cham-soc-sac-dep',
#                 'cate_name': 'Chăm sóc sắc đẹp'
#             }
#         }
#     )

# with open('data.json', 'w') as file:
#     json.dump(list_item, file)

data_decode = json.dumps(list_item, ensure_ascii=False).encode('utf-8')
with open('data_new.json', 'w') as file:
    file.write(data_decode.decode())
# driver.close()