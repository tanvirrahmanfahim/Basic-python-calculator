                             '''Pycalculator'''
num = float(input("\033[0;35m Number: "))
oparetor = input('''\033[1;33m]
1.+
2.-
3.*
4./
5.^
6.!
Choose(1/2/3/4/5/6): ''')
if oparetor == "1":
    num2 = float(input("\033[0;35m Number: "))
    print("\033[1;34m Answer is:",num+num2)
elif oparetor == "2":
    num2 = float(input("\033[0;35m Number: "))
    print("\033[1;34m Answer is:",num-num2)
elif oparetor =="3":
    num2 = float(input("\033[0;35m Number: "))
    print("\033[1;34m Answer is:",num*num2)
elif oparetor == "4":
    num2 = float(input("\033[0;35m Number: "))
    print("\033[1;34m Answer is:",num/num2)
elif oparetor == "5":
    num2 = float(input("\033[0;35m Number: "))
    print("\033[1;34m Answer is:",num**num2)
elif oparetor == "6":
    fac=1
    while (num>0):
        fac=fac*num
        num=num-1
    print("\033[1;34m Ans is:",fac)
else:
    print("\033[0;31m ERROR!!!  \n")
