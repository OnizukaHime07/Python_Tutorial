a= int(input("First number: "))
b= int(input("Second number: "))
c= int(input("Thrid number: "))
if a>b and a>c:
    print("First is largest among three")
elif b>a and b>c:
    print("Second number is largest") 
elif c>b and c>a:
    print("Third number is largest")      
else:
    print("Invalid")

