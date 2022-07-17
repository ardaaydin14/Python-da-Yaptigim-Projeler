#addition
def addition(a,b):
    return a+b
#extraction
def extraction(a,b):
    return a-b
#multiple
def multiple(a,b):
    return a*b
#divide
def divide(a,b):
    return a/b
#choose
print("Select Action.")
print("=======================")
print("1.Addition")
print("2.Extraction")
print("3.Multiple")
print("4.Divide")

#Asking User for Selection
choose = input("Your Selection (1/2/3/4):")
 
number1 = int(input("1.number: "))
number2 = int(input("2.number: "))
 
if choose == '1':
   print(number1,"+",number2,"=", addition (number1,number2))
 
elif choose == '2':
   print(number1,"-",number2,"=", extraction(number1,number2))
 
elif choose == '3':
   print(number1,"*",number2,"=", multiple(number1,number2))
 
elif choose == '4':
   print(number1,"/",number2,"=", divide(number1,number2))
else:
   print("Invalid Entry")