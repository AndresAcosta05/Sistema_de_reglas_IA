import tkinter as tk
from VW_propiets_login import *


class Login:

    def __init__(self):

        # CREACION DE VENTANA
        self.ventanalogin = tk.Tk()
        self.ventanalogin.geometry("375x600")

        #URL Logo
        img = tk.PhotoImage(file="VW_img/img_logo1.png")
        Buttons(self.ventanalogin)
        logo(self.ventanalogin,img)
        titleWindows(self.ventanalogin)
        positionLabels(self.ventanalogin)
        BackgroundColor(self.ventanalogin)
        positionEntry(self.ventanalogin)
        loginView(self.ventanalogin)

        self.ventanalogin.mainloop()
