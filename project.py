import tkinter as tk
from tkinter import ttk

def open_second_gui():
    second_gui = tk.Toplevel(root)
    second_gui.title("Second GUI")
    second_gui.geometry("400x300")

    label = ttk.Label(second_gui, text="This is the second GUI.")
    label.pack(padx=20, pady=20)

# Create the main GUI
root = tk.Tk()
root.title("Main GUI")

# Create a frame to hold the map
map_frame = ttk.Frame(root, width=400, height=300, relief="solid", borderwidth=2)
map_frame.grid(row=0, column=0, padx=10, pady=10)

# Create buttons at the bottom
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=0, pady=10)

open_button = ttk.Button(button_frame, text="Open Second GUI", command=open_second_gui)
open_button.grid(row=0, column=0, padx=5)

exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.grid(row=0, column=1, padx=5)

root.mainloop()
