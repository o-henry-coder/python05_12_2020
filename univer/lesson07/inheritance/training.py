def get_minprice():
    vehicles = [("12°05'20'", 56576, 235, 1958), ("12°05'20'", 56576, 235, 1958, 2100, 59), ("14°08'70'", 7678, 80, 1995)]

    # for min_price in vehicles :
    #     min = min_price[1]
    #     if min_price[1] > min :
    #         min = min_price[1]
    # print(min)
    print(vehicles[0][1])

    min = vehicles[0][1]
    for min_price in vehicles :
        if min_price[1] < min :
            min = min_price[1]
    print(min)

get_minprice()

