import tkinter as tk
from tkinter import ttk
from CR_diagnostic import diagnostic_Crud

class Visualizar (tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Ecosalud")
        #CENTRAR VENTANA
        wtotal = self.winfo_screenwidth()
        htotal = self.winfo_screenheight()
        wventana = 850
        hventana = 600
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.geometry(str(wventana)+"x"+str(hventana) +
                "+"+str(pwidth)+"+"+str(pheight))
        
        self.configure(background="sky blue")
        self.lbltitle = tk.Label(
        self,
        text="Diagnosticos",
        font=("ComicSansMS", 24, "bold"),
        justify="center",
        background="sky blue",
        fg="snow")
        self.lbltitle.place(relx=0.5, rely=0.1, anchor="center")
        # Creation of the table for diagnostics
        self.table = ttk.Treeview(self, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8'))
        # adding width for the colums
        self.table.column('#0', width=125, anchor=tk.CENTER)
        self.table.column('#1', width=125, anchor=tk.CENTER)
        self.table.column('#2', width=125, anchor=tk.CENTER)
        self.table.column('#3', width=50, anchor=tk.CENTER)
        self.table.column('#4', width=50, anchor=tk.CENTER)
        self.table.column('#5', width=50, anchor=tk.CENTER)
        self.table.column('#6', width=50, anchor=tk.CENTER)
        self.table.column('#7', width=50, anchor=tk.CENTER)
        self.table.column('#8', width=173, anchor=tk.CENTER)
        # adding the text of the columns
        self.table.heading('#0', text='DOCUMENTO', anchor=tk.CENTER)
        self.table.heading('#1', text='NOMBRE', anchor=tk.CENTER)
        self.table.heading('#2', text='APELLIDO', anchor=tk.CENTER)
        self.table.heading('#3', text='TP', anchor=tk.CENTER)
        self.table.heading('#4', text='DP', anchor=tk.CENTER)
        self.table.heading('#5', text='DR', anchor=tk.CENTER)
        self.table.heading('#6', text='TCS', anchor=tk.CENTER)
        self.table.heading('#7', text='E', anchor=tk.CENTER)
        self.table.heading('#8', text='DIAGNOSTICO', anchor=tk.CENTER)
        self.table.place(relx=0.5, rely=0.4, anchor="center", width=800)
        # Executing the sql consult
        crud_diag = diagnostic_Crud()
        records = crud_diag.select_DG()
        # inserting datas in the table
        for record in records:
            self.table.insert("", 0, text=record['document'], values=(record['name'], record['surname'], record['persistent_cough'], record['chest_pain'], record['difficulty_breathing'], record['coughing_blood'], record['sneezing'], record['diagnostic']))
        
        self.mainloop()