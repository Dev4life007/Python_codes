                                    #Product catalogue using dictionary.
Products ={
    "Phones and Tablets":{
        "Mobiles Phones": ["Smartphones", "Cellphones"],
        "Tablets": ["Ipad Tablets", "Other Tablets", "Tablets Accessories"],
        "Accessories": ["Batteries and battery pads", "Cases", "Chargers", "Power Adapters", "Memory cards", "Screen Protectors", "Tripods"]
    },
    "Computing" :{
            "Computers": ["Macbook", "Hp", "Life", "Acer", "Dell"],
            "Printers": ["Inkjet", "Laserjet", "Toner"],
            "Accessories": ["Batteries", "Scanners", "Projectors", "Keyboards", "Mouse", "Memory Cards"]
        },  
}
print(Products["Computing"]["Computers"][0])
print(Products.keys())
Buyer = input("What are you interested in?: ")
response = input("Great! What exactly do you want from this category?: ")
print(Products[Buyer][response])

# Products = dict(
#     Electronics = dict(
#         Television = ["Panasonic", "Sharp", "LG", "Samsumg", "Apple"],
#         Video = ["DvD Players", "Blu-ray Players", "Recorders"],
#         Home_Audio = ["Home theater systems", "speakers", "Compact Radios", "Stereos", "Sound Bars"],
#         Camera_and_Photo = ["Digital Cameras", "Lenses", "Projectors"]
#     ),
#     Home_Office = dict(
#         Appliances = dict(
#             Kitchen = dict(
#                 Cookers = ["Stoves", "Heaters", "Burners", "Microwaves", "Toasters"],
#                 Cleaning = ["Dishwashers", "Waste-bin", "Brushes", "Parkers"],
#             Bathroom = dict(
#                 Laundry = ["Washers", "Dryers", "Heaters"],
#                 Beddings = ["Bedsheets", "Pillow-cases", "Lighting"]
#             ),
#             ),
#         ),
#     ),
#     Gaming = dict(
#         Consoles = [("Modern", ["Playstation 4", "Nintendo Switch", "Xbox One"]),("Retro", ["Playstation", "Xbox 180", "Sega"])],
#         Hand_held = [("Vogue", ["Nintendo 3DS", "Ps Vita"]),("Classic", ["Gameboy", "Brick-builder"])]
#         ),
# )   
# print(Products["Home_Office"])


# Product = {}
# print(type(Product))
# Product["Grocery"] = {"Beverages": ["Energy Drink","Milk"], "Toiletries": ["Detergent", "Tissue paper"]}
# Product["Food_Cupboard"] = ["Snacks", "Tins", "Cans", "Cereals"]
# Product["Swimming"] = ["Googles", "Nose clips", "Swim caps"]
# Product["States_in_Nigeria"] = 36
# print(Product["Grocery"]["Beverages"])