import pandas as pd
import tkinter as tk
from tkinter import ttk

def open_excel_sheet(sheet_name):
    df = pd.read_excel('Questions.xlsx', sheet_name=sheet_name)
    # window = tk.Toplevel(root)
    # window.title(sheet_name)

    # Create a treeview widget to display the data
    # tree = ttk.Treeview(window)

    # # Add columns to the treeview
    # tree["columns"] = tuple(df.columns)
    # for col in df.columns:
    #     tree.column(col, anchor="center", width=100)
    #     tree.heading(col, text=col, anchor="center")

    # # Insert data into the treeview
    # for index, row in df.iterrows():
    #     tree.insert("", index, values=tuple(row))

    # # Pack the treeview
    # tree.pack(expand=True, fill="both")
    
    print(df)
    # print(df.loc[2])

# Create the main Tkinter window
root = tk.Tk()
root.title("Excel Viewer")

# Create a button to open sheet w2
button_w2 = tk.Button(root, text="Open Sheet w2", command=lambda: open_excel_sheet(0))
button_w2.pack(pady=10)

# Add more buttons for other sheets if needed

# Start the Tkinter event loop
root.mainloop()
