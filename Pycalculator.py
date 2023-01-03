'''Pycalculator'''
# Coded by Tanvir
num1 = float(input("Number: "))
oparetor = input('''oparetor:
1.+ 
2.- 
3.* 
4./
5.^
Choose: ''')
num2 = float(input("Number: "))
if oparetor == "1":
    print(num1,"+",num2,"=",num1+num2)
elif oparetor == "2":
    print(num1,"-",num2,"=",num1-num2)
elif oparetor == "3":
    print(num1,"*",num2,"=",num1*num2)
elif oparetor == "4":
    print(num1,"/",num2,"=",num1/num2)
elif oparetor == "5":
    print(num1,"^",num2,"=",num1**num2)
else:
    print("ERROR!!!")
print("Credit goes to Tanvir")
print("VISIT  https://github.com/tanvirrahmanfahim?tab=repositories")
