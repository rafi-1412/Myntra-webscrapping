import webscrap_myntra as wm
from selenium import webdriver
links=wm.product_links
driver = webdriver.Chrome('chromedriver')

product_desc=""
count=1
for link in links:
    driver.get(link)
    element = driver.find_element_by_class_name("index-tableContainer")
    product_desc+="\nItem {}:\n".format(count)
    product_desc+=element.text
    product_desc+="\n---------------------\n"
    count+=1
