# Pharmacy Management System

This simple Python project is a Pharmacy Management System implemented using the Tkinter library for the graphical user interface. The system allows users to add medicines to the inventory, sell medicines, view the current inventory, and check sales details.

## Getting Started

Make sure you have Python installed on your system. You can run the program by executing the following command in your terminal or command prompt:

```bash
python src.py
```

Replace `src.py` with the name of the file containing the provided Python code.

## Project Structure

The project consists of three main classes:

1. **Medicine Class**: Represents a medicine with attributes such as name, quantity, price, and form. Provides methods to add, sell, update, and view medicine details.

2. **Pharmacy Class**: Manages the pharmacy's inventory and financial data. Handles loading and saving data to files, adding medicines, selling medicines, and providing inventory and sales information.

3. **PharmacyGUI Class**: Implements the graphical user interface using Tkinter. Allows users to interact with the pharmacy system by adding medicines, selling medicines, and viewing inventory and sales.

## Usage

Upon running the program, a Tkinter window will appear with the following options:

- **Add Medicine**: Allows the user to add a new medicine to the inventory by providing the medicine's name, quantity, price, and form.

- **Sell Medicine**: Enables the user to sell a specific quantity of a medicine. The user needs to provide the medicine's name, quantity, price, and form.

- **Show Inventory**: Displays the current inventory of medicines, including details such as name, quantity, price, and form.

- **Show Sales**: Shows the total sales and profit made by the pharmacy.

## Notes

- The system uses file-based data storage. Medicine and financial data are loaded from and saved to files (`medicines.txt` and `data.txt`).

- Closing the application window triggers the saving of data to files.

- Error messages will be displayed if the user attempts to perform actions without providing the necessary information.

Feel free to explore and modify the code to meet your specific requirements or extend its functionality.
