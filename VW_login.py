import tkinter as tk

class aplication:

    def __init__(self):
     
     # DIMENSIONES DE LA VENTANA
     self.ventanalogin = tk.Tk()
     self.ventanalogin.geometry("400x600")

     #COLOR FONDO
     self.ventanalogin.configure(background = "sky blue")

     #TITULO DE LA VENTANA
     tk.Wm.wm_title(self.ventanalogin,"EcoSalud")
     
     #LABELS
     self.lbltitle= tk.Label(
        self.ventanalogin, 
        text= "EcoSalud",
        justify="center",
        background="sky blue",
        fg="snow")


     #Posicion Labels y Botones
     self.lbltitle.place(x="170",y="50")




     self.ventanalogin.mainloop()

    