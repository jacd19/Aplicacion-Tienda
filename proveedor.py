import sqlite3
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

class Ventana_proveedor:

    db = 'database/proyecto.db'

    def __init__(self,toplevel,ventana_principal):
        self.ventana = ventana_principal
        self.ventana_proveedor = toplevel
        self.ventana_proveedor.title("Ventana Proveedro")
        self.ventana_proveedor.geometry('830x565+250+50')

        # FRAMES

        self.frame_titulo = Frame(self.ventana_proveedor, background='black', width=500, height=50)
        self.frame_titulo.grid(row=0, column=1, sticky='nsew')
        self.frame_menu = Frame(self.ventana_proveedor, background='black', width=60, height=560)
        self.frame_menu.grid(row=0, column=0, rowspan=2, sticky='nsew')
        self.frame_info = Frame(self.ventana_proveedor, background='black', width=500, height=500)
        self.frame_info.grid(row=1, column=1, sticky='nsew')

        self.widgets()

    def forma_imagen(self, nombre):
        self.imagen = Image.open(nombre)
        self.imagen = self.imagen.resize((45, 45))
        self.imagen.save(nombre)
        return ImageTk.PhotoImage(self.imagen)

    def forma_imagen_principal(self, nombre):
        self.imagen = Image.open(nombre)
        self.imagen = self.imagen.resize((765, 494))
        self.imagen.save(nombre)
        return ImageTk.PhotoImage(self.imagen)

    def forma_imagen_prox(self, nombre):
        self.imagen = Image.open(nombre)
        self.imagen = self.imagen.resize((300, 300))
        self.imagen.save(nombre)
        return ImageTk.PhotoImage(self.imagen)

    def widgets(self):

        #FRAME TITULO

        #etiqueta para el titulo
        self.etiqueta_titulo = Label(self.frame_titulo,text = ('Innovative Compani JACD'), font = ('perpetua',20,'bold'),bg = 'black',fg = 'White')
        self.etiqueta_titulo.grid(row=0, column= 0, sticky = 'nsew', ipadx=210,ipady=10)

        #FRAME MENU

        #imagenes
        self.home = self.forma_imagen('imagenes/menu.png')
        self.inventario = self.forma_imagen('imagenes/inventario.png')
        self.ag_pedido = self.forma_imagen('imagenes/ag_pedido.png')
        self.salir = self.forma_imagen('imagenes/salir.png')
        self.img_principal = self.forma_imagen_principal('imagenes/imagen_pedido_proveedor.jpg')
        self.img_prox = self.forma_imagen_prox('imagenes/imagen_prox.png')

        #Botones del menu
        self.boton_home = Button(self.frame_menu,image = self.home,bg = 'black', activebackground = 'black', bd = 0,command = self.pagina_principal)
        self.boton_home.grid(row= 0, column= 0, sticky = 'nsew', ipady = 10, ipadx = 8)
        self.boton_inventario = Button(self.frame_menu, image = self.inventario,bg = 'black', activebackground = 'black',bd = 0,command = self.pagina_inventario)
        self.boton_inventario.grid(row = 1,column = 0, sticky = 'nsew', ipady = 30, ipadx = 8)
        self.boton_ag_pedido = Button(self.frame_menu, image = self.ag_pedido,bg = 'black', activebackground = 'black', bd = 0,command = self.pagina_pedidos)
        self.boton_ag_pedido.grid(row = 2,column = 0, sticky = 'nsew')
        Label(self.frame_menu,text = '',bg = 'black').grid(row=4,column = 0, sticky = 'nsew',pady=120)#Etiqueta de espacio para baja el boton salida
        self.boton_salir = Button(self.frame_menu, image = self.salir,bg='black',activebackground='black',bd=0,command=self.cerrar_sesion)
        self.boton_salir.grid(row=5,column=0,sticky='nsew')



        #FRAME INFO

        # Estilo de paginas
        estilo_paginas = ttk.Style()
        estilo_paginas.configure('MyStyle.TNotebook', background='black', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure('MyStyle.TNotebook', background='black', borderwidth=0)
        estilo_paginas.configure('MyStyle.TNotebook.Tab', background='black', borderwidth=0)
        estilo_paginas.map('MyStyle.TNotebook.Tab', background=[('selected', 'black')], foreground=[('selected', 'black')])

        #Creacion de paginas
        self.paginas = ttk.Notebook(self.frame_info, style = 'MyStyle.TNotebook')
        self.paginas.grid( row=0,column=0,sticky = 'nsew')
        self.pagina_uno = Frame(self.paginas,bg = 'black')
        self.pagina_dos = Frame(self.paginas,bg = 'black')
        self.pagina_tres = Frame(self.paginas,bg = '#4FA1CA')
        self.paginas.add(self.pagina_uno)
        self.paginas.add(self.pagina_dos)
        self.paginas.add(self.pagina_tres)

        # Pagina Uno

        self.imagen_principal = Label(self.pagina_uno, image=self.img_principal, bg='black')
        self.imagen_principal.grid(row = 0,column = 0)

        # Pagina Dos - Inventario

        #Encabezado
        self.encabezado = Label(self.pagina_dos, text = 'INVENTARIO', font=('Calibri',16,'bold'),bg = 'black',fg='#4FA1CA')
        self.encabezado.grid(row = 0,column=0,sticky='nsew',padx=150)

        #Boton Pedir al Proveedor
        estilo_boton_pedir = ttk.Style()
        estilo_boton_pedir.configure('mystyle.TButton', font=('Arial', 12, 'bold'), foreground='white', background='#4FA1CA', relief = 'flat')
        estilo_boton_pedir.map('mystyle.TButton', foreground=[('active', '!disabled', 'black')],background=[('active', 'white')])
        self.boton_pedir = ttk.Button(self.pagina_dos, text='Pedir al Proveedor', style='mystyle.TButton',command = self.ag_pedidos)
        self.boton_pedir.grid(row=0, column=1, sticky='ne', padx=20)

        #Treeview Inventario

        #Estilo
        estilo_tabla = ttk.Style()
        estilo_tabla.configure('MyStyle.Treeview',highlightthickness = 0,bd = 0, font = ('Calibri',11),width = 2)
        estilo_tabla.configure('MyStyle.Treeview.Heading',font = ('Calibri',13,'bold'),background = 'white')

        self.frame_tabla_inventario = Frame (self.pagina_dos)
        self.frame_tabla_inventario.grid(row = 1,column = 0, columnspan = 2)

        self.tabla_inventario = ttk.Treeview(self.frame_tabla_inventario,height = 21,columns = ('1','2','3','4'),style = 'MyStyle.Treeview')
        self.tabla_inventario.grid(row = 1, column = 0, columnspan = 2,sticky = 'nsew')
        self.tabla_inventario.heading('#0', text='Id', anchor=CENTER)
        self.tabla_inventario.column('#0', width=150)
        self.tabla_inventario.heading('#1', text = 'Categoria', anchor = CENTER)
        self.tabla_inventario.column('#1', width = 150)
        self.tabla_inventario.heading('#2', text = 'Color', anchor = CENTER)
        self.tabla_inventario.column('#2', width = 150)
        self.tabla_inventario.heading('#3', text = 'Marca', anchor = CENTER)
        self.tabla_inventario.column('#3', width = 150)
        self.tabla_inventario.heading('#4', text = 'Stock', anchor = CENTER)
        self.tabla_inventario.column('#4', width  = 150)

        ladoy = ttk.Scrollbar(self.frame_tabla_inventario, orient = 'vertical',command = self.tabla_inventario.yview)
        ladoy.grid(column = 2, row = 1, sticky = 'ns')
        self.tabla_inventario.configure(yscrollcommand = ladoy.set)

        #Pagina Tres - Pedidos

        #Etiquetas
        self.etiqueta_pedido = Label(self.pagina_tres, text = 'Pedidos a Proveedores', font = ('Lucida Bright',24,'bold'),bg = '#4FA1CA',fg = 'white')
        self.etiqueta_pedido.grid(row = 0, column = 0, sticky = 'nsew',columnspan = 3,pady = 27,ipadx = 170)

        self.etiqueta_cat = Label(self.pagina_tres, text = 'Categoria:', font = ('Calibri',18,'bold'),bg = '#4FA1CA',fg= 'white')
        self.etiqueta_cat.grid(row=1,column= 0,sticky = 'nse',pady = 30)
        self.etiqueta_col = Label(self.pagina_tres, text='Color:', font=('Calibri', 18, 'bold'), bg='#4FA1CA',fg='white')
        self.etiqueta_col.grid(row=2, column=0, sticky='nse')
        self.etiqueta_mar = Label(self.pagina_tres, text='Marca:', font=('Calibri', 18, 'bold'), bg='#4FA1CA',fg='white')
        self.etiqueta_mar.grid(row=3, column=0, sticky='nse',pady = 30)
        self.etiqueta_cant = Label(self.pagina_tres, text='Cantidad:', font=('Calibri', 18, 'bold'), bg='#4FA1CA',fg='white')
        self.etiqueta_cant.grid(row=4, column=0, sticky='nse')

        #Combo Box


        self.lista_cat = {'Seleccionar', }
        self.lista_categoria(self.lista_cat)

        self.combo_cat = ttk.Combobox(self.pagina_tres,height = 30,width = '10',values = list(self.lista_cat),state = 'readonly', font=('Arial',13))
        self.combo_cat.grid(row = 1,column = 1,ipady = 3)
        self.combo_cat.set('Seleccionar')

        self.lista_col = {'Seleccionar',}
        self.lista_color(self.lista_col)
        self.combo_col = ttk.Combobox(self.pagina_tres, height='15', width='10', values=list(self.lista_col),state='readonly', font=('Arial', 13))
        self.combo_col.grid(row=2, column=1,ipady = 3 )
        self.combo_col.set('Seleccionar')

        self.lista_mar = {'Seleccionar',}
        self.lista_marca(self.lista_mar)
        self.combo_mar = ttk.Combobox(self.pagina_tres, height='15', width='10', values=list(self.lista_mar),state='readonly', font=('Arial', 13))
        self.combo_mar.grid(row=3, column=1,ipady = 3)
        self.combo_mar.set('Seleccionar')

        self.combo_cant = ttk.Combobox(self.pagina_tres, height='15', width='10', values=('Seleccionar', '10','20','30','40','50'),state='readonly', font=('Arial', 13))
        self.combo_cant.grid(row=4, column=1,ipady = 3)
        self.combo_cant.set('Seleccionar')

        #Botones -Cancelar y hacer pedido
        estilo_boton_limpiar = ttk.Style()
        estilo_boton_limpiar.configure('my.TButton', font=('Calibri', 12, 'bold'), foreground='black', background='#FF2C2E')
        self.boton_limpiar = ttk.Button(self.pagina_tres, text= 'LIMPIAR',command = self.limpiar,style = 'my.TButton')
        self.boton_limpiar.grid(row = 5,column= 0,pady = 30)

        estilo_boton_hacer_pedido = ttk.Style()
        estilo_boton_hacer_pedido.configure('pedidomy.TButton', font=('Calibri', 12, 'bold'), foreground='black',background='#87FF5D')
        self.boton_hacer_pedido= ttk.Button(self.pagina_tres, text= 'HACER PEDIDO',style = 'pedidomy.TButton',command = self.hacer_pedido)
        self.boton_hacer_pedido.grid(row= 5,column= 1,pady = 30)

        self.get_productos()

        #Imagen Para ocupar espacio
        Label(self.pagina_tres, image = self.img_prox,bg ='#4FA1CA' ).grid(row=1,column=2,rowspan=5,ipady=30)

        ############ OCULTAR LA VENTANA PRINCIPAL #################
        self.ventana.withdraw()  # ocultar la ventana principal


    #Estado de las paginas Notebook

    def pagina_principal(self):
        self.paginas.select([self.pagina_uno])


    def pagina_inventario(self):
        self.paginas.select([self.pagina_dos])
        self.get_productos()

    def pagina_pedidos(self):
        self.paginas.select([self.pagina_tres])

    def db_consulta(self,consulta,parametros = ()):
        with sqlite3.connect(self.db) as con :
            cursor = con.cursor()
            resultado= cursor.execute(consulta,parametros)
            con.commit()
        return resultado

    def get_productos(self):
        registros_tabla= self.tabla_inventario.get_children()
        for fila in registros_tabla:
            self.tabla_inventario.delete(fila)
        query = 'SELECT * FROM inventario ORDER BY categoria DESC'
        registros= self.db_consulta(query)
        for fila in registros:
            self.tabla_inventario.insert('',0, text= fila[0], values= (fila[1],fila[2],fila[3],fila[5]))

    def lista_categoria(self,lista ):
        query = 'SELECT inventario.categoria FROM inventario'
        registro = self.db_consulta(query)
        for i in registro:
            lista.add(i)

    def lista_color(self,lista ):
        query = 'SELECT inventario.color FROM inventario'
        registro = self.db_consulta(query)
        for i in registro:
            lista.add(i)

    def lista_marca(self,lista ):
        query = 'SELECT inventario.marca FROM inventario'
        registro = self.db_consulta(query)
        for i in registro:
            lista.add(i)

    def ag_pedidos(self):
        try:
            self.cat = self.tabla_inventario.item(self.tabla_inventario.selection())['values'][0]
            self.col = self.tabla_inventario.item(self.tabla_inventario.selection())['values'][1]
            self.marc = self.tabla_inventario.item(self.tabla_inventario.selection())['values'][2]

            self.combo_cat.set(self.cat)
            self.combo_col.set(self.col)
            self.combo_mar.set(self.marc)
            self.combo_cant.set('Seleccionar')

            self.paginas.select([self.pagina_tres])
        except IndexError as e :
            messagebox.showwarning('Error','¡Por Favor! Selecciona un Producto')
            return

    def limpiar(self):
        self.combo_cat.set('Seleccionar')
        self.combo_col.set('Seleccionar')
        self.combo_mar.set('Seleccionar')
        self.combo_cant.set('Seleccionar')

    def hacer_pedido(self):
        if self.combo_cat.get() != 'Seleccionar' and self.combo_col.get() != 'Seleccionar' and self.combo_mar.get() != 'Seleccionar' and self.combo_cant.get() != 'Seleccionar':
            try:
                parametros= (self.combo_cat.get(),self.combo_col.get(),self.combo_mar.get())
                query = 'SELECT inventario.stock FROM inventario WHERE categoria =? AND color= ? AND marca= ?'
                stock = self.db_consulta(query,parametros)
                stock_nuevo = stock.fetchone()[0] + int(self.combo_cant.get())
                print(stock_nuevo)
                stock.close()
                parametros_act= (stock_nuevo,self.combo_cat.get(),self.combo_col.get(),self.combo_mar.get())
                query = 'UPDATE inventario SET stock = ? WHERE categoria = ? AND color= ? AND marca= ?'
                inventario_act = self.db_consulta(query,parametros_act)
                inventario_act.close()
                messagebox.showinfo('','Se ha hecho el pedido con EXITO!')
            except:
                messagebox.showwarning('Error','La Seleccion de Articulos no existe en el Inventario')


        else:
            messagebox.showwarning('Error','Te falta agregar algun dato!')

    def cerrar_sesion(self):
        self.ventana.deiconify()
        self.ventana_proveedor.destroy()
