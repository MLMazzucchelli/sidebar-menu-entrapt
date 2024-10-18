from ._anvil_designer import MAINTemplate
from anvil import *
from .. import _Navigation

class MAIN(MAINTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

        _Navigation.register_Homeview(self)
        print("MAIN LOADED")

    def sidebar_menu_1_clicked(self, clicked_item, **event_args):
        print(clicked_item)

        print(self.sidebar_menu_1.selected_item)


