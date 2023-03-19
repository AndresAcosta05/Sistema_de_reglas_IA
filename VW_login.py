import tkinter as tk
from VW_propiets_login import *


class Login:

    def __init__(self):
        # CREACION DE VENTANA
        self.ventanalogin = login.Windowslogin()
        
        #URL Logo
        img = tk.PhotoImage(file="VW_img/img_logo1.png")
        login.Buttons(self.ventanalogin)
        login.logo(self.ventanalogin,img)
        login.titleWindows(self.ventanalogin)
        login.positionLabels(self.ventanalogin)
        login.BackgroundColor(self.ventanalogin)
        login.positionEntry(self.ventanalogin)
        login.loginView(self.ventanalogin)

        self.ventanalogin.mainloop()
