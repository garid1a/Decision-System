import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import font
from app.views.main_layout import MainLayout
from app.auth.landing import LandingPage
from data.db_controller import get_top_product_preferences, get_preference_count_by_month
from data.db_controller import generate_product_preference_report
from data.db_controller import generate_product_preference_report_by_location
from data.db_controller import generate_product_preference_report_by_month, generate_product_preference_report_by_product
from data.db_connection import create_db_connection
from data.db_controller import generate_product_report

class FarmerDashboardScreen:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection
        self.root.title("Farmer Dashboard")
        self.root.geometry("1200x600")  # Set the window size
        self.root.configure(bg="#12DB81") 

        MainLayout(root)

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Roboto")

        # Create a label for the title
        title_label = tk.Label(root, text="Farmer Dashboard", font=(default_font, 20, "bold"))
        title_label.pack(pady=10)

      # Create a frame for recommendations
        recommendations_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")
        recommendations_frame.pack(fill="both", expand=True)

        # Create a label for recommendations
        recommendations_label = tk.Label(recommendations_frame, text="Most Preferred Products/Crops", font=(default_font, 16, "bold"), bg="white", foreground="#12DB81")
        recommendations_label.pack(side=tk.LEFT, pady=10)

        # Simulate recommendations data
        self.recommendations_data = get_top_product_preferences(self.connection)
        self.recommendations_data_month = get_preference_count_by_month(self.connection)
    
        # Display recommendations using Labels in a row
        for idx, product in enumerate(self.recommendations_data, start=1):
            product_label = tk.Label(recommendations_frame, text=f"{idx}. {product['ProductName']}", font=(default_font, 12), bg="white")
            product_label.pack(side=tk.LEFT, padx=10)
        
        # Create a frame for analytics
        analytics_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")
        analytics_frame.pack(side="right", fill="both", expand=True, )

        # Create analytics charts (using matplotlib)
        self.plot_analytics(analytics_frame)
        self.plot_analytics1(analytics_frame)

       

        # Create a frame for navigation
        navigation_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")  # Add a border
        navigation_frame.pack(side="bottom", fill="both", expand=True)

        # Create navigation buttons
        creports_button = tk.Button(navigation_frame, text="Consumer Report", command=self.view_reports,  bg="#12DB81", fg="white",
                                 bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                 cursor="hand2", font=(default_font, 12), width=20)
        creports_button.pack(pady=5) 
        # Create navigation buttons
        reports_button = tk.Button(navigation_frame, text="Product Report", command=self.preference_reports_by_product,  bg="#12DB81", fg="white",
                                 bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                 cursor="hand2", font=(default_font, 12), width=20)
        reports_button.pack(pady=5) 

        # Create navigation buttons
        preports_button = tk.Button(navigation_frame, text="Preference Report", command=self.preference_reports,  bg="#12DB81", fg="white",
                                 bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                 cursor="hand2", font=(default_font, 12), width=20)
        preports_button.pack(pady=5)

        # Create navigation buttons
        locatio_button = tk.Button(navigation_frame, text="Location Report", command=self.preference_reports_by_location,  bg="#12DB81", fg="white",
                                 bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                 cursor="hand2", font=(default_font, 12), width=20)
        locatio_button.pack(pady=5) 
        # Create navigation buttons
        months_button = tk.Button(navigation_frame, text="Monthly Report", command=self.preference_reports_by_month,  bg="#12DB81", fg="white",
                                 bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                 cursor="hand2", font=(default_font, 12), width=20)
        months_button.pack(pady=5) 

        exit_button = tk.Button(navigation_frame, text="Sign Out", command=self.close, bg="#63E8A6", fg="white",
                                bd=0, relief=tk.GROOVE, padx=20, pady=10, borderwidth=2, highlightthickness=0,
                                cursor="hand2", font=(default_font, 12), width=20)
        exit_button.pack(side=tk.BOTTOM, pady=10, anchor=tk.S)
        

    def plot_analytics(self, frame):
        # Simulate analytics data
        # locations = ["Location A", "Location B", "Location C", "Location D"]
        # age_groups = ["18-25", "26-35", "36-50", "50+"]
        product_names = [entry["ProductName"] for entry in self.recommendations_data]
        preference_counts = [entry["PreferenceCount"] for entry in self.recommendations_data]
 
        # Plot analytics data using matplotlib as a bar graph
        fig, ax = plt.subplots(figsize=(12, 3))
        bar_width = 0.4  # Adjust the width of the bars as needed

        # Create a bar graph
        bars = ax.bar(product_names, preference_counts, width=bar_width, color="orange")

        # Customize the plot
        ax.set_xlabel("Product Names")
        ax.set_ylabel("Preference Counts")
        ax.set_title("Top Product Preferences")

        # Rotate x-axis labels for better readability
        plt.setp(ax.get_xticklabels(), rotation=0, ha="right", rotation_mode="anchor")

        # Add data labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, round(yval, 2), ha='center', va='bottom')

        plt.tight_layout()
        # Display the plot on the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    def plot_analytics1(self, frame):
        # Simulate analytics data
        # locations = ["Location A", "Location B", "Location C", "Location D"]
        # age_groups = ["18-25", "26-35", "36-50", "50+"]
        months = [entry["Month"] for entry in self.recommendations_data_month]
        preference_counts = [entry["PreferenceCount"] for entry in self.recommendations_data_month]
 
        # Plot analytics data using matplotlib as a bar graph
        fig, ax = plt.subplots(figsize=(12, 3))
        bar_width = 0.4  # Adjust the width of the bars as needed

        # Create a bar graph
        bars = ax.bar(months, preference_counts, width=bar_width, color="orange")

        # Customize the plot
        ax.set_xlabel("Months")
        ax.set_ylabel("Preference Counts")
        ax.set_title("Product Preferences - Monthly")

        # Rotate x-axis labels for better readability
        plt.setp(ax.get_xticklabels(), rotation=0, ha="right", rotation_mode="anchor")

        # Add data labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2), ha='center', va='bottom')

        plt.tight_layout()
        # Display the plot on the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def view_reports(self):
        # You can implement the logic to navigate to the Farmer Report Screen here
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")
            
        report = generate_product_preference_report(self.db_connection) 
        print(report)
        messagebox.showinfo("Success", f"Report Downloaded.")

    def preference_reports(self):
        # You can implement the logic to navigate to the Farmer Report Screen here
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")
            
        report = generate_product_report(self.db_connection) 
        print(report)
        messagebox.showinfo("Success", f"Report Downloaded.")

    def preference_reports_by_location(self):
        # You can implement the logic to navigate to the Farmer Report Screen here
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")
            
        report = generate_product_preference_report_by_location(self.db_connection) 
        print(report)
        messagebox.showinfo("Success", f"Location Report Downloaded.")

    def preference_reports_by_month(self):
        # You can implement the logic to navigate to the Farmer Report Screen here
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")
            
        report = generate_product_preference_report_by_month(self.db_connection) 
        print(report)
        messagebox.showinfo("Success", f"Monthly Report Downloaded.")

    def preference_reports_by_product(self):
        # You can implement the logic to navigate to the Farmer Report Screen here
        self.db_connection = create_db_connection()

        if self.db_connection:
            print("Connected to the database")
            
        report = generate_product_preference_report_by_product(self.db_connection) 
        print(report)
        messagebox.showinfo("Success", f"Monthly Report Downloaded.")

    def close(self):
        self.root.withdraw()  # Close the Thank You Screen
        Landing_window = tk.Toplevel()  # Create a new window
        landing_app = LandingPage(Landing_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = FarmerDashboardScreen(root)
    root.mainloop()
