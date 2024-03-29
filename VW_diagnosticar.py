import tkinter as tk
from tkinter import ttk
from VW_windows_principal import *
from tkinter import messagebox
from SBR_sistema import Sistema
from random import choice
from SBR_reglas import Reglas
from CR_question import question_Crud
from CL_question import Question
from CR_diagnostic import diagnostic_Crud
from CL_diagnostic import Diagnostic


class diag(tk.Tk):
    def __init__(self, id_usuario):
        self.id_us_diag = id_usuario
        super().__init__()
        self.geometry("800x600")
        self.title("EcoSalud")

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
        text="Diagnostico",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        self.lbltitle.place(relx=0.5, rely=0.1, anchor="center")

#PREGUNTA  Y RESPUESTA 1
        lblpregunta1 = tk.Label(
            self,
            text="1. ¿Estornudo?",
            font=("ComicSansMS",12,"bold"),
            justify= "center",
            background="sky blue",
            fg="snow"
        )
        lblpregunta1.place(relx=0.18, rely=0.2)
        self.combo = ttk.Combobox(self, state="readonly", values=["no", "si"])
        self.combo.place(relx= 0.2, rely=0.25)


#PREGUNTA  Y RESPUESTA 2
        lblpregunta2 = tk.Label(
            self,
            text="2. ¿Tos persistente?",
            font=("ComicSansMS",12,"bold"),
            justify= "center",
            background="sky blue",
            fg="snow"
        )
        lblpregunta2.place(relx=0.5, rely=0.2)
        self.combo2 = ttk.Combobox(self, state="readonly", values=["no", "si"])
        self.combo2.place(relx= 0.55, rely=0.25)


#PREGUNTA  Y RESPUESTA 3
        lblpregunta3 = tk.Label(
            self,
            text="3. ¿Dolor en el pecho?",
            font=("ComicSansMS",12,"bold"),
            justify= "center",
            background="sky blue",
            fg="snow"
        )
        lblpregunta3.place(relx=0.17, rely=0.4)
        self.combo3 = ttk.Combobox(self, state="readonly", values=["no", "si"])
        self.combo3.place(relx= 0.2, rely=0.45)

#PREGUNTA  Y RESPUESTA 4
        lblpregunta4 = tk.Label(
            self,
            text="4. ¿Dificultad para respirar?",
            font=("ComicSansMS",12,"bold"),
            justify= "center",
            background="sky blue",
            fg="snow"
        )
        lblpregunta4.place(relx=0.5, rely=0.4)
        self.combo4 = ttk.Combobox(self, state="readonly", values=["no", "si"])
        self.combo4.place(relx= 0.55, rely=0.45)

#PREGUNTA  Y RESPUESTA 5
        lblpregunta5 = tk.Label(
            self,
            text="5. ¿Tos con Sangre?",
            font=("ComicSansMS",12,"bold"),
            justify= "center",
            background="sky blue",
            fg="snow"
        )
        lblpregunta5.place(relx=0.38, rely=0.55)
        self.combo5 = ttk.Combobox(self, state="readonly", values=["no", "si"])
        self.combo5.place(relx= 0.4, rely=0.6)

#Boton Diagnosticar
        btndiag = tk.Button(self, text="Diagnosticar",
        font=("ComicSansMS", 12,"bold"),
        justify="center",
        background="sky blue",
        fg= "snow", 
        command= self.data)
        btndiag.place(relx=0.425,rely=0.7)
        
# Boton cerrar
        btnBack = tk.Button(self, text="Cerrar", command=self.back,
        font=("ComicSansMS", 12, "bold"),
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





#Respuesta Combobox1
    def data(self):
        index = self.combo.current() #ESTORNUDO
        index2 = self.combo2.current() #TOS PERSISTENTE
        index3 = self.combo3.current() # DOLOR EN EL PECHO
        index4 = self.combo4.current() # DIFICULTAD PARA RESPIRAR
        index5 = self.combo5.current() #TOS CON SANGRE

        if index == -1 or index2 == -1 or index3 == -1 or index4 == -1 or index5 == -1:
            messagebox.showerror(message="INGRESE TODOS LOS DATOS POR FAVOR",)
        else:
            
            engine = Sistema()
            engine.reset()
            engine.declare(Reglas(estornudos=choice([str(self.combo.get())])))
            engine.declare(Reglas(tos_persistente=choice([str(self.combo2.get())]))) 
            engine.declare(Reglas(dolor_pecho=choice([str(self.combo3.get())])))
            engine.declare(Reglas(df_respirar=choice([str(self.combo4.get())])))
            engine.declare(Reglas(tos_sangre=choice([str(self.combo5.get())])))

            engine.run()

            diagnostico = engine.__str__()
            crud = question_Crud()
            crud_diag= diagnostic_Crud()
            id_question = crud.insert_QU(Question(0,index2,index3,index4,index5,index))
            if id_question:
                result = crud_diag.insert_DG(Diagnostic(0,self.id_us_diag,id_question,diagnostico))
                if result:
                    messagebox.showinfo(message="Sintomas Ingresados Correctamente", title="Diagnostico")
                else:
                    messagebox.showerror(message="Error al ingresar el diagnostico", title="ERROR DIAGNOSTICO")
            else:
                messagebox.showerror(message="Error al insertar las preguntas", title="ERROR DE PREGUNTAS!")
       
