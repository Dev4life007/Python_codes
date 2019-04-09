# num = [13, 24, 65, 747, 22, 25]
# del num[2:5]
# print(max(num) - min(num))

# a, b =  132, 673
# print(a * b)


# _list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# x_bar_list = []
# def xbar(_list):
#         sum_ = sum(_list)
#         mean = (sum_) / len(_list)
#         for number in _list:
#                 dev = number - mean
#                 x_bar_list.append(dev)
#         return x_bar_list

# xbar(_list)
# print(xbar(_list))

# import matplotlib.pyplot as plt

# # plt.plot([1,2,3,4], [2,4,6,8], "bo")
# # plt.axis([0,5, 0,10])
# # plt.title("My world")
# # plt.show()

# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt
 
# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]
 
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
# plt.show()

file = open("death_causes.csv", "r")


index = 0
length_of_column = []
column_list = [] 
list_of_data = [] 

no_of_titles = 11

for each in file:
    list_of_data.append(each)    #appends the whole data into a list
    title_of_data = list_of_data[0].split(",")  #this returns the title of the data into a variable
    no_of_titles = len(title_of_data)  #no of title returned

def no_of_columns():   #this function returns the no of column under a title
    index = 0
    for each in file:
        column_item = each.split(",")[index]    
        column_list.append(column_item)     #this place the column items in a list
    length_of_column.append(len(column_list))  #this count the no of column after listing it
    

while index < no_of_titles:   
    index += 1         #this enable the code to loop through the next column
    no_of_columns()    #running the funtion again enable the next column to be counted
print(title_of_data)        
print(length_of_column)    

title_and_columns_dict = dict(zip(title_of_data,length_of_column))
print(title_and_columns_dict)