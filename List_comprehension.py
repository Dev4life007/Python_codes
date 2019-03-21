a = [1, 3, 5, 7, 9, 11] # lets achieve this = [2, 6, 10, 14, 18, 22] using append and list comprehension methods.
b = []                  # lets understand the .append() function very well 
b.append(10)
b.append(20)
b.append(30)
print(b)               #great! b was an empty list till we appended [10, 20, 30] to it. 

                        
c = []                # now lets solve the original task using the append function.
for x in a:
    c.append(x * 2)   #we've achieved that using the append function.
print(c)              #let's try to achieve it using the list comprehension method.
                        
d = [x * 2 for x in a]  #we've also achieved it using the list comprehension method but with slightly simpler syntax.
print(d)              #now lets create another list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] using the above methods.

e1 = []
for x in range(1,11):
    e1.append(x ** 2)
print(e1)
e2 = [x ** 2 for x in range(1,11)]
print(e2)             #Now lets do a reverse of the above numbers

f1 = []
for x in range(10, 0, -1): #we created a new range that starts from 10 down to 0 but not including 0 and goes down to -1.
    f1.append(x**2)
print(f1)
f2 = [x ** 2 for x in range(10, 0, -1)]
print(f2)


pt = print
numbers = []

for number in range(15):
    numbers.append(number)
    pt(numbers, "\n")

# cart = ["Apple", "Goat", "Milk", "Polony", "Cheese", "Rat", "Palindrome", "Cow"]

# cart = (cart[::2]) + [23, 45, 23, 53]


# print(cart)
