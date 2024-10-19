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
            "entrapment": {"link": self.link_calculate_entrapment, "type": "item"},
            "project": {"link": self.link_project, "type": "group"},
            "view_analyses": {"link": self.link_view_analyses, "type": "group-item"},
            "new_project": {"link": self.link_new_project, "type": "group-item"},
            "upload_project": {"link": self.link_upload_project, "type": "group-item"},
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

    def set_selected(self, id_string, file = []):
        for i in self.menu_items:
            self.menu_items[i]["link"].role = None

        self.menu_items[id_string]["link"].role = "selected"

        self.selected_item = id_string

        if not self.first_load:
            self.raise_event('clicked', clicked_item=id_string, file = file)
        else:
            self.first_load = False

      

    def unselect(self):
        for i in self.menu_items:
            self.menu_items[i]["link"].role = None
        


    def link_home_click(self, **event_args):
        self.set_selected("home")
        #open_form('Home')

    def link_calculate_entrapment_click(self, **event_args):
        self.set_selected("entrapment")

    def link_project_click(self, **event_args):
        if self.link_project.icon == "fa:angle-right":
            self.link_project.icon = "fa:angle-down"
            self.link_view_analyses.visible    = True
            self.link_new_project.visible      = True
            self.link_upload_project.visible   = True
        else:
            self.link_project.icon = "fa:angle-right"
            self.link_view_analyses.visible = False
            self.link_new_project.visible = False
            self.link_upload_project.visible   = False
            
    def link_view_analyses_click(self, **event_args):
        self.set_selected("view_analyses")

    def link_new_project_click(self, **event_args):
        self.set_selected("new_project")
        self.unselect()
        self.set_selected("view_analyses")


    def link_settings_click(self, **event_args):
         self.set_selected("settings")
         self.unselect()

    def link_upload_project_change(self, file, **event_args):
      self.set_selected("upload_project", file)
      self.link_upload_project.clear()
      self.unselect()
      self.set_selected("view_analyses")
     


