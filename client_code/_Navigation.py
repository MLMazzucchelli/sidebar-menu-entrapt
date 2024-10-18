from .Home import Home
from .Video import Video

homeview = {}

def register_Homeview(view):
    global homeview
    homeview = view
    #print(Homeview.content_panel)

#def set_view()