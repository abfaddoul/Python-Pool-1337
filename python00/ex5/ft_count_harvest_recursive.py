def ft_count_harvest_recursive(day=-67, i=1):
    if day == -67:
        day = int(input("Days until harvest: "))
    if day != 0:
        print(f"Day {i}")
        day -= 1
        i += 1
        ft_count_harvest_recursive(day, i)
    else:
        print("Harvest time!")
