# total = 0   #Working with For Loops and while Loops.
# for i in range(1, 6):
#     total += i
# print(total)

# total2 = 0
# k = 1
# while k < 6: # what this block says is when we get to the while loop check if k is less than 5, since its true do the following.
#     total2 += k # add k total2 and add 1 to k. so basically it runs from 1 to 4 since its less than 5 and breaks.
#     k += 1  #this block of code basically means go over to the next object which is index 1 and run the procedure again.
# print(total2)

# given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7] # this doesnt work if we remove the negative numbers.
# total3 = 0
# i = 0
# while given_list[i] > 0:
#     total3 += given_list[i]
#     i += 1
# print(total3)
# given_list = [7, 5, 4, 4, 3, 1,] 
# total3 = 0
# i = 0
# while i < len(given_list) and given_list[i] > 0:  #this works if you remove the negatives
#     total3 += given_list[i]
#     i += 1
# print(total3)
# given_list2 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total4 = 0
# for element in given_list2:
#     total4 += element
# print(total4)         # this is to calculate for all the elements in the list using For loop.

# given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total5 = 0
# for element in given_list2:
#     if element <= 0:
#         break
#     total5 += element
# print(total5)          # this is to sum up only the positive numbers using For loop.

# total6 = 0
# i = 0
# while 10 > 0:
#     total6 += given_list3[i]
#     i += 1
#     if given_list3[i] <= 0:
#         break
# print(total6)  # this sums up the positive numbers using While loop.
# given_list4 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total7 = 0
# i = len(given_list4) -1     #using while loop to sum up the negative numbers.
# while given_list4[i] < 0:
#     total7 += given_list4[i]
#     i -= 1
# print(total7)

py_class_studs = ""
response = ""

while 10 > 1:
    response = input("Please enter a name: ")
    if response == "end":
        break
    py_class_studs += response if len(py_class_studs) == 0 else ", " + response  
print(py_class_studs)