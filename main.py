    from pyscript import display
    #Restaurant Ordering System using Python Data Types

    #String Data Types
    restaurant_name = "Cafe Delights"
    owner_name = "Athena"

    #Integer Data Types
    year_since = 2025

    #Float Data Types
    tax_rate = 0.08

    #Boolean Data Types
    has_delivery = True
    has_dine_in = True
    is_takeaway = False

    #List Data Types
    product_names = ["Spaghetti", "Garlic Bread", "Caesar Salad"]
    beverage =["Iced Tea", "Sparkling Water"]

    #Tuple Data Types
    business_hours = ("11:00 AM", "10:00 AM")

    #Dictionary Data Types
    menu = {
        "Spaghetti": 79.99,
        "Garlic Bread": 50.00,
        "Caesar Salad": 150.00,
        "Iced Tea": 30.00,
        "Sparkling Water": 20.00
    }

    #Set Data Types
    common_allergens = {"nuts", "dairy", "gluten"}

    #Displaying restaurant information
    display(restaurant_name, target="name1")
    display(f"Owner: {owner_name}", target="owner")
    display(f"Since: {year_since}", target="since")
    display(f"Menu Pricelist", target="heading1")

    #Displaying Menu Items
    display(product_names[0], target="prod1")
    display(f"₱{menu['Spaghetti']:.2f}", target="price1")
    display(product_names[1], target="prod2")
    display(f"₱{menu['Garlic Bread']:.2f}", target="price2")
    display(product_names[2], target="prod3")
    display(f"₱{menu['Caeser Salad']:.2f}", target="price3")
    display(beverage[0], target="prod4")
    display(f"₱{menu['Iced Tea']:.2f}", target="price4")
    display(beverage[1], target="prod4")
    display(f"₱{menu['Sparkling Water']:.2f}", target="price5")


    #Display additional information
    display(f"Open: {business_hours[0]} - {business_hours[1]}", target="Opening Hours")

    #Display Order type
    display(f"Dine-in Available", target="orderType")