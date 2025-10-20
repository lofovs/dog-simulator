import json
from colorama import Fore, init
import os
import time
import requests
import webbrowser

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 100
        self.is_hungry = False
        self.xp = 0
        self.rank = "Puppy"
        self.money = 0


    def have_birthday(self):
        age = int(self.age)
        age += 1
        self.age = age
        print(f"\n{self.name} is now {self.age} years old! Happy Birthday!")



    def kill(self):
        print(f"\n{self.name} has passed away... Goodbye, old friend.")
        if os.path.exists(f"saves/{self.name}_data.json"):
            Dog.delete_saved_file(f"saves/{self.name}_data.json")
        print(f"Goodbye {self.name}!")
        time.sleep(5)
        print(Fore.RED + "You are a monster." + Fore.WHITE)
        time.sleep(1)
        exit()



    def kick(self):
        print(f"\nYou kicked {self.name}. That's not nice!")
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} is hurt and now has {self.energy} energy left.")
            if self.energy <= 50:
                self.is_hungry = True
            self.xp += 5
            return True
        else:
            print(f"{self.name} is too tired to react.")
            return False



    def bark(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"\n{self.name} says Woof!, and has now {self.energy} energy left.")
            if self.energy <= 50:
                self.is_hungry = True
            self.xp += 10
            return True
        else:
            print(f"\n{self.name} is too tired to bark.")
            return False



    def sleep(self):
        if self.energy >= 50:
            print(f"\n{self.name} is too energetic to sleep!")
            return False
        else:
            print(f"\n{self.name} is sleeping...")
            time.sleep(10)
            print("Zzzzz...")
            time.sleep(10)
            print("Zzzzzzzzzzzzzzzzzzzzzzzzzz...")
            time.sleep(10)
            print("Zzzzzzzzzzzzzzzzzzzzzzzzzzzzz...")
            time.sleep(10)
            print("Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz...")
            time.sleep(10)
            print("Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz...")
            time.sleep(10)
            old_energy = self.energy
            self.energy = 100
            self.is_hungry = False
            with open('ascii/awaken_sleep.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
            print (f"\n{self.name} has slept and restores {100 - old_energy} energy!")
            self.xp += 20
            return True




    def eat(self):
     if self.is_hungry or self.energy <= 75:
        self.energy += 25
        if self.energy > 100: 
            self.energy = 100
        self.is_hungry = False
        print(f"\n{self.name} ate a meal and restored 25 energy!")
        self.xp += 10
        return True
     else:
        print(f"\n{self.name} is too full to eat right now.")
        return False


    def play(self):
        if self.energy >= 30 and self.is_hungry == False:
            self.energy -= 30
            print(f"\n{self.name} is playing! and now has {self.energy} energy left.")
            if self.energy <= 50:
                self.is_hungry = True
            self.xp += 15
            return True
        else:
            if self.energy <= 30:
                print(f"\n{self.name} is too tired to play...")
                return False
            elif self.is_hungry:
                print(f"\n{self.name} is too hungry to play.")
                return False



    @classmethod
    def get_all_saved_dogs(cls):
        if not os.path.exists("saves"):
            return []
        files = os.listdir("saves")
        dog_names = []
        for filename in files:
            if filename.endswith("_data.json"):
                name = filename.replace("_data.json", "")
                dog_names.append(name)
        return dog_names
    


    @classmethod
    def load_from_file(cls, filename):
        if not os.path.exists(filename):
            print(f"No saved file found. No {filename}.")
            return None
        with open(filename, "r") as file:
            data = json.load(file)

        dog = cls(
            name=data["name"],
            breed=data["breed"],
            age=data["age"]
        )
        dog.energy = data["energy"]
        dog.is_hungry = data["is_hungry"]
        dog.xp = data["xp"]
        dog.rank = data["rank"]
        dog.money = data["money"]
        print(f"{dog.name}'s data is loaded from {filename}")
        return dog
    


    @classmethod
    def delete_saved_file(cls, filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Deleted saved file: {filename}")
        else:
            print(f"No saved file found to delete: {filename}")
    
    def to_dict(self):
        return {
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "energy": self.energy,
            "is_hungry": self.is_hungry,
            "xp": self.xp,
            "rank": self.rank,
            "money": self.money
        }
    
    def save_to_file(self):
        if not os.path.exists("saves"):
            os.makedirs("saves")
        with open(f"saves/{self.name}_data.json", "w") as file:
            json.dump(self.to_dict(), file)
        print(f"{self.name}'s data has been saved to saves/{self.name}_data.json!")






class GameManager:
    def __init__(self):
        self.last_drain_time = time.time()
        self.rank_thresholds = {
            "Puppy": 0,
            "Good Dog": 150,
            "Senior Dog": 400,
            "Grand Master": 1000
        }


    def check_passive_drain(self, dog):
        current_time = time.time()
        time_passed = current_time - self.last_drain_time
    
        if time_passed >= 60:
            minutes_passed = int(time_passed // 60)
            energy_to_drain = minutes_passed * 5
            dog.energy -= energy_to_drain
        
        
            if dog.energy < 0:
                dog.energy = 0
                print(f"{dog.name} is completely exhausted!") 
        
            if dog.energy <= 50:
                dog.is_hungry = True
        
        self.last_drain_time = current_time

    def check_rank_up(self, dog):
        old_rank = dog.rank
        for rank_name, min_xp in sorted(self.rank_thresholds.items(), key= lambda x: x[1], reverse= True):
            if dog.xp >= min_xp:
                dog.rank = rank_name
                break
        if old_rank != dog.rank:
            print(f"{dog.name} ranked up to {dog.rank}!")
            return True
        return False
    




class versionChecker:
    def __init__(self):
        with open("config/version.json", "r") as version_file:
            version_data = json.load(version_file)
        self.current_version = version_data.get("latest_version")
        self.version_url = "https://raw.githubusercontent.com/lofovs/dog-simulator/refs/heads/main/config/version.json"
        self.cached_data = None
        self.latest_changelog = ""
        
    def fetch_latest_version(self):
        try:
            response = requests.get(self.version_url)
            return response.json()
        except:
            return None
        
    def refresh(self):
        self.cached_data = None
    
    def check_new_update(self):
        data = self.fetch_latest_version()
        if data is None:
            return False
        latest = data["latest_version"]
        current = self.current_version
        self.latest_changelog = data["changelog"]
        latest_tuple = tuple(map(int, latest.split('.')))
        current_tuple = tuple(map(int, current.split('.')))
        return latest_tuple > current_tuple
    
    def prompt_for_update(self):
        if self.check_new_update():
            clear_screen()
            print(Fore.YELLOW + "🎮 UPDATE AVAILABLE!" + Fore.WHITE)
            print(f"Current: {self.current_version} → New: {self.fetch_latest_version()['latest_version']}")
            print(f"📝 Changes: {self.latest_changelog}")
            print("\nWhat would you like to do?")
            print("1. Download update now")
            print("2. Continue playing (remind me later)")
        
            choice = input("\nChoose: ")
            if choice == "1":
                import webbrowser
                webbrowser.open(self.fetch_latest_version()['download_url'])
                print("\n📥 Update page opened in browser!")
                print("💡 Replace all files in your Dog Simulator folder with the new ones.")
                input("\nPress Enter to continue playing...")
        else:
            print(Fore.GREEN + "✅ You're running the latest version!" + Fore.WHITE)