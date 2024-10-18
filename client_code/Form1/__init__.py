from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

        self.selected = 0
        self.sidebar_items = {
            "home": {"link": self.link_home, "selected_role": "selected", "not_selected_role": None},
            "performance": {"link": self.link_performance, "selected_role": "selected", "not_selected_role": None},
            "pages": {"link": self.link_pages, "selected_role": ["selected", "padding-left"], "not_selected_role": ["padding-left"]},
            "video": {"link": self.link_video, "selected_role": ["selected", "padding-left"], "not_selected_role": ["padding-left"]},
            "page_experience": {"link": self.link_page_experience, "selected_role": ["selected", "padding-left"], "not_selected_role": ["padding-left"]},
            "core_web": {"link": self.link_core_web, "selected_role": ["selected", "padding-left"], "not_selected_role": ["padding-left"]},
            "links": {"link": self.link_links, "selected_role": "selected", "not_selected_role": None},
            "settings": {"link": self.link_settings, "selected_role": "selected", "not_selected_role": None}
        }

        self.set_selected("home")

        self.link_indexing.role = ["submenu-group-item"]
        self.link_experience.role = ["submenu-group-item"]
        

    def set_selected(self, id_string):
        for i in self.sidebar_items:
            self.sidebar_items[i]["link"].role = self.sidebar_items[i]["not_selected_role"]

        self.sidebar_items[id_string]["link"].role = self.sidebar_items[id_string]["selected_role"]

    def link_indexing_click(self, **event_args):
        if self.link_indexing.icon == "fa:angle-right":
            self.link_indexing.icon = "fa:angle-down"
            self.link_pages.visible = True
            self.link_video.visible = True
        else:
            self.link_indexing.icon = "fa:angle-right"
            self.link_pages.visible = False
            self.link_video.visible = False

    def link_home_click(self, **event_args):
        self.set_selected("home")

    def link_performance_click(self, **event_args):
        self.set_selected("performance")

    def link_pages_click(self, **event_args):
        self.set_selected("pages")

    def link_video_click(self, **event_args):
        self.set_selected("video")

    def link_experience_click(self, **event_args):
        if self.link_experience.icon == "fa:angle-right":
            self.link_experience.icon = "fa:angle-down"
            self.link_page_experience.visible = True
            self.link_core_web.visible = True
        else:
            self.link_experience.icon = "fa:angle-right"
            self.link_page_experience.visible = False
            self.link_core_web.visible = False

    def link_page_experience_click(self, **event_args):
        self.set_selected("page_experience")

    def link_core_web_click(self, **event_args):
        self.set_selected("core_web")

    def link_links_click(self, **event_args):
        self.set_selected("links")

    def link_settings_click(self, **event_args):
        self.set_selected("settings")
