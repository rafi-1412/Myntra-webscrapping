
#Scrapping Myntra website data


import description as ds
import  webscrap_myntra as wm

names=wm.product_list
prices=wm.product_price
links=wm.product_links
specs=ds.product_desc
print(specs)
with open('products_details.txt', 'w') as f:
    f.write("PRODUCT DETAILS:\n\n")
    for name in names:
        f.write(name)
        f.write("\n")
    f.write("\nPRODUCT PRICES :\n\n")
    for price in prices:
        f.write(price)
        f.write("\n")
    f.write("\nPRODUCT LINKS:\n\n")
    for link in links:
        f.write(link)
        f.write("\n")
    f.write("\nPRODUCT SPECIFICATIONS\n\n")
    f.write(specs)


