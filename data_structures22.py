#LISTS

# shopping_cart = ["apple", "coca cola", "Soap", "chicken", "chicken"]

# print("Original", (shopping_cart))
# #indexing  list

# print(shopping_cart[0])
# print("Before append",len(shopping_cart))

# shopping_cart.append("pot")
# print("after append", len(shopping_cart))

# shopping_cart.remove(shopping_cart[0])
# print("after remove", len(shopping_cart))
# print("after remove", (shopping_cart))

# duplicate_cart = shopping_cart.copy()
# print("duplicate_cart", len(duplicate_cart))
# print("duplicate_cart", (duplicate_cart))

# shopping_cart.clear()
# print("after Clear", len(shopping_cart))
# print("after Clear", (shopping_cart))

# print("duplicate_cart", len(duplicate_cart))
# print("duplicate_cart", (duplicate_cart))

# print(duplicate_cart.count("chicken"))

# print(duplicate_cart.reverse())
# print(duplicate_cart)
# duplicate_cart.pop(3)
# duplicate_cart.sort()
# print(duplicate_cart)

# hertero_list = [1,"hello", print, list, int, str, bool]
# hertero_list[2](hertero_list)
# hertero_list[2]("i am a boy")

# femi_print = print

# femi_print("this is the new type of print")


# numbers = [number *10 for number in range(20)]

# print(numbers)
# pt = print
# numbers = []

# for number in range(100):
#     numbers.append(number)
#     pt(numbers, "\n")
# print(numbers)

# print(shopping_cart[-1])

# shopping_cart = ["apple", "coca cola", "Soap", "chicken", "pork", "ham", "polony"]

# print(shopping_cart[::2])

# shopping_cart[::] = [23,45,23,53]
# print(shopping_cart)

# shopping_cart = ["apple", "coca cola", "Soap", "chicken", "pork", "ham", "polony", ["screwdriver", "wrench", "plier"] ]

# print(shopping_cart[-1][2])

#TUPLES
# new_tuple  = ("apple", "coca cola", "Soap", "chicken", "pork", "ham", "polony")

# #new_tuple[0] = "orange"

# print(new_tuple[0])
# print(new_tuple[::-1])
# print(new_tuple)

# _dict = {"key": "value","key2": "value"}

# MLB_team = {
#      'Colorado' : 'Rockies',
#      'Boston'   : 'Red Sox',
#      'Minnesota': 'Twins',
#      'Milwaukee': 'Brewers',
#      'Seattle'  : 'Mariners'
#  }

# print(MLB_team['Colorado'])

# oxford = {
#     "noun": "Name of person animal place or thing",
#     "pronoun": "Used instead of a noun",
#     "verb": "Action word",
#     "adjective": "describes a noun"
# }

# print(oxford["pronoun"])

# _class = {
#     "chidi":["sleeping", "eating", "travelling"],
#     "tolu":["coding", "reading complex stuff", "writing advanced code"],
#     "femi":["speaking big grammar", "lightening class mood", "teaching complex math",  "analysing grammar"],
#     "omotayo":[ "drinking sweet stuff", "chowing biscuit", "pressing phone"],
#     "Mr tayo": ["Selling insurance", "Giving updates", "Encyclopedia"],
#     "shade" : ["accounting", "coming late", "shalaye'ing"],
#     "attah": ["being cool", "being calm", "being collected", "being awesome", "eating affang"]
# }

# print(_class["chidi"])

_class = {
    "chidi":{
        "surname": "Igbo",
        "hobbies":["sleeping", "eating", "travelling"],
        "phone": "0804465862"
        },
    "tolu":{
        "surname": "Igbo",
        "hobbies":["sleeping", "eating", "travelling"],
        "phone": "0804465862"
        },
    "femi":["speaking big grammar", "lightening class mood", "teaching complex math",  "analysing grammar"],
    "omotayo":[ "drinking sweet stuff", "chowing biscuit", "pressing phone"],
    "Mr tayo": ["Selling insurance", "Giving updates", "Encyclopedia"],
    "shade" : ["accounting", "coming late", "shalaye'ing"],
    "attah": ["being cool", "being calm", "being collected", "being awesome", "eating affang"]
}

#creating dictionaries VIA TUPLES

# # print(_class["chidi"])
# print((_class["chidi"]))
# print(type(_class["chidi"]))

for_conversion = [("happy", ["pleased", "excited"]),("angry", "vexed"),("run", "sare")]

synonyms = dict(for_conversion)

print(synonyms)
#CREATING DICT VIA VARIABLES
products = dict(
    key= 'value',
    rice='200',
    garri='2000',
    meat='300',
    poundo='900',
    pork='600'
 )

print(products)



# (x,y) tuple
# [x,y] list
# {x:value, y:value} dict