import tkinter as tk
from user_interface.main_window import MoodBoardApp  # Assuming all the functionalities are bundled within this class


def main():
    root = tk.Tk()  # Initialize the main Tkinter window
    root.geometry("800x600")  # Setting an initial size for the window

    app = MoodBoardApp(root)  # Instantiate our main application

    root.mainloop()  # Start the Tkinter event loop


if __name__ == "__main__":
    main()
