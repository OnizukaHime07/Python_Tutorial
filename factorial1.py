y = int(input("enter a number: "))
 
factorial = 1
 
for x in range(1, y + 1):

   factorial = factorial * x
 
print("factorial of ", y, " is ", factorial)