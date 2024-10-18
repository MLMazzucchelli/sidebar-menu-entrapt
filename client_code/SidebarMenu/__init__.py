from ._anvil_designer import SidebarMenuTemplate
from anvil import *
import anvil.js

class SidebarMenu(SidebarMenuTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        #print(self.main_form)

        # register items
        self.menu_items = {
            "home": {"link": self.link_home, "type": "item"},
            "performance": {"link": self.link_performance, "type": "item"},
            "indexing": {"link": self.link_indexing, "type": "group"},
            "pages": {"link": self.link_pages, "type": "group-item"},
            "video": {"link": self.link_video, "type": "group-item"},
            "experience": {"link": self.link_experience, "type": "group"},
            "core_web": {"link": self.link_core_web, "type": "group-item"},
            "page_experience": {"link": self.link_page_experience, "type": "group-item"},
            "links": {"link": self.link_links, "type": "item"},
            "settings": {"link": self.link_settings, "type": "item"}
        }

        # apply basic styles
        for menu_item in self.menu_items:
            item = self.menu_items[menu_item]
            dom_item = anvil.js.get_dom_node(item["link"])
            dom_item.style.borderRadius = "0 100px 100px 0"
            dom_item.style.margin = "0 -16px"
            dom_item.style.marginRight = "1px";

            if item["type"] == "group-item":
                dom_item.style.paddingLeft = "25px"

        self.first_load = True
        self.set_selected("home")

    def set_selected(self, id_string):
        for i in self.menu_items:
            self.menu_items[i]["link"].role = None

        self.menu_items[id_string]["link"].role = "selected"

        self.selected_item = id_string

        if self.first_load == False:
            self.raise_event('clicked', clicked_item=id_string)
        else:
            self.first_load = False
        


    def link_home_click(self, **event_args):
        self.set_selected("home")
        #open_form('Home')

    def link_performance_click(self, **event_args):
        self.set_selected("performance")

    def link_indexing_click(self, **event_args):
        if self.link_indexing.icon == "fa:angle-right":
            self.link_indexing.icon = "fa:angle-down"
            self.link_pages.visible = True
            self.link_video.visible = True
        else:
            self.link_indexing.icon = "fa:angle-right"
            self.link_pages.visible = False
            self.link_video.visible = False
            
    def link_pages_click(self, **event_args):
        self.set_selected("pages")

    def link_video_click(self, **event_args):
        self.set_selected("video")
        #open_form('Video')

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
