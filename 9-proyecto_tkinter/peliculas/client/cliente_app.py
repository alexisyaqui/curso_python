import tkinter as tk
from tkinter import ttk, messagebox

from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar


def barra_menu(root):
    barra_menu = tk.Menu(root, bg='red', border='3px', background='#468B97')
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro en la Base de Datos', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en la Base de Datos', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consulas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        # self.config(bg='white')

        self.id_pelicula = None

        # metodos
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()

    def campos_pelicula(self):
        # label de cada campo
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duracion: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Genero: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        #######################
        # entradas
        #######################
        self.mi_nombre = tk.StringVar()
        self.entrada_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entrada_nombre.config(width=50, font=('Arial', 12))
        self.entrada_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # entrada de duracion
        self.mi_duracion = tk.StringVar()
        self.entrada_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entrada_duracion.config(width=50, font=('Arial', 12))
        self.entrada_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        # entrada de Genero
        self.mi_genero = tk.StringVar()

        self.entrada_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entrada_genero.config(width=50, font=('Arial', 12,))
        self.entrada_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #######################
        # botones
        #######################
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#2F58CD', bg='black', cursor='hand2',
                                activebackground='#19376D')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), bg='#0079FF', cursor='hand2',
                                  activebackground='#468B97')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), bg='#F94C10', cursor='hand2',
                                   activebackground='#468B97')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_campos(self):

        # 2
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        # 1
        self.entrada_nombre.config(state='normal')
        self.entrada_duracion.config(state='normal')
        self.entrada_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_pelicula = None

        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entrada_nombre.config(state='disabled')
        self.entrada_duracion.config(state='disabled')
        self.entrada_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    def guardar_datos(self):
        self.pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )

        if self.id_pelicula == None:
            guardar(self.pelicula)
        else:
            editar(self.pelicula, self.id_pelicula)

        self.tabla_peliculas()

        # Desabilira campos
        self.deshabilitar_campos()

    def tabla_peliculas(self):
        self.lista_peliculas = listar()  # crea el objeto para listar los datos en la base de datos
        self.lista_peliculas.reverse()  # revierte la lista en modo inverso

        self.tabla = ttk.Treeview(self,
                                  column=('Nombre', 'Duracion', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        ##scrolbar para la tabla si excede mas de 10 registros
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', tex='DURACION')
        self.tabla.heading('#3', tex='GENERO')

        # iterar la lista de peliculas con un for
        for lista in self.lista_peliculas:
            self.tabla.insert('', 0, text=lista[0], values=(lista[1], lista[2], lista[3]))

        #######################
        # botones Editar dentro de la tabla
        #######################
        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#2F58CD', bg='black', cursor='hand2',
                                 activebackground='#19376D')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        #######################
        # botones Eliminar dentro de la Tabla
        #######################

        self.boton_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), bg='#F94C10', cursor='hand2',
                                   activebackground='#468B97')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.entrada_nombre.insert(0, self.nombre_pelicula)
            self.entrada_duracion.insert(0, self.duracion_pelicula)
            self.entrada_genero.insert(0, self.genero_pelicula)

        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado nigun registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)

            self.tabla_peliculas()
            self.id_pelicula = None

        except:
            titulo = 'Eliminar Registro'
            mensaje = 'No ha seleccionado ningun elemento para eliminar!!!, favor seleccione un elemento'
            messagebox.showerror(titulo, mensaje)
