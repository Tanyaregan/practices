def hotel_cost(nights):
    """Calculates the cost of hotel stay."""
    rate = 140
    hotel_total = rate * nights
    return hotel_total


def plane_ride_cost(city):
    """Calculates cost of plane fare."""
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    """Calculates the cost of rental car."""
    daily_rate = 40
    if days >= 7:
        return days * daily_rate - 50
    elif days >= 3:
        return days * daily_rate - 20
    else:
        return days * daily_rate


def trip_cost(days, city):
    """Calculates total trip cost."""
    total = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)
    return total

days = raw_input('How many days? ')
city = raw_input('Which city? (Los Angeles, Pittsburgh, Tampa or Charlotte): ')

print 'Your trip will cost', trip_cost(days, city)
