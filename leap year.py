x= int(input("Give a year: "))
if ((x%400 == 0) or (x%4 == 0) and (x%100 != 0)):
    print("True")
else:
    print(" False")
    
    