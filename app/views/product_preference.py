import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from app.views.thankyou import ThankYouScreen
from data.db_controller import get_all_products
from data.db_controller import insert_preference
from tkinter import font 
from data.db_connection import create_db_connection
class ProductPreferenceScreen:
    def __init__(self, root, connection, consumerID):
        
        self.root = root
        self.connection = connection
        self.consumerID = consumerID
        self.root.title("Crop/Product Preference")
        self.root.geometry("1200x600")  # Set the window to full screen
 

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Roboto")

        self.root.configure(bg="white")
        title_label = tk.Label(root, text="Product/Crop Preferences", font=(default_font, 16), bg="white")
        title_label.grid(row=0, column=1, pady=10)

        # Fetch products from the database
        self.products = get_all_products(self.connection)

        # Create a frame for product preferences and month selection
        preference_frame = tk.Frame(root, bg="white")
        preference_frame.grid(row=1, column=1, pady=10)

        # Create a frame for month selection
        month_frame = tk.Frame(preference_frame, bg="white")
        month_frame.grid(row=0, column=2, padx=10)

        # Create a label for month selection
        month_label = tk.Label(month_frame, text="Select Month and Year:", bg="white")
        month_label.pack()

        # Create a dropdown for month and year
        months_years = [("January", 2024), ("February", 2024), ("March", 2024),
                        ("April", 2024), ("May", 2024), ("June", 2024), ("July", 2024), 
                        ("August", 2024), ("September", 2024), ("November", 2024), ("December", 2024)]
        self.month_year_var = tk.StringVar()
        self.month_year_var.set(months_years[0])  # Set default value
        month_year_dropdown = tk.OptionMenu(month_frame, self.month_year_var, *months_years)
        month_year_dropdown.pack()

        # Create a frame for product selection using checkboxes
        product_frame = tk.Frame(preference_frame, bg="white")
        product_frame.grid(row=0, column=1, padx=10)

        # Create a label for product selection
        product_label = tk.Label(product_frame, text="Select Crop/Products:", bg="white")
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
        submit_button = tk.Button(button_frame, text="Add Preferences", command=self.add_preferences, bg="#12DB81", fg="white",
                                  bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                  cursor="hand2", font=(default_font, 12))
        submit_button.pack(pady=10)

        # Create a listbox to display selected preferences at the bottom
        self.preference_listbox = tk.Listbox(root, selectbackground="#12DB81", selectforeground="white", bg="white", width=80)
        self.preference_listbox.grid(row=2, column=1, pady=10)

        # Create a frame for the "Add Preferences" button
        submit_button_frame = tk.Frame(root, bg="white")
        submit_button_frame.grid(row=3, column=1, padx=10)

        # Set the button color to green
        final_button = tk.Button(submit_button_frame, text="Finish", command=self.submit_preferences, bg="#12DB81", fg="white",
                                 bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                 cursor="hand2", font=(default_font, 12))
        final_button.pack(pady=10) 

        image_frame = tk.Frame(root, bg="#12DB81")
        image_frame.grid(row=0, column=0, rowspan=4, padx=10)
        # Add image to header using PIL
        image_path = "C:/BIS608/FarmChoice/Decision-System/app/static/preference.jpg"  # Replace with your image path
        original_image = Image.open(image_path) 

        # Resize the image to the desired dimensions
        resized_image = original_image.resize((600, 400))
        photo = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(image_frame, image=photo, bg="#12DB81")
        image_label.image = photo
        image_label.pack()
        
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")

    def add_preferences(self):
        selected_products = [product['ProductName'] for product, var in zip(self.products, self.product_vars) if var.get()]
        selected_month_year = self.month_year_var.get()

        if not selected_products:
            messagebox.showerror("Error", "Please select at least one product.")
            return
        try:
            self.preferences = insert_preference(self.db_connection, selected_month_year, self.consumerID, self.products, selected_products)
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
