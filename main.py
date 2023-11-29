from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk,Image
from cliente import Ventana_cliente
from proveedor import Ventana_proveedor
from admin import Ventana_admin

class Aplicacion:
    db = 'database/proyecto.db'

    def __init__(self,root):
        self.ventana = root
        self.ventana.title("App Gestiones de Empresa")
        self.ventana.config(background = '#4FA1CA')
        self.ventana.geometry('500x500+350+50')

        #Frame principal inicio de sesion
        self.frame_inicio = Frame(self.ventana,background="White",height=450,width=450)
        self.frame_inicio.grid(row = 0,column = 0, pady= 20,padx=20,sticky='nsew')

        #Cambiar tamaño del  logo
        self.logo = Image.open('imagenes/JACD.LOGO.png')
        self.logo = self.logo.resize((179,115))
        self.logo.save('imagenes/logo.png')
        self.logo_img = ImageTk.PhotoImage(self.logo)

        #Etiqueta logo
        self.etiqueta_logo = Label(self.frame_inicio, image = self.logo_img,background = 'White')
        self.etiqueta_logo.grid(row = 0, column = 0,columnspan=2, sticky= 'nsew',padx=120,pady= 20)

        #Etiquetas inicio de sesion
        self.etiqueta_inicio=Label(self.frame_inicio,text='Iniciar Sesion',font=('Calibri',18,'bold'),bg='white')
        self.etiqueta_inicio.grid(row=1,column=0,sticky='nsew',pady=35,ipadx=152,padx=10,columnspan=2)
        self.etiqueta_usuario=Label(self.frame_inicio,text='Usuario:',font=('Calibri',14,'bold'),bg='white')
        self.etiqueta_usuario.grid(row=2,column=0)
        self.etiqueta_contrasenia = Label(self.frame_inicio, text='Contraseña:', font=('Calibri', 14,'bold'), bg='white')
        self.etiqueta_contrasenia.grid(row=3, column=0)

        #Entry inicio de Sesion
        self.usuario=StringVar()
        self.entry_usuario=Entry(self.frame_inicio,textvariable=self.usuario)
        self.entry_usuario.focus()
        self.entry_usuario.grid(row=2,column=1)
        self.contrasenia= StringVar()
        self.entry_contrasenia=Entry(self.frame_inicio,textvariable=self.contrasenia,show="*")
        self.entry_contrasenia.grid(row=3, column=1)

        # Botones iniciar y registrar
        self.boton_registrarse = ttk.Button(self.frame_inicio, text='Registrarse',command=self.registarse)
        self.boton_registrarse.grid(row=4, column=0, pady=10,ipady=2,ipadx=5)
        self.boton_inicar = ttk.Button(self.frame_inicio, text='Iniciar Sesion',command=self.inicio_sesion)
        self.boton_inicar.grid(row=4, column=1,pady=10,ipady=2,ipadx=5)

        # Mensaje para el usuario
        self.mensaje= Label(self.frame_inicio,text='',fg='red',bg='white')
        self.mensaje.grid(row=5,column=0,columnspan=2,pady=30)

    def db_consulta(self,consulta,parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor=con.cursor()
            resultado= cursor.execute(consulta,parametros)
            con.commit()
        return resultado

    def inicio_sesion(self,*args):
        query= 'SELECT * FROM usuarios WHERE usuario= ?'
        registro = self.db_consulta(query,(self.usuario.get(),))
        datos_usuario = registro.fetchone()

        if len(self.usuario.get())==0 or len(self.contrasenia.get())==0:
            self.mensaje['text']='Falta ingresar algun Dato'
        else:
            if datos_usuario == None:
                self.mensaje['text']='No existe usuario'
            else:
                contra_usuario = datos_usuario[2]

                if self.contrasenia.get() == contra_usuario:

                    self.mensaje['text'] = ''
                    self.usuario.set("")
                    self.contrasenia.set("")
                    clase_usuario=datos_usuario[3]
                    print(clase_usuario)
                    if clase_usuario == 'Cliente':
                        ventana_cliente = Toplevel()
                        Ventana_cliente(ventana_cliente,self.ventana)

                    if clase_usuario == 'Proveedor':
                        ventana_proveedor = Toplevel()
                        Ventana_proveedor(ventana_proveedor,self.ventana)

                    if clase_usuario == 'Admin':
                        ventana_admin = Toplevel()
                        Ventana_admin(ventana_admin,self.ventana)



                else:
                    self.mensaje['text']='La contraseña es incorrecta'


    def registarse(self):
        self.ventana_registro=Toplevel()
        self.ventana_registro.title("Registro")
        self.ventana_registro.config(bg='#D6EAF8')
        self.ventana_registro.geometry('350x350+350+50')

        ######## FRAME REGISTRO ##########
        self.frame_titulo=LabelFrame(self.ventana_registro,text='Registro de Usuario',font=("Calibri",20,"bold"),bg='#D6EAF8')
        self.frame_titulo.grid(row=0,column=0,columnspan=2,padx=40,pady=40)

        ######## ETIQUETAS USUARIOS Y CONTRASEÑA ##########
        etiqueta_usuario=Label(self.frame_titulo,text='Usuario',font=("calibri",18),bg='#D6EAF8')
        etiqueta_usuario.grid(row=1,column=0)
        etiqueta_contrasenia=Label(self.frame_titulo,text='Contraseña',font=("calibri",18),bg='#D6EAF8')
        etiqueta_contrasenia.grid(row=2,column=0)
        etiqueta_categoria= Label(self.frame_titulo,text='Categoria',font=("calibri",18),bg='#D6EAF8')
        etiqueta_categoria.grid(row=3,column=0)
        self.etiqueta_mensaje=Label(self.frame_titulo,text="",font=("calibri",10),fg="red",bg='#D6EAF8')
        self.etiqueta_mensaje.grid(row=5,column=0,columnspan=2,sticky="nsew")

        ######## ENTRY USUARIO Y CONTRASEÑA #########
        self.registro_usuario=StringVar()
        entry_usuario=Entry(self.frame_titulo,textvariable=self.registro_usuario)
        entry_usuario.focus()
        entry_usuario.grid(row=1,column=1,padx=4)
        self.registro_contrasenia=StringVar()
        entry_contrasenia=Entry(self.frame_titulo,textvariable=self.registro_contrasenia)
        entry_contrasenia.grid(row=2,column=1,padx=4)
        self.categorias= ["Cliente","Proveedor","Admin"]
        self.entry_categoria= ttk.Combobox(self.frame_titulo,width='11',values=self.categorias,state="readonly",font=('calibri',13))
        self.entry_categoria.grid(row=3,column=1,padx=4)
        self.entry_categoria.set("Seleccionar")

        ######## BOTONES CANCELAR Y REGISTRAR #########
        boton_cancelar=ttk.Button(self.frame_titulo,text='Cancelar',command=self.salir)
        boton_cancelar.grid(row=4,column=0,pady=10,ipady=4,ipadx=2)
        boton_registrar=ttk.Button(self.frame_titulo,text='Registrar',command=self.registrar_usuario)
        boton_registrar.grid(row=4,column=1,pady=10,ipady=4,ipadx=2)

        self.ventana.withdraw()#Oculta la ventana principal

    def registrar_usuario(self):

        try:
            query= "CREATE TABLE 'Usuarios' ('id' INTEGER NOT NULL UNIQUE, 'usuario' TEXT NOT NULL,	'contraseña' TEXT NOT NULL, 'cargo'	TEXT NOT NULL, PRIMARY KEY('id' AUTOINCREMENT))"
            self.db_consulta(query,parametros=())
        except:
            pass
        
        if self.registro_usuario.get() != "" and self.registro_contrasenia.get() != "" and self.entry_categoria.get() != "Seleccionar":
            query= "INSERT INTO usuarios VALUES(NULL,?,?,?)"
            parametros=(self.registro_usuario.get(),self.registro_contrasenia.get(),self.entry_categoria.get())
            print(parametros)
            self.db_consulta(query,parametros)
            self.mensaje['text']="Usuario Registrado correctamente"
            self.salir()
        else:
            self.etiqueta_mensaje['text']="Te ha faltado algun dato"


    ####### BOTON SALIR VUELVE AL LOGIN #######
    def salir(self):
        self.ventana.deiconify()
        self.ventana_registro.destroy()




if __name__ == "__main__":
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()