lst= []
chem= input("Enter Chemistry marks: ")
chem= int(chem)
lst.append(chem)
phy= input("Enter Physics marks: ")
phy= int(phy)
lst.append(phy)
eng= input("Enter English marks: ")
eng= int(eng)
lst.append(eng)
math= input("Enter Maths marks: ")
math= int(math)
lst.append(math)
print("Marks you entered", lst)
a= sum(lst)
per_cent= (a/400)*100
if per_cent>70: 
    print("You have passed with Grade A", per_cent,"%")
else: 
    print("You have passed with Grade B", per_cent,"%")
    
