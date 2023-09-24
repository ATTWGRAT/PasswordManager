import PasswordManager
import customtkinter

import back.App


class Gui:
    def __init__(self):
        self.exitcode = "exit"
        self.app = customtkinter.CTk()
        self.app.geometry("500x600")
        self.logins = PasswordManager.getProfiles(back.App.getProfileLocation())

        self.mainframe = customtkinter.CTkFrame(master=self.app)
        self.mainframe.pack(padx=20, pady=20, expand=True, fill="both")
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure((0,1,2,3,4), weight=1)

        self.mainlabel = customtkinter.CTkLabel(master=self.mainframe,
                                                text="Password Manager",
                                                font=('Arial', 30),
                                                text_color='Aqua')

        self.mainlabel.grid(row=0, column=0, pady=20, padx=20, sticky='nsew')

        self.profilepick = customtkinter.CTkComboBox(master=self.mainframe,
                                                     width=220,
                                                     height=32,
                                                     values=self.logins)

        self.profilepick.grid(row=1, column=0, pady=20, padx=20)

    def run(self):
        self.app.mainloop()
        return self.exitcode
