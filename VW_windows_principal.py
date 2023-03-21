import tkinter as tk
from VW_diagnosticar import diag
from VW_acercade import Acerca
from VW_visualizar import Visualizar


class Principal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('EcoSalud')
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
        text="BIENVENIDO",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        self.lbltitle.place(relx=0.5, rely=0.2, anchor="center")


        #BARRA DE MENUS 
        menubar = tk.Menu(self)
        self.config( menu=menubar)


        filemenu = tk.Menu(menubar,tearoff=0, bg="snow")
        menubar.add_cascade(label="Menu", menu=filemenu)
        filemenu.add_command(label="Diagnosticar", command= self.go_diag)
        filemenu.add_command(label="Visualizar", command= self.go_visualizar)
        filemenu.add_command(label="Acerca de...", command= self.go_acerca)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.exit_visualizar)

        self.mainloop()
    
    def go_diag(self):
        diag()
    
    def go_visualizar(self):
        Visualizar()
    
    def go_acerca(self):
        Acerca()
    
    def exit_visualizar(self):
        self.destroy()
