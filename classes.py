import json
from colorama import Fore, init
import os
import time

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 100
        self.is_hungry = False



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
        else:
            print(f"{self.name} is too tired to react.")



    def bark(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"\n{self.name} says Woof!, and has now {self.energy} energy left.")
            if self.energy <= 50:
                self.is_hungry = True
        else:
            print(f"\n{self.name} is too tired to bark.")



    def sleep(self):
        if self.energy >= 50:
            print(f"\n{self.name} is too energetic to sleep!")
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
            print(f"\n{self.name} has awakened!")
            old_energy = self.energy
            self.energy = 100
            self.is_hungry = False
            print (f"\n{self.name} has slept and restores {100 - old_energy}!")
            print(f"\n{self.name} has now awaken and rested with {self.energy} energy!")




    def eat(self):
     if self.is_hungry or self.energy <= 75:
        self.energy += 25
        if self.energy > 100: 
            self.energy = 100
        self.is_hungry = False
        print(f"\n{self.name} ate a meal and restored 25 energy!")
     else:
        print(f"\n{self.name} is too full to eat right now.")



    def play(self):
        if self.energy >= 30 and self.is_hungry == False:
            self.energy -= 30
            print(f"\n{self.name} is playing! and now has {self.energy} energy left.")
            if self.energy <= 50:
                self.is_hungry = True
        else:
            if self.energy <= 30:
                print(f"\n{self.name} is too tired to play...")
            elif self.is_hungry:
                print(f"\n{self.name} is too hungry to play.")



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
            "is_hungry": self.is_hungry
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