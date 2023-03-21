import tkinter as tk
from tkinter import messagebox
from CR_user_crud import user_Crud
from CL_user import User
from validaciones import validation

# Crear Ventana


class Register(tk.Tk):
    def __init__(self):
    # CREAR VENTANA
        super().__init__()
        self.geometry("800x600")
        self.title("EcoSalud")

    # CENTRAR VENTANA
        wtotal = self.winfo_screenwidth()
        htotal = self.winfo_screenheight()
        wventana = 800
        hventana = 600
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))

    # COLOR FONDO
        self.configure(background="sky blue")

    # lABEL
        self.lbltitle = tk.Label(
            self,
            text="Ingrese Sus Datos",
            font=("ComicSansMS", 24, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lbltitle.place(relx=0.5, rely=0.25, anchor="center")

   # CAJA DE TEXTO Y LABEL NOMBRE USUARIO
        self.lbltitle = tk.Label(
            self,
            text="Nombre: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lbltitle.place(relx=0.2, rely=0.4, anchor="center")

        self.nombre = tk.Entry(self)
        self.nombre.place(relx=0.35, rely=0.4, anchor="center")


# CAJA DE TEXTO Y LABEL APELLIDO USUARIO
        self.lbltitle = tk.Label(
            self,
            text="Apellido: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lbltitle.place(relx=0.2, rely=0.5, anchor="center")

        self.apellido = tk.Entry(self)
        self.apellido.place(relx=0.35, rely=0.5, anchor="center")

    # CAJA DE TEXTO  y label SEGUNDO NOMBRE
        self.lbltitle = tk.Label(
            self,
            text="Segundo Nombre: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lbltitle.place(relx=0.6, rely=0.4, anchor="center")
        self.segundo_nombre = tk.Entry(self)
        self.segundo_nombre.place(relx=0.8, rely=0.4, anchor="center")

    # CAJA DE TEXTO  y label SEGUNDO APELLIDO
        self.lbltitle = tk.Label(
            self,
            text="Segundo apellido: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lbltitle.place(relx=0.6, rely=0.5, anchor="center")
        self.segundo_apellido = tk.Entry(self)
        self.segundo_apellido.place(relx=0.8, rely=0.5, anchor="center")

# LABEL NUMERO DE DOCUMENTO Y CAJA DE TEXTO
        self.lblnumdoc = tk.Label(
            self,
            text="Numero Documento: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lblnumdoc.place(relx=0.13, rely=0.6, anchor="center")
        self.numdoc = tk.Entry(self)
        self.numdoc.place(relx=0.35, rely=0.6, anchor="center")


# LABEL USUARIO Y CAJA DE TEXTO
        self.lblusuario = tk.Label(
            self,
            text="Usuario: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lblusuario.place(relx=0.6, rely=0.6, anchor="center")
        self.txtuser = tk.Entry(self)
        self.txtuser.place(relx=0.8, rely=0.6, anchor="center")

# LABEL CONTRASEÑA Y CAJA DE TEXTO
        self.lblcontraseña = tk.Label(
            self,
            text="Contraseña: ",
            font=("ComicSansMS", 15, "bold"),
            justify="center",
            background="sky blue",
            fg="snow")
        self.lblcontraseña.place(relx=0.6, rely=0.65, anchor="center")
        self.txtpass = tk.Entry(self)
        self.txtpass.place(relx=0.8, rely=0.65, anchor="center")

# BOTON REGISTRAR
        btnregister = tk.Button(self, text="Registrar", command=self.data,
        font=("ComicSansMS", 11),
        justify="center",
        background="sky blue",
        fg="snow")
        btnregister.place(relx=0.35, rely=0.8, anchor="center")

# Boton cerrar
        btnBack = tk.Button(self, text="Cerrar", command=self.back,
        font=("ComicSansMS", 11),
        justify="center",
        background="sky blue",
        fg="snow")
        btnBack.place(relx=0.65, rely=0.8, anchor="center")

        self.lblfooter = tk.Label(
            self,
            text="@Copyright 2023 Grupo EcoSalud \n Samir Rojas - Andres Acosta - Carlos Quintero",
            font=("ComicSansMS", 9, "bold"),
            justify="center",
            background="sky blue",
        fg="snow")

        self.lblfooter.place(relx=0.5, rely=0.97, anchor="center")


    def data(self):
        Nombre = self.nombre.get()
        Apellido = self.apellido.get()
        SegundoNombre = self.segundo_apellido.get()
        SegundoApellido = self.segundo_apellido.get()
        NumeroIdenti = self.numdoc.get()
        Usuario = self.txtuser.get()
        Contraseña = self.txtpass.get()

        dic = {
            'Nombre':Nombre,
            'Apellido': Apellido,
            'Segundo Nombre': SegundoNombre,
            'Segundo Apellido': SegundoApellido,
            'Numero Identificacion': NumeroIdenti,
            'Usuario': Usuario,
            'Contraseña': Contraseña
        }

        if not validation(dic):
            Crud = user_Crud()
            result = Crud.insert_US(User(0,NumeroIdenti,Nombre,SegundoNombre,Apellido,SegundoApellido,Usuario,Contraseña))

            if result:
                messagebox.showinfo(message="Datos Insertados Exitosamente", title="Título")
            else:
                messagebox.showerror(message="Error Al guardar usuario", title="ERROR!")
    
    def back(self):
        self.destroy()

        

  



   
   


 
 
