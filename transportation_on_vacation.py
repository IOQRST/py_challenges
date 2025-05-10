def rental_car_cost(d):
    return d * 40 if d < 3 else d * 40 - 20 if d < 7 else d * 40 - 50


print(rental_car_cost(1))
print(rental_car_cost(3))
print(rental_car_cost(4))
print(rental_car_cost(7))
print(rental_car_cost(8))
print(rental_car_cost(10))
