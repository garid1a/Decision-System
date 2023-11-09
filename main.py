import tkinter as tk
from app.auth.landing import LandingPage

if __name__ == "__main__":
    root = tk.Tk()
    app = LandingPage(root)
    root.mainloop() 