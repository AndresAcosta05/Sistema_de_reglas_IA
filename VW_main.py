import tkinter as tk
from VW_properties_login import *
from VW_properties_register import *


class main:

    def __init__(self):
        # CREACION DE VENTANA
        self.ventanalogin = login.Windowslogin()
        
        #URL Logo
        #VENTANA DE LOGIN
        img = tk.PhotoImage(file="VW_img/img_logo1.png")
        login.Buttons(self.ventanalogin)
        login.logo(self.ventanalogin,img)
        login.titleWindows(self.ventanalogin)
        login.positionLabels(self.ventanalogin)
        login.BackgroundColor(self.ventanalogin)
        login.positionEntry(self.ventanalogin)
        login.loginView(self.ventanalogin)


        #VENTANA DE REGISTRO

   

        

        self.ventanalogin.mainloop()
