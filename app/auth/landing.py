import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from app.views.layout import Layout 

class LandingPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Landing Page")
        self.root.geometry("800x400")  # Set the window size
        self.root.configure(bg="white") 

        # Load the background image
        # image = Image.open("C:/BIS608/FarmChoice/Decision-System/app/static/background.jpg")  # Replace with the actual path to your image
        # photo = ImageTk.PhotoImage(image)
        # background_label = tk.Label(root, image=photo)
        # background_label.place(relwidth=1, relheight=1)

        # Reuse the common header and footer
        Layout(root) 
        # Create a label for the title
        title_label = tk.Label(root, text="Consumer-Farmer Decision Support System", font=("Helvetica", 24, "bold"), bg="white")
        title_label.pack(pady=20)

        # Create a label for user type selection
        user_type_label = tk.Label(root, text="Select User Type:", font=("Helvetica", 14), bg="white")
        user_type_label.pack()

        # Create radio buttons for user type selection
        user_type = tk.StringVar()
        consumer_radio = tk.Radiobutton(root, text="Consumer", variable=user_type, value="Consumer", font=("Helvetica", 12), bg="white")
        farmer_radio = tk.Radiobutton(root, text="Farmer", variable=user_type, value="Farmer", font=("Helvetica", 12), bg="white")
        consumer_radio.pack()
        farmer_radio.pack()

        # Create a Proceed button
        proceed_button = tk.Button(root, text="Proceed", command=lambda: self.proceed(user_type.get()), font=("Helvetica", 14), bg="white", fg="black")
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
