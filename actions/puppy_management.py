import time
import os
from colorama import Fore, init
from classes import Dog, GameManager, versionChecker
from utils.display_utils import clear_screen


def puppy_manager(my_dog, game_manager, version_checker):
    while True:
        if my_dog.rank != "Puppy":
            print(f"🎉 {my_dog.name} is now a {my_dog.rank}!")
            time.sleep(2)
            return
        
        game_manager.check_passive_drain(my_dog)
        
        clear_screen()
        
        status = "🔴" if version_checker.check_new_update() else "✅"
        print(f"Dog Simulator {version_checker.current_version} {status}")
        print(f"{my_dog.name} | Energy: {my_dog.energy} | Hungry: {my_dog.is_hungry} | Rank: {Fore.GREEN}{my_dog.rank}{Fore.WHITE} | XP: {my_dog.xp} | $: {my_dog.money}") 
        print("________________________________")
        print("|                              |")
        print("|  1. Bark                     |")
        print("|  2. Play                     |")
        print("|  3. Eat                      |")
        print("|  4. Sleep                    |")
        print("|  5. Kick                     |")
        print("|  6. Kill                     |")
        print("|  7. Happy Birthday           |")
        print("|                              |")
        print("|                              |")
        print("|  8. Go back to menu          |")
        print("|                              |")
        print("-------------------------------")
        actionchoice = input("Choose an option: ")
        
        if actionchoice == "1":
            clear_screen()
            with open('ascii/bark.txt', 'r') as file:
                content = file.read()
                print(content)
                success = my_dog.bark()
                if success:
                    game_manager.check_rank_up(my_dog)
            input("\nPress enter to continue")
                
        elif actionchoice == "2":
            clear_screen()
            with open('ascii/play.txt', 'r') as file:
                content = file.read()
                print(content)
            success = my_dog.play()
            if success:
                game_manager.check_rank_up(my_dog)
            input("\nPress enter to continue")
                
        elif actionchoice == "3":
            clear_screen()
            with open('ascii/eat.txt', 'r') as file:
                content = file.read()
                print(content)
            success = my_dog.eat()
            if success:
                game_manager.check_rank_up(my_dog)
            input("\nPress enter to continue")

        elif actionchoice == "4":
            clear_screen()
            with open('ascii/sleep.txt', 'r') as file:
                content = file.read()
                print(content)
            success = my_dog.sleep()
            if success:
                game_manager.check_rank_up(my_dog)
            input("\nPress enter to continue")
            
        elif actionchoice == "5":
            clear_screen()
            success = my_dog.kick()
            if success:
                game_manager.check_rank_up(my_dog)
            input("\nPress enter to continue")
            
        elif actionchoice == "6":
            clear_screen()
            confirm = input(f"Are you sure you want to kill {my_dog.name}? This action cannot be undone. (y/n): ")
            if confirm.lower() == 'yes' or confirm.lower() == 'y':
                my_dog.kill()
            elif confirm.lower() == "n" or confirm.lower() == "no":
                print(f"{my_dog.name} is safe for now.")
            else:
                print("Invalid command.")
            input("\nPress enter to continue")
        
        elif actionchoice == "7":
            clear_screen()
            success = my_dog.have_birthday()
            if success:
                game_manager.check_rank_up(my_dog)
            input("\nPress enter to continue")
                
        elif actionchoice == "8":
            return