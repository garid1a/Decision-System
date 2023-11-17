import tkinter as tk

from app.auth.landing import LandingPage
from app.views.layout import Layout 
from tkinter import font

class ThankYouScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Thank You")
        self.root.geometry("1200x600") 
        self.root.configure(bg="white") 

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Roboto")
        # Reuse the common header and footer
        Layout(root)

        # Create a label for the thank-you message
        thank_you_label = tk.Label(root, text="Thanks for sharing your crop/product preferences!", font=(default_font, 16), fg="white", background="#12DB81")
        thank_you_label.pack(pady=10)

        # Create a button to return to the Product Preference Screen
        return_button = tk.Button(root, text="Back to Home", command=self.return_to_product_preferences, bg="#12DB81", fg="white", bd=0,
                                 relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0, cursor="hand2",
                                 font=(default_font, 12))
        return_button.pack(pady=10)

    def return_to_product_preferences(self):
        # You can implement logic here to go back to the Product Preference Screen
        self.root.withdraw()  # Close the Thank You Screen
        Landing_window = tk.Toplevel()  # Create a new window
        landing_app = LandingPage(Landing_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = ThankYouScreen(root)
    root.mainloop()
