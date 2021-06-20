n= input("Type a number ")
n= int(n)
if 2<=n<=5 and n%2==0:
    print("Not weird")
elif n%2!=0:
    print("Werid")
elif 6<=n<=20 and n%2==0:
    print("Weird")
elif 20<=n<=100 and n%2==0:
    print("Not weird")
else:
    print("Goodbye")


    