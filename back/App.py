import os.path

import customtkinter

import main
from front import Gui


def start():
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")
    startgui = Gui.Gui()
    code = startgui.run()

def getProfileLocation():
    apppath = os.getcwd()
    profilepath = apppath + "\\Profiles"
    print(profilepath)
    if os.path.isdir(profilepath):
        return profilepath
    else:
        os.mkdir(profilepath)
        return profilepath

