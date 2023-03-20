import tkinter as tk
from VW_properties_login import *
from VW_diagnosticar import *
from VW_visualizar import *
from VW_acercade import *

class Principal():

    def windows():
        Vw2 = tk.Tk()
        Vw2.geometry("800x600")
        tk.Wm.wm_title(Vw2, "EcoSalud")

            #CENTRAR VENTANA
        wtotal = Vw2.winfo_screenwidth()
        htotal = Vw2.winfo_screenheight()
        wventana = 800
        hventana = 600
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        Vw2.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))
        

        Vw2.configure(background="sky blue")
        Vw2.lbltitle = tk.Label(
        Vw2,
        text="BIENVENIDO",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        Vw2.lbltitle.place(relx=0.5, rely=0.2, anchor="center")


        #BARRA DE MENUS 
        menubar = tk.Menu(Vw2)
        Vw2.config( menu=menubar)


        filemenu = tk.Menu(menubar,tearoff=0, bg="snow")
        menubar.add_cascade(label="Menu", menu=filemenu)
        filemenu.add_command(label="Diagnosticar", command= diag.WindowsDiag )
        filemenu.add_command(label="Visualizar", command=visualizar.windowsvisual)
        filemenu.add_command(label="Acerca de...", command= acerca.WindowsAcer)
        filemenu.add_separator()
        filemenu.add_command(label="Salir")
