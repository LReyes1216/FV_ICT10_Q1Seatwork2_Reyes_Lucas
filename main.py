from pyscript import display

#Strings

store_name ="Pastee Inc: Designer Edition" 
product_names = "Products" 
category1 = "Bags & Wallets"
category2 = "Clothes"
category3 = "Shoes"
price = "Prices with Tax (₱)" 
product1 = "Pasté Handbag"
product2 = "Pasté Wallet"
product3 = "Pasté Duffle Bag"
product4 = "Pasté Sling Bag"
product5 = "Pasté Doctor Bag"
product6 = "Pasté Backpack"
product7 = "Pasté Polo 1"
product8 = "Pasté Straight Pants 1"
product9 = "Pasté Jackt 1"
bestseller = "Bestseller | Pasté 1 Series"

#Integers

year_founded = 2025

#Prices without Tax

price1 = 57300
price2 = 5160
price3 = 84200
price4 = 35100
price5 = 68200
price6 = 119000
price7 = 2700
price8 = 3200
price9 = 6500
bestsellerPrice = 29981

#Final Prices with Tax

finalprice1 = round(price1 + (price1 * 0.08))
finalprice2 = round(price2 + (price2 * 0.08))
finalprice3 = round(price3 + (price3 * 0.08))
finalprice4 = round(price4 + (price4 * 0.08))
finalprice5 = round(price5 + (price5 * 0.08))
finalprice6 = round(price6 + (price6 * 0.08))
finalprice7 = round(price7 + (price7 * 0.08))
finalprice8 = round(price8 + (price8 * 0.08))
finalprice9 = round(price9 + (price9 * 0.08))
finalbestsellerPrice = round(bestsellerPrice + (bestsellerPrice * 0.08))



#Tuple

business_hours = ("Monday to Friday: 5:00 AM - 9:16 PM", "Saturday to Sunday: 5:00 AM - 8:23 PM")
owner = ("Lucas Reyes", "Co Founders: Shia Cruz, Jairo Agudo, Adrian Gavina, Giovanni Escarda, and Joel Janayan")

#Boolean
has_delivery = False

#Floating Point
tax_rate = 0.08


# Displaying the values in the HTML elements

# String1 Values
display(store_name, target = "storeName")
display(year_founded, target = "yearFounded")
display(product_names, target = "productNames")
display(category1, target = "Category")
display(category2, target = "Category2")
display(category3, target = "Category3")

# Integer/Float Values
display(price, target = "price")
display(finalprice1, target = "price1")
display(finalprice2, target = "price2")
display(finalprice3, target = "price3")
display(finalprice4, target = "price4")
display(finalprice5, target = "price5")
display(finalprice6, target = "price6")
display(finalprice7, target = "price7")
display(finalprice8, target = "price8")
display(finalprice9, target = "price9")
display(finalbestsellerPrice, target = "bestsellerPrice")

# String2 Values
display(product1, target = "pr1")
display(product2, target = "pr2")
display(product3, target = "pr3")
display(product4, target = "pr4")
display(product5, target = "pr5")
display(product6, target = "pr6")
display(product7, target = "pr7")
display(product8, target = "pr8")
display(product9, target = "pr9")
display(bestseller, target = "bestseller")

# Tuple Values
display (business_hours[0], target = "hours")
display (business_hours[1], target = "hours")
display(owner[0], target = "ownerName")
display(owner[1], target = "ownerName")

# Boolean Value with Conditional Statement
if has_delivery == False:
    delivery_status = "Disclaimer: We do not offer delivery services."
display(delivery_status, target="delivery_status")