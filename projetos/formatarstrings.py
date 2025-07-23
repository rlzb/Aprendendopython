# here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound)
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99),
]

# Calculate the total price for each item (weight times price per pound)
# And add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)
    
# Now calculate the sales tax and total bill.
tax_rate = 0.06626 # 2.625% sales tax in new jersey
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
#
# Print the receipt for the customer.
#
print("Subtotal: ${:5.2f}".format( subtotal))
print("Sales ${:5.2f}".format(tax_amount))
print("Total: ${:5.2f}".format(total))
a = [('hello')]
b = 'world'
converter = str(a + b)
print(converter)
print("emoji")
if a < b:
    print("maior")