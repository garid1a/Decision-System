import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from app.views.layout import Layout 
from tkinter import font

class LandingPage:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Landing Page")
        self.root.geometry("1200x600")  # Set the window size
        self.root.configure(bg="white")  

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Roboto")
        # Reuse the common header and footer
        Layout(root)

        landing_frame = tk.Frame(root)  # Add a border
        landing_frame.pack(fill="both", expand=True, side="top")

        background_color = "white"
        landing_frame.configure(bg=background_color)

        # Create a label for the title
        title_label = tk.Label(landing_frame, text="Welcome to the Consumer-Farmer Decision Support System", font=(default_font, 20, "bold"), bg="white")
        title_label.pack(pady=20)

        # Create a label for user type selection
        user_type_label = tk.Label(landing_frame, text="Please choose your user type:", font=(default_font, 14), bg="white")
        user_type_label.pack()

        # Create radio buttons for user type selection
        user_type = tk.StringVar()
        consumer_radio = tk.Radiobutton(landing_frame, text="I am a Consumer", variable=user_type, value="Consumer", font=(default_font, 12), bg="white")
        farmer_radio = tk.Radiobutton(landing_frame, text="I am a Farmer", variable=user_type, value="Farmer", font=(default_font, 12), bg="white")
        consumer_radio.pack()
        farmer_radio.pack()

        user_info_label = tk.Label(landing_frame, text='Click the "Proceed" button when you are ready.', font=(default_font, 10), bg="white")
        user_info_label.pack(pady=10)

        # Create a Proceed button
        proceed_button = tk.Button(landing_frame, text="Proceed", command=lambda: self.proceed(user_type.get()), bg="#12DB81", fg="white",
                                    bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                    cursor="hand2", font=(default_font, 12))
        proceed_button.pack(pady=20)

    def proceed(self, user_type):
        print(self, user_type)
        if user_type == "Consumer":
            self.open_consumer_login_registration()
        elif user_type == "Farmer":
            self.open_farmer_login_registration()
        else:
            messagebox.showerror("Error", "Please select a user type.")

    def open_consumer_login_registration(self):
        self.root.withdraw()  # Hide the login/registration screen
        from app.auth.consumers import ConsumerLoginRegistrationScreen
        dashboard_window = tk.Toplevel()  # Create a new window
        consumer_app = ConsumerLoginRegistrationScreen(dashboard_window, self.show_landing_page)

    def open_farmer_login_registration(self):
        self.root.withdraw()  # Hide the login/registration screen
        from app.auth.farmers import FarmerLoginRegistrationScreen
        dashboard_window = tk.Toplevel()  # Create a new window
        farmer_app = FarmerLoginRegistrationScreen(dashboard_window,  self.show_landing_page)
    def show_landing_page(self):
        self.root.deiconify()
if __name__ == "__main__":
    root = tk.Tk()
    app = LandingPage(root)
    root.mainloop()
