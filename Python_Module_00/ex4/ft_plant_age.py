def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    if days < 61:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
