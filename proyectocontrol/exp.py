from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()

###
import tkinter
from tkinter import filedialog
from tkinter import *
import os

root = tkinter.Tk()
#root.withdraw() #use to hide tkinter window
top = Tk()
top.geometry("100x100")
def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

B = Button (top, text ="Hello", command = search_for_file_path())
#file_path_variable = search_for_file_path()
#print ("\nfile_path_variable = ", file_path_variable)
#import exp
B.place(x = 50,y = 50)
top.mainloop()
print(B)

####

from tkinter import *
from tkinter import filedialog
import os

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

        self.L2 = Label(upp,text = "El archivo seleccionado es :")
        self.L2.pack(side=BOTTOM)

        down=Frame(root)
        down.pack(side=BOTTOM)
        #Permite salir del programa
        self.salir = Button(down,text = 'Quitar', command = self.quitApp)
        self.salir.pack(side=BOTTOM)


    #inicializa las variables
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        
        self.pack()
        self.createWidgets()

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
        height = root.winfo_screenheight() 
        width = root.winfo_screenwidth() 

        a=(str(width)+"x"+str(height))

        root.geometry(a.format(positionRight, positionDown))
        

#Crea el objeto tkinter root
root = Tk()
#Asigna el titulo
root.title("Modelacion arx")
#Crea objeto app 
app = Application(master=root)
#por herencia activa el mainloop()
app.mainloop()
print(app.filename)


###
import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager