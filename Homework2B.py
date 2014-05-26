item_price = input("What is the price of the item?: ")
tax_rate = input("What is the sales tax rate on the item?: ")

new_price = item_price + (item_price*tax_rate)
print "Your item including tax will be %.2f."%new_price
