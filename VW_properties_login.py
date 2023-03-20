import tkinter as tk
from VW_properties_register import *
from VW_windows_principal import *
from CL_user import User
from CR_user_crud import *
from tkinter import messagebox


#Crear Ventana
class Login:
 def __init__(self):
    self.ventana = tk.Tk()
    self.ventana.geometry("375x600")
   
    # Centrar Ventana
    wtotal = self.ventana.winfo_screenwidth()
    htotal = self.ventana.winfo_screenheight()
    wventana = 375
    hventana = 600
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    self.ventana.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))


# Posicion y Creacion de  Cajas de Texto
    self.user = tk.Entry(self.ventana)
    self.password = tk.Entry(self.ventana)
    
    self.user.place(relx=0.5, rely=0.45, anchor="center")
    self.password.place(relx=0.5, rely=0.55, anchor="center")
   
# COLOR FONDO

    self.ventana.configure(background="sky blue")

# Posicion Y Creacion de Labels
 
    self.ventana.lbluser = tk.Label(
        self.ventana,
        text="User",
        font=("ComicSansMS", 15),
        justify="center",
        background="sky blue",
        fg="snow")

    self.ventana.lblpass = tk.Label(
        self.ventana,
        text="Password",
        font=("ComicSansMS", 15),
        justify="center",
        background="sky blue",
        fg="snow")
    

    self.ventana.lblfooter = tk.Label(
        self.ventana,
        text="@Copyright 2023 Grupo EcoSalud \n Samir Rojas - Andres Acosta - Carlos Quintero",
        font=("ComicSansMS", 9, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")

    self.ventana.lbluser.place(relx=0.5, rely=0.4, anchor="center")
    self.ventana.lblpass.place(relx=0.5, rely=0.5, anchor="center")
    self.ventana.lblfooter.place(relx=0.5, rely=0.97, anchor="center")

#Titulo de la Ventana
    tk.Wm.wm_title(self.ventana, "EcoSalud")

#Logo
    img = tk.PhotoImage(file="VW_img/img_logo1.png")
    self.ventana.lblimg = tk.Label(self.ventana, image= img)
    self.ventana.lblimg.place(relx=0.5, rely=0.111, anchor="center")

#Creacion de botones
    btningresar = tk.Button(self.ventana,text="Ingresar",command= self.Data,
    font=("ComicSansMS", 11),
    justify="center",
    background="sky blue",
    fg="snow")
    btningresar.place(relx=0.5, rely=0.63, anchor="center")

    btnregistrar = tk.Button(self.ventana,text="Registrarse",command= self.next,
    font=("ComicSansMS", 11),
    justify="center",
    background="sky blue",
    fg="snow")
    
    btnregistrar.place(relx=0.5, rely=0.7, anchor="center")

    self.ventana.mainloop()


 def Data(self):
    try:
     usuario = self.user.get()
     password = self.password.get()
     CR_login = user_Crud()
     validacion = CR_login.login_US(User(user=usuario, password= password))
     if validacion:
       Principal.windows()
     else:
      messagebox.showerror(message="USUARIO O CONTRASEÑA INCORRECTO", title="ERROR!")

    except ValueError:
        print("")


 def next(self):
     self.ventana.destroy()
     Register()
  

 ##############################################################



 









        






 




