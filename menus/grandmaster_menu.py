import json
import os
import time
from colorama import Fore, init
from classes import Dog, GameManager

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def grandMasterMenu(my_dog, game_manager):
    while True:
        if my_dog.rank != "Grand Master":
            return
        clear_screen()
        game_manager.check_passive_drain(my_dog)
        print(""" 
  / \\__
 (    @\\____
 /         O
/   (_____/
/_____/   U
""")
        print(f"{my_dog.name} | Energy: {my_dog.energy} | Hungry: {my_dog.is_hungry} | Rank: {Fore.RED}{my_dog.rank}{Fore.WHITE} | XP: {my_dog.xp} | $: {my_dog.money}") 
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
            clear_screen()
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
            success = my_dog.bark()
            if success:
                game_manager.check_rank_up(my_dog)
        elif choice == "3":
            clear_screen()
            with open('ascii/sleep.txt', 'r') as file:
                content = file.read()
                print(content)
            success = my_dog.sleep()
            if success:
                game_manager.check_rank_up(my_dog)
        elif choice == "4":
            clear_screen()
            with open('ascii/eat.txt', 'r') as file:
                content = file.read()
                print(content)
            success = my_dog.eat()
            if success:
                game_manager.check_rank_up(my_dog)
        elif choice == "5":
            clear_screen()
            with open('ascii/play.txt', 'r') as file:
                content = file.read()
                print(content)
            success = my_dog.play()
            if success:
                game_manager.check_rank_up(my_dog)
        elif choice == "6":
            success = my_dog.kick()
            if success:
                game_manager.check_rank_up(my_dog)
        elif choice == "7":
            success = my_dog.have_birthday()
            if success:
                game_manager.check_rank_up(my_dog)
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
        