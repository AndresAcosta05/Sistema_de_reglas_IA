
import tkinter as tk
from tkinter import ttk
from VW_properties_login import *


#Crear Ventana
class register:
 
 def Windowsregister():
    #CREAR VENTANA
    Vw1 = tk.Tk()
    Vw1.geometry("800x600")
    tk.Wm.wm_title(Vw1, "EcoSalud")

    #CENTRAR VENTANA
    wtotal = Vw1.winfo_screenwidth()
    htotal = Vw1.winfo_screenheight()
    wventana = 800
    hventana = 600
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    Vw1.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))



    #COLOR FONDO
    Vw1.configure(background="sky blue")

    #lABEL
    Vw1.lbltitle = tk.Label(
        Vw1,
        text="Ingrese Sus Datos",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
    Vw1.lbltitle.place(relx=0.5, rely=0.25, anchor="center")


    Vw1.lbltitle = tk.Label(
        Vw1,
        text="Nombre: ",
        font=("ComicSansMS", 15, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
    Vw1.lbltitle.place(relx=0.2, rely=0.4, anchor="center")

    #CAJA DE TEXTO
    Vw1.nombre = tk.Entry(Vw1)
    Vw1.nombre.place(relx=0.35, rely=0.4, anchor="center")


    Vw1.lbltitle = tk.Label(
        Vw1,
        text="Apellido: ",
        font=("ComicSansMS", 15, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
    Vw1.lbltitle.place(relx=0.2, rely=0.5, anchor="center")

    #CAJA DE TEXTO
    Vw1.apellido = tk.Entry(Vw1)
    Vw1.apellido.place(relx=0.35, rely=0.5, anchor="center")

#TIPO DOCUMENTO
    Vw1.lbltitle = tk.Label(
        Vw1,
        text="Tipo Documento: ",
        font=("ComicSansMS", 15, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
    
    #Combo Box
    Vw1.lbltitle.place(relx=0.6, rely=0.4, anchor="center")
    TI = ['CEDULA','TARJETA','EXTRANJERO']
    cmb= ttk.Combobox(Vw1,values=TI,width=17,state="readonly")
    cmb.current(0)
    
    cmb.place(relx=0.8, rely=0.4, anchor="center")





#LABEL NUMERO DE DOCUMENTO Y CAJA DE TEXTO
    Vw1.lblnumdoc = tk.Label(
        Vw1,
        text="Numero Documento: ",
        font=("ComicSansMS", 15, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
    Vw1.lblnumdoc.place(relx=0.6, rely=0.5, anchor="center")
    Vw1.numdoc= tk.Entry(Vw1)
    Vw1.numdoc.place(relx=0.8, rely=0.5, anchor="center")



#BOTON REGISTRAR
    btnregister = tk.Button(Vw1,text="Registrar",command="AQUI VA EL METODO DEL BOTON",
    font=("ComicSansMS", 11),
    justify="center",
    background="sky blue",
    fg="snow")
    btnregister.place(relx=0.35, rely=0.6, anchor="center")

#BOTON ATRAS
    btnBack = tk.Button(Vw1,text="Atras",command= "",
    font=("ComicSansMS", 11),
    justify="center",
    background="sky blue",
    fg="snow")
    btnBack.place(relx=0.65, rely=0.6, anchor="center")


   


 
 
