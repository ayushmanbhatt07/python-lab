# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary.
n=int(input("enter the number of products:"))
dict={}
for i in range(0,n):
    name=input("enter the name of the product:" )
    price=int(input("enter the price of the product:" ))
    dict.update({name:price})
for key in dict:
    a=input("enter the name of the product to get its price:")
    print(f"the price of {a} is {dict[a]}")
else:
    print("product not found")

