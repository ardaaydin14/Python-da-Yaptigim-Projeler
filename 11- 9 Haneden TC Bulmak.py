a = str(input("T.C. kimlik numaranızın ilk 9 hanesini giriniz:"))

count = 0 
double = 0 
single = 0 

for i in a:
    count += 1
    i = int(i)
    if count%2 == 0:
        double = double + i
    else:
        single = single + i
a = int(a)*100
number_11 = (single*8)%10
number_10 = (((single * 7) - (double))%10)*10
print("T.C. Kimlik No:",a+(number_10)+number_11)