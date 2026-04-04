def ft_count_harvest_recursive(i=1, days=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if i in range(1, days + 1):
        print(f"Day {i}")
        ft_count_harvest_recursive(i + 1, days)
    else:
        print("Harvest time!")
