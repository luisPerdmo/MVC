import tkinter as tk
from tkinter import *
from tkinter import messagebox


class CrearUsuario():

    def guardarUsuario(self, event):
        self.usuario.crearUsuario(self.txtNombre.get(), self.txtCedula.get(), self.txtRol.get())
        messagebox.showinfo("Confirmacion", "Nuevo usuario registrado con exito!!")

    def __init__(self, menu, usuario):
        self.ventana = tk.Toplevel(menu)
        self.ventana.config(width=380, height=385)
        self.ventana.resizable(0,0)
        self.ventana.title("Crear Nuevo Usuario")

        self.usuario = usuario

        #Texto
        self.lblTitulo = tk.Label(self.ventana, text="Crear Usuario")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nombre*: ")
        self.lblNombre.place(x=50, y=125, width=80, height=25)

        self.lblCedula = tk.Label(self.ventana, text="Cédula*: ")
        self.lblCedula.place(x=50, y=180, width=80, height=25)

        self.lblRol = tk.Label(self.ventana, text="Rol*: ")
        self.lblRol.place(x=50, y=235, width=80, height=25)

        #Campo de Texto
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(x=160, y=125, width=150, height=25)

        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(x=160, y=180, width=150, height=25)

        self.txtRol = tk.Entry(self.ventana)
        self.txtRol.place(x=160, y=235, width=150, height=25)

        #Botones
        self.iconoGuardar = tk.PhotoImage(file=r"Src/icons/disk.png")
        self.btnGuardar = tk.Button(self.ventana, text="Guardar", image=self.iconoGuardar, compound="left")
        self.btnGuardar.place(x=85, y=310, width=80, height=25)
        self.btnGuardar.bind("<Button-1>", self.guardarUsuario)

        self.iconoLimpiar = tk.PhotoImage(file=r"Src/icons/textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar)
        self.btnLimpiar.place(x=195, y=310, width=80, height=25)

        self.ventana.mainloop()