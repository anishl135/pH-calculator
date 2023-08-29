import tkinter as tk
from tkinter import ttk
import math


class BiochemistryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biochemistry Tool")

        # Create a tabbed interface
        self.tabControl = ttk.Notebook(root)
        self.tab_pH = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_pH, text="pH Calculator")
        self.tabControl.pack(expand=1, fill="both")

        # Create pH calculator components
        self.label_input = tk.Label(self.tab_pH, text="Enter H+ Concentration (mol/L):")
        self.label_input.pack(pady=10)

        self.entry_concentration = tk.Entry(self.tab_pH)
        self.entry_concentration.pack()

        self.calculate_button = tk.Button(self.tab_pH, text="Calculate pH", command=self.calculate_pH)
        self.calculate_button.pack(pady=10)

        self.clear_button = tk.Button(self.tab_pH, text="Clear", command=self.clear_fields)
        self.clear_button.pack()

        self.result_label = tk.Label(self.tab_pH, text="")
        self.result_label.pack()

    def calculate_pH(self):
        try:
            concentration = float(self.entry_concentration.get())
            pH = -math.log(concentration,10)
            self.result_label.config(text=f"pH: {pH:.2f}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a numeric concentration.")

    def clear_fields(self):
        self.entry_concentration.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = BiochemistryApp(root)
    root.mainloop()
