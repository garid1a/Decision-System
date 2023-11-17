import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

class MainLayout:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#12DB81")
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Lato")

        # Load and set background image
        image_path = "C:/BIS608/FarmChoice/Decision-System/app/static/background.jpg"  # Replace with your image path
        try:
            self.background_image = Image.open(image_path)
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.background_label = ttk.Label(self.root, image=self.background_photo)
            self.background_label.place(relwidth=1, relheight=1)
            print('Image Loaded')
        except Exception as e:
            print(f"Error loading the background image: {e}")

        # Create footer
        self.create_footer()

    def create_footer(self):
        footer_frame = ttk.Frame(self.root, style="TFrame")

        # Add white text to the footer
        footer_label = ttk.Label(footer_frame, text="© 2023 FarmChoice. All rights reserved.", foreground="white",
                                 background="#12DB81")
        footer_label.pack(pady=5)

        # Configure a style for the footer components with a #12DB81 background
        style = ttk.Style()
        style.configure("TFrame", background="#12DB81")
        # style.configure("TLabel", background="green")

        footer_frame.pack(side="bottom", fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainLayout(root)
    root.mainloop()
