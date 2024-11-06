import tkinter as tk
from tkinter import *
from tkinter import messagebox


class EliminarUsuario():
    def __init__(self, menu):
        self.ventana = tk.Toplevel(menu)
        self.ventana.config(width=415, height=385)
        self.ventana.resizable(0,0)
        self.ventana.title("Eliminar Usuario")

        #Texto
        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Usuario")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nombre*: ")
        self.lblNombre.place(x=50, y=125, width=80, height=25)

        self.lblCedula = tk.Label(self.ventana, text="Cédula*: ")
        self.lblCedula.place(x=50, y=180, width=80, height=25)

        self.lblRol = tk.Label(self.ventana, text="Rol*: ")
        self.lblRol.place(x=50, y=235, width=80, height=25)

        #Campo de Texto
        self.txtNombre = tk.Entry(self.ventana, state="disabled")
        self.txtNombre.place(x=160, y=125, width=150, height=25)

        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(x=160, y=180, width=150, height=25)

        self.txtRol = tk.Entry(self.ventana, state="disabled")
        self.txtRol.place(x=160, y=235, width=150, height=25)

        #Botones
        self.iconoBuscar = tk.PhotoImage(file=r"Src/icons/magnifier.png")
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar)
        self.btnBuscar.place(x=340, y=180, width=25, height=25)

        self.iconoEliminar = tk.PhotoImage(file=r"Src/icons/bin_closed.png")
        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", image=self.iconoEliminar, compound="left")
        self.btnEliminar.place(x=85, y=310, width=80, height=25)

        self.iconoLimpiar = tk.PhotoImage(file=r"Src/icons/textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar)
        self.btnLimpiar.place(x=195, y=310, width=80, height=25)

        self.ventana.mainloop()