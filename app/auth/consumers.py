import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data.db_connection import create_db_connection
from data.db_controller import login_consumer, insert_consumer
import re 
from app.views.layout import Layout 


class ConsumerLoginRegistrationScreen:
    def __init__(self, root, landing_page_callback): 
        self.root = root
        self.root.title("Consumer Login/Registration")
        self.root.geometry("800x400")  # Set the window size
        self.landing_page_callback = landing_page_callback 
        # Set background color
        self.root.configure(bg="light gray")  # Light gray background

        # Reuse the common header and footer
        Layout(root) 
        
        # Create a frame for login
        login_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")  # Light gray border, white background
        login_frame.pack(side="left", fill="both", expand=True)

        # Create a frame for registration
        registration_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")  # Light gray border, white background
        registration_frame.pack(side="left", fill="both", expand=True)

        # Create a label for the title
        title_label = tk.Label(login_frame, text="Consumer Login", font=("Helvetica", 16), bg="white")  # White background
        title_label.pack(pady=10)

        # Create a label and entry for username
        self.loginusername_label = tk.Label(login_frame, text="Username:", bg="white")  # White background
        self.loginusername_label.pack()
        self.loginusername_entry = tk.Entry(login_frame)
        self.loginusername_entry.pack()

        # Create a label and entry for password
        self.loginpassword_label = tk.Label(login_frame, text="Password:", bg="white")  # White background
        self.loginpassword_label.pack()
        self.loginpassword_entry = tk.Entry(login_frame, show='*')
        self.loginpassword_entry.pack()

        # Create a login button
        login_button = tk.Button(login_frame, text="Login", command=self.login, bg="green", fg="white")  # Blue button with white text
        login_button.pack(pady=10)

        back_button = tk.Button(login_frame, text="Back", command=self.back, bg="grey", fg="white")  # Green button with white text
        back_button.pack(pady=5)


        # Create a label for the title
        title_label = tk.Label(registration_frame, text="Consumer Registration", font=("Helvetica", 16), bg="white")  # White background
        title_label.pack(pady=10)

        # Create a label and entry for name
        self.name_label = tk.Label(registration_frame, text="Full Name:", bg="white")  # White background
        self.name_label.pack()
        self.name_entry = tk.Entry(registration_frame)
        self.name_entry.pack()

                # Create a label and entry for age
        self.age_label = tk.Label(registration_frame, text="Age:", bg="white")
        self.age_label.pack()
        self.age_entry = tk.Entry(registration_frame, validate="key", validatecommand=(root.register(self.validate_numeric), '%P'))
        self.age_entry.pack()

        # Create a label and dropdown for location
        self.location_label = tk.Label(registration_frame, text="Location:", bg="white")
        self.location_label.pack()

        # Sample list of states for the dropdown
         # Static Data:
        states = [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Goa",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jharkhand",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Maharashtra",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Tamil Nadu",
            "Telangana",
            "Tripura",
            "Uttar Pradesh",
            "Uttarakhand",
            "West Bengal"
        ]


        # Create a Combobox for the location
        self.location_var = tk.StringVar()
        self.location_combobox = ttk.Combobox(registration_frame, textvariable=self.location_var, values=states)
        self.location_combobox.pack()
 
        # Create a label for UserName
        self.username_label = tk.Label(registration_frame, text="UserName:", bg="white")  # White background
        self.username_label.pack()
        self.username_entry = tk.Entry(registration_frame)
        self.username_entry.pack()

        # Create a label for Password
        self.password_label = tk.Label(registration_frame, text="Password:", bg="white")  # White background
        self.password_label.pack()
        self.password_entry = tk.Entry(registration_frame)
        self.password_entry.pack()

        # Create a label for Password
        self.cpassword_label = tk.Label(registration_frame, text="Confirm Password:", bg="white")  # White background
        self.cpassword_label.pack()
        self.cpassword_entry = tk.Entry(registration_frame)
        self.cpassword_entry.pack()

        # Create a register button
        register_button = tk.Button(registration_frame, text="Register", command=self.register, bg="green", fg="white")  # Green button with white text
        register_button.pack(pady=10)

        back_button = tk.Button(registration_frame, text="Back", command=self.back, bg="grey", fg="white")  # Green button with white text
        back_button.pack(pady=5)
 
        # Connect to Database
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")
    def validate_numeric(self, value):
            # Validate that the input is a numeric value
            return value.isdigit()
    def back(self):
        self.root.withdraw()
        self.landing_page_callback()

    def login(self):
        username = self.loginusername_entry.get()
        password = self.loginpassword_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        consumer = login_consumer(self.db_connection, username, password)

        if consumer:
            self.consumer_id = consumer['ConsumerID']
            print(f"Logged in as {consumer['Name']}")
            self.open_product_preference_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        location = self.location_combobox.get()
        password = self.password_entry.get()
        cpassword = self.cpassword_entry.get()
        user_name = self.username_entry.get()

        if not name or not age or not location or not password or not cpassword or not user_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return 
        
        #UserName Validation
        if not re.match("^[a-zA-Z0-9]*$", user_name):
            messagebox.showerror("Error", "Username can only contain letters and numbers.")
            return
        
        # Validate Password 
        error_message = []

        if len(password) < 12:
            error_message.append("Password must be at least 12 characters long.")
        
        if not any(c.isupper() for c in password):
            error_message.append("Password must contain at least one uppercase letter.")
        
        if not any(c.islower() for c in password):
            error_message.append("Password must contain at least one lowercase letter.")
        
        if not any(c.isdigit() for c in password):
            error_message.append("Password must contain at least one numeric digit.")
        
        if not any(c in r'!@#$%' for c in password):
            error_message.append("Password must contain at least one special character (!, @, #, $, %).")
        
        if any(common_word in password.lower() for common_word in ['password', '12345', 'qwerty']):
            error_message.append("Avoid using easily guessable information, such as common words or patterns.")
        
        if error_message:
            messagebox.showerror("Error", "\n".join(error_message))
            return

        # Validate Password and Confirm Password match
        if self.password_entry.get() != self.cpassword_entry.get():
            messagebox.showerror("Error", "Passwords do not match.")
            return
 

        consumer_data = {
            "Name": name,
            "Age": age,
            "Location": location,
            "UserName": user_name,
            "Password": password
        }

        # We need to generate the UserName & Password

        self.consumer_id = insert_consumer(self.db_connection, consumer_data)

        if self.consumer_id:
            print(f"Registered as {name} (ConsumerID: {self.consumer_id})")
            self.open_product_preference_screen()
        else:
            messagebox.showerror("Error", "Registration failed. Please try again.")

    def open_product_preference_screen(self):
        self.root.withdraw()  # Hide the login/registration screen
        from app.views.product_preference import ProductPreferenceScreen 
        product_preference_window = tk.Toplevel()  # Create a new window
        product_preference_app = ProductPreferenceScreen(product_preference_window, self.db_connection, self.consumer_id)

    def close(self):
        if self.db_connection:
            self.db_connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsumerLoginRegistrationScreen(root) 
    root.mainloop()
