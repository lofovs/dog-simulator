import json
import os
import time
from colorama import Fore, init
from classes import Dog, GameManager
from menus.puppy_menu import puppymenu
# from menus.gooddog_menu import goodDogMenu
# from menus.seniordog_menu import seniorDogMenu
# from menus.grandmaster_menu import grandMasterMenu


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


def menu(my_dog, game_manager):
    if my_dog is None:
        return
    if my_dog.rank == "Puppy":
        puppymenu(my_dog, game_manager)
    if my_dog.rank == "Good Dog":
        puppymenu(my_dog, game_manager)
    if my_dog.rank == "Senior Dog":
        puppymenu(my_dog, game_manager)
    if my_dog.rank == "Grand Master":
        puppymenu(my_dog, game_manager) 

#skift dei til riktig menu




game_manager = GameManager()
my_dog = startup_menu()
if my_dog:
    menu(my_dog, game_manager)