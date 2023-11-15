
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Layout:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter App")

        # Create header
        self.create_header()

        # Create content frame
        self.content_frame = ttk.Frame(root)
        self.content_frame.pack(fill='both', expand=True)

        # Create footer
        self.create_footer()

    def create_header(self):

        header_frame = tk.Frame(self.root)

        # Add image to header using PIL
        image_path = "C:/BIS608/FarmChoice/Decision-System/app/static/background.jpg"  # Replace with your image path
        original_image = Image.open(image_path)

        # Set the desired height and width for the header
        desired_height = 100
        screen_width = self.root.winfo_screenwidth()
        new_width = screen_width  # Set the width to the screen width

        # Resize the image to the desired dimensions
        resized_image = original_image.resize((new_width, desired_height))
        photo = ImageTk.PhotoImage(resized_image)

        header_label = tk.Label(header_frame, image=photo)
        header_label.image = photo
        header_label.pack(pady=10)

        # You can add more header components here

        header_frame.pack(side="top", fill="x")


    def create_footer(self):
        footer_frame = ttk.Frame(self.root)

        # Add footer components
        footer_label = ttk.Label(footer_frame, text="© 2023 My App. All rights reserved.")
        footer_label.pack(pady=5)

        # You can add more footer components here

        footer_frame.pack(side="bottom", fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    app = Layout(root)
    root.mainloop()
