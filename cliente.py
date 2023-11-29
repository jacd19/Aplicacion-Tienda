from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3


class Ventana_cliente:
    db = 'database/proyecto.db'

    def __init__(self,toplevel,ventana_principal):
        self.ventana = ventana_principal
        self.ventana_cliente= toplevel
        self.ventana_cliente.title("Ventana Cliente")
        self.ventana_cliente.geometry('830x565+250+50')


        # FRAMES

        self.frame_titulo = Frame(self.ventana_cliente,background= 'black',width=500,height=50)
        self.frame_titulo.grid(row=0,column=1,sticky='nsew')
        self.frame_menu = Frame(self.ventana_cliente,background='black',width=60,height = 560)
        self.frame_menu.grid(row=0,column=0,rowspan=2,sticky='nsew')
        self.frame_info = Frame(self.ventana_cliente,background='black',width= 500,height= 500)
        self.frame_info.grid(row=1,column=1,sticky='nsew')

        self.widgets()

    def forma_imagen(self,nombre):
        self.imagen = Image.open(nombre)
        self.imagen = self.imagen.resize((45,45))
        self.imagen.save(nombre)
        return ImageTk.PhotoImage(self.imagen)

    def forma_imagen_principal(self,nombre):
        self.imagen = Image.open(nombre)
        self.imagen = self.imagen.resize((825,554))
        self.imagen.save(nombre)
        return ImageTk.PhotoImage(self.imagen)

    def widgets(self):

        #FRAME TITULO

        #etiqueta para el titulo
        self.etiqueta_titulo = Label(self.frame_titulo,text=('Innovative Compani JACD'),font=('perpetua',20,'bold'),bg='black',fg='white')
        self.etiqueta_titulo.grid(row=0,column=0,sticky='nsew',ipadx=210,ipady=10)

        #FRAME MENU

        #Imagenes
        self.home = self.forma_imagen('imagenes/home.png')
        self.compra = self.forma_imagen('imagenes/compras.png')
        self.lista_compras = self.forma_imagen('imagenes/lista_compras.png')
        self.salir= self.forma_imagen('imagenes/salir.png')
        self.img_principal = self.forma_imagen_principal('imagenes/imagen_principal.png')

        #Botones del menu
        self.boton_home = Button(self.frame_menu,image=self.home,bg='black',activebackground='black',bd=0,command = self.pagina_principal)
        self.boton_home.grid(row=0,column=0,sticky= 'nsew',ipady=10,ipadx=8)
        self.boton_compras = Button(self.frame_menu, image= self.compra,bg='black',activebackground='black',bd=0, command = self.pagina_compras)
        self.boton_compras.grid(row= 1,column= 0,sticky='nsew',ipady = 30,ipadx=8)
        self.boton_lista_compras = Button(self.frame_menu, image=self.lista_compras,bg='black',activebackground='black',bd=0, command = self.pagina_lista_compra)
        self.boton_lista_compras.grid(row=2,column=0,sticky='nsew')
        Label(self.frame_menu,text='',bg='black').grid(row=3,column=0,sticky='nsew',pady=120)#etiqueta para espacio
        self.boton_salir = Button(self.frame_menu, image = self.salir,bg='black',activebackground='black',bd=0,command=self.cerrar_sesion)
        self.boton_salir.grid(row=4,column=0,sticky='nsew')

        #FRAME INFO

        #Estilo de paginas
        estilo_paginas = ttk.Style()
        estilo_paginas.configure('TNotebook', background = 'black', foreground= 'black', padding= 0,borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure('TNotebook', background='black',borderwidth=0)
        estilo_paginas.configure('TNotebook.Tab',background='black',borderwidth=0)
        estilo_paginas.map('TNotebook.Tab',background=[('selected','black')],foreground=[('selected','black')])

        #Creacion de paginas

        self.paginas = ttk.Notebook(self.frame_info, style= 'TNotebook')
        self.paginas.grid(column=0,row=0,sticky='nsew')
        self.pagina_uno = Frame(self.paginas, bg='cyan')
        self.pagina_dos = Frame(self.paginas, bg='black')
        self.pagina_tres = Frame(self.paginas, bg = 'black')
        self.paginas.add(self.pagina_uno)
        self.paginas.add(self.pagina_dos)
        self.paginas.add(self.pagina_tres)

        #Pagina Uno

        self.imagen_principal = Label(self.pagina_uno, image = self.img_principal,bg='#52A8D2')
        self.imagen_principal.place(x=-2,y=-44)#grid(row = 1,column = 0,ipadx=15,sticky='nsew',rowspan=3)

        #Pagina Dos - Articulos

        #Encabezado
        self.encabezado=Label(self.pagina_dos, text= 'ARTICULOS',font=('Calibri',16,'bold'),bg='black',fg='#4FA1CA')
        self.encabezado.grid(row=0,column=0,sticky='ne')

        #estilo del boton Comprar
        boton_comprar = ttk.Style()
        boton_comprar.configure('my.TButton',font=('Calibri',12,'bold'),foreground = 'black',background = '#DBFFD7')
        self.boton_agregar_producto = ttk.Button(self.pagina_dos, text = 'Agregar Producto', style='my.TButton',command=self.boton_comprar)
        self.boton_agregar_producto.grid(row=0,column=1,sticky='ne',padx=20)

        #treeview base de datos

        #Estilo
        estilo= ttk.Style()
        estilo.configure('mystyle.Treeview', highlightthickness=0,bd=0,font=('Calibri',11),width=2)
        estilo.configure('mystyle.Treeview.Heading',font=('Calibri',13,'bold'),background = 'white')
        #estilo.layout('mystyle.Treewiew', [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        self.frame_tabla_compras = Frame (self.pagina_dos)
        self.frame_tabla_compras.grid(row= 1, column= 0,columnspan=2)

        self.tabla_compras = ttk.Treeview(self.frame_tabla_compras, height= 21, columns= ('1','2','3','4'), style = 'mystyle.Treeview')
        self.tabla_compras.grid(row=1,column=0,columnspan= 2,sticky='nsew')
        self.tabla_compras.heading('#0', text='Id', anchor=CENTER)
        self.tabla_compras.column('#0', width=150)
        self.tabla_compras.heading('#1', text= 'Categoria', anchor = CENTER)
        self.tabla_compras.column('#1',width=150)
        self.tabla_compras.heading('#2',text='Color', anchor= CENTER)
        self.tabla_compras.column('#2', width=150)
        self.tabla_compras.heading('#3', text= 'Marca', anchor= CENTER)
        self.tabla_compras.column('#3', width=150)
        self.tabla_compras.heading('#4',text = 'Precio',anchor=CENTER)
        self.tabla_compras.column('#4', width=150)


        ladoy = ttk.Scrollbar(self.frame_tabla_compras, orient= 'vertical', command = self.tabla_compras.yview)
        ladoy.grid(column=2, row= 1, sticky = 'ns')
        self.tabla_compras.configure(yscrollcommand = ladoy.set)

        self.db_get_compra()

        #Pagina Tres - Lista de la Compra

        # Encabezado
        self.encabezado = Label(self.pagina_tres, text='LISTA DE ARTICULOS', font=('Calibri', 16, 'bold'), bg='black',fg='#4FA1CA')
        self.encabezado.grid(row=0, column=0, sticky='ne')

        # estilo del boton Comprar
        boton_comprar = ttk.Style()
        boton_comprar.configure('my.TButton', font=('Calibri', 12, 'bold'), foreground='black', background='#DBFFD7')
        self.boton_comprar = ttk.Button(self.pagina_tres, text='Comprar', style='my.TButton', command = self.boton_terminar_compra)
        self.boton_comprar.grid(row=0, column=2, sticky='ne', padx=15)
        self.boton_eliminar = ttk.Button(self.pagina_tres, text='Eliminar', style='my.TButton',command = self.boton_eliminar)
        self.boton_eliminar.grid(row=0, column=1, sticky='ne')

        # treeview base de datos

        self.frame_tabla_lista_compras = Frame(self.pagina_tres,bg= 'gray90')
        self.frame_tabla_lista_compras.grid(columnspan= 3 , row= 1,sticky= 'nsew')

        self.tabla_lista_compras = ttk.Treeview(self.frame_tabla_lista_compras, height=20, columns=('1', '2', '3','4'), style='mystyle.Treeview')
        self.tabla_lista_compras.grid(row=1, column=0,columnspan=3)
        self.tabla_lista_compras.heading('#0', text='Id', anchor=CENTER)
        self.tabla_lista_compras.column(column='#0',width=150)
        self.tabla_lista_compras.heading('#1', text='Categoria', anchor=CENTER)
        self.tabla_lista_compras.column(column='#1', width=150)
        self.tabla_lista_compras.heading('#2', text='Color', anchor=CENTER)
        self.tabla_lista_compras.column(column='#2', width=150)
        self.tabla_lista_compras.heading('#3', text='Marca', anchor=CENTER)
        self.tabla_lista_compras.column(column='#3', width=150)
        self.tabla_lista_compras.heading('#4',text = 'Precio', anchor = CENTER)
        self.tabla_lista_compras.column(column='#4', width=150)

        self.db_get_lista_compras()


        ladoy = ttk.Scrollbar(self.frame_tabla_lista_compras, orient = 'vertical', command = self.tabla_lista_compras.yview)
        ladoy.grid(row= 1, column = 3, sticky = 'ns')
        self.tabla_compras.configure(yscrollcommand = ladoy.set)

        ############ OCULTAR LA VENTANA PRINCIPAL #################
        self.ventana.withdraw()  # ocultar la ventana principal

    #Estado de las paginas del Notebook

    def pagina_principal(self):
        self.paginas.select([self.pagina_uno])

    def pagina_compras(self):
        self.paginas.select([self.pagina_dos])

    def pagina_lista_compra(self):
        self.paginas.select([self.pagina_tres])

    #Base de Datos

    def db_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta,parametros)
            con.commit()
        return resultado

    def db_get_compra(self,*args):
        registros_tabla = self.tabla_compras.get_children()
        for fila in registros_tabla:
            self.tabla_compras.delete(fila)
        query = 'SELECT * FROM Inventario ORDER BY categoria DESC'
        registros = self.db_consulta(query)
        for fila in registros:
            print(fila)
            self.tabla_compras.insert('',0,text = fila[0],values = (fila[1],fila[2],fila[3],fila[4]))


    def db_get_lista_compras(self):
        registros_tabla = self.tabla_lista_compras.get_children()
        for fila in registros_tabla:
            self.tabla_lista_compras.delete(fila)
        query = 'SELECT * FROM lista_de_compras ORDER BY categoria DESC'
        registros = self.db_consulta(query)
        self.total_compra = 0
        for fila in registros:
            print(fila)
            print(self.total_compra)
            self.total_compra += fila[4]
            self.tabla_lista_compras.insert('', 0, text=fila[0], values=(fila[1], fila[2], fila[3],fila[4]))

        self.total = Label(self.pagina_tres, text='TOTAL' + ': ' + str(self.total_compra) + '$',
                           font=('Calibri', 16, 'bold'), background='black', foreground='#4FA1CA')
        self.total.grid(row=2, column=2, sticky='ne', ipadx=20)

    #Funcion del boton comprar

    def boton_comprar(self):
        try:
            query= "CREATE TABLE 'lista_de_compras' ('id' INTEGER NOT NULL UNIQUE, 'Categoria'	TEXT NOT NULL, 'Color' TEXT NOT NULL, 'Marca'	TEXT NOT NULL, 'Precio' INTEGER NOT NULL, PRIMARY KEY('id' AUTOINCREMENT))"
            self.db_consulta(query,parametros=())
        except:
            pass
        try:
            self.tabla_compras.item(self.tabla_compras.selection())['values'][0]
        except IndexError as e:
            messagebox.showwarning('Error','¡Por Favor! Selecciona un Producto')
            return

        categoria = self.tabla_compras.item(self.tabla_compras.selection())['values'][0]
        color = self.tabla_compras.item(self.tabla_compras.selection())['values'][1]
        marca = self.tabla_compras.item(self.tabla_compras.selection())['values'][2]
        precio = self.tabla_compras.item(self.tabla_compras.selection())['values'][3]
        parametros = (categoria, color, marca, precio)
        query = 'SELECT inventario.stock FROM inventario WHERE categoria = ? AND color = ? AND marca = ? AND precio_venta= ?'
        stock = self.db_consulta(query,parametros)
        if stock.fetchone()[0] > 0:
            stock.close()
            query = 'INSERT INTO lista_de_compras VALUES(NULL,?, ?, ?, ?)'
            print(parametros)
            actualizar = self.db_consulta(query, parametros)
            actualizar.close()

            query = 'SELECT inventario.stock FROM inventario WHERE categoria = ? AND color = ? AND marca = ? AND precio_venta = ?'
            stock_antiguo = self.db_consulta(query, parametros)
            stock = stock_antiguo.fetchone()[0]
            stock_nuevo = stock - 1
            stock_antiguo.close()

            parametros_nuevo = (stock_nuevo, categoria,color,marca)
            query = 'UPDATE inventario SET stock = ? WHERE categoria = ? AND color = ? AND marca = ?'
            inventario_act = self.db_consulta(query, parametros_nuevo)
            inventario_act.close()

            messagebox.showinfo('Correcto', '''      -Compra Realizada con ¡EXITO! 
            Recuerda ir a la lista de compras a terminar tu Compra!''')
        else:
            messagebox.showerror('Lo Siento', 'El Articulo seleccionado se encuentra agotado!')

        self.db_get_lista_compras()

    #Boton eliminar

    def boton_eliminar(self):

        try:
            self.tabla_lista_compras.item(self.tabla_lista_compras.selection())['values'][0]
        except IndexError as e:
            messagebox.showwarning('Error','¡Por Favor! Selecciona un Producto')
            return

        id = self.tabla_lista_compras.item(self.tabla_lista_compras.selection())['text']
        categoria = self.tabla_lista_compras.item(self.tabla_lista_compras.selection())['values'][0]
        color = self.tabla_lista_compras.item(self.tabla_lista_compras.selection())['values'][1]
        marca = self.tabla_lista_compras.item(self.tabla_lista_compras.selection())['values'][2]
        precio = self.tabla_lista_compras.item(self.tabla_lista_compras.selection())['values'][3]
        query = 'DELETE FROM lista_de_compras WHERE id = ?'
        parametros = (id)
        print(parametros)
        eliminar = self.db_consulta(query,(parametros,))
        eliminar.close()

        parametros = (categoria,color,marca,precio)
        query = 'SELECT inventario.stock FROM inventario WHERE categoria = ? AND color = ? AND marca = ? AND precio_venta = ?'
        stock_antiguo = self.db_consulta(query, parametros)
        stock = stock_antiguo.fetchone()[0]
        stock_nuevo = stock + 1
        stock_antiguo.close()

        parametros_nuevo = (stock_nuevo, categoria, color, marca)
        query = 'UPDATE inventario SET stock = ? WHERE categoria = ? AND color = ? AND marca = ?'
        inventario_act = self.db_consulta(query, parametros_nuevo)
        inventario_act.close()

        self.db_get_lista_compras()

    #Boton terminar compra
    def boton_terminar_compra(self):
        try:
            if self.total_compra <= 0:
                raise ValueError
        except ValueError as e:
            messagebox.showwarning('Error', '¡Por Favor! Añade un Producto')
            return

        query = 'SELECT * FROM lista_de_compras'
        resultado = self.db_consulta(query, )
        parametros = []

        for fila in resultado:
            print(fila)

            parametros.append(fila)
        resultado.close()

        for row in parametros:
            query = 'DELETE FROM lista_de_compras WHERE id = ?'
            eliminar = self.db_consulta(query,(row[0],))
            eliminar.close()
        messagebox.showinfo('PERFECTO', '¡Tu compra se ha cealizado con EXITO!')
        self.db_get_lista_compras()

    def cerrar_sesion(self):
        self.ventana.deiconify()
        self.ventana_cliente.destroy()

