Pet Registry CLI Application

 Overview:

 This Python application, Pet Registry CLI, provides a command-line interface for managing a registry of pets and their associated commands. It utilizes SQLite for persistent storage of pet data and commands, allowing users to add pets, add commands to pets, view commands associated with pets, and list all pets in the registry.

Features

Add Pet:

Allows users to add a new pet to the registry by specifying the pet's name and species.
Optionally opens a web browser to a specific link if the pet is a "SpaceMonkey".
Add Command:

Enables users to add commands or instructions associated with a selected pet from the registry.
Show Commands:

Displays all commands associated with a selected pet.

List Pets:


Lists all pets currently registered in the system.
SQLite Database Integration:

Utilizes SQLite to store and retrieve data about pets and their associated commands.
Two tables (pets and commands) are used with appropriate relationships for storing and querying data.
Menu-Driven Interface:

Provides a clear menu-driven interface for users to navigate and perform various operations on the pet registry.
Installation
To run the application, follow these steps:

Clone the repository:



git clone 
cd <repository-name>

Install dependencies:

Ensure you have Python 3.x installed.
Install required Python packages using pip:


pip install sqlite3

Run the application:

Execute the main Python file:
Копировать код
python pet_registry_cli.py
Usage
Upon running the application, you will be presented with a menu.
Choose an option by entering the corresponding number.
Follow the prompts to add pets, add commands to pets, view commands, list pets, or exit the application.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or support, please contact Maksim at mivanov222@gmail.com.

