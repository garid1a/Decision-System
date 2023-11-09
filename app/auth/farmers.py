import tkinter as tk
from tkinter import messagebox
from app.views.dashboard import FarmerDashboardScreen
from data.db_connection import create_db_connection
from data.db_controller import login_farmer, insert_farmer

class FarmerLoginRegistrationScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Farmer Login/Registration")
        self.root.geometry("800x400")  # Set the window size

        # Create a frame for login
        login_frame = tk.Frame(root, bd=2, relief="ridge")  # Add a border
        login_frame.pack(side="left", fill="both", expand=True)

        # Create a frame for registration
        registration_frame = tk.Frame(root, bd=2, relief="ridge")  # Add a border
        registration_frame.pack(side="left", fill="both", expand=True)

        # Set Background Color
        background_color = "light gray"
        login_frame.configure(bg=background_color)
        registration_frame.configure(bg=background_color)

        # Create a label for the title
        title_label = tk.Label(login_frame, text="Farmer Login", font=("Helvetica", 16), bg=background_color)
        title_label.pack(pady=10)

        # Create a label and entry for username
        self.username_label = tk.Label(login_frame, text="Username:", bg=background_color)
        self.username_label.pack()
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.pack()

        # Create a label and entry for password
        self.password_label = tk.Label(login_frame, text="Password:", bg=background_color)
        self.password_label.pack()
        self.password_entry = tk.Entry(login_frame, show='*')
        self.password_entry.pack()

        # Create a login button
        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.pack(pady=10)

        # Create a label for the title
        title_label = tk.Label(registration_frame, text="Farmer Registration", font=("Helvetica", 16), bg=background_color)
        title_label.pack(pady=10)

        # Create a label and entry for name
        self.name_label = tk.Label(registration_frame, text="Name:", bg=background_color)
        self.name_label.pack()
        self.name_entry = tk.Entry(registration_frame)
        self.name_entry.pack()

        # Create a label and entry for location
        self.location_label = tk.Label(registration_frame, text="Location:", bg=background_color)
        self.location_label.pack()
        self.location_entry = tk.Entry(registration_frame)
        self.location_entry.pack()

        # Create a label and entry for soil_type
        self.soil_type_label = tk.Label(registration_frame, text="Soil Type:", bg=background_color)
        self.soil_type_label.pack()
        self.soil_type_entry = tk.Entry(registration_frame)
        self.soil_type_entry.pack()

        # Create a register button
        register_button = tk.Button(registration_frame, text="Register", command=self.register)
        register_button.pack(pady=10)

        # Connect to Database
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        farmer = login_farmer(self.db_connection, username, password)

        if farmer:
            self.open_dashboard()
        else:
            print('Login failed: Invalid username or password')
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        soil_type = self.soil_type_entry.get()
        if not name or not location or not soil_type:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        farmer_data = {
            "Name": name,
            "Location": location,
            "SoilType": soil_type
        }
        farmer_id = insert_farmer(self.db_connection, farmer_data)
        if farmer_id:
            print('SIGNUP')
            farmer = {"FarmerID": farmer_id, "Name": name, "Location": location}
            self.open_dashboard()
        else:
            print('Registration failed')
            messagebox.showerror("Registration Failed", "Failed to register farmer")

    def open_dashboard(self):
        self.root.withdraw()  # Hide the login/registration screen
        farmer_window = tk.Toplevel()  # Create a new window
        farmer_app = FarmerDashboardScreen(farmer_window)
        self.close()

    def close(self):
        if self.db_connection:
            self.db_connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = FarmerLoginRegistrationScreen(root)
    root.mainloop() 