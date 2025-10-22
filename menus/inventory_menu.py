from classes import SHOP_ITEMS
from utils.display_utils import clear_screen

def inventory_menu(my_dog, game_manager):
    while True:
        clear_screen()
        print("🎒 INVENTORY")
        print("=" * 50)
        
        if not my_dog.inventory:
            print("Your inventory is empty!")
            print("Visit the shop to buy some items!")
        else:
            for i, item_id in enumerate(my_dog.inventory, 1):
                item = SHOP_ITEMS[item_id]
                equipped = "⚡" if item_id in my_dog.equipped else " "
                print(f"{i}. {item.name} {equipped}")
                print(f"   Effect: {item.description}")
                if item_id in my_dog.equipped:
                    print(f"   Status: EQUIPPED")
                print()
        
        print(f"{len(my_dog.inventory) + 1}. Back to main menu")
        print("=" * 50)
        
        if my_dog.inventory:
            choice = input("Choose item to equip/unequip: ")
            
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(my_dog.inventory):
                    item_id = my_dog.inventory[choice_num - 1]
                    item = SHOP_ITEMS[item_id]
                    
                    if item_id in my_dog.equipped:
                        my_dog.unequip_item(item_id)
                        print(f"📦 Unequipped {item.name}")
                    else:
                        my_dog.equip_item(item_id)
                        print(f"⚡ Equipped {item.name}")
                    input("\nPress Enter to continue...")
                elif choice_num == len(my_dog.inventory) + 1:
                    return
            else:
                print("❌ Invalid choice!")
                input("\nPress Enter to continue...")
        else:
            input("Press Enter to go back...")
            return