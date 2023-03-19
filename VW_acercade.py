import tkinter as tk
from VW_windows_principal import *


class acerca():

    def WindowsAcer():
        Vw4 = tk.Tk()
        Vw4.geometry("800x600")
        tk.Wm.wm_title(Vw4, "EcoSalud")

            #CENTRAR VENTANA
        wtotal = Vw4.winfo_screenwidth()
        htotal = Vw4.winfo_screenheight()
        wventana = 800
        hventana = 600
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        Vw4.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))
        
        Vw4.configure(background="sky blue")
        Vw4.lbltitle = tk.Label(
        Vw4,
        text="INFORMACION DEL SOFTWARE LOGO Y INFO",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        Vw4.lbltitle.place(relx=0.5, rely=0.1, anchor="center")


