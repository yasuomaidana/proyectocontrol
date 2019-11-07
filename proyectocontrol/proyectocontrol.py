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
        

    def quitApp(self):
        #Cierra la ventana
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
        self.graph1.get_tk_widget().pack(side=LEFT)
        self.toolbar = NavigationToolbar2Tk(self.graph1, graphscFl)
        self.toolbar.update()
        self.graph1.get_tk_widget().pack(side=LEFT)

        self.graph2= FigureCanvasTkAgg(fig2, graphs)
        self.graph2.draw()
        self.graph2.get_tk_widget().pack(side=LEFT)
        self.toolbar = NavigationToolbar2Tk(self.graph2, graphscFr)
        self.toolbar.update()
        self.graph1.get_tk_widget().pack(side=LEFT)

        down=Frame(root)
        down.pack()
        #Permite salir del programa
        self.salir = Button(down,text = 'Quitar', command = self.quitApp)
        self.salir.pack(side=BOTTOM)


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

        ##
        
        

#Crea el objeto tkinter root
root = Tk()
#Asigna el titulo
root.title("Modelacion arx")
#Crea objeto app 

fig = Figure(figsize=(5, 4), dpi=100)
fig2 = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
fig2.add_subplot(111).plot(t, 2 * np.cos(2 * np.pi * t))

app = Application(master=root)
#por herencia activa el mainloop()
app.mainloop()
print(app.filename)
