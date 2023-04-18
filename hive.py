# pylint: disable=missing-module-docstring

import customtkinter as ctk

from core import *  # pylint: disable=unused-wildcard-import,wildcard-import

class App(ctk.CTk):
    # pylint: disable=missing-class-docstring
    def __init__(self):
        """
        Main app class that contains all the widgets and logic. To run, simply create an instance of the
        class and call the ".mainloop()" method on the instance.
        """

        # window setup
        super().__init__()
        self.title("hive")
        self.iconbitmap("./src/icon.ico")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)
        ctk.set_appearance_mode("system")

        # layout
        self.columnconfigure((0, 1), weight = 0)
        self.rowconfigure((0, 1), weight = 0)

        # widgets
        self.appearance_selector = AppearanceSelector(self)
        self.appearance_selector.grid(row = 1, column = 0, padx = PADX, pady = PADY)

        self.appearance_label = AppearanceLabel(self)
        self.appearance_label.grid(row = 0, column = 0, padx = PADX, pady = PADY)

class SystemFilesLabel(ctk.CTkLabel):  # pylint: disable=too-many-ancestors
    # pylint: disable=missing-class-docstring
    def __init__(self, master: ctk.CTk):
        """
        Widget that explains what the checkbox below it is for/does.
        """

        # widget setup
        super().__init__(master = master,
                         text = "Display system files"
                         )

class SystemFilesBox(ctk.CTkCheckBox):  # pylint: disable=too-many-ancestors
    # pylint: disable=missing-class-docstring
    def __init__(self, master: ctk.CTk):
        """
        Widget that allows the user to toggle the visibility of system files.
        """

        # widget setup
        super().__init__(master = master)

class AppearanceLabel(ctk.CTkLabel):  # pylint: disable=too-many-ancestors
    # pylint: disable=missing-class-docstring
    def __init__(self, master: ctk.CTk):
        """
        Widget that explains what the menu below it is for/does.
        """

        # widget setup
        super().__init__(master = master,
                         text = "Appearance"
                         )

class AppearanceSelector(ctk.CTkOptionMenu):  # pylint: disable=too-many-ancestors
    # pylint: disable=missing-class-docstring
    def __init__(self, master: ctk.CTk):
        """
        Widget that allows the user to select a theme from light, dark, or system default.
        """

        # widget setup
        self.values = ["System", "Light", "Dark"]
        super().__init__(master = master,
                         values = self.values,
                         command = self.change_appearance,
                         )

    def change_appearance(self, new_appearance: str):
        """
        Changes the appearance/theme of the app.

        Args:
            new_appearance (str): The new appearance/theme. Either "system", "light", or "dark".
        """
        ctk.set_appearance_mode(new_appearance)

# create and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
