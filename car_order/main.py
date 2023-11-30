from car import Car, ElectricCar, Battery
flag = True
if __name__ == "__main__":
    while True:
        car_name = input("Enter cars'name: ")
        if car_name == "exit":
            break
        car_model = input("Enter cars'model: ")
        if car_model == "exit":
            break
        car_year = int(input("Enter cars'year: "))
        if car_year == -1:
            break

        type_car = input("Is the car electric or gas? ")
        while type_car != "electric" and type_car != "gas" and type_car != "exit":
            type_car = input("Invalid answer! Again is the car electric or gas? ")
        if type_car == "electric":
            car_ins = ElectricCar(car_name, car_model, car_year)
            car_props = car_ins.descriptive_car()
            print(f"Properties: {car_props}")
            car_ins.fill_gas_tank()
            car_ins.read_odometer()
            if car_ins.name == "BMW":
                print(f"The size of your battery'{car_ins.name.upper()} is {car_ins.battery_size}-kWh.")
            else:
                print(f"The size of your battery'{car_ins.name.title()} is {car_ins.battery_size}-kWh.")
            ans = input(f"Do you want modify your battery size? ")
            while ans.lower() != "yes" and ans.lower() != "y" and ans.lower() != "no" and ans.lower() != "n":
                ans = input(f"Invalid answer! Again do you want modify your battery size? ")
            if ans.lower() == "yes" or ans.lower() == "y":
                while True:
                    try:
                        if car_ins.name == "BMW":
                            b_s = int(input(f"Enter your favorite battery size for your {car_ins.name.upper()}: "))
                        else:
                            b_s = int(input(f"Enter your favorite battery size for your {car_ins.name.title()}: "))
                        while b_s != 40 and b_s != 65:
                            if flag:
                                print("Invalid battery size!")
                            try:
                                flag = True
                                if car_ins.name == "BMW":
                                    b_s = int(input(f"Enter your favorite battery size for your {car_ins.name.upper()}: "))
                                else:
                                    b_s = int(input(f"Enter your favorite battery size for your {car_ins.name.title()}: "))
                            except ValueError:
                                print("Sorry, Value errors occurred!:( Please enter a real number")
                                flag = False
                        car_ins.battery.descriptive_battery(b_s)
                        break
                    except (ValueError, NameError):
                        print("Sorry, Value and Name errors occurred!:( Please enter a real number")
                        continue
                car_ins.battery.specify_range()
        elif type_car == "gas":
            car_ins = Car(car_name, car_model, car_year)
            car_props = car_ins.descriptive_car()
            print(f"Properties: {car_props}")
            car_ins.fill_gas_tank()
            car_ins.read_odometer()
        else:
            break

        while True:
            try:
                mileage = int(input("Enter mileage: "))
                if mileage == -1:
                    break
                car_ins.update_odometer(mileage)
                car_ins.read_odometer()
                break
            except (ValueError, NameError):
                print("Sorry, Value and Name errors occurred!:( Please enter a real number")
                continue
        car_ins.read_odometer()
        while True:
            ans = input("Do you want increment mileage? ")
            if ans.lower() == "yes" or ans.lower() == "y":
                try:
                    inc = int(input("Enter increment value: "))
                    car_ins.increment_odometer(inc)
                    car_ins.read_odometer()
                    break
                except (ValueError, NameError):
                    print("Sorry, Value and Name errors occurred!:( Please enter a real number")
                    continue
            elif ans.lower() == "no" or ans.lower() == "n":
                break
            else:
                continue