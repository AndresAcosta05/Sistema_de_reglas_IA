
from tkinter import messagebox

def validation (diccionary):
    errores= []
    
    for var,value in diccionary.items():
        if not value:
            messagebox.showerror(message=f'El campo {var} está vacío')
            errores.append(var)
    return errores



        

