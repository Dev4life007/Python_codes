# names = ["Charles", "Raymond", "Tracy", "Bill"]
# ages = [17, 45, 31, 30]

# def say_hello(Noms):
#     print("Hello", Noms, "how are you today?")

# # for elements in names:
# #     say_hello(elements)

# def say_hello_with_age(name, age):
#     computer_age = 18

#     if computer_age < ages:
#         print("You're all grown", name + "!")
#     else:
#         print("I'm proud of the adult you're turning out to be", name +"!")


# for names, ages in zip(names, ages): 
#     say_hello_with_age(names, ages)

# def sum(num1, num2, num3):
#     print(num1 * num2 * num3)
# sum (5, 10, 10)

# def list_summation(_list):
#     sum = 0
#     for elements in _list:
#         sum += elements
#     print("The sum of ", _list, "is", sum)

# list_summation([4,3,4,2,1,65,7,5,4,3,5,6,3,2])
# products = dict(
#     key= 600,
#     rice= 2000,
#     garri= 2000,
#     meat= 850,
#     poundo= 800,
#     pork= 700
#  )

# def dict_summation(_dict):
#     sum = 0
#     if isinstance(_dict, dict):        #ISINSTANCE / DNA OF THE ORIGINAL THING LIKA A PROTOTYPE

#         for key in _dict:
#             sum += _dict[key]

#         print("The sum of", _dict, "is", sum)
#     else:
#         print(type(_dict), "is not a dict")


# dict_summation(products


def name_len(Name1, Name2):

    if len(Name1) > len(Name2): 
        print(Name1,"is lengthier than", Name2 + ", yikes!")
    elif len(Name2) > len(Name1):
        print(Name2,"is lengthier than", Name1 + ", yikes!")
    else:
        print("They're both equal dummy!")

Name1 = input("Enter a name: ")
Name2 = input("Enter another name: ")

name_len(Name1, Name2)

#             #Program to check leap years.
# year = int(input("Please enter the year you want to check: "))
# def leap_year_checker(year):
#     if (year % 4 == 0):
#         print(str(year) + ", is a leap year chap!")
#     else:
#         print(str(year) + ", isn't a leap year darling.")

# leap_year_checker(year)

#             #Program to reverse numbers
# number = int(input("Please enter numbers: "))
# def rev_num(number):
#     rev = 0
#     while number > 0:                   
#         step = number % 10
#         rev = rev * 10 + step
#         number = number // 10 
#     print("Reverse of the number is:", rev)

# rev_num(number)


#             #Program to find numbers than can divide an integer

# _int = int(input("Please enter an integer: "))
# def divisors():
#     if _int > 1:
#         print("The divisors of the integer are: ")
#     else:
#         print("The divisor of the integer is: ")

#     for i in range(1, _int + 1):
#         if (_int % i == 0): 
#             print(i)

# divisors()

# def fractions():
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     c = float(input("Enter another number: "))
#     d = float(input("Enter another number: "))
#     ans_1 = (a / b)
#     ans_2 = (c / d)
#     add_ans = (ans_1 + ans_2)
#     print(add_ans)
# fractions()


# def fraction(num1,den1,num2,den2):
#     sol_num = (num1 * den1) + (num2 * den2)
#     sol_den = (den1 * den2)

#     for i in range(1, 10):
#         if sol_num % i == 0 and sol_den % i == 0:
#             sol_num = sol_num // i
#             sol_den = sol_den // i
#     print("Sum is: ", str(sol_num) + "/" + str(sol_den))

# num1 = int(input("Please enter num1: "))
# den1 = int(input("Please enter den1: "))
# num2 = int(input("Please enter num2: "))
# den2 = int(input("Please enter den2: "))

# fraction(num1,den1,num2,den2)