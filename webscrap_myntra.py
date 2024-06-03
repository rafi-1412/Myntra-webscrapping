from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.myntra.com/tsirts-under-10000")

product_list=[]
product_links=[]
product_price=[]
elements = driver.find_elements_by_class_name("product-base")
for element in elements:   #Filtering all brands
    product_list.append((element.find_element_by_class_name("product-brand").text))
    product_price.append((element.find_element_by_class_name("product-price").text))
    product_links.append(element.find_element_by_tag_name("a").get_attribute("href"))





