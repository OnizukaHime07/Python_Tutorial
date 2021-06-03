#You went to a mall to purchase some grocery you purchaseed 4 food items and went to billing counter for billing
#after billing you realized you need to add one more food item to the existing list 
#write a python program to calculate price of 4 food items before and one more food item in the last

lst= []
a= input("Enter the price: ")
a= int(a)
lst.append(a)
b= input("Enter your price: ")
b= int(b)
lst.append(b)
c= input("Enter the price: ")
c= int(c)
lst.append(c)
d= input("Enter the price: ")
d= int(d)
lst.append(d)
total= sum(lst)
print("Total price is",total)
e= input("Enter your price: ")
e= int(e)
lst.append(e)
total1= sum(lst)
print("Total price is",total1)
print(len(lst))
