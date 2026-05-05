from car_utils import create_car_from_input, display_cars
 
cars = {}
 
while True:
    print("Options: (1) Add Car, (2) View Cars, (3) Drive Car, (4) Paint Car, (5) Quit:")
    option = input()
 
    if option == '1':
        new_car = create_car_from_input()
        cars[new_car.car_id] = new_car
        print(new_car)
        print("Car added.")
 
    elif option == '2':
        display_cars(cars)
 
    elif option == '3':
        car_id = input("Enter car ID:\n")
        miles = float(input("Enter miles driven:\n"))
        cars[car_id].drive(miles)
        print("Mileage updated.")
        print(cars[car_id])
 
    elif option == '4':
        car_id = input("Enter car ID:\n")
        new_color = input("Enter new color:\n")
        cars[car_id].change_color(new_color)
        print("Color updated.")
        print(cars[car_id])
 
    elif option == '5':
        print("Goodbye!")
        break
 
    else:
        print("Invalid option selected!")