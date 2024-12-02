"""The general structure of the user interface is defined here.

Variables:
    screen_height: int
    screen_width: int

Classes:
    PageBase: Each page must inherit from this class. It gives structure.
    It is also the base to connect to the main application.
    MainApp: All pages are attached to this class. It organizes transitions between pages,
    provides consistentcy and controlls the aplication itself.
"""
import customtkinter as ctk  # type: ignore


screen_height: int = 800
screen_width: int = 600

class PageBase(ctk.CTkFrame):
    """PageBase is the parent class of all subpages. 
    The class itself inherits from CTkFrame meaning every subclass of
    PageBase is a Frame to. The subclasses should work as normal windows
    controlled by the main application.

    Parameters:
        controller (ctk.CTk): The main application to control the pages
    
    Example:
    >>> class PageOne(PageBase):
    >>>     def setup(self):
    >>>         # Create the GUI
    >>>         label = ctk.CTkLabel(self, text="Seite 1", font=("Arial", 20))
    >>>         label.pack(pady=10)
    """
    def __init__(self, parent: ctk.CTk, controller: ctk.CTk):
        """Initizing an new subpage. The Function sets the parent end the controler of each page

        Args:
            parent (ctk.CTk): The window, containing the page
            controller (ctk.CTk): The application to control the pages and switch between
        """
        super().__init__(parent)  # type: ignore
        self.controller = controller
        self.configure(height=screen_height, width=screen_width)  # type: ignore

class MainApp(ctk.CTk):
    """MainApp is the main application to control the pages and switch between them.

    Parameters:
        title (str): The title of the application
        size (str): The size of the application
        It it is ot set it is created by default variables in a f-string
    """
    def __init__(self, title: str = "Main Application",
                 size: str = f"{screen_width}x{screen_height}"):
        super().__init__()  # type: ignore
        self.title(title)
        self.geometry(size)
