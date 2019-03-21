for x in "Banana":
    print(x)

_list = [1,2,3,"Banana",5]

count = 0 

for element in _list:
    print(element)
    count += 1
    if str(element).isalpha():
        for letter in (element):
            print(letter)

print("Total count is:", count)

Name = input("Please enter name: ")
count = 0

for characters in Name:
    count += 1
print("The count in your character is:", count)

password = 7664
for i in range(9999):
    print("testing", "--->", i == password)
    if password == i:
        print("Your password is:", i)
        break
a = ["Apple", "Game", "World"]
print(a[0])
print(a[1])
print(a[2])
for d in a:
    print(d)
b = [20, 30, 63, 636]
sum = 0
for chidi in b:
   sum = sum + chidi
print(sum)
1, 2, 3, 4
r = list(range(1, 100))
print(r)
sum2 = 0
for t in range(1,5):
    sum2 += t
    print(sum2)
print(list(range(1,8)))
sum3 = 0
for c in range(1,20): #we range numbers from 1 to 20 excluding 20.
    if c % 3 == 0: #here the modulus helps to find the multiples of 3.
      sum3 += c #here the += function helps to add up the  multiples to give us a 63 sum.
print(sum3)
                      # so basically what we did here was to find the multiples of 3/5 in range[1,100] and sum it up.
sum4 = 0 
for v in range(1,100):
    if v % 3 == 0:
        sum4 += v
    elif v % 5 == 0:
        sum4 += v
print(sum4)
                    # Another way of doing this is:
sum4 = 0 
for v in range(1,100):
    if v % 3 == 0 or v % 5 == 0:
        sum4 += v
print(sum4)
      
b = ["Banana", "Apple", "Microsoft"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

z = ["Banana", "Apple", "Microsoft"]
for element in z: #first method by default which is the simpler method. but the method below is much better in cases where you want to print multiple times.
    print(element)
for i in range(len(z)): #you can use either the indexes or the len function which is the case here.
    for u in range(i + 1): #here we used the + function to increment the resulting values, such that it increases throughout the len of the range. 
        print(z[i])
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
