'''Pycalculator'''
# Coded by Tanvir
num1 = float(input("Number: "))
oparetor = input('''
1.Addition(+)
2.Substraction(-)
3.Multipication(*)
4.Division(/)
5.Power(^)
6.Factorial(!)
Choose a oparetor(1/2/3/4/5/6): ''')
if oparetor == "1":
    num2 = float(input("Number: "))
    print(num1,"+",num2,"=",num1+num2)
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")
elif oparetor == "2":
    num2 = float(input("Number: "))
    print(num1,"-",num2,"=",num1-num2)
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")

elif oparetor == "3":
    num2 = float(input("Number: "))
    print(num1,"*",num2,"=",num1*num2)
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")
elif oparetor == "4":
    num2 = float(input("Number: "))
    print(num1,"/",num2,"=",num1/num2)
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")
elif oparetor == "5":
    num2 = float(input("Number: "))
    print(num1,"^",num2,"=",num1**num2)
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")
elif oparetor == "6":
    fac=1
    while (num1>0):
        fac=fac*num1
        num1=num1-1
    print("Factorial is",fac)
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")
else:
    print("ERROR!!!")
    print("Credit goes to Tanvir")
    print("VISIT https://github.com/tanvirrahmanfahim ")
