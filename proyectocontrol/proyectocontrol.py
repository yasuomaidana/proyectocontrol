#Librerias necesarias para crear pantalla
from tkinter import *
from tkinter import filedialog
import os

#Librerias necesarias para graficar
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from arxmod import arxM 

#Clase applicacion, contiene los elementos de nuestra pantalla
class Application(Frame):
    
    
    #Imprime las fsa
    def main(self):
        #Obtiene la direccion de donde se aloja el programa
        currdir = os.getcwd()
        #Permite navegar y obtener el archivo deseado
        self.filename = filedialog.askopenfilename(initialdir=currdir)
        #Actualiza el nombre del label
        self.L1.config(text="El archivo de entrada se encuentra en :"+self.filename)
        a= self.filename
        b=a.rsplit("/",1)
        self.L2.config(text="El archivo seleccionado es :"+b[1])
        self.arx.loadmk(self.filename)

        
    def quitApp(self):
        #Cierra la ventana
        self.stop= False
        self.bye = root.destroy()

    #Crea los objetos de la pantalla
    def createWidgets(self):
        #Definicion de labels
        upp=Frame(root)
        upp.pack()
        self.L0 = Label(upp,text = "Para salir haga click en quitar, si no lo encuentra maximice la pantalla")
        self.L0.pack()
        
        self.L1 = Label(upp,text = "Selecciona el archivo")
        self.L1.pack(side=LEFT)
      
        #Creacion de boton para acceder al archivo
        self.button = Button(upp,text="Selecciona la entrada",command=self.main)
        self.button.pack(side=LEFT)

        upp1=Frame(root)
        upp1.pack()
        self.L2 = Label(upp1,text = "El archivo seleccionado es :")
        self.L2.pack(side=LEFT)
        
        self.inCo = Button(upp1,text="Ingresar constantes",command=self.constWindow)
        self.inCo.pack(side=LEFT)
        
        self.lerr = Label(upp1, text="Ingrese el error")
        self.lerr.pack(side=LEFT)
        
        self.err = Entry(upp1)
        self.err.insert(END, '0')
        self.err.pack(side=LEFT)



        graphs=Frame(root)
        graphs.pack()
        graphscF=Frame(root)
        graphscF.pack()
        graphscFl=Frame(graphscF)
        graphscFl.pack(side=LEFT)
        graphscFr=Frame(graphscF)
        graphscFr.pack(side=LEFT)

        self.graph1= FigureCanvasTkAgg(fig, graphs)
        self.graph1.draw()
        self.graph1.get_tk_widget().pack(side=LEFT,fill=BOTH, expand=1)
        self.toolbar = NavigationToolbar2Tk(self.graph1, graphscFl)
        self.toolbar.update()
        self.graph1.get_tk_widget().pack(side=LEFT,fill=BOTH, expand=1)

        self.graph2= FigureCanvasTkAgg(fig2, graphs)
        self.graph2.draw()
        self.graph2.get_tk_widget().pack(side=LEFT,fill=BOTH, expand=1)
        self.toolbar = NavigationToolbar2Tk(self.graph2, graphscFr)
        self.toolbar.update()
        self.graph1.get_tk_widget().pack(side=LEFT,fill=BOTH, expand=1)

        pf=Frame(root)
        pf.pack()
        self.pausa = Button(pf,text = 'Start', command = self.startpause)
        self.pausa.pack()

        down=Frame(root)
        down.pack()
        #Permite salir del programa
        self.salir = Button(down,text = 'Quitar', command = self.quitApp)
        
        self.salir.pack(side=BOTTOM)
        

    def startpause(self):
        if self.pausa["text"] == "Start":
            self.pausa.config(text="Pausa")
            self.start=1
        else:
            self.start=0
            self.pausa.config(text="Start")

    #Crea la venta donde se aloja la interfaz de entrada de datos
    def constWindow(self):

        self.consFrame=Tk()
        self.consFrame.title("Ingrese las constantes")
        
        fca1=Frame(self.consFrame)
        fca1.pack()
        self.lcA1 = Label(fca1, text="Ingrese la constante A1")
        self.entryA1 = Entry(fca1)
        self.lcA1.pack(side=LEFT)
        self.entryA1.pack(side=LEFT)

        fca2=Frame(self.consFrame)
        fca2.pack()
        self.lcA2 = Label(fca2, text="Ingrese la constante A2")
        self.entryA2 = Entry(fca2)
        self.lcA2.pack(side=LEFT)
        self.entryA2.pack(side=LEFT)

        fca3=Frame(self.consFrame)
        fca3.pack()
        self.lcA3 = Label(fca3, text="Ingrese la constante A3")
        self.entryA3 = Entry(fca3)
        self.lcA3.pack(side=LEFT)
        self.entryA3.pack(side=LEFT)

        fca4=Frame(self.consFrame)
        fca4.pack()
        self.lcA4 = Label(fca4, text="Ingrese la constante A4")
        self.entryA4 = Entry(fca4)
        self.lcA4.pack(side=LEFT)
        self.entryA4.pack(side=LEFT)

        fcb0=Frame(self.consFrame)
        fcb0.pack()
        self.lcB0 = Label(fcb0, text="Ingrese la constante B0")
        self.entryB0 = Entry(fcb0)
        self.lcB0.pack(side=LEFT)
        self.entryB0.pack(side=LEFT)

        fcb1=Frame(self.consFrame)
        fcb1.pack()
        self.lcB1 = Label(fcb1, text="Ingrese la constante B1")
        self.entryB1 = Entry(fcb1)
        self.lcB1.pack(side=LEFT)
        self.entryB1.pack(side=LEFT)

        fcb2=Frame(self.consFrame)
        fcb2.pack()
        self.lcB2 = Label(fcb2, text="Ingrese la constante B2")
        self.entryB2 = Entry(fcb2)
        self.lcB2.pack(side=LEFT)
        self.entryB2.pack(side=LEFT)

        fcb3=Frame(self.consFrame)
        fcb3.pack()
        self.lcB3 = Label(fcb3, text="Ingrese la constante B3")
        self.entryB3 = Entry(fcb3)
        self.lcB3.pack(side=LEFT)
        self.entryB3.pack(side=LEFT)

        fcb4=Frame(self.consFrame)
        fcb4.pack()
        self.lcB4 = Label(fcb4, text="Ingrese la constante B4")
        self.entryB4 = Entry(fcb4)
        self.lcB4.pack(side=LEFT)
        self.entryB4.pack(side=LEFT)

        fcd=Frame(self.consFrame)
        fcd.pack()
        self.lcD = Label(fcd, text="Ingrese la constante D")
        self.entryD = Entry(fcd)
        self.lcD.pack(side=LEFT)
        self.entryD.pack(side=LEFT)

        fce=Frame(self.consFrame)
        fce.pack()
        self.exC =  Button(fce,text = 'Registrar constantes', command = self.registCons)
        self.exC.pack()

        #self.consFrame.mainloop()

    #Registra los datos y cierra la ventana
    def registCons(self):

        self.A1= float(self.entryA1.get())
        self.A2= float(self.entryA2.get())
        self.A3= float(self.entryA3.get())
        self.A4= float(self.entryA4.get())

        self.B0= float(self.entryB0.get())
        self.B1= float(self.entryB1.get())
        self.B2= float(self.entryB2.get())
        self.B3= float(self.entryB3.get())
        self.B4= float(self.entryB4.get())

        self.D= int(self.entryD.get())


        self.arx.getConst(self.A1, self.A2, self.A3, self.A4, self.B0, self.B1, self.B2, self.B3, self.B4, self.D)
        self.consFrame.destroy()
        
        
    #inicializa las variables
    def __init__(self, master=None):
        #No se que hace pero iba
        Frame.__init__(self, master)
        self.filename = None
        
        self.pack()
        self.createWidgets()

        #Obtiene dimensiones 
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
        height = root.winfo_screenheight() 
        width = root.winfo_screenwidth() 

        a=(str(width)+"x"+str(height))

        root.geometry(a.format(positionRight, positionDown))
        self.initCons()

        self.stop= True
        self.start=0
        self.ti=1

        self.arx=arxM()


    #Actualiza la grafica
    def refplot(self):
        
        if self.start==1:
            

            self.arx.getval(self.error)
            
            entrada=self.arx.rmk
            error=self.arx.pk
            salida=self.arx.ck
            te = np.arange(0, len(entrada),1)
            ter = np.arange(0, len(error),1)
            tsa= np.arange(0, len(salida),1)
            #Grafica

            #Limpia la grafica
            fig.add_subplot(111).cla()
            #Imprime los datos
            fig.add_subplot(111).plot(te, entrada,ter, error,'--')
            #Asigna nombres a las lineas
            fig.legend(('Entradas', 'Error'))

            
            fig2.add_subplot(111).cla()
            fig2.add_subplot(111).cla()
            fig2.add_subplot(111).plot(tsa, salida,te,entrada,'--')
            fig2.legend(('Salida', 'Entrada'))

            self.graph2.draw()
            self.graph1.draw()
            
            self.ti+=1

    #Inicializa las constantes en 0
    def initCons(self):
        self.A1=0
        self.A2=0
        self.A3=0
        self.A4=0
        self.B0=0
        self.B1=0
        self.B2=0
        self.B3=0
        self.B4=0
        self.E=0
    def geterr(self):
        self.error=float(self.err.get())
        
#Crea el objeto tkinter root
root = Tk()
#Asigna el titulo
root.title("Modelacion arx")



#Crea objetos de graficas
fig = Figure(figsize=(7, 5), dpi=100)
fig2 = Figure(figsize=(7, 5), dpi=100)
fig.suptitle('Entrada vs Error', fontsize=16)
fig2.suptitle('Salida vs Entrada', fontsize=16)

#Genera un espacio de 0 a 3
t = np.arange(0, 3, .01)
#Grafica
fig.add_subplot(111).plot()
fig2.add_subplot(111).plot()

#Crea objeto app 
app = Application(master=root)
#por herencia activa el mainloop()
#app.mainloop()
while app.stop:
    app.update()
    if app.start==1:
        app.geterr()
        app.refplot()
#print(app.filename)


