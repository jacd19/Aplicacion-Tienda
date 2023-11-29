import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk# instalar PIL para poder modificar el tamaño da las imagenes
import matplotlib.pyplot as plt# instalar matplotlib para poder crear las graficas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Ventana_admin:

    db= 'database/proyecto.db'

    def __init__(self, toplevel,ventana_principal):
        self.ventana = ventana_principal
        self.ventana_admin = toplevel
        self.ventana_admin.title("Ventana Admin")
        self.ventana_admin.geometry('830x565+250+50')

        '#FRAMES'

        self.frame_titulo= Frame(self.ventana_admin,background= 'black', width= 500, height= 50)
        self.frame_titulo.grid(row= 0, column= 1,sticky= 'nsew')
        self.frame_menu= Frame(self.ventana_admin, background= 'black',width=60,height= 560)
        self.frame_menu.grid(row= 0, column= 0, rowspan= 2, sticky= 'nsew')
        self.frame_info= Frame(self.ventana_admin, background= 'white', width= 500, height= 500)
        self.frame_info.grid(row= 1, column= 1, sticky= 'nsew')

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

    def forma_imagen_productos(self, nombre):
        self.imagen = Image.open(nombre)
        self.imagen = self.imagen.resize((180, 300))
        self.imagen.save(nombre)
        return ImageTk.PhotoImage(self.imagen)

    def widgets(self):

        #FRAME TITULO

        #Etiqueta para el titulo
        self.etiqueta_titulo = Label(self.frame_titulo, text=('Innovative Compani JACD'), font=('perpetua', 20, 'bold'),
                                     bg='black', fg='White')
        self.etiqueta_titulo.grid(row=0, column=0, sticky='nsew', ipadx=210, ipady=10)

        #FRAME MENU

        #Imagenes
        self.home_imagen= self.forma_imagen('imagenes/menu.png')
        self.db_imagen= self.forma_imagen('imagenes/base_de_datos.png')
        self.editar_imagen= self.forma_imagen('imagenes/editar.png')
        self.ag_producto_imagen= self.forma_imagen('imagenes/ag_producto.png')
        self.graficas_imagen= self.forma_imagen('imagenes/graficas.png')
        self.salir_imagen= self.forma_imagen('imagenes/salir.png')
        self.imagen_admin= self.forma_imagen_principal('imagenes/imagen_admin.jpg')
        self.imagen_crear_archivo= self.forma_imagen_productos('imagenes/crear_archivo.png')
        self.imagen_editar_archivo= self.forma_imagen_productos('imagenes/editar_archivo.png')

        #Botones del Menu
        self.boton_home= Button(self.frame_menu, image= self.home_imagen, bg= 'black', activebackground= 'black', bd= 0, command= self.pagina_principal)
        self.boton_home.grid(row= 0, column= 0, sticky= 'nsew', ipady= 15, ipadx= 8)
        self.boton_db= Button(self.frame_menu, image= self.db_imagen, bg= 'black', activebackground= 'black', bd= 0, command= self.pagina_db)
        self.boton_db.grid(row= 1, column= 0, sticky= 'nsew', ipady= 30, ipadx= 8)
        self.boton_editar= Button(self.frame_menu, image= self.editar_imagen, bg= 'black', activebackground= 'black', bd= 0, command= self.pagina_editar)
        self.boton_editar.grid(row=2 ,column=0, sticky= 'nsew', ipadx= 8)
        self.boton_ag_producto= Button(self.frame_menu, image= self.ag_producto_imagen, bg= 'black', activebackground= 'black', bd= 0, command= self.pagina_agregar)
        self.boton_ag_producto.grid(row= 3, column= 0, sticky= 'nsew',ipady=30, ipadx=8)
        self.boton_graficas= Button(self.frame_menu, image= self.graficas_imagen, bg= 'black', activebackground= 'black', bd= 0, command= self.pagina_graficas)
        self.boton_graficas.grid(row= 4, column=0, sticky= 'nsew', ipadx= 8)
        Label(self.frame_menu, text= ' ', bg= 'black').grid(row= 5, column= 0, ipady= 45)# Espacio para bajar el boton salida
        self.boton_salir= Button(self.frame_menu, image= self.salir_imagen, bg= 'black', activebackground= 'black', bd= 0,command=self.cerrar_sesion)
        self.boton_salir.grid(row= 6, column=0, sticky= 'nsew')

        # FRAME INFO

        #Estilo de paginas
        estilo_paginas= ttk.Style()
        estilo_paginas.configure('MyStyle.TNotebook', background='black', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure('MyStyle.TNotebook', background='black', borderwidth=0)
        estilo_paginas.configure('MyStyle.TNotebook.Tab', background='black', borderwidth=0)
        estilo_paginas.map('MyStyle.TNotebook.Tab', background=[('selected', 'black')], foreground=[('selected', 'black')])

        #Creacion de paginas
        self.paginas= ttk.Notebook(self.frame_info, style= 'MyStyle.TNotebook')
        self.paginas.grid(row=0, column=0, sticky='nsew')
        self.pagina_uno = Frame(self.paginas, bg='black')
        self.pagina_dos = Frame(self.paginas, bg='black')
        self.pagina_tres = Frame(self.paginas, bg='#4FA1CA')
        self.pagina_cuatro= Frame(self.paginas, bg='#2C539D')
        self.pagina_cinco= Frame(self.paginas, bg= 'cyan')
        self.paginas.add(self.pagina_uno)
        self.paginas.add(self.pagina_dos)
        self.paginas.add(self.pagina_tres)
        self.paginas.add(self.pagina_cuatro)
        self.paginas.add(self.pagina_cinco)

        # Pagina uno
        self.imagen_principal= Label(self.pagina_uno, image= self.imagen_admin, bg= 'black')
        self.imagen_principal.grid(row=0, column=0)

        # Pagina dos - Base de Datos

        #Encabezado
        self.encabezado_db= Label(self.pagina_dos, text= 'Base de Datos', font= ('Calibri',16,'bold'),bg= 'black', fg='#4FA1CA')
        self.encabezado_db.grid(row= 0,column= 0, sticky= 'nsew', padx= 150)

        #Boton Eliminar
        estilo_boton_eliminar= ttk.Style()
        estilo_boton_eliminar.configure('Eliminar.TButton', font=('Calibri',14,'bold'),foreground= 'black', background= 'red')
        self.boton_eliminar = ttk.Button(self.pagina_dos, text= 'Eliminar',style= 'Eliminar.TButton', command= self.eliminar_producto)
        self.boton_eliminar.grid(row=0, column= 1)

        #Boton Editar
        estilo_boton_editar = ttk.Style()
        estilo_boton_editar.configure('Editar.TButton', font=('Calibri', 14, 'bold'), foreground='black',
                                        background='#4FA1CA')
        self.boton_editar = ttk.Button(self.pagina_dos, text='Editar', style='Editar.TButton',command=self.editar_pasar_producto)
        self.boton_editar.grid(row=0, column=2)

        #Treeview base de datos
        estilo_tabla= ttk.Style()
        estilo_tabla.configure('MyStyle.Treeview',highlightthickness = 0,bd = 0, font = ('Calibri',11),width = 2)
        estilo_tabla.configure('MyStyle.Treeview.Heading',font = ('Calibri',13,'bold'),background = 'white')

        self.frame_tabla_db = Frame(self.pagina_dos)
        self.frame_tabla_db.grid(row=1, column=0, columnspan=3)

        self.tabla_db = ttk.Treeview(self.frame_tabla_db, height=21, columns=('1', '2', '3', '4','5','6'),
                                             style='MyStyle.Treeview')
        self.tabla_db.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.tabla_db.heading('#0', text='Id', anchor=CENTER)
        self.tabla_db.column('#0', width=50)
        self.tabla_db.heading('#1', text='Categoria', anchor=CENTER)
        self.tabla_db.column('#1', width=150)
        self.tabla_db.heading('#2', text='Color', anchor=CENTER)
        self.tabla_db.column('#2', width=100)
        self.tabla_db.heading('#3', text='Marca', anchor=CENTER)
        self.tabla_db.column('#3', width=110)
        self.tabla_db.heading('#4', text='Stock', anchor=CENTER)
        self.tabla_db.column('#4', width=100)
        self.tabla_db.heading('#5', text='Prec. Venta', anchor=CENTER)
        self.tabla_db.column('#5', width=120)
        self.tabla_db.heading('#6', text='Prec. Compra', anchor=CENTER)
        self.tabla_db.column('#6', width=120)

        ladoy = ttk.Scrollbar(self.frame_tabla_db, orient='vertical', command=self.tabla_db.yview)
        ladoy.grid(column=2, row=1, sticky='ns')
        self.tabla_db.configure(yscrollcommand=ladoy.set)

        # Pagina tres - Editar Productos

        #Etiquetas
        self.agregar_titulo = Label(self.pagina_tres, text= 'Editar Producto', font= ('Lucida Bright', 24,'bold'), bg= '#4FA1CA', fg= 'white')
        self.agregar_titulo.grid(row= 0, column= 0, sticky= 'nsew', ipady=30, columnspan=3,padx=110)

        self.etiqueta_cat= Label(self.pagina_tres, text= 'Categoria', font= ('Calibri',18,'bold'),  bg= '#4FA1CA', fg= 'white')
        self.etiqueta_cat.grid(row= 1, column= 0)
        self.etiqueta_col= Label(self.pagina_tres, text= 'Color', font=('Calibri',18,'bold'), bg= '#4FA1CA',fg= 'white')
        self.etiqueta_col.grid(row= 2, column= 0,pady= 10)
        self.etiqueta_mar= Label(self.pagina_tres, text= 'Marca', font= ('Calibri',18,'bold'), bg= '#4FA1CA', fg= 'white')
        self.etiqueta_mar.grid(row=3, column= 0)
        self.etiqueta_stock= Label(self.pagina_tres, text= 'Stock', font= ('Calibri',18,'bold'), bg= '#4FA1CA', fg= 'white')
        self.etiqueta_stock.grid(row= 4, column=0,pady=10)
        self.etiqueta_prec_venta= Label(self.pagina_tres, text= 'Precio Venta', font= ('Calibri',18,'bold'), bg= '#4FA1CA', fg= 'white')
        self.etiqueta_prec_venta.grid(row= 5, column= 0)
        self.etiqueta_prec_compra= Label(self.pagina_tres, text= 'Precio Compra', font=('Calibri',18,'bold'), bg= '#4FA1CA', fg= 'white')
        self.etiqueta_prec_compra.grid(row= 6, column= 0,pady=10)

        #imagen editar
        self.etiqueta_imagen_editar= Label(self.pagina_tres, image= self.imagen_editar_archivo,  bg="#4FA1CA")
        self.etiqueta_imagen_editar.grid(row= 1, column= 3, rowspan=7,padx=5)

        # Entry con informacion actual
        self.categoria_act = StringVar()
        self.info_act_cat = Entry(self.pagina_tres, textvariable=self.categoria_act,state='readonly')
        self.info_act_cat.grid(row=1, column=1)

        self.color_act = StringVar()
        self.info_act_col = Entry(self.pagina_tres, textvariable=self.color_act,state='readonly')
        self.info_act_col.grid(row=2, column=1)

        self.marca_act = StringVar()
        self.info_act_mar = Entry(self.pagina_tres, textvariable=self.marca_act,state='readonly')
        self.info_act_mar.grid(row=3, column=1)

        self.stock_act = StringVar()
        self.info_act_stock = Entry(self.pagina_tres, textvariable=self.stock_act,state='readonly')
        self.info_act_stock.grid(row=4, column=1)

        self.prec_venta_act = StringVar()
        self.info_act_prec_venta = Entry(self.pagina_tres, textvariable=self.prec_venta_act,state='readonly')
        self.info_act_prec_venta.grid(row=5, column=1)

        self.prec_compra_act = StringVar()
        self.info_act_prec_compra = Entry(self.pagina_tres, textvariable=self.prec_compra_act,state='readonly')
        self.info_act_prec_compra.grid(row=6, column=1)

        # Entry para editar
        self.categoria_edit = StringVar()
        self.info_edit_cat = Entry(self.pagina_tres, textvariable=self.categoria_edit)
        self.info_edit_cat.grid(row=1, column=2)

        self.color_edit = StringVar()
        self.info_edit_col = Entry(self.pagina_tres, textvariable=self.color_edit)
        self.info_edit_col.grid(row=2, column=2)

        self.marca_edit = StringVar()
        self.info_edit_mar = Entry(self.pagina_tres, textvariable=self.marca_edit)
        self.info_edit_mar.grid(row=3, column=2)

        self.stock_edit = StringVar()
        self.info_edit_stock = Entry(self.pagina_tres, textvariable=self.stock_edit)
        self.info_edit_stock.grid(row=4, column=2)

        self.prec_venta_edit = StringVar()
        self.info_edit_prec_venta = Entry(self.pagina_tres, textvariable=self.prec_venta_edit)
        self.info_edit_prec_venta.grid(row=5, column=2)

        self.prec_compra_edit = StringVar()
        self.info_edit_prec_compra = Entry(self.pagina_tres, textvariable=self.prec_compra_edit)
        self.info_edit_prec_compra.grid(row=6, column=2)

        # Botones editar y limpiar
        self.boton_actualizar = ttk.Button(self.pagina_tres, text='Actualizar', style='Editar.TButton',command= self.actualizar_producto)
        self.boton_actualizar.grid(row=7, column=0,columnspan=2,pady=10)

        estilo_boton_limpiar = ttk.Style()
        estilo_boton_limpiar.configure('Limpiar.TButton', font=('Calibri', 14, 'bold'), foreground='black',
                                       background='orange')
        self.boton_limpiar_edit = ttk.Button(self.pagina_tres, text='Limpiar', style='Limpiar.TButton',command=self.limpiar_edit_producto)
        self.boton_limpiar_edit.grid(row=7, column=1,columnspan=2,pady=10)

        # Pagina Cuatro - Agregar

        #Etiquetas
        self.agregar_titulo = Label(self.pagina_cuatro, text='Agregar Producto', font=('Lucida Bright', 24, 'bold'),
                                    bg='#2C539D', fg='white')
        self.agregar_titulo.grid(row=0, column=0, sticky='nsew', ipady=30, columnspan=2,padx=90)

        self.etiqueta_cat = Label(self.pagina_cuatro, text='Categoria', font=('Calibri', 18, 'bold'), bg='#2C539D',
                                  fg='white')
        self.etiqueta_cat.grid(row=1, column=0)
        self.etiqueta_col = Label(self.pagina_cuatro, text='Color', font=('Calibri', 18, 'bold'), bg='#2C539D',
                                  fg='white')
        self.etiqueta_col.grid(row=2, column=0,pady=10)
        self.etiqueta_mar = Label(self.pagina_cuatro, text='Marca', font=('Calibri', 18, 'bold'), bg='#2C539D',
                                  fg='white')
        self.etiqueta_mar.grid(row=3, column=0)
        self.etiqueta_stock = Label(self.pagina_cuatro, text='Stock', font=('Calibri', 18, 'bold'), bg='#2C539D',
                                    fg='white')
        self.etiqueta_stock.grid(row=4, column=0,pady=10)
        self.etiqueta_prec_venta = Label(self.pagina_cuatro, text='Precio Venta', font=('Calibri', 18, 'bold'),
                                         bg='#2C539D', fg='white')
        self.etiqueta_prec_venta.grid(row=5, column=0)
        self.etiqueta_prec_compra = Label(self.pagina_cuatro, text='Precio Compra', font=('Calibri', 18, 'bold'),
                                          bg='#2C539D', fg='white')
        self.etiqueta_prec_compra.grid(row=6, column=0,pady=10)

        #imagen
        self.etiqueta_imagen_crear= Label(self.pagina_cuatro, image= self.imagen_crear_archivo, bg="#2C539D")
        self.etiqueta_imagen_crear.grid(row= 1,column= 2,rowspan= 7)

        #Entry para agregar productos
        self.categoria_agg = StringVar()
        self.entrada_cat= Entry(self.pagina_cuatro, textvariable= self.categoria_agg)
        self.entrada_cat.grid( row=1, column=1)

        self.color_agg= StringVar()
        self.entrada_col= Entry(self.pagina_cuatro, textvariable= self.color_agg)
        self.entrada_col.grid(row= 2, column=1)

        self.marca_agg= StringVar()
        self.entrada_mar= Entry(self.pagina_cuatro, textvariable= self.marca_agg)
        self.entrada_mar.grid(row= 3, column= 1)

        self.stock_agg= StringVar()
        self.entrada_stock= Entry(self.pagina_cuatro, textvariable= self.stock_agg)
        self.entrada_stock.grid(row= 4, column=1)

        self.prec_venta_agg=StringVar()
        self.entrada_prec_venta= Entry(self.pagina_cuatro,textvariable= self.prec_venta_agg)
        self.entrada_prec_venta.grid(row= 5, column= 1)

        self.prec_compra_agg= StringVar()
        self.entrada_prec_compra= Entry( self.pagina_cuatro, textvariable= self.prec_compra_agg)
        self.entrada_prec_compra.grid(row= 6, column=1)

        #Botones agregar y limpiar
        self.boton_agregar= ttk.Button(self.pagina_cuatro, text='Agregar', style='Editar.TButton', command = self.agg_producto)
        self.boton_agregar.grid(row=7, column=0,pady=10)

        estilo_boton_limpiar = ttk.Style()
        estilo_boton_limpiar.configure('Limpiar.TButton', font=('Calibri', 14, 'bold'), foreground='black',
                                        background='orange')
        self.boton_limpiar= ttk.Button(self.pagina_cuatro, text= 'Limpiar', style= 'Limpiar.TButton',command = self.limpiar_agg_producto)
        self.boton_limpiar.grid(row= 7, column=1,pady=10)

        # Pagina cinco - Graficas

        #Etiqueta titulo
        self.encabezado_graficas= Label(self.pagina_cinco,text= "GRAFICAS DE PRODUCTOS Y MARCAS",font=("Calibri",20,"bold"),bg="cyan",fg= "black")
        self.encabezado_graficas.grid(column= 0, row= 0)

        #caja de opciones
        self.categorias=["Productos por Cantidad","Productos por Ganacias","Marcas por Cantidad","Marcas por Ganancias"]
        self.cuadro_filtrar = ttk.Combobox(self.pagina_cinco, width= '19', values= self.categorias,state= 'readonly', font=("Calibri",16,"bold"))
        self.cuadro_filtrar.grid(column= 0, row= 1)
        self.cuadro_filtrar.current(0)
        self.cuadro_filtrar.bind("<<ComboboxSelected>>",self.cambiar)

        ############ OCULTAR LA VENTANA PRINCIPAL #################
        self.ventana.withdraw()  # ocultar la ventana principal

        self.get_db()

    def pagina_principal(self):
        self.paginas.select([self.pagina_uno])
    def pagina_db(self):
        self.paginas.select([self.pagina_dos])
    def pagina_editar(self):
        self.paginas.select([self.pagina_tres])
        self.info_edit_cat.focus()#poner el foco de la escritura
    def pagina_agregar(self):
        self.paginas.select([self.pagina_cuatro])
        self.entrada_cat.focus()#poner el foco de la escritura
    def pagina_graficas(self):
        self.graficas()
        self.cambiar()
        self.paginas.select([self.pagina_cinco])


    def db_consulta(self,consulta,parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor= con.cursor()
            resultado= cursor.execute(consulta,parametros)
            con.commit()
        return resultado

    def get_db(self):
        registros_tabla= self.tabla_db.get_children()
        for fila in registros_tabla:
            self.tabla_db.delete(fila)
        query= 'SELECT * FROM inventario ORDER BY categoria DESC'
        registros= self.db_consulta(query)
        for fila in registros:
            self.tabla_db.insert('',0, text=fila[0], values= (fila[1],fila[2],fila[3],fila[5],fila[4],fila[6]))

    def eliminar_producto(self):
        try:
            self.tabla_db.item(self.tabla_db.selection())['values'][0]#Sin esta linea no da la except !
            id = self.tabla_db.item(self.tabla_db.selection())['text']
            query = 'DELETE FROM inventario WHERE id = ?'
            self.db_consulta(query, (id,))
            messagebox.showinfo('Exito', 'Se ha Eliminado el Articulo Seleccionado.')
            self.get_db()
        except IndexError as e:
            messagebox.showwarning('Error','Seleciona un Articulo.')
            return

    def editar_pasar_producto(self):

        try:
            self.categoria_act.set(self.tabla_db.item(self.tabla_db.selection())['values'][0])
            self.color_act.set(self.tabla_db.item(self.tabla_db.selection())['values'][1])
            self.marca_act.set(self.tabla_db.item(self.tabla_db.selection())['values'][2])
            self.stock_act.set(self.tabla_db.item(self.tabla_db.selection())['values'][3])
            self.prec_venta_act.set(self.tabla_db.item(self.tabla_db.selection())['values'][4])
            self.prec_compra_act.set(self.tabla_db.item(self.tabla_db.selection())['values'][5])

            self.paginas.select([self.pagina_tres])
        except:
            messagebox.showwarning('Error','Selecciona un Articulo')
            return

    def limpiar_edit_producto(self):
        self.categoria_edit.set('')
        self.color_edit.set('')
        self.marca_edit.set('')
        self.stock_edit.set('')
        self.prec_venta_edit.set('')
        self.prec_compra_edit.set('')

    def limpiar_agg_producto(self):
        self.categoria_agg.set('')
        self.color_agg.set('')
        self.marca_agg.set('')
        self.stock_agg.set('')
        self.prec_venta_agg.set('')
        self.prec_compra_agg.set('')


    def actualizar_producto(self):
        campos_antiguos= [self.categoria_act.get(),self.color_act.get(),self.marca_act.get(),self.stock_act.get(),self.prec_venta_act.get(),self.prec_compra_act.get()]
        campos_nuevos= [self.categoria_edit.get(),self.color_edit.get(),self.marca_edit.get(),self.stock_edit.get(),self.prec_venta_edit.get(),self.prec_compra_edit.get()]
        campos_actualizados= []
        limpiar_campos=[self.categoria_act,self.color_act,self.marca_act,self.stock_act,self.prec_venta_act,self.prec_compra_act,self.categoria_edit,self.color_edit,self.marca_edit,self.stock_edit,self.prec_venta_edit,self.prec_compra_edit]
        producto_modificado= False
        query= 'UPDATE inventario SET categoria= ?, color= ?, marca= ?, stock= ?, precio_venta= ?, precio_compra= ? WHERE categoria= ? AND color= ? AND marca= ? AND stock= ? AND precio_venta= ? AND precio_compra= ?'
        for nuevo_campo in campos_nuevos:
            if nuevo_campo != "" and self.info_act_cat.get() != "":
                producto_modificado= True
        if producto_modificado:
            for indice,nuevo_campo in enumerate(campos_nuevos):
                if nuevo_campo != "":
                    campos_actualizados.append(campos_nuevos[indice])
                else:
                    campos_actualizados.append(campos_antiguos[indice])
            campos_actualizados = campos_actualizados + campos_antiguos
            parametros = tuple(campos_actualizados)
            self.db_consulta(query,parametros) #ejecutar consulta
            messagebox.showinfo('Perfecto', 'Articulo actualizado.')
            self.get_db() #Actualizar tabla
            for indice in range(len(limpiar_campos)):
                limpiar_campos[indice].set("")

        else:
            messagebox.showwarning('Error','No se ha cambiado ningun dato.')

    def agg_producto(self):
        try:
            query= "CREATE TABLE 'Inventario' ('id' INTEGER NOT NULL UNIQUE, 'categoria' TEXT NOT NULL,	'color'	TEXT NOT NULL, 'marca' TEXT NOT NULL, 'precio_venta' INTEGER NOT NULL, 'stock' INTEGER NOT NULL, 'precio_compra' INTEGER NOT NULL, PRIMARY KEY('id' AUTOINCREMENT))"
            self.db_consulta(query,parametros=())
        except:
            pass

        if self.categoria_agg.get() != "" and self.color_agg.get() != "" and self.marca_agg.get() != "" and self.stock_agg.get() != "" and self.prec_venta_agg.get() != "" and self.prec_compra_agg.get() != "":
            limpiar_campos=[self.categoria_agg,self.color_agg,self.marca_agg,self.stock_agg,self.prec_venta_agg,self.prec_compra_agg]
            query = "INSERT INTO inventario VALUES(NULL,?,?,?,?,?,?)"
            parametros=(self.categoria_agg.get(),self.color_agg.get(),self.marca_agg.get(),self.prec_venta_agg.get(),self.stock_agg.get(),self.prec_compra_agg.get())
            self.db_consulta(query,parametros)
            messagebox.showinfo("Excelente","Los Datos han sido Guardados con Exito!")
            self.get_db()  # Actualizar tabla
            for indice in range(len(limpiar_campos)):
                limpiar_campos[indice].set("")



        else:
            messagebox.showwarning("Error","Falta Agregar algun dato.")

    def graficas(self):
        self.registros_tabla = self.tabla_db.get_children()
        self.categorias_graficas = []
        self.categorias_stock = []
        self.categorias_ganancias = []

        self.marcas_graficas = []
        self.marcas_stock = []
        self.marcas_ganancias = []

        self.lista_colores = ["red", "blue", "yellow", "green", "orange", "purple", "pink"]

        query = 'SELECT * FROM Inventario ORDER BY categoria DESC'
        registros = self.db_consulta(query)
        for registro in registros:
            if not registro[1] in self.categorias_graficas:
                self.categorias_graficas.append(registro[1])
            if not registro[3] in self.marcas_graficas:
                self.marcas_graficas.append(registro[3])

        for categoria in self.categorias_graficas:
            print(categoria)
            contador_categorias_stock = 0
            contador_categorias_ganancias = 0
            for articulo in self.db_consulta(query):
                if articulo[1] == categoria:
                    contador_categorias_stock += articulo[5]
                    contador_categorias_ganancias += (articulo[4] - articulo[6]) * articulo[5]
            self.categorias_stock.append(contador_categorias_stock)
            self.categorias_ganancias.append(contador_categorias_ganancias)
        for marca in self.marcas_graficas:
            contador_marcas_stock = 0
            contador_marcas_ganancias = 0
            for articulo in self.db_consulta(query):
                if articulo[3] == marca:
                    contador_marcas_stock += articulo[5]
                    contador_marcas_ganancias += (articulo[4] - articulo[6]) * articulo[5]
            self.marcas_stock.append(contador_marcas_stock)
            self.marcas_ganancias.append(contador_marcas_ganancias)
        print("categoria:", self.categorias_graficas, "Marcas:", self.marcas_graficas, "categorias stock:",
              self.categorias_stock, "categorias ganancias:", self.categorias_ganancias,"stock marcas:",self.marcas_stock,"Ganancias marcas:",self.marcas_ganancias)


    def cambiar(self,*args):
        #"Productos por Cantidad","Productos por Ganacias","Marcas por Cantidad","Marcas por Ganancias"
        if self.cuadro_filtrar.get() == "Productos por Cantidad":

            fig, axs = plt.subplots(figsize=(7, 4), facecolor="cyan")
            fig.suptitle("Stock de Productos")
            axs.bar(self.categorias_graficas, self.categorias_stock, color=self.lista_colores)
            canvas = FigureCanvasTkAgg(fig, master=self.pagina_cinco)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=2)

        if self.cuadro_filtrar.get() == "Productos por Ganacias":

            fig, axs = plt.subplots(figsize=(7, 4), facecolor="cyan")
            fig.suptitle("Ganancias de Productos")
            axs.bar(self.categorias_graficas, self.categorias_ganancias, color=self.lista_colores)
            canvas = FigureCanvasTkAgg(fig, master=self.pagina_cinco)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=2)

        if self.cuadro_filtrar.get() == "Marcas por Cantidad":
            fig, axs = plt.subplots(figsize=(7, 4), facecolor="cyan")
            fig.suptitle("Stock de Marcas")
            axs.bar(self.marcas_graficas, self.marcas_stock, color=self.lista_colores)
            canvas = FigureCanvasTkAgg(fig, master=self.pagina_cinco)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=2)

        if self.cuadro_filtrar.get() == "Marcas por Ganancias":
            fig, axs = plt.subplots(figsize=(7, 4), facecolor="cyan")
            fig.suptitle("Ganacias de Marcas")
            axs.bar(self.marcas_graficas, self.marcas_ganancias, color=self.lista_colores)
            canvas = FigureCanvasTkAgg(fig, master=self.pagina_cinco)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=2)

    def cerrar_sesion(self):
        self.ventana.deiconify()
        self.ventana_admin.destroy()