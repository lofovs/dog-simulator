import json
import os
import time
from classes import Dog


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def startup_menu():
    dog_names = Dog.get_all_saved_dogs()
    if len(dog_names) == 0:
        print("No saved dog found, let's create a new one!")
        name = input("Name: ")
        breed = input("Breed: ")
        age = input("Age: ")
        my_dog = Dog(name, breed, age)
        return my_dog
        
    else:
        print("Choose a dog:")
        for i, name in enumerate(dog_names, 1):
            print(f"{i}. {name}")
        
        print(f"{len(dog_names) + 1}. Create New Dog")
        
        choice = input("Choose: ")
        
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(dog_names):
                selected_name = dog_names[choice_num - 1]
                return Dog.load_from_file(f"saves/{selected_name}_data.json")
                
            elif choice_num == len(dog_names) + 1:
                print("Creating a new dog...")
                while True: 
                    name = input("Name: ")
                    if name in dog_names:
                        print("A dog with that name already exists. Please choose a different name.")
                        continue
                    break
                breed = input("Breed: ")
                age = int(input("Age: "))
                return Dog(name, breed, age)
            
    print("Invalid choice!")
    return None


def menu(my_dog):
    if my_dog is None:
        return

    while True:
        clear_screen()
        print(""" 
  / \\__
 (    @\\____
 /         O
/   (_____/
/_____/   U
""")
        print(f"{my_dog.name} | Energy: {my_dog.energy} | Hungry: {my_dog.is_hungry}")
        print("<------------->")
        print("1. More info")
        print("2. Bark")
        print("3. Sleep")
        print("4. Eat")
        print("5. Play")
        print("6. Kick Dog")
        print("7. Have Birthday")
        print("8. Kill Dog")
        print("9. Save and quit")
        print("<------------->")
        choice = input("Choose an option: ")
        if choice == "1":
            with open('ascii/info.txt', 'r') as file:
                content = file.read()
                print(content)
            print(f"Name: {my_dog.name}")
            print(f"Breed: {my_dog.breed}")
            print(f"Age: {my_dog.age}")
            print(f"Energy: {my_dog.energy}")
            print(f"Hungry: {my_dog.is_hungry}")
        elif choice == "2":
            clear_screen()
            with open('ascii/bark.txt', 'r') as file:
                content = file.read()
                print(content)
            my_dog.bark()
        elif choice == "3":
            clear_screen()
            with open('ascii/sleep.txt', 'r') as file:
                content = file.read()
                print(content)
            my_dog.sleep()
        elif choice == "4":
            clear_screen()
            with open('ascii/eat.txt', 'r') as file:
                content = file.read()
                print(content)
            my_dog.eat()
        elif choice == "5":
            clear_screen()
            with open('ascii/play.txt', 'r') as file:
                content = file.read()
                print(content)
            my_dog.play()
        elif choice == "6":
            my_dog.kick()
        elif choice == "7":
            my_dog.have_birthday()
        elif choice == "8":
            confirm = input(f"Are you sure you want to kill {my_dog.name}? This action cannot be undone. (y/n): ")
            if confirm.lower() == 'yes' or confirm.lower() == 'y':
                my_dog.kill()
            elif confirm.lower() == "n" or confirm.lower() == "no":
                print(f"{my_dog.name} is safe for now.")
            else:
                print("Invalid command.")
        elif choice == "9":
            my_dog.save_to_file()
            print("Goodbye.")
            time.sleep(3)
            break
        else:
            print("Invalid choice, try again.")
        input("\nPress enter to continue...")



my_dog = startup_menu()
if my_dog:
    menu(my_dog)