import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class FarmerDashboardScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Farmer Dashboard")
        self.root.geometry("1000x800")  # Set the window size
        self.root.configure(bg="white") 

        # Create a label for the title
        title_label = tk.Label(root, text="Farmer Dashboard", font=("Helvetica", 20, "bold"), bg="white")
        title_label.pack(pady=10)

        # Create a frame for recommendations
        recommendations_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")
        recommendations_frame.pack(fill="both", expand=True)

        # Create a label for recommendations
        recommendations_label = tk.Label(recommendations_frame, text="Most Preferred Products", font=("Helvetica", 16, "bold"), bg="white")
        recommendations_label.pack(pady=10)

        # Display recommendations using Text widget
        recommendations_text = tk.Text(recommendations_frame, height=6, width=50)
        recommendations_text.pack()

        # Simulate recommendations data
        recommendations_data = "1. Rice\n2. Wheate\n3. Cotton\n4. Tea"
        recommendations_text.insert(tk.END, recommendations_data)

        # Create a frame for analytics
        analytics_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")
        analytics_frame.pack(side="right", fill="both", expand=True)

        # Create analytics charts (using matplotlib)
        self.plot_analytics(analytics_frame)

        # Create a frame for navigation
        navigation_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")  # Add a border
        navigation_frame.pack(side="bottom", fill="both", expand=True)

        # Create navigation buttons
        reports_button = tk.Button(navigation_frame, text="View Reports", command=self.view_reports, bg="lightblue")
        reports_button.pack(pady=10)

        visualizations_button = tk.Button(navigation_frame, text="View Visualizations", command=self.view_visualizations, bg="lightgreen")
        visualizations_button.pack(pady=10)

        exit_button = tk.Button(navigation_frame, text="Exit", command=self.close, bg="salmon")
        exit_button.pack(pady=10)

    def plot_analytics(self, frame):
        # Simulate analytics data
        locations = ["Location A", "Location B", "Location C", "Location D"]
        age_groups = ["18-25", "26-35", "36-50", "50+"]
        production_data = np.random.randint(10, 100, size=(len(locations), len(age_groups)))

        # Plot analytics data using matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))
        im = ax.imshow(production_data, cmap="Blues")

        # Customize the plot
        ax.set_xticks(np.arange(len(age_groups)))
        ax.set_yticks(np.arange(len(locations)))
        ax.set_xticklabels(age_groups)
        ax.set_yticklabels(locations)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        # Add colorbar
        cbar = ax.figure.colorbar(im, ax=ax)

        # Display the plot on the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def view_reports(self):
        # You can implement the logic to navigate to the Farmer Report Screen here
        pass

    def view_visualizations(self):
        # You can implement the logic to navigate to the Farmer Visualization Screen here
        pass

    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FarmerDashboardScreen(root)
    root.mainloop()
