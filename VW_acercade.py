import tkinter as tk
from VW_windows_principal import *


class Acerca(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title( "EcoSalud")

            #CENTRAR VENTANA
        wtotal = self.winfo_screenwidth()
        htotal = self.winfo_screenheight()
        wventana = 800
        hventana = 600
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))
        
        self.configure(background="sky blue")
        self.lbltitle = tk.Label(
        self,
        text="INFORMACION DEL SOFTWARE LOGO Y INFO",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        self.lbltitle.place(relx=0.5, rely=0.1, anchor="center")
        
# Boton Cerrar
        btnBack = tk.Button(self, text="Cerrar", command=self.back,
        font=("ComicSansMS", 12),
        justify="center",
        background="sky blue",
        fg="snow")
        btnBack.place(relx=0.5, rely=0.8, anchor="center")
        
        #footer
        self.lblfooter = tk.Label(
            self,
            text="@Copyright 2023 Grupo EcoSalud \n Samir Rojas - Andres Acosta - Carlos Quintero",
            font=("ComicSansMS", 9, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")

    
        self.lblfooter.place(relx=0.5, rely=0.97, anchor="center")
        
    def back(self):
        self.destroy()


