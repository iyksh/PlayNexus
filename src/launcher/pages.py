import customtkinter as ctk

from PIL import Image
from .utils import *
from .backend.backend import *
from functools import partial


SIDE_BAR_COLOR = "#2a2a2a"

class Pages:
    def __init__(self, main_view: ctk.CTkFrame) -> None:
        """Initialize Pages with a main view and frame management."""
        self.main_view = main_view
        self.frames = {}
    
    def home_page(self) -> None:
        """Return to the home page."""
        if "home_page" not in self.frames:
            home_frame = ctk.CTkScrollableFrame(master=self.main_view)
            home_frame.pack(fill="both", expand=True)
            self.frames["home_page"] = home_frame

            content_frame = ctk.CTkFrame(master=home_frame, fg_color="transparent")
            content_frame.pack(anchor="n", fill="both", padx=24, pady=24)

            self.create_search_bar(content_frame, " Search in store")
            self.create_labels_and_content(content_frame,"Recently added")
        else:
            self.frames["home_page"].pack(fill="both", expand=True)

    def library_page(self) -> None:
        """Show the user's library."""
        if "library_page" not in self.frames:
            library_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            library_frame.pack(fill="both", expand=True)
            self.frames["library_page"] = library_frame

            content_frame = ctk.CTkFrame(master=library_frame, fg_color="transparent")
            content_frame.pack(anchor="n", fill="x", padx=24, pady=24)

            self.create_search_bar(content_frame, " Search in library")
            self.create_labels_and_content(content_frame,"Last played")
        else:
            self.frames["library_page"].pack(fill="both", expand=True)

    def create_search_bar(self, master: ctk.CTkFrame, placeholder) -> None:
        """Create the first line of the main view with a search bar and a button."""
        first_line = ctk.CTkFrame(master=master, fg_color="transparent")
        first_line.pack(anchor="n", fill="x")

        search_entry = ctk.CTkEntry(master=first_line, height=30,
                                    font=("Roboto", 12), placeholder_text=placeholder)
        search_entry.pack(side="left", fill="x", expand=True)

        icon = load_image("search-md.png")
        icon = ctk.CTkImage(dark_image=icon, light_image=icon, size=(16, 16))

        search_button = ctk.CTkButton(master=first_line, height=30, text="Search", text_color="#ffffff",
                                      width=112, command=search_in_store, compound="left", image=icon)
        search_button.pack(anchor="w", padx=(8, 0), side="right")

    def create_labels_and_content(self, master: ctk.CTkFrame, header) -> None:
        """Create labels and content sections."""
        ctk.CTkLabel(master=master, text=header, text_color="#ffffff", anchor="w", justify="left",
                     font=("Roboto Bold", 24)).pack(anchor="w", pady=(30, 10))

        recently_added_frame = ctk.CTkFrame(master, fg_color="transparent")
        recently_added_frame.pack(fill="x", pady=(10, 0))
        self.show_games(recently_added_frame)

        ctk.CTkLabel(master=master, text_color=SIDE_BAR_COLOR,
                     text="__________________________________________________________________________________________",
                     fg_color="transparent").pack(fill="x", pady=(20, 0))

        # Tabs:
        tabs = ["Popular", "New", "Upcoming", "All"]

        tabs_frame = ctk.CTkFrame(master, fg_color="transparent")
        tabs_frame.pack(fill="x", pady=(10, 0))

        for tab in tabs:
            ctk.CTkButton(master=tabs_frame, text=tab, fg_color="transparent", text_color="#ffffff",
                          font=("Roboto", 24), hover_color=SIDE_BAR_COLOR).pack(side="left", padx=10)

        self.show_games(tabs_frame)

    def show_games(self, master: ctk.CTkFrame) -> None: # This function is temporary
        """Display game cards in the provided frame."""
        for _ in range(5):
            game_frame = ctk.CTkFrame(master, corner_radius=10, fg_color="#1a1a1a", width=150, height=200)
            game_frame.pack(side="left", padx=10, pady=10)

            game_img_data = load_image("secondary-logo-colored.png")
            game_img = ctk.CTkImage(dark_image=game_img_data, light_image=game_img_data, size=(150, 150))
            ctk.CTkLabel(master=game_frame, image=game_img, text="").pack()

            ctk.CTkLabel(master=game_frame, text="Game Title", text_color="#ffffff", anchor="w", justify="left",
                         font=("Roboto Bold", 12)).pack(anchor="w", pady=(8, 0))

            ctk.CTkLabel(master=game_frame, text="Publisher Name", text_color="#b3b3b3", anchor="w", justify="left",
                         font=("Roboto Bold", 12)).pack(anchor="w")

            ctk.CTkLabel(master=game_frame, text="Price", text_color="#ffffff", anchor="w", justify="left",
                         font=("Roboto Bold", 12)).pack(anchor="w")

    def create_main_view(self) -> None:
        """Create the main view frame with the title and content."""
        self.main_view = ctk.CTkFrame(master=self.app, width=680, height=650, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.show_frame(self.home_page)