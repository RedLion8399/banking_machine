""" Here is the place, were all GUI components comes together.
All subpages are imported and attached to the main application
so that the main class can control them and swich between these different frames.

Variables:
    screen_height: int
    screen_width: int

Functions:
    run_user_interface: Builds the main application, sets parameters and starts it
"""
import customtkinter as ctk  # type: ignore
from basic_interface import MainApp


def run_user_interface() -> None:
    """Builds the main application, sets parameters and starts it"""
    ctk.set_appearance_mode("dark")
    app: ctk.CTk = MainApp()
    app.mainloop()  # type: ignore
