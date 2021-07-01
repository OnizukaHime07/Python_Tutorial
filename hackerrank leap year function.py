def leap_year(x):
    leap= False
    leap1= True
    if((x%400 == 0) or (x%4 == 0) and (x%100 != 0)):
        return leap1
    else:
         return leap


leap_year(1900)
