import json
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
        self.energy = 0
        self.is_hungry = False

        if os.path.exists(f"saves/{self.name}_data.json"):
            Dog.delete_saved_file(f"saves/{self.name}_data.json")
        print(f"Goodbye {self.name}!")
        exit()


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

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
        print("6. Have Birthday")
        print("7. Kill Dog")
        print("8. Save and quit")
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
            my_dog.have_birthday()
        elif choice == "7":
            confirm = input(f"Are you sure you want to kill {my_dog.name}? This action cannot be undone. (yes/no): ")
            if confirm.lower() == 'yes' or confirm.lower() == 'y':
                my_dog.kill()
            else:
                print(f"{my_dog.name} is safe for now.")
        elif choice == "8":
            my_dog.save_to_file()
            print("Goodbye.")
            time.sleep(3)
            break
        else:
            print("Invalid choice, try again.")
        input("\nPress enter to continue...")

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
                name = input("Name: ")
                breed = input("Breed: ")
                age = int(input("Age: "))
                return Dog(name, breed, age)
            
    print("Invalid choice!")
    return None

my_dog = startup_menu()
if my_dog:
    menu(my_dog)