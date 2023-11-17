import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import font

class Layout:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#12DB81")
        # self.root.title("My Tkinter App")
        
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Lato")

        # Create header
        self.create_header()

        # Create content frame
        self.content_frame = ttk.Frame(root)
        self.content_frame.pack(fill='both', expand=True)

        # Create footer
        self.create_footer()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#12DB81")

        # Add image to header using PIL
        image_path = "C:/BIS608/FarmChoice/Decision-System/app/static/background.jpg"  # Replace with your image path
        original_image = Image.open(image_path)

        # Set the desired height and width for the header
        desired_height = 250
        screen_width = self.root.winfo_screenwidth()
        new_width = screen_width  # Set the width to the screen width

        # Resize the image to the desired dimensions
        resized_image = original_image.resize((new_width, desired_height))
        photo = ImageTk.PhotoImage(resized_image)

        header_label = tk.Label(header_frame, image=photo, bg="#12DB81")
        header_label.image = photo
        header_label.pack()

        # Add white text to the header
        header_text = tk.Label(header_frame, text="FarmChoice", font=("Helvetica", 18), fg="white", bg="#12DB81")
        header_text.pack()

        header_frame.pack(side="top", fill="x")

    def create_footer(self):
        footer_frame = ttk.Frame(self.root, style="TFrame")  

        # Add white text to the footer
        footer_label = ttk.Label(footer_frame, text="© 2023 FarmChoice. All rights reserved.", foreground="white", background="#12DB81")
        footer_label.pack(pady=5)
         # Configure a style for the footer components with a #12DB81 background
        style = ttk.Style()
        style.configure("TFrame", background="#12DB81")
        # style.configure("TLabel", background="green")


        footer_frame.pack(side="bottom", fill="x")

if __name__ == "__main__":
    root = tk.Tk()

   
    app = Layout(root)
    root.mainloop()
