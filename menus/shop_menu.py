from classes import SHOP_ITEMS
from utils.display_utils import clear_screen

def shop_menu(my_dog, game_manager):
    while True:
        clear_screen()
        print("🛍️  DOG SHOP")
        print(f"Money: ${my_dog.money}")
        print("=" * 50)
        
        
        items_list = list(SHOP_ITEMS.items())
        for i, (item_id, item) in enumerate(items_list, 1):
            owned = "✅" if item_id in my_dog.inventory else " "
            print(f"{i}. {item.name} - ${item.cost} {owned}")
            print(f"   {item.description}")
            print()
        
        print(f"{len(items_list) + 1}. Back to main menu")
        print("=" * 50)
        
        choice = input("Choose item to buy: ")
        
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(items_list):
                item_id, item = items_list[choice_num - 1]
                
                if item_id in my_dog.inventory:
                    print(f"❌ You already own {item.name}!")
                elif my_dog.money >= item.cost:
                    my_dog.money -= item.cost
                    my_dog.add_item(item_id)
                    print(f"🎉 Bought {item.name}!")
                    print(f"💰 Remaining money: ${my_dog.money}")
                else:
                    print("❌ Not enough money!")
                input("\nPress Enter to continue...")
                
            elif choice_num == len(items_list) + 1:
                return
        else:
            print("❌ Invalid choice!")
            input("\nPress Enter to continue...")