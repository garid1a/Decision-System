import tkinter as tk
from tkinter import messagebox
from app.auth.consumers import ConsumerLoginRegistrationScreen
from app.auth.farmers import FarmerLoginRegistrationScreen

class LandingPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Landing Page")
        self.root.geometry("800x400")  # Set the window size

        # Create a label for the title
        title_label = tk.Label(root, text="Consumer-Farmer Decision Support System", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=20)

        # Create a label for user type selection
        user_type_label = tk.Label(root, text="Select User Type:", font=("Helvetica", 14))
        user_type_label.pack()

        # Create radio buttons for user type selection
        user_type = tk.StringVar()
        consumer_radio = tk.Radiobutton(root, text="Consumer", variable=user_type, value="Consumer", font=("Helvetica", 12))
        farmer_radio = tk.Radiobutton(root, text="Farmer", variable=user_type, value="Farmer", font=("Helvetica", 12))
        consumer_radio.pack()
        farmer_radio.pack()

        # Create a Proceed button
        proceed_button = tk.Button(root, text="Proceed", command=lambda: self.proceed(user_type.get()), font=("Helvetica", 14), bg="white", fg="black")
        proceed_button.pack(pady=20)

    def proceed(self, user_type):
        if user_type == "Consumer":
            self.open_consumer_login_registration()
        elif user_type == "Farmer":
            self.open_farmer_login_registration()
        else:
            messagebox.showerror("Error", "Please select a user type.")

    def open_consumer_login_registration(self):
        self.root.withdraw()  # Hide the login/registration screen
        dashboard_window = tk.Toplevel()  # Create a new window
        consumer_app = ConsumerLoginRegistrationScreen(dashboard_window)

    def open_farmer_login_registration(self):
        self.root.withdraw()  # Hide the login/registration screen
        dashboard_window = tk.Toplevel()  # Create a new window
        farmer_app = FarmerLoginRegistrationScreen(dashboard_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = LandingPage(root)
    root.mainloop()
