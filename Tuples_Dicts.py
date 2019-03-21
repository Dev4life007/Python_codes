new_tuple = ("apple", "coca cola", "soap", "chicken", "pork", "ham", "polony")
print(new_tuple[0])
print(new_tuple[::-1])   #before you can use the reverse assign it to a variable.
print(new_tuple)         #still retains the original list.

                                    #dictionary
oxford = {
    "Noun": "Name of person animal place or thing",
    "Pronoun": "used instead of a noun",
    "Verb": "Action word",
    "Adjective": "describes the noun"
}

print(oxford["Pronoun"])
                                #using dictionary
Our_Class = {
    "Chidi":{           #Chidi - Key, elements under chidi are values. Dicts work with Keys and Values.
        "Surname": "Igbo",
        "Hobbies": ["sleeping", "Eating", "Gaming", "Travelling"],
        "Phone": "Infinix"
    },
    "Tolu":{
        "Surname": "Ogidan",
        "Hobbies": ["coding", "reading complex stuff", "writting advanced code"],
        "Phone": "Motorola"
    },
    "Femi":{
        "Surname": "Onabola",
        "Hobbies": ["speaking big grammar", "lightening class mood", "teaching complex math", "analysing grammar"],
        "Phone": "Sony"
    }, 
    "Omotayo":{
        "Surname": "Omotayo",
        "Hobbies": ["drinking sweet stuff", "chowing biscuit", "pressing phone"],
        "Phone": "LG"
    },
    "Mr Tayo":{
        "Surname": "Adeyinka",
        "Hobbies": ["selling insurance", "giving updates", "class encyclopedia"],
        "Phone": "Samsumg"
    }, 
    "Shade":{
        "Surname": "Agunbiade",
        "Hobbies": ["accounting", "late comer", "shalaye'ing"],
        "Phone": "Iphone"
    },
    "Mr Attah":{
        "Surname": "Gete",
        "Hobbies": ["being cool", "being calm", "being collected", "eating affang"],
        "Phone": "itel"
    },
}
print(Our_Class["Chidi"]["Hobbies"][0])
# here we appended Dancing to Tolu's Hobbies
# (Our_Class["Tolu"]["Hobbies"]).append("Dancing")

# print(Our_Class["Tolu"]["Hobbies"])
# #                   creating a dictionary
synonyms = dict([("happy", "elated"),("angry","annoyed"),("gigantic", "enormous"),("fast", "swift")])
print((synonyms["happy"]))

# #Another way to make a dictionary

# Products = dict(
#     Rice = "2500",
#     garri = "2000",
#     Meat = dict(
#         Pork = "730",
#         Beef = "350",
#         Hotdog = "900"
#     ),
#     Poundo = "500",
#     Amala = "400",
#     Burger = "1500",
# )
# print(Products["Burger"])
# # How to update a dictionary
# Products["Rice"] = "500"
# print(Products["Rice"])