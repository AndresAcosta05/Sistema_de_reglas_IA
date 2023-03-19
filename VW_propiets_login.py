import tkinter as tk
from VW_login import *


    # Centrar Ventana
def loginView(Vw):
    wtotal = Vw.winfo_screenwidth()
    htotal = Vw.winfo_screenheight()
    wventana = 375
    hventana = 600
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    Vw.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))


# Posicion y Creacion de  Cajas de Texto
def positionEntry(Vw):
    Vw.user = tk.Entry(Vw)
    Vw.password = tk.Entry(Vw)

    Vw.user.place(relx=0.5, rely=0.45, anchor="center")
    Vw.password.place(relx=0.5, rely=0.55, anchor="center")

# COLOR FONDO


def BackgroundColor(Vw):
    Vw.configure(background="sky blue")

# Posicion Y Creacion de Labels


def positionLabels(Vw):
    Vw.lbluser = tk.Label(
        Vw,
        text="User",
        font=("ComicSansMS", 15),
        justify="center",
        background="sky blue",
        fg="snow")

    Vw.lblpass = tk.Label(
        Vw,
        text="Password",
        font=("ComicSansMS", 15),
        justify="center",
        background="sky blue",
        fg="snow")
    

    Vw.lblfooter = tk.Label(
        Vw,
        text="@Copyright 2023 Grupo EcoSalud \n Samir Rojas - Andres Acosta - Carlos Quintero",
        font=("ComicSansMS", 9, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")

    Vw.lbluser.place(relx=0.5, rely=0.4, anchor="center")
    Vw.lblpass.place(relx=0.5, rely=0.5, anchor="center")
    Vw.lblfooter.place(relx=0.5, rely=0.97, anchor="center")

#Titulo de la Ventana
def titleWindows(Vw):
    tk.Wm.wm_title(Vw, "EcoSalud")


#Logo
def logo(Vw,url):
    Vw.lblimg = tk.Label(Vw, image=url)
    Vw.lblimg.place(relx=0.5, rely=0.111, anchor="center")

#Creacion de botones
def Buttons(Vw):
    btningresar = tk.Button(Vw,text="Ingresar",command="AQUI VA EL METODO DEL BOTON",
    font=("ComicSansMS", 11),
    justify="center",
    background="sky blue",
    fg="snow")
    btningresar.place(relx=0.5, rely=0.63, anchor="center")

    btnregistrar = tk.Button(Vw,text="Registrarse",command="AQUI VA EL METODO DEL BOTON",
    font=("ComicSansMS", 11),
    justify="center",
    background="sky blue",
    fg="snow")
    btnregistrar.place(relx=0.5, rely=0.7, anchor="center")





