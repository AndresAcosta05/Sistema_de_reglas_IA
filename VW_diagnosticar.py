import tkinter as tk
from VW_windows_principal import *

class diag():

    def WindowsDiag():
        Vw3 = tk.Tk()
        Vw3.geometry("800x600")
        tk.Wm.wm_title(Vw3, "EcoSalud")

            #CENTRAR VENTANA
        wtotal = Vw3.winfo_screenwidth()
        htotal = Vw3.winfo_screenheight()
        wventana = 800
        hventana = 600
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        Vw3.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))
        
        Vw3.configure(background="sky blue")
        Vw3.lbltitle = tk.Label(
        Vw3,
        text="Diagnostico",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        Vw3.lbltitle.place(relx=0.5, rely=0.1, anchor="center")


