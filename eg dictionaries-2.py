Fruits_dictionary = {"Apple": 345,"Banana": 870,"Mango":432,"Jack": 290}
choice = None
while choice != "0":
    print("0 - Exit")
    print("1 - Search for Fruit")
    print("2 - Add a New Fruit to Dictionary")
    print("3 - Update a Fruits")
    print("4 - Delete a Fruit from Dictionary")
    choice = input("Enter your choice:")
    if choice == "0":
            print("\nExiting....")
    elif choice == "1":
        fruit = input("\nEnter Fruit to find out its Stock:")
        if fruit in Fruits_dictionary:
                print(fruit,"Found in the Dictionary")
                fruit_stock = Fruits_dictionary[fruit]
                print(fruit_stock)
                print(Fruits_dictionary)
        else:
                print("not found!")
    elif choice == "2":
        fruit = input("\nEnter Fruit to include in dictionary:")
        if fruit not in Fruits_dictionary:
            fruit_stock = input("Enter its Stock:")
            Fruits_dictionary[fruit] = fruit_stock
            print(fruit,"successfully added to the dictionary.")
            print(Fruits_dictionary)
        else:
            print("already exists!")
    elif choice == "3":
        fruit = input("\nEnter Fruit to update:")
        if fruit in Fruits_dictionary:
            fruit_stock = input("Enter its Stock:")
            Fruits_dictionary[fruit] = fruit_stock
            print(fruit,"has been updated successfully.")
            print(Fruits_dictionary)
        else:
            print("not found!")
    elif choice == "4":
        fruit = input("\nEnter Fruit to delete it form dictionary:")
        if fruit in Fruits_dictionary:
            del Fruits_dictionary[fruit]
            print(fruit,"deleted from dictionary successfully.")
            print(Fruits_dictionary)
        else:
            print("not found!")
    else:
        print("\nChoice is not valid!")
