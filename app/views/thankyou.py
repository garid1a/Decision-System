import tkinter as tk

class ThankYouScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Thank You")
        self.root.geometry("800x400") 
        
        # Create a label for the thank-you message
        thank_you_label = tk.Label(root, text="Thank you for submitting your product preferences!", font=("Helvetica", 16))
        thank_you_label.pack(pady=10)

        # Create a button to return to the Product Preference Screen
        return_button = tk.Button(root, text="Return to Product Preferences", command=self.return_to_product_preferences)
        return_button.pack(pady=10)

    def return_to_product_preferences(self):
        # You can implement logic here to go back to the Product Preference Screen
        self.root.destroy()  # Close the Thank You Screen

if __name__ == "__main__":
    root = tk.Tk()
    app = ThankYouScreen(root)
    root.mainloop()
