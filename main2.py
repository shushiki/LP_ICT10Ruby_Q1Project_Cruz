from pyscript import display

    #Displaying Menu Items
    display(product_names[0], target="prod1")
    display(f"₱{menu['Sausage Rolls']:.2f}", target="price1")
    display(product_names[1], target="prod2")
    display(f"₱{menu['Bagel']:.2f}", target="price2")
    display(product_names[2], target="prod3")
    display(f"₱{menu['Chicken Sandwich']:.2f}", target="price3")
    display(beverage[0], target="prod4")
    display(f"₱{menu['Americano']:.2f}", target="price4")
    display(beverage[1], target="prod4")
    display(f"₱{menu['Iced tea']:.2f}", target="price5")