from tkinter import *
from tkinter import ttk
import analysis as an

class Homepage:
    def __init__(self, root):
        # Create the main GUI
        root.title("Wildfire Analysis")

        # style = ttk.Style(root)
        # style.theme_use('clam')

        # Create a frame to hold the map
        mainframe = ttk.Frame(root, padding = "3 3 3 3")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # create an image using a PhotoImage object
        
        self.file_name = an.download_map()
        self.img = PhotoImage(file=self.file_name)

        # add a label and set the image to the photo image object
        self.image_label = ttk.Label(mainframe, image=self.img)
        self.image_label.image = self.img


        # add the Label with the image to the GUI
        self.image_label.grid(column=0, row=0, sticky=(W, E), columnspan=4)

        # Create buttons at the bottom
        self.button_frame = ttk.Frame(root)
        self.button_frame.grid(row=2, column=0, pady=10)

        self.open_button = ttk.Button(self.button_frame, text="Open Second GUI", command=self.open_second_gui)
        self.open_button.grid(row=1, column=0, padx=5)

        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=root.destroy)
        self.exit_button.grid(row=1, column=1, padx=5)


    def open_second_gui(self):
        second_gui = Toplevel(root)
        second_gui.title("Second GUI")
        second_gui.geometry("400x300")

        label = ttk.Label(second_gui, text="This is the second GUI.")
        label.pack(padx=20, pady=20)

root = Tk()
Homepage(root)
root.mainloop()
