from random import randint

FIRST_NAME_INDEX = 0

CATEGORIES_SUBCATEGORIES = {
    "Gadgets":
        ("Notebooks", "Phones", "Tablets", "PC", "Game Consoles"),
    "Vehicles":
        ("Cars", "Bikes", "Boats"),
    "Clothes-Shoes":
        ("Men", "Women", "Kids"),
    "Appliances":
        ("Laundry", "Fridges", "Cooking", "Climate", "Health-Beauty")
}

ADV_TEMPLATES = [
    {
        "title": "Brand new Nike Air 2022",
        "body": "New Nike Air Shoes - Bought in USA Nike Official Store",
        "is_active": True,
        "price": randint(100, 200)
    },
    {
        "title": "Used iPhone 11 Pro",
        "body": "My own iPhone 11 Pro - Good state, no scratches or any damages",
        "is_active": True,
        "price": randint(300, 400)
    },
]