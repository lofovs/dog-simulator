import os
import time
from colorama import Fore, init
from classes import Dog, GameManager, versionChecker
from actions.puppy_management import puppy_manager
from actions.goodDog_management import goodDog_manager
from actions.seniorDog_management import seniorDog_manager
from actions.grandMaster_management import grandMaster_manager


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')







def menu_management(my_dog, game_manager, version_checker):
    version_checker.prompt_for_update()
    input("\nPress enter to continue..")
    while True:
        clear_screen()
        game_manager.check_passive_drain(my_dog)
        status = "🔴" if version_checker.check_new_update() else "✅"
        print(f"Dog Simulator {version_checker.current_version} {status}")

        if my_dog.rank == "Puppy":
            with open('ascii/puppy.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                colored_content = Fore.GREEN + content + Fore.WHITE
                print(colored_content)
                time.sleep(1)
                clear_screen()

        if my_dog.rank == "Good Dog":
            with open('ascii/good_dog.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                colored_content = Fore.BLUE + content + Fore.WHITE
                print(colored_content)
                time.sleep(1)
                clear_screen()
        if my_dog.rank == "Senior Dog":
            with open('ascii/senior_dog.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                colored_content = Fore.ORANGE + content + Fore.WHITE
                print(colored_content)

        if my_dog.rank == "Grand Master":
            with open('ascii/grand_master.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                colored_content = Fore.RED + content + Fore.WHITE
                print(colored_content)
        with open('ascii/senior_dog.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                colored_content = Fore.RED + content + Fore.WHITE
                print(colored_content)
        print(f"{my_dog.name} | Energy: {my_dog.energy} | Hungry: {my_dog.is_hungry} | Rank: {Fore.GREEN}{my_dog.rank}{Fore.WHITE} | XP: {my_dog.xp} | $: {my_dog.money}") 
        print("________________________________")
        print("|                              |")
        print("|  1. Dog Info                 |")
        print("|  2. Shop                     |")
        print("|  3. Inventory                |")
        print("|  4. Actions                  |")
        print("|                              |")
        print("|                              |")
        print("|                              |")
        print("|                              |")
        print("|  9. Check For Updates        |")
        print("|  10. Save And Quit           |")
        print("|                              |")
        print(" -----------------------------")
        
        
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
            print(f"Rank: {my_dog.rank}")
            print(f"XP: {my_dog.xp}")
            print(f"Balance: {my_dog.money}")
            input("\nPress enter to continue")

        elif choice == "2":
            clear_screen()
            #shop_menu()
            input("\nPress enter to continue")
        
        elif choice == "3":
            clear_screen()
            #inventory()
            input("\nPress enter to continue")

        elif choice == "4":
            if my_dog.rank == "Puppy":
                puppy_manager(my_dog, game_manager, version_checker)
            if my_dog.rank == "Good Dog":
                goodDog_manager(my_dog, game_manager, version_checker)
            if my_dog.rank == "Senior Dog":
                seniorDog_manager(my_dog, game_manager, version_checker)
            if my_dog.rank == "grandMaster":
                grandMaster_manager(my_dog, game_manager, version_checker)

        
        elif choice == "9":
            version_checker = versionChecker()
            version_checker.prompt_for_update()
            input("\nPress enter to continue")
        
        elif choice == "10":
            my_dog.save_to_file()
            print("Goodbye.")
            time.sleep(3)
            break
        else:
            print("\nInvalid choice, try again.")




