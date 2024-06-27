import sqlite3
import webbrowser

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        return "\n".join(self.commands)

class PetRegistryCLI:
    def __init__(self):
        self.conn = sqlite3.connect('pet_registry.db')
        self.create_tables()

        self.pet_registry = []
        self.load_pets_from_db()

    def create_tables(self):
        # Создание таблицы pets (если она не существует)
        create_pets_table = '''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL
        );
        '''
        self.conn.execute(create_pets_table)

        # Создание таблицы commands (если она не существует)
        create_commands_table = '''
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            command TEXT NOT NULL,
            FOREIGN KEY (pet_id) REFERENCES pets (id) ON DELETE CASCADE
        );
        '''
        self.conn.execute(create_commands_table)
        self.conn.commit()

    def add_pet_to_db(self, name, species):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO pets (name, species) VALUES (?, ?)', (name, species))
        pet_id = cursor.lastrowid
        self.conn.commit()
        return pet_id

    def add_command_to_db(self, pet_id, command):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO commands (pet_id, command) VALUES (?, ?)', (pet_id, command))
        self.conn.commit()

    def load_pets_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, species FROM pets')
        pets = cursor.fetchall()
        for pet in pets:
            pet_obj = Pet(pet[1], pet[2])
            pet_obj.id = pet[0]
            cursor.execute('SELECT command FROM commands WHERE pet_id = ?', (pet[0],))
            commands = cursor.fetchall()
            for cmd in commands:
                pet_obj.add_command(cmd[0])
            self.pet_registry.append(pet_obj)

    def add_pet(self):
        name = input("Enter pet's name: ")
        species = input("Enter pet's species: ")
        if name and species:
            pet_id = self.add_pet_to_db(name, species)
            pet = Pet(name, species)
            pet.id = pet_id
            self.pet_registry.append(pet)
            print(f"{pet.species} named {pet.name} added to the registry.")
            if species == "Monkey" and name == "SpaceMonkey":
                webbrowser.open("https://www.youtube.com/watch?v=vKOv8ohYJTA&t=52")
        else:
            print("Please enter both name and species.")

    def add_command(self):
        pet_names = [pet.name for pet in self.pet_registry]
        if not pet_names:
            print("No pets found in the registry.")
            return
        
        print("Select a pet:")
        for index, name in enumerate(pet_names):
            print(f"{index + 1}. {name}")
        
        choice = input("Enter the number of the pet: ")
        try:
            pet_index = int(choice) - 1
            if 0 <= pet_index < len(self.pet_registry):
                selected_pet = self.pet_registry[pet_index]
                command = input(f"Enter command for {selected_pet.name}: ")
                selected_pet.add_command(command)
                self.add_command_to_db(selected_pet.id, command)
                print(f"Command '{command}' added to {selected_pet.name}.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_commands(self):
        pet_names = [pet.name for pet in self.pet_registry]
        if not pet_names:
            print("No pets found in the registry.")
            return
        
        print("Select a pet:")
        for index, name in enumerate(pet_names):
            print(f"{index + 1}. {name}")
        
        choice = input("Enter the number of the pet: ")
        try:
            pet_index = int(choice) - 1
            if 0 <= pet_index < len(self.pet_registry):
                selected_pet = self.pet_registry[pet_index]
                print(f"Commands for {selected_pet.name}:")
                print(selected_pet.show_commands())
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def list_pets(self):
        if not self.pet_registry:
            print("No pets found in the registry.")
            return
        
        print("Pets in the registry:")
        for pet in self.pet_registry:
            print(f"{pet.species} named {pet.name}")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add Pet")
            print("2. Add Command")
            print("3. Show Commands")
            print("4. List Pets")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.add_pet()
            elif choice == "2":
                self.add_command()
            elif choice == "3":
                self.show_commands()
            elif choice == "4":
                self.list_pets()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

def main():
    app = PetRegistryCLI()
    app.run()

if __name__ == "__main__":
    main()
