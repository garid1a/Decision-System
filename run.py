import tkinter as tk
from backend.app import App

def main():
    root = tk.Tk()
    user_type = "consumer"  # Replace with actual user type (consumer/farmer)
    # user_type = "farmer"  # Replace with actual user type (consumer/farmer)
    app = App(root, user_type)
    root.mainloop()

if __name__ == "__main__":
    main()
