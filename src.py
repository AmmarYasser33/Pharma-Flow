from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

#* Medicine class

class Medicine:
    def __init__(self, name, quantity, price, form):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.form = form
    
    def add_medicine(self, quantity):
        self.quantity += quantity

    def sell_medicine(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return True
        else:
            return False
        
    def update_medicine(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def view_medicine(self):
        return f"{self.name}\t{self.quantity}\t{self.price}\t{self.form}"
    
#* Pharmacy class

class Pharmacy:
    def __init__(self):
        self.medicines = self.load_data()
        self.total_sales, self.profit = self.load_financial_data()

    def load_financial_data(self):
        with open('data.txt', 'r') as f:
            data = eval(f.read())
            return data['total_sales'], data['profit']
        
    def save_financial_data(self):
        data = {'total_sales': round(self.total_sales, 2), 'profit': round(self.profit, 2)}
        with open('data.txt', 'w') as file:
            file.write(str(data))

    def load_data(self):
        with open('medicines.txt', 'r') as f:
            data = eval(f.read())
            return [Medicine(*item) for item in data]
        
    def save_data(self):
        with open('medicines.txt', 'w') as file:
            data = [[med.name, med.quantity, med.price, med.form] for med in self.medicines]
            file.write(str(data))
        
        self.save_financial_data()

    def add_medicine(self, medicine):
        for med in self.medicines:
            if med.name == medicine.name and med.form == medicine.form:
                med.update_medicine(medicine.quantity + med.quantity, medicine.price)
                return
            
        self.medicines.append(medicine)

    def sell_medicine(self, name, quantity, form, selling_price):
        for med in self.medicines:
            if med.name == name and med.form == form:
                if med.sell_medicine(quantity):
                    self.total_sales += quantity * selling_price
                    self.profit += quantity * (selling_price - med.price)
                    return True
                else:
                    return False
        return -1
    
    def view_inventory(self):
        inventory_details = [med.view_medicine() for med in self.medicines]
        return inventory_details
    
    def view_sales(self):
        return f"Total Sales: {round(self.total_sales, 2)} L.E\nProfit: {round(self.profit, 2)} L.E"
    
#* GUI class

class PharmacyGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(background="#e1d8b9", padx=10, pady=10)

        self.pharmacy = Pharmacy()

        self.create_widgets()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.pharmacy.save_data()
        self.root.destroy()

    def create_widgets(self):
        # Labels
        Label(self.root, text="Pharmacy", font=("Arial", 26, "bold"), fg="#111", bg="#e1d8b9").grid(row=0, column=0, columnspan=2, pady=10)
        Label(self.root, text="Medicine Name:", font=("Arial", 14, "bold"), fg="#111", bg="#e1d8b9").grid(row=1, column=0, padx=5, pady=5)
        Label(self.root, text="Quantity:", font=("Arial", 14, "bold"), fg="#111", bg="#e1d8b9").grid(row=2, column=0, padx=5, pady=5)
        Label(self.root, text="Price:", font=("Arial", 14, "bold"), fg="#111", bg="#e1d8b9").grid(row=3, column=0, padx=5, pady=5)
        Label(self.root, text="Form:", font=("Arial", 14, "bold"), fg="#111", bg="#e1d8b9").grid(row=4, column=0, padx=5, pady=5)

        # Entry Widgets
        # add padding to the entry widgets
        self.medicine_entry = Entry(self.root, width=25, font=("Arial", 12, "normal"))
        self.quantity_entry = Entry(self.root, width=25, font=("Arial", 12, "normal"))
        self.price_entry = Entry(self.root, width=25, font=("Arial", 12, "normal"))

        self.medicine_entry.grid(row=1, column=1, padx=5, pady=5)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        # Radio Buttons for medicine form
        frame1 = Frame(self.root, bg="#e1d8b9")
        frame1.grid(row=4, column=1, padx=5, pady=5)
        frame2 = Frame(self.root, bg="#e1d8b9")
        frame2.grid(row=5, column=1, padx=5, pady=5)

        self.form = StringVar()
        self.form.set("Tablet")
        Radiobutton(frame1, text="Tablet", variable=self.form, value="Tablet", bg="#e1d8b9", font=("Arial", 12, "normal")).grid(row=0, column=0, padx=5, pady=5)
        Radiobutton(frame1, text="Capsule", variable=self.form, value="Capsule", bg="#e1d8b9", font=("Arial", 12, "normal")).grid(row=0, column=1, padx=5, pady=5)
        Radiobutton(frame2, text="Syrup", variable=self.form, value="Syrup", bg="#e1d8b9", font=("Arial", 12, "normal")).grid(row=0, column=0, padx=5, pady=5)
        Radiobutton(frame2, text="Injection", variable=self.form, value="Injection", bg="#e1d8b9", font=("Arial", 12, "normal")).grid(row=0, column=1, padx=5, pady=5)

        # Buttons
        Button(self.root, text="Add Medicine", command=self.add_medicine, width=15, height=2, bg="#111", fg="#fff", font=("Arial", 12, "normal")).grid(row=6, column=0, columnspan=2, pady=10)
        Button(self.root, text="Sell Medicine", command=self.sell_medicine, width=15, height=2, bg="#111", fg="#fff", font=("Arial", 12, "normal")).grid(row=7, column=0, columnspan=2, pady=10)
        Button(self.root, text="Show Inventory", command=self.show_inventory, width=15, height=2, bg="#111", fg="#fff", font=("Arial", 12, "normal")).grid(row=8, column=0, columnspan=2, pady=10)
        Button(self.root, text="Show Sales", command=self.show_sales, width=15, height=2, bg="#111", fg="#fff", font=("Arial", 12, "normal")).grid(row=9, column=0, columnspan=2, pady=10)
        
    def add_medicine(self):
        medicine_name = self.medicine_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        form = self.form.get()

        if medicine_name == "" or quantity == "" or price == "":
            showerror("Error", "Please fill all fields.")
            return
        
        quantity = int(quantity)
        price = int(price)
        if quantity <= 0 or price <= 0:
            showerror("Error", "Quantity and price must be positive.")
            return

        medicine = Medicine(medicine_name, quantity, price, form)
        self.pharmacy.add_medicine(medicine)
        showinfo("Success", f"{quantity} units of {medicine_name}-{form} added.")

        self.clear_entries()
        
    def sell_medicine(self):
        medicine_name = self.medicine_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        form = self.form.get()

        if medicine_name == "" or quantity == "" or price == "":
            showerror("Error", "Please fill all fields.")
            return
        quantity = int(quantity)
        price = int(price)
        if quantity <= 0 or price <= 0:
            showerror("Error", "Quantity and price must be positive.")
            return

        result = self.pharmacy.sell_medicine(medicine_name, quantity, form, price)
        if result == True:
            showinfo("Success", f"{quantity} units of {medicine_name}-{form} sold.")
            self.clear_entries()
        elif result == False:
            showerror("Error", f"Quantity of {medicine_name}-{form} is not enough.")
        else:
            showerror("Error", f"{medicine_name}-{form} is not available.")

    def show_inventory(self):
        inventory_details = self.pharmacy.view_inventory()
        infoHeaders = "Name\tQuantity\tPrice\tForm\n---------------------------------------------\n"
        showinfo("Medicines", infoHeaders + "\n".join(inventory_details))

    def show_sales(self):
        sales_details = self.pharmacy.view_sales()
        showinfo("Sales", sales_details)

    def clear_entries(self):
        self.medicine_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.form.set("Tablet")



root = Tk()
gui = PharmacyGUI(root)
mainloop()
