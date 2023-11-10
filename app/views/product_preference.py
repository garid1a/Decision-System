import tkinter as tk
from tkinter import messagebox
from app.views.thankyou import ThankYouScreen
from data.db_controller import get_all_products
from data.db_controller import insert_preference

class ProductPreferenceScreen:
    def __init__(self, root, connection, consumerID):
        self.root = root
        self.connection = connection
        self.consumerID = consumerID
        self.root.title("Product Preference")
        self.root.geometry("800x400")   # Set the window to full screen

        # Create a label for the title
        title_label = tk.Label(root, text="Product Preference", font=("Helvetica", 16), bg="white")
        title_label.grid(row=0, column=2, pady=10)

        # Fetch products from the database
        self.products = get_all_products(self.connection)

        # Create a frame for product preferences and month selection
        preference_frame = tk.Frame(root, bg="white")
        preference_frame.grid(row=1, column=2, pady=10)

        # Create a frame for month selection
        month_frame = tk.Frame(preference_frame, bg="white")
        month_frame.grid(row=0, column=1, padx=10)

        # Create a label for month selection
        month_label = tk.Label(month_frame, text="Select Month and Year:", bg="white")
        month_label.pack()

        # Create a dropdown for month and year
        months_years = [("January", 2023), ("February", 2023), ("March", 2023),
                        ("April", 2024), ("May", 2024), ("June", 2024)]
        self.month_year_var = tk.StringVar()
        self.month_year_var.set(months_years[0])  # Set default value
        month_year_dropdown = tk.OptionMenu(month_frame, self.month_year_var, *months_years)
        month_year_dropdown.pack()

        # Create a frame for product selection using checkboxes
        product_frame = tk.Frame(preference_frame, bg="white")
        product_frame.grid(row=0, column=2, padx=10)

        # Create a label for product selection
        product_label = tk.Label(product_frame, text="Select Products:", bg="white")
        product_label.pack()

        # Create variables to store the state of the checkboxes
        self.product_vars = []
        for i, product in enumerate(self.products):
            var = tk.BooleanVar()
            self.product_vars.append(var)
            checkbox = tk.Checkbutton(product_frame, text=product['ProductName'], variable=var, bg="white")
            checkbox.pack(anchor="w")

        # Create a frame for the "Add Preferences" button
        button_frame = tk.Frame(preference_frame, bg="white")
        button_frame.grid(row=0, column=3, padx=10)

        # Set the button color to green
        submit_button = tk.Button(button_frame, text="Add Preferences", command=self.add_preferences, bg="green", fg="white")
        submit_button.pack(pady=10)

        # Create a listbox to display selected preferences at the bottom
        self.preference_listbox = tk.Listbox(root, selectbackground="green", selectforeground="white", bg="white", width=50)
        self.preference_listbox.grid(row=1, column=5, pady=10)

         # Create a frame for the "Add Preferences" button
        submit_button_frame = tk.Frame(root, bg="white")
        submit_button_frame.grid(row=2, column=5, padx=10)

        # Set the button color to green
        final_button = tk.Button(submit_button_frame, text="Finish", command=self.submit_preferences, bg="green", fg="white")
        final_button.pack(pady=10)

    def add_preferences(self):
        selected_products = [product['ProductName'] for product, var in zip(self.products, self.product_vars) if var.get()]
        selected_month_year = self.month_year_var.get()

        if not selected_products:
            messagebox.showerror("Error", "Please select at least one product.")
            return
        try:
            self.preferences = insert_preference(self.connection, selected_month_year, self.consumerID, self.products, selected_products)
        except:
            messagebox.showerror("Error", "Error Occured")

        # Display selected preferences in the listbox
        preferences_str = f"{selected_month_year}: {', '.join(selected_products)}"
        self.preference_listbox.insert(tk.END, preferences_str)

        # Display a message box for successful addition of preferences
        messagebox.showinfo("Success", f"Preferences added for {selected_month_year}.")

        # You can add more logic to update the display or reset selections if needed

    def submit_preferences(self):
        self.thankyou()
      

    def thankyou(self):
        self.root.withdraw()  # Hide the login/registration screen
        thankyou_window = tk.Toplevel()  # Create a new window
        thankyou_app = ThankYouScreen(thankyou_window)

if __name__ == "__main__":
    root = tk.Tk()
    connection = None  # You should establish a database connection
    app = ProductPreferenceScreen(root, connection)
    root.mainloop()
