if __name__ == "__main__":
    my_list = [item for item in range(0, 100) if item % 2 == 0]
    print(my_list)

    cars = ["Volkswagen", "Audi", "Toyota", "Opel", "Alfa Romeo"]

    cars_with_A = [item for item in cars if item[0] == "A"]
    print(cars_with_A)