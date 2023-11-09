import tkinter as tk
from tkinter import messagebox
from app.views.thankyou import ThankYouScreen
from data.db_controller import get_all_products

class ProductPreferenceScreen:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Product Preference")
        self.root.geometry("800x700")  # Set the initial window size

        # Limit the maximum height to 400 pixels
        self.root.maxsize(800, 700)

        # Create a label for the title
        title_label = tk.Label(root, text="Product Preference", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Fetch products from the database
        self.products = get_all_products(self.connection)

        # Create a frame for product preferences and month selection
        preference_frame = tk.Frame(root)
        preference_frame.pack(pady=10)

        # Create a frame for product selection using checkboxes
        product_frame = tk.Frame(preference_frame)
        product_frame.pack(side="left", padx=10)

        # Create a label for product selection
        product_label = tk.Label(product_frame, text="Select Products:")
        product_label.pack()

        # Create variables to store the state of the checkboxes
        self.product_vars = []
        for product in self.products:
            var = tk.BooleanVar()
            self.product_vars.append(var)
            print(product)
            checkbox = tk.Checkbutton(product_frame, text=product['ProductName'], variable=var)
            checkbox.pack(anchor="w")

        # Create a frame for month selection
        month_frame = tk.Frame(preference_frame)
        month_frame.pack(side="left", padx=10)

        # Create a label for month selection
        month_label = tk.Label(month_frame, text="Select Months:")
        month_label.pack()

        # Create a list of month options
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        # Create variables to store the state of the month checkboxes
        self.month_vars = []
        for month in months:
            var = tk.BooleanVar()
            self.month_vars.append(var)
            checkbox = tk.Checkbutton(month_frame, text=month, variable=var)
            checkbox.pack(anchor="w")

        # Create a submit button
        submit_button = tk.Button(root, text="Submit Preferences", command=self.submit_preferences)
        submit_button.pack(pady=10)

    def submit_preferences(self):
        selected_products = [product for product, var in zip(self.products, self.product_vars) if var.get()]
        selected_months = [month for month, var in zip(
            ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            self.month_vars) if var.get()]

        if not selected_products:
            messagebox.showerror("Error", "Please select at least one product.")
            return

        if not selected_months:
            messagebox.showerror("Error", "Please select at least one month.")
            return

        # Process and save consumer's preferences in the database
        # You can add your logic to store the preferences

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
