#%% 
## IMPORTAMOS los paquetes necesarios.

import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import numpy as np
import math
from prettytable import PrettyTable
import datetime

import tifffile as tif
import matplotlib.pyplot as plt
#%%
refPt = []
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Se construye la ventana y se manda 
        llamar la inicializacion de la ventana

        """
        super().__init__()
        
        #QtWidgets.QWidget.__init__(self)
        self.inicializaUI()

#%% Inicialización de la ventana
    def inicializaUI(self):
        """
        Se manda llamar a la ventana creada en el Qt designer
       
        """   

        uic.loadUi("APP_FIS-MED.ui", self)   
        #Se llama a la ventana que se creo en el qt designer y debe estar en la misma carpeta  
        
        #Primeramente escondemos una parte de la ventana para que el usuario decida que hacer
        self.btnanz.hide()
        self.btnBC.hide()
        self.obtD.hide()
        self.BTN_GI_2.hide()
        #self.scrollArea.hide()
        #self.label_3.hide()
        #self.BTN_CURVA.hide()
        #self.textEdit.hide()
        
        #Primeramente escondemos una parte de la ventana para que el usuario decida que hacer
        self.btnanz.hide()
        
        #Definimos los colores de algunos botones por interactividad
        self.PELICULA0.setStyleSheet("background-color: #95ffa5")
        self.PELICULA1.setStyleSheet("background-color: #95ffa5")
        self.PELICULA2.setStyleSheet("background-color: #95ffa5")
        self.PELICULA3.setStyleSheet("background-color: #95ffa5")
        self.PELICULA4.setStyleSheet("background-color: #95ffa5")
        self.PELICULA5.setStyleSheet("background-color: #95ffa5")
        self.PELICULA6.setStyleSheet("background-color: #95ffa5")
        self.PELICULA7.setStyleSheet("background-color: #95ffa5")
        self.PELICULA8.setStyleSheet("background-color: #95ffa5")
        self.PELICULA9.setStyleSheet("background-color: #95ffa5")
        self.PELICULA10.setStyleSheet("background-color: #95ffa5")
        self.PELICULA11.setStyleSheet("background-color: #95ffa5")
        self.PELICULA12.setStyleSheet("background-color: #95ffa5")
        self.PELICULA13.setStyleSheet("background-color: #95ffa5")
        self.PELICULA14.setStyleSheet("background-color: #95ffa5")
        self.PELICULA15.setStyleSheet("background-color: #95ffa5")
        self.PELICULA16.setStyleSheet("background-color: #95ffa5")
        self.PELICULA17.setStyleSheet("background-color: #95ffa5")
        self.PELICULA18.setStyleSheet("background-color: #95ffa5")
        self.PELICULA19.setStyleSheet("background-color: #95ffa5")
        self.PELICULA20.setStyleSheet("background-color: #95ffa5")
        #Definimos la llamada a los procedimientos de cada boton
        #Abrir
        self.PELICULA0.clicked.connect(self.Abrir0)
        self.PELICULA1.clicked.connect(self.Abrir1)
        self.PELICULA2.clicked.connect(self.Abrir2)
        self.PELICULA3.clicked.connect(self.Abrir3)
        self.PELICULA4.clicked.connect(self.Abrir4)
        self.PELICULA5.clicked.connect(self.Abrir5)
        self.PELICULA6.clicked.connect(self.Abrir6)
        self.PELICULA7.clicked.connect(self.Abrir7)
        self.PELICULA8.clicked.connect(self.Abrir8)
        self.PELICULA9.clicked.connect(self.Abrir9)
        self.PELICULA10.clicked.connect(self.Abrir10)
        self.PELICULA11.clicked.connect(self.Abrir11)
        self.PELICULA12.clicked.connect(self.Abrir12)
        self.PELICULA13.clicked.connect(self.Abrir13)
        self.PELICULA14.clicked.connect(self.Abrir14)
        self.PELICULA15.clicked.connect(self.Abrir15)
        self.PELICULA16.clicked.connect(self.Abrir16)
        self.PELICULA17.clicked.connect(self.Abrir17)
        self.PELICULA18.clicked.connect(self.Abrir18)
        self.PELICULA19.clicked.connect(self.Abrir19)
        self.PELICULA20.clicked.connect(self.Abrir20)
        #cortar
        self.BTN_CORTAR.clicked.connect(self.Cortar)
        #reestablecer
        self.BTN_REESTABLECER.clicked.connect(self.Reestablecer)
        #aceptar
        self.BTN_ACEPTAR.clicked.connect(self.Aceptar)
        #código de las lineas de texto para dósis:
        #Primero se hacen inutilizables las líneas (se harán utilizables hasta "aceptar" un ROI para la película correspondiente)
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_14.setEnabled(False)
        self.lineEdit_15.setEnabled(False)
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_17.setEnabled(False)
        self.lineEdit_18.setEnabled(False)
        self.lineEdit_19.setEnabled(False)
        self.lineEdit_20.setEnabled(False)
        #Ahora se conectan a la función de presionar la tecla "enter" para introducir una dosis
        self.lineEdit_1.returnPressed.connect(self.introducirDosis)
        self.lineEdit_2.returnPressed.connect(self.introducirDosis)
        self.lineEdit_3.returnPressed.connect(self.introducirDosis)
        self.lineEdit_4.returnPressed.connect(self.introducirDosis)
        self.lineEdit_5.returnPressed.connect(self.introducirDosis)
        self.lineEdit_6.returnPressed.connect(self.introducirDosis)
        self.lineEdit_7.returnPressed.connect(self.introducirDosis)
        self.lineEdit_8.returnPressed.connect(self.introducirDosis)
        self.lineEdit_9.returnPressed.connect(self.introducirDosis)
        self.lineEdit_10.returnPressed.connect(self.introducirDosis)
        self.lineEdit_11.returnPressed.connect(self.introducirDosis)
        self.lineEdit_12.returnPressed.connect(self.introducirDosis)
        self.lineEdit_13.returnPressed.connect(self.introducirDosis)
        self.lineEdit_14.returnPressed.connect(self.introducirDosis)
        self.lineEdit_15.returnPressed.connect(self.introducirDosis)
        self.lineEdit_16.returnPressed.connect(self.introducirDosis)
        self.lineEdit_17.returnPressed.connect(self.introducirDosis)
        self.lineEdit_18.returnPressed.connect(self.introducirDosis)
        self.lineEdit_19.returnPressed.connect(self.introducirDosis)
        self.lineEdit_20.returnPressed.connect(self.introducirDosis)
        #Conectamos cada linea de texto de manera que si se cambia el contenido de la misma, el programa lo identifique con esa posición
        self.lineEdit_1.textChanged.connect(self.cuadro1)
        self.lineEdit_2.textChanged.connect(self.cuadro2)
        self.lineEdit_3.textChanged.connect(self.cuadro3)
        self.lineEdit_4.textChanged.connect(self.cuadro4)
        self.lineEdit_5.textChanged.connect(self.cuadro5)
        self.lineEdit_6.textChanged.connect(self.cuadro6)
        self.lineEdit_7.textChanged.connect(self.cuadro7)
        self.lineEdit_8.textChanged.connect(self.cuadro8)
        self.lineEdit_9.textChanged.connect(self.cuadro9)
        self.lineEdit_10.textChanged.connect(self.cuadro10)
        self.lineEdit_11.textChanged.connect(self.cuadro11)
        self.lineEdit_12.textChanged.connect(self.cuadro12)
        self.lineEdit_13.textChanged.connect(self.cuadro13)
        self.lineEdit_14.textChanged.connect(self.cuadro14)
        self.lineEdit_15.textChanged.connect(self.cuadro15)
        self.lineEdit_16.textChanged.connect(self.cuadro16)
        self.lineEdit_17.textChanged.connect(self.cuadro17)
        self.lineEdit_18.textChanged.connect(self.cuadro18)
        self.lineEdit_19.textChanged.connect(self.cuadro19)
        self.lineEdit_20.textChanged.connect(self.cuadro20)
        
        #Obtener Curva: 
        self.BTN_CURVA3.clicked.connect(self.btnObtenerCurva3)
        self.BTN_CURVA4.clicked.connect(self.btnObtenerCurva4)
        
        #para mostrar lo que se seleccionó "obtener curva" u "obtener dosis"
        self.curva.clicked.connect(self.abrirCurva)
        self.dosis.clicked.connect(self.abrirDosis)
        
        #Botón "PELÍCULA A ANALILZAR"
        self.btnanz.clicked.connect(self.analizarPel)
        #botón "GUADRDAR INFORMACIÓN
        self.BTN_GI.clicked.connect(self.gdrInfo)
        #Botón "CURVA DE CALIBRACIÓN A UTILIZAR"
        self.btnBC.clicked.connect(self.AbrirCurva)
        #Botón "OBTENER DOSIS"
        self.obtD.clicked.connect(self.evaluarDosis)
        #Botón "CAPTURA DE PANTALLA"
        self.BTN_GI_2.clicked.connect(self.SS)
        
        self.textEdit.setEnabled(False)
        
        self.i=1 # contador necesario para evitar problemas con el botón recortar
        self.matI = np.zeros(20) #matriz que contendrá los valores de intensidad promedio en el canal rojo de c/película.
        self.dosis = np.zeros(21) # matriz que contendrá los valores de dosis introducidos.
        self.stdDev = np.zeros(21)
        
        #mostramos la ventana
        self.show()

#%% Botones "ABRIR"
    """
    Código para abrir los archivos, cambiar el color de los botones al ser presionado, abrir la imagen en el rectificador 
    de imágenes, crear la matriz que se irá modificando con los cortes y en cada botón de abrir irá cambiand un 
    "identificador", el cual posteriormente servirá para no sólo tener una función de "aceptar" y una de introducirDosis".
    También cambia el color del botón presionado, para identificar que está siendo utilizado.
    """
    def Abrir0(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", #getSaveNameFile pythonspot pyqt5 file dialog
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA0.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA0.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 0 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
    
####################################################################################
    def Abrir1(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA1.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA1.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 1 
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir2(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA2.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA2.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 2 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir3(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA3.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA3.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 3 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir4(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA4.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA4.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 4 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir5(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA5.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA5.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 5 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir6(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA6.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA6.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 6 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir7(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA7.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA7.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 7 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir8(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA8.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA8.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 8 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir9(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA9.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA9.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 9 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir10(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA10.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA10.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 10 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir11(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA11.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA11.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 11 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir12(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA12.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA12.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 12 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir13(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA13.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA13.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 13 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir14(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA14.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA14.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 14 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir15(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA15.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA15.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 15 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir16(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA16.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA16.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 16 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir17(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA17.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA17.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 17 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir18(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA18.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA18.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 18 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir19(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA19.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA19.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 19 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
####################################################################################
    def Abrir20(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.PELICULA20.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.PELICULA20.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 20 #condicional para saber que botón se utilizó, útil para los botones "aceptar" y la función "introducirDosis"
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
#%% Código para seleccionar el ROI
    """
    Código para marcar la región de interés para cortar la imágen
    """
    @QtCore.pyqtSlot("QRect", "QPointF", "QPointF")
    def on_rubberBandChanged(self, rubberBandRect, fromScenePoint, toScenePoint):
        self.r = QtCore.QRectF(fromScenePoint, toScenePoint)
        #selected = self.gphcImagen.items(rubberBandRect)
        #se guardan los valores de los vertices del ROI
        self.x.append(self.r.getCoords())
        self.long=len(self.x)
        #condicional para cortar sólo si hay región de interés
        if self.x!=[]:
            self.cont=0        

#%% Botón "CORTAR"
    """
    Código para el botón "cortar" de la app, corta la región de interés de la imágen y la muestra, también corta la matriz
    que contiene los valores de intensidad en el canal rojo de cada pixel de la imágen en las mismas coordenadas que la 
    región de interés seleccionada.
    """
    def Cortar(self):
        if self.cont==0: #condicional para cortar sólo si hay región de interés
            #Se importan las coordenadas de la última posición del ROI y se identifica a que vertice corresponde c/u
     
             if self.x[self.long-self.i][0] > self.x[self.long-self.i][2]:
                 self.x1=self.x[self.long-self.i][2]
                 self.x2=self.x[self.long-self.i][0]
                 self.long=0
                 corte =1 
             else:
                 self.x1=self.x[self.long-self.i][0]
                 self.x2=self.x[self.long-self.i][2]
                 self.long=0
                 corte =1
             if self.x[self.long-self.i][1] > self.x[self.long-self.i][3]:
                 self.y1=self.x[self.long-self.i][3]
                 self.y2=self.x[self.long-self.i][1]
                 self.long=0
                 corte = 1
             else:
                 self.y1=self.x[self.long-self.i][1]
                 self.y2=self.x[self.long-self.i][3]
                 self.long=0
                 corte = 1
         #se corta además la matriz que representa a la película en las mismas coordenadas delimitadas, en el canal rojo
             if corte == 1:
                 #coordenadas que se usarán para cortar la matriz del rojo
                 x1 = int(self.x1)
                 x2 = int(self.x2)
                 y1 = int(self.y1)
                 y2 = int(self.y2)
                 self.matIR = np.copy(self.matTifR[y1:y2, x1:x2]) #corte de la matriz del rojo en las coordenadas marcadas
                 self.matTifR = np.copy(self.matIR) #reespaldo de la matriz cortada, por si se hace otro corte
             
        #cortamos la región de interés 
        self.crop=self.pix.copy(int(self.x1),int(self.y1), int(self.x2)-int(self.x1),int(self.y2)-int(self.y1)) 
        self.item = QtWidgets.QGraphicsPixmapItem(self.crop)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.pix = self.crop

        #Contador para eliminar la ultima posición del ROI al abrir otra imagen
        self.long=0
        self.x=[]
        self.cont=1
        #A continuación el código para guardar la desviación estándar en cada muestra de datos y mostrarla al usuario cada vez que se corta.
        if self.pelicula == 0:
            self.stdDev[0] = np.std(self.matIR)
        elif self.pelicula == 1:
            self.stdDev[1] = np.std(self.matIR)
        elif self.pelicula == 2:
            self.stdDev[2] = np.std(self.matIR)
        elif self.pelicula == 3:
            self.stdDev[3] = np.std(self.matIR)
        elif self.pelicula == 4:
            self.stdDev[4] = np.std(self.matIR)
        elif self.pelicula == 5:
            self.stdDev[5] = np.std(self.matIR)
        elif self.pelicula == 6:
            self.stdDev[6] = np.std(self.matIR)
        elif self.pelicula == 7:
            self.stdDev[7] = np.std(self.matIR)
        elif self.pelicula == 8:
            self.stdDev[8] = np.std(self.matIR)
        elif self.pelicula == 9:
            self.stdDev[9] = np.std(self.matIR)
        elif self.pelicula == 10:
            self.stdDev[10] = np.std(self.matIR)
        elif self.pelicula == 11:
            self.stdDev[11] = np.std(self.matIR)
        elif self.pelicula == 12:
            self.stdDev[12] = np.std(self.matIR)
        elif self.pelicula == 13:
            self.stdDev[13] = np.std(self.matIR)
        elif self.pelicula == 14:
            self.stdDev[14] = np.std(self.matIR)
        elif self.pelicula == 15:
            self.stdDev[15] = np.std(self.matIR)
        elif self.pelicula == 16:
            self.stdDev[16] = np.std(self.matIR)
        elif self.pelicula == 17:
            self.stdDev[17] = np.std(self.matIR)
        elif self.pelicula == 18:
            self.stdDev[18] = np.std(self.matIR)
        elif self.pelicula == 19:
            self.stdDev[19] = np.std(self.matIR)
        elif self.pelicula == 20:
            self.stdDev[20] = np.std(self.matIR)
        elif self.pelicula == 100: #para la película que queremos evaluar y obtener su dosis:
            self.pelDev = np.std(self.matIR)
            
        
        #código para mostras los datos de la región de interes cortada
        y = "Iprom: " +str(format(np.mean(self.matIR), ".3f"))
        self.label_6.setText(y)
        z = "Desviación estándar: "+str(format(np.std(self.matIR), ".3f"))
        self.label_7.setText(z)

#%% Botón "REESTABLECER"
    """
    Código para el botón "REESTABLECER" que nos hace reiniciar la imágen cortada a la última imágen seleccionada original.
    aquí se repite básicamente lo que hay en el botón de abrir, para reiniciar el proceso de corte si hubo un error.
    """
    def Reestablecer(self):  
        
        self.pix = QPixmap()
        self.pix.load(self.fileNamecopy)
        self.x=[]
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1
        self.cont=1
        self.matTif = tif.imread(self.fileNamecopy) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo

#%% Botón "ACEPTAR"
    """
    Código de el de aceptar: Guarda el dato de intensidad promedio de las imágenes cortadas y da retroalimentación del 
    mismo, cambiando tanto el color del botón en uso, cómo habilitando la línea de texto para introducir la dosis 
    correspondiente a la película.
    """
    def Aceptar(self):
        if self.pelicula == 0: 
            self.pelicula0 = np.mean(self.matIR) #En caso del primer botón identificamos la I0 del canal rojo.
            self.PELICULA0.setStyleSheet("background-color: ##") #retroalimentación en el color del botón en uso.
            self.PELICULA0.setFont(QFont('Calibri', 12))
        elif self.pelicula == 1: #condicional para identificar el botón que se oprimió.
            self.PELICULA1.setStyleSheet("background-color: ##") #retroalimentación en el color del botón en uso.
            self.matI[0] = np.mean(self.matIR) #introducimos el valor promedio de la intensidad en el canal rojo para el ROI seleccionado.
            self.lineEdit_1.setStyleSheet("background-color: #95ffa5") #retroalimentación en la línea de texto para la dosis correspondiente.
            self.PELICULA1.setFont(QFont('Calibri', 12))
            self.lineEdit_1.setFont(QFont('Calibri', 12))
            self.lineEdit_1.setText("") #vaciamos el contenido de la línea de texto correspondiente al botón de la película
            self.lineEdit_1.setEnabled(True) # habilitamos el uso de la línea de texto correspondiente al botón de la película.
        #a partir de de aquí cada elif repite la función del elif anterior, para cada botón y línea de texto.
        elif self.pelicula == 2: 
            self.PELICULA2.setStyleSheet("background-color: ##")
            self.matI[1] = np.mean(self.matIR)
            self.lineEdit_2.setStyleSheet("background-color: #95ffa5")
            self.PELICULA2.setFont(QFont('Calibri', 12))
            self.lineEdit_2.setFont(QFont('Calibri', 12))
            self.lineEdit_2.setText("")
            self.lineEdit_2.setEnabled(True)
        elif self.pelicula == 3: 
            self.PELICULA3.setStyleSheet("background-color: ##")
            self.matI[2] = np.mean(self.matIR)
            self.lineEdit_3.setStyleSheet("background-color: #95ffa5")
            self.PELICULA3.setFont(QFont('Calibri', 12))
            self.lineEdit_3.setFont(QFont('Calibri', 12))
            self.lineEdit_3.setText("")
            self.lineEdit_3.setEnabled(True)
        elif self.pelicula == 4: 
            self.PELICULA4.setStyleSheet("background-color: ##")
            self.matI[3] = np.mean(self.matIR)
            self.lineEdit_4.setStyleSheet("background-color: #95ffa5")
            self.PELICULA4.setFont(QFont('Calibri', 12))
            self.lineEdit_4.setFont(QFont('Calibri', 12))
            self.lineEdit_4.setText("")
            self.lineEdit_4.setEnabled(True)
        elif self.pelicula == 5: 
            self.PELICULA5.setStyleSheet("background-color: ##")
            self.matI[4] = np.mean(self.matIR)
            self.lineEdit_5.setStyleSheet("background-color: #95ffa5")
            self.PELICULA5.setFont(QFont('Calibri', 12))
            self.lineEdit_5.setFont(QFont('Calibri', 12))
            self.lineEdit_5.setText("")
            self.lineEdit_5.setEnabled(True)
        elif self.pelicula == 6: 
            self.PELICULA6.setStyleSheet("background-color: ##")
            self.matI[5] = np.mean(self.matIR)
            self.lineEdit_6.setStyleSheet("background-color: #95ffa5")
            self.PELICULA6.setFont(QFont('Calibri', 12))
            self.lineEdit_6.setFont(QFont('Calibri', 12))
            self.lineEdit_6.setText("")
            self.lineEdit_6.setEnabled(True)
        elif self.pelicula == 7: 
            self.PELICULA7.setStyleSheet("background-color: ##")
            self.matI[6] = np.mean(self.matIR)
            self.lineEdit_7.setStyleSheet("background-color: #95ffa5")
            self.PELICULA7.setFont(QFont('Calibri', 12))
            self.lineEdit_7.setFont(QFont('Calibri', 12))
            self.lineEdit_7.setText("")
            self.lineEdit_7.setEnabled(True)
        elif self.pelicula == 8: 
            self.PELICULA8.setStyleSheet("background-color: ##")
            self.matI[7] = np.mean(self.matIR)
            self.lineEdit_8.setStyleSheet("background-color: #95ffa5")
            self.PELICULA8.setFont(QFont('Calibri', 12))
            self.lineEdit_8.setFont(QFont('Calibri', 12))
            self.lineEdit_8.setText("")
            self.lineEdit_8.setEnabled(True)
        elif self.pelicula == 9: 
            self.PELICULA9.setStyleSheet("background-color: ##")
            self.matI[8] = np.mean(self.matIR)
            self.lineEdit_9.setStyleSheet("background-color: #95ffa5")
            self.PELICULA9.setFont(QFont('Calibri', 12))
            self.lineEdit_9.setFont(QFont('Calibri', 12))
            self.lineEdit_9.setText("")
            self.lineEdit_9.setEnabled(True)
        elif self.pelicula == 10: 
            self.PELICULA10.setStyleSheet("background-color: ##")
            self.matI[9] = np.mean(self.matIR)
            self.lineEdit_10.setStyleSheet("background-color: #95ffa5")
            self.PELICULA10.setFont(QFont('Calibri', 12))
            self.lineEdit_10.setFont(QFont('Calibri', 12))
            self.lineEdit_10.setText("")
            self.lineEdit_10.setEnabled(True)
        elif self.pelicula == 11: 
            self.PELICULA11.setStyleSheet("background-color: ##")
            self.matI[10] = np.mean(self.matIR)
            self.lineEdit_11.setStyleSheet("background-color: #95ffa5")
            self.PELICULA11.setFont(QFont('Calibri', 12))
            self.lineEdit_11.setFont(QFont('Calibri', 12))
            self.lineEdit_11.setText("")
            self.lineEdit_11.setEnabled(True)
        elif self.pelicula == 12: 
            self.PELICULA12.setStyleSheet("background-color: ##")
            self.matI[11] = np.mean(self.matIR)
            self.lineEdit_12.setStyleSheet("background-color: #95ffa5")
            self.PELICULA12.setFont(QFont('Calibri', 12))
            self.lineEdit_12.setFont(QFont('Calibri', 12))
            self.lineEdit_12.setText("")
            self.lineEdit_12.setEnabled(True)
        elif self.pelicula == 13: 
            self.PELICULA13.setStyleSheet("background-color: ##")
            self.matI[12] = np.mean(self.matIR)
            self.lineEdit_13.setStyleSheet("background-color: #95ffa5")
            self.PELICULA13.setFont(QFont('Calibri', 12))
            self.lineEdit_13.setFont(QFont('Calibri', 12))
            self.lineEdit_13.setText("")
            self.lineEdit_13.setEnabled(True)
        elif self.pelicula == 14: 
            self.PELICULA14.setStyleSheet("background-color: ##")
            self.matI[13] = np.mean(self.matIR)
            self.lineEdit_14.setStyleSheet("background-color: #95ffa5")
            self.PELICULA14.setFont(QFont('Calibri', 12))
            self.lineEdit_14.setFont(QFont('Calibri', 12))
            self.lineEdit_14.setText("")
            self.lineEdit_14.setEnabled(True)
        elif self.pelicula == 15: 
            self.PELICULA15.setStyleSheet("background-color: ##")
            self.matI[14] = np.mean(self.matIR)
            self.lineEdit_15.setStyleSheet("background-color: #95ffa5")
            self.PELICULA15.setFont(QFont('Calibri', 12))
            self.lineEdit_15.setFont(QFont('Calibri', 12))
            self.lineEdit_15.setText("")
            self.lineEdit_15.setEnabled(True)
        elif self.pelicula == 16: 
            self.PELICULA16.setStyleSheet("background-color: ##")
            self.matI[15] = np.mean(self.matIR)
            self.lineEdit_16.setStyleSheet("background-color: #95ffa5")
            self.PELICULA16.setFont(QFont('Calibri', 12))
            self.lineEdit_16.setFont(QFont('Calibri', 12))
            self.lineEdit_16.setText("")
            self.lineEdit_16.setEnabled(True)
        elif self.pelicula == 17: 
            self.PELICULA17.setStyleSheet("background-color: ##")
            self.matI[16] = np.mean(self.matIR)
            self.lineEdit_17.setStyleSheet("background-color: #95ffa5")
            self.PELICULA17.setFont(QFont('Calibri', 12))
            self.lineEdit_17.setFont(QFont('Calibri', 12))
            self.lineEdit_17.setText("")
            self.lineEdit_17.setEnabled(True)
        elif self.pelicula == 18: 
            self.PELICULA18.setStyleSheet("background-color: ##")
            self.matI[17] = np.mean(self.matIR)
            self.lineEdit_18.setStyleSheet("background-color: #95ffa5")
            self.PELICULA18.setFont(QFont('Calibri', 12))
            self.lineEdit_18.setFont(QFont('Calibri', 12))
            self.lineEdit_18.setText("")
            self.lineEdit_18.setEnabled(True)
        elif self.pelicula == 19: 
            self.PELICULA19.setStyleSheet("background-color: ##")
            self.matI[18] = np.mean(self.matIR)
            self.lineEdit_19.setStyleSheet("background-color: #95ffa5")
            self.PELICULA19.setFont(QFont('Calibri', 12))
            self.lineEdit_19.setFont(QFont('Calibri', 12))
            self.lineEdit_19.setText("")
            self.lineEdit_19.setEnabled(True)
        elif self.pelicula == 20: 
            self.PELICULA20.setStyleSheet("background-color: ##")
            self.matI[19] = np.mean(self.matIR)
            self.lineEdit_20.setStyleSheet("background-color: #95ffa5")
            self.PELICULA20.setFont(QFont('Calibri', 12))
            self.lineEdit_20.setFont(QFont('Calibri', 12))
            self.lineEdit_20.setText("")
            self.lineEdit_20.setEnabled(True)
        elif self.pelicula == 100: 
            self.btnanz.setStyleSheet("background-color: ##")
            self.pelAnz = np.mean(self.matIR)
            self.btnanz.setFont(QFont('Calibri', 12))

#%% Código para introducir las dosis
    """
    Código para cuadros de texto "DOSIS". Para introducir los valores de dosis mediante un enter, de manera que sólo 
    acepta números enteros y da retroalimentación del último valor de dosis introducido.
    """
    def introducirDosis(self):
        if self.pelicula == 1:  # condicional para identificar a que botón pertenece la dosis.
            if self.lineEdit_1.text().isnumeric() == True:  # condicional para verificar que se introduzca un número.
                self.dosis[0] = float(self.lineEdit_1.text()) # introducimos el valor a la matriz de las dosis.
                x = "Última dosis introducida: " + str(self.dosis[0]) + "cGy. " #variable para reconocer el último valor de dosis reconocido.
                self.lineEdit_1.setStyleSheet("background-color: #ffffff") #cambio de color del line text correspondiente.
                self.lineEdit_1.setFont(QFont('Calibri', 12))
                self.label_5.setText(x) #retroalimentación del último valor de dosis introducido
            else:
                self.lineEdit_1.setText("FALTAN DATOS") #retroalimentación de que no se introdujo bien la dosis.
        elif self.pelicula == 2:  
            if self.lineEdit_2.text().isnumeric() == True:  
                self.dosis[1] = float(self.lineEdit_2.text()) 
                x = "Última dosis introducida: " + str(self.dosis[1]) + "cGy"
                self.lineEdit_2.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_2.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_2.setText("FALTAN DATOS") 
        elif self.pelicula == 3:  
            if self.lineEdit_3.text().isnumeric() == True:  
                self.dosis[2] = float(self.lineEdit_3.text()) 
                x = "Última dosis introducida: " + str(self.dosis[2]) + "cGy"
                self.lineEdit_3.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_3.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_3.setText("FALTAN DATOS") 
        elif self.pelicula == 4:  
            if self.lineEdit_4.text().isnumeric() == True:  
                self.dosis[3] = float(self.lineEdit_4.text()) 
                x = "Última dosis introducida: " + str(self.dosis[3]) + "cGy"
                self.lineEdit_4.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_4.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_4.setText("FALTAN DATOS") 
        elif self.pelicula == 5:  
            if self.lineEdit_5.text().isnumeric() == True:  
                self.dosis[4] = float(self.lineEdit_5.text()) 
                x = "Última dosis introducida: " + str(self.dosis[4]) + "cGy"
                self.lineEdit_5.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_5.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_5.setText("FALTAN DATOS") 
        elif self.pelicula == 6:  
            if self.lineEdit_6.text().isnumeric() == True:  
                self.dosis[5] = float(self.lineEdit_6.text()) 
                x = "Última dosis introducida: " + str(self.dosis[5]) + "cGy"
                self.lineEdit_6.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_6.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_6.setText("FALTAN DATOS") 
        elif self.pelicula == 7:  
            if self.lineEdit_7.text().isnumeric() == True:  
                self.dosis[6] = float(self.lineEdit_7.text()) 
                x = "Última dosis introducida: " + str(self.dosis[6]) + "cGy"
                self.lineEdit_7.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_7.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_7.setText("FALTAN DATOS") 
        elif self.pelicula == 8:  
            if self.lineEdit_8.text().isnumeric() == True:  
                self.dosis[7] = float(self.lineEdit_8.text()) 
                x = "Última dosis introducida: " + str(self.dosis[7]) + "cGy"
                self.lineEdit_8.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_8.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_8.setText("FALTAN DATOS") 
        elif self.pelicula == 9:  
            if self.lineEdit_9.text().isnumeric() == True:  
                self.dosis[8] = float(self.lineEdit_9.text()) 
                x = "Última dosis introducida: " + str(self.dosis[8]) + "cGy"
                self.lineEdit_9.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_9.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_9.setText("FALTAN DATOS") 
        elif self.pelicula == 10:  
            if self.lineEdit_10.text().isnumeric() == True:  
                self.dosis[9] = float(self.lineEdit_10.text()) 
                x = "Última dosis introducida: " + str(self.dosis[9]) + "cGy"
                self.lineEdit_10.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_10.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_10.setText("FALTAN DATOS") 
        elif self.pelicula == 11:  
            if self.lineEdit_11.text().isnumeric() == True:  
                self.dosis[10] = float(self.lineEdit_11.text()) 
                x = "Última dosis introducida: " + str(self.dosis[10]) + "cGy"
                self.lineEdit_11.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_11.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_11.setText("FALTAN DATOS") 
        elif self.pelicula == 12:  
            if self.lineEdit_12.text().isnumeric() == True:  
                self.dosis[11] = float(self.lineEdit_12.text()) 
                x = "Última dosis introducida: " + str(self.dosis[11]) + "cGy"
                self.lineEdit_12.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_12.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_12.setText("FALTAN DATOS") 
        elif self.pelicula == 13:  
            if self.lineEdit_13.text().isnumeric() == True:  
                self.dosis[12] = float(self.lineEdit_13.text()) 
                x = "Última dosis introducida: " + str(self.dosis[12]) + "cGy"
                self.lineEdit_13.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_13.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_13.setText("FALTAN DATOS") 
        elif self.pelicula == 14:  
            if self.lineEdit_14.text().isnumeric() == True:  
                self.dosis[13] = float(self.lineEdit_14.text()) 
                x = "Última dosis introducida: " + str(self.dosis[13]) + "cGy"
                self.lineEdit_14.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_14.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_14.setText("FALTAN DATOS") 
        elif self.pelicula == 15:  
            if self.lineEdit_15.text().isnumeric() == True:  
                self.dosis[14] = float(self.lineEdit_15.text()) 
                x = "Última dosis introducida: " + str(self.dosis[14]) + "cGy"
                self.lineEdit_15.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_15.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_15.setText("FALTAN DATOS") 
        elif self.pelicula == 16:  
            if self.lineEdit_16.text().isnumeric() == True:  
                self.dosis[15] = float(self.lineEdit_16.text()) 
                x = "Última dosis introducida: " + str(self.dosis[15]) + "cGy"
                self.lineEdit_16.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_16.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_16.setText("FALTAN DATOS") 
        elif self.pelicula == 17:  
            if self.lineEdit_17.text().isnumeric() == True:  
                self.dosis[16] = float(self.lineEdit_17.text()) 
                x = "Última dosis introducida: " + str(self.dosis[16]) + "cGy"
                self.lineEdit_17.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_17.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_17.setText("FALTAN DATOS") 
        elif self.pelicula == 18:  
            if self.lineEdit_18.text().isnumeric() == True:  
                self.dosis[17] = float(self.lineEdit_18.text()) 
                x = "Última dosis introducida: " + str(self.dosis[17]) + "cGy"
                self.lineEdit_18.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_18.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_18.setText("FALTAN DATOS") 
        elif self.pelicula == 19:  
            if self.lineEdit_19.text().isnumeric() == True:  
                self.dosis[18] = float(self.lineEdit_19.text()) 
                x = "Última dosis introducida: " + str(self.dosis[18]) + "cGy"
                self.lineEdit_19.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_19.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_19.setText("FALTAN DATOS") 
        elif self.pelicula == 20:  
            if self.lineEdit_20.text().isnumeric() == True:  
                self.dosis[19] = float(self.lineEdit_20.text()) 
                x = "Última dosis introducida: " + str(self.dosis[19]) + "cGy" 
                self.lineEdit_20.setStyleSheet("background-color: #ffffff") 
                self.lineEdit_20.setFont(QFont('Calibri', 12))
                self.label_5.setText(x)
            else:
                self.lineEdit_20.setText("FALTAN DATOS") 

#%% Código para cambiar la dosis de un cuadro anterior
    def cuadro1(self):
        self.lineEdit_1.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_1.setFont(QFont('Calibri', 12))
        self.pelicula = 1
    def cuadro2(self):
        self.lineEdit_2.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_2.setFont(QFont('Calibri', 12))
        self.pelicula = 2
    def cuadro3(self):
        self.lineEdit_3.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_3.setFont(QFont('Calibri', 12))
        self.pelicula = 3
    def cuadro4(self):
        self.lineEdit_4.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_4.setFont(QFont('Calibri', 12))
        self.pelicula = 4
    def cuadro5(self):
        self.lineEdit_5.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_5.setFont(QFont('Calibri', 12))
        self.pelicula = 5
    def cuadro6(self):
        self.lineEdit_6.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_6.setFont(QFont('Calibri', 12))
        self.pelicula = 6
    def cuadro7(self):
        self.lineEdit_7.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_7.setFont(QFont('Calibri', 12))
        self.pelicula = 7
    def cuadro8(self):
        self.lineEdit_8.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_8.setFont(QFont('Calibri', 12))
        self.pelicula = 8
    def cuadro9(self):
        self.lineEdit_9.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_9.setFont(QFont('Calibri', 12))
        self.pelicula = 9
    def cuadro10(self):
        self.lineEdit_10.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_10.setFont(QFont('Calibri', 12))
        self.pelicula = 10
    def cuadro11(self):
        self.lineEdit_11.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_11.setFont(QFont('Calibri', 12))
        self.pelicula = 11
    def cuadro12(self):
        self.lineEdit_12.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_12.setFont(QFont('Calibri', 12))
        self.pelicula = 12
    def cuadro13(self):
        self.lineEdit_13.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_13.setFont(QFont('Calibri', 12))
        self.pelicula = 13
    def cuadro14(self):
        self.lineEdit_14.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_14.setFont(QFont('Calibri', 12))
        self.pelicula = 14
    def cuadro15(self):
        self.lineEdit_15.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_15.setFont(QFont('Calibri', 12))
        self.pelicula = 15
    def cuadro16(self):
        self.lineEdit_16.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_16.setFont(QFont('Calibri', 12))
        self.pelicula = 16
    def cuadro17(self):
        self.lineEdit_17.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_17.setFont(QFont('Calibri', 12))
        self.pelicula = 17
    def cuadro18(self):
        self.lineEdit_18.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_18.setFont(QFont('Calibri', 12))
        self.pelicula = 18
    def cuadro19(self):
        
        self.lineEdit_19.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_19.setFont(QFont('Calibri', 12))
        self.pelicula = 19
    def cuadro20(self):
        self.lineEdit_20.setStyleSheet("background-color: #95ffa5")
        self.lineEdit_20.setFont(QFont('Calibri', 12))
        self.pelicula = 20
    
#%% Botón "OBTENER CURVA"
    def btnObtenerCurva3(self):
        self.textEdit.setEnabled(True) #habilitamos la linea de texto que está junto al botón "obtener curva"
        
        self.I = [] #matriz self.MatI con filtro para quitar los 0's.
        self.D = [] #matriz self.dosis con filtro para quitar los 0's.
        self.desvStd = [] #matriz stdDev con filtro para quitar los 0's
        self.DO = [] #matriz para los valores de densidad óptica.
        numeroDeDO = 0 #Contador para saber cuántas densidades ópticas se necesitan sacar.
        for a in self.matI:
            if a != 0:
                self.I.append(a)
                numeroDeDO = numeroDeDO + 1
        for a in self.dosis:
            if a != 0:
                self.D.append(a)
        for a in self.stdDev:
            if a !=0:
                self.desvStd.append(a)
        #print("I0:", self.pelicula0)
        #print("dosis: ",dosis)
        #print("intensidades", matI)
        for i in range (0, numeroDeDO):
            self.DO.append(math.log10(self.pelicula0/self.I[i]))
        #print(DO)
        self.eq = np.polyfit(self.DO, self.D, 3) #regresión de grado 4 con las densidades ópticas cómo X y las dosis cómo Y
        self.ran = np.poly1d(self.eq) 
        x = np.linspace(0,1) #rango X para graficar
        #forma = "ax^4+bx^3+cx^2+dx+e"
        # a = "a = " + str("{:.3e}".format(eq[0]))
        # b = "b = " + str("{:.3e}".format(eq[1]))
        # c = "c = " + str("{:.3e}".format(eq[2]))
        # d = "d = " + str("{:.3e}".format(eq[3]))
        # e = "e = " + str("{:.3e}".format(eq[4]))
        # curva = forma +"\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e
        b = str("{:.3e}".format(self.eq[0])) + "x^3 + "
        c = str("{:.3e}".format(self.eq[1])) + "x^2 + " 
        d = str("{:.3e}".format(self.eq[2])) + "x + "
        e = str("{:.3e}".format(self.eq[3]))
        self.curva = b + c + d + e
        
        self.textEdit.setText(self.curva)

        plt.plot(x, self.ran(x))
        plt.scatter(self.DO,self.D, color = 'red', marker = '.')
        plt.xlabel("Densidad óptica")
        plt.ylabel("Dosis [cGy]")
        plt.grid()
        
        self.figure = plt.gcf()
        
        self.figure.set_size_inches(8.5, 6.5)
        plt.savefig("curva.png", dpi=100)
        
        self.pix = QPixmap()
        self.pix.load("curva.png")
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMGCURVA.setScene(self.scene)
        self.IMGCURVA.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
    
    def btnObtenerCurva4(self):
        self.textEdit.setEnabled(True) #habilitamos la linea de texto que está junto al botón "obtener curva"
        
        self.I = [] #matriz self.MatI con filtro para quitar los 0's.
        self.D = [] #matriz self.dosis con filtro para quitar los 0's.
        self.desvStd = []
        self.DO = [] #matriz para los valores de densidad óptica.
        numeroDeDO = 0 #Contador para saber cuántas densidades ópticas se necesitan sacar.
        for a in self.matI:
            if a != 0:
                self.I.append(a)
                numeroDeDO = numeroDeDO + 1
        for a in self.dosis:
            if a != 0:
                self.D.append(a)
        for a in self.stdDev:
            if a !=0:
                self.desvStd.append(a)
        #print("I0:", self.pelicula0)
        #print("dosis: ",dosis)
        #print("intensidades", matI)
        for i in range (0, numeroDeDO):
            self.DO.append(math.log10(self.pelicula0/self.I[i]))
        #print(DO)
        self.eq = np.polyfit(self.DO, self.D, 4) #regresión de grado 4 con las densidades ópticas cómo X y las dosis cómo Y
        self.ran = np.poly1d(self.eq) 
        x = np.linspace(0,1) #rango X para graficar
        #forma = "ax^4+bx^3+cx^2+dx+e"
        # a = "a = " + str("{:.3e}".format(eq[0]))
        # b = "b = " + str("{:.3e}".format(eq[1]))
        # c = "c = " + str("{:.3e}".format(eq[2]))
        # d = "d = " + str("{:.3e}".format(eq[3]))
        # e = "e = " + str("{:.3e}".format(eq[4]))
        # curva = forma +"\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e
        
        a = str("{:.3e}".format(self.eq[0])) + "x^4 + "
        b = str("{:.3e}".format(self.eq[1])) + "x^3 + "
        c = str("{:.3e}".format(self.eq[2])) + "x^2 + " 
        d = str("{:.3e}".format(self.eq[3])) + "x + "
        e = str("{:.3e}".format(self.eq[4]))
        self.curva =  a + b + c + d + e
        
        self.textEdit.setText(self.curva)

        plt.plot(x, self.ran(x))
        plt.scatter(self.DO,self.D, color = 'red', marker = '.')
        plt.xlabel("Densidad óptica")
        plt.ylabel("Dosis [cGy]")
        plt.grid()
        
        self.figure = plt.gcf()
        
        self.figure.set_size_inches(8.5, 6.5)
        plt.savefig("curva.png", dpi=100)
        
        self.pix = QPixmap()
        self.pix.load("curva.png")
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMGCURVA.setScene(self.scene)
        self.IMGCURVA.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        
#%% Botónes "obtener curva" y "obtener dosis"
    def abrirCurva(self):
        self.btnanz.hide()
        self.btnBC.hide()
        self.scrollArea.show()
        self.label_3.show()
        self.BTN_CURVA3.show()
        self.BTN_CURVA4.show()
        self.textEdit.show()
        self.BTN_GI.show()
        self.BTN_GI_2.hide()
        self.obtD.hide()
        self.textEdit.setText("")
        self.label_8.hide()
    
    def abrirDosis(self):
        self.btnanz.show()
        self.btnBC.show()
        self.obtD.show()
        self.scrollArea.hide()
        self.label_3.hide()
        self.BTN_CURVA3.hide()
        self.BTN_CURVA4.hide()
        self.BTN_GI.hide()
        self.BTN_GI_2.show()
        self.textEdit.setText("")
        self.label_8.show()
        
#%% Botón película a analizar
    def analizarPel(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", 
                                            "TIFFFiles (*tif)")

        if fileName:
            #Se hace una copia del nombre del archivo para la funcionalidad del botón "reestablecer
            self.fileNamecopy = fileName 
            self.btnanz.setStyleSheet("background-color: #ff9e66") # cambiar color del botón
            self.btnanz.setFont(QFont('MS Shell Dlg 2', 12))
            
        
        self.pix = QPixmap()
        self.pix.load(fileName)
        self.r = []
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(self.item)
        self.IMAGEN.setScene(self.scene)
        self.IMAGEN.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.IMAGEN.rubberBandChanged.connect(self.on_rubberBandChanged)
        self.IMAGEN.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        self.x1=0 #x
        self.x2=0 #w
        self.y1=0 #y
        self.y2=0 #h
        self.x=[] #vector que delimita el ROI
        self.i= self.i+1 #contador para el funcionamiento correcto del botón cortar
        self.cont = 1 #condicional que permite utilizar el botón cortar
        self.matTif = tif.imread(fileName) #matríz que representa las intensidades de color de la película
        self.matTifR = np.copy(self.matTif[:, :, 0]) #matriz que representa las intensidades de la película en el rojo
        self.pelicula = 100
        self.label_6.setText("") #vaciamos las leyendas de la Iprom y desviación estándar de la última imágen abierta.
        self.label_7.setText("")
        
#%% Botón "GUARDAR INFORMACIÓN"
    """
    Código para realizar un archivo de texto donde se guarde toda la información utilizada.
    """
    def gdrInfo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, 
                                                  "Seleccionar dirección",
                                                  "", "All Files (*);;Text Files (*.txt)") #getSaveNameFile pythonspot pyqt5 file dialog
        date = datetime.datetime.now() #fecha al momento de guardar el archivo.
        letras = 0 #contador para obtener el mismo directorio del .txt y guardar la imágen de la curvad de calibración también
        for char in fileName: #con este for obtenermos el tamaño del directorio, le restaremos el ".txt" y agregaremos algo para identificar la imágen
            letras = letras + 1
        imgDir = str() #dirección en el que guardaremos la imágen.
        for i in range (0, letras-4):
            imgDir = imgDir + fileName[i]
        imgDir = imgDir + "_gráfica.png"
        f = open(fileName, "w")
        self.ecuacionarchivo = []
        
        contador = 0 #contador para los valores en el array de desviación estandar, que se usará para hacer una tabla en el archivo .txt con pretty table
        grado = 0
        for i in self.eq: #esto es para hacer un arreglo en el archivo que se utilizará para obtener dosis.
            self.ecuacionarchivo.append(i)
            grado = grado +1
        self.ecuacionarchivo.append(self.pelicula0)
        f.write(str(self.ecuacionarchivo)) # a partir de aquí se guardara información en el archivo y se generara de nuevo la gráfica que se guardará
        x = np.linspace(0,1) #rango X para graficar

        plt.plot(x, self.ran(x))
        plt.scatter(self.DO,self.D, color = 'red', marker = '.')
        plt.xlabel("Densidad óptica")
        plt.ylabel("Dosis [cGy]")
        plt.grid()
        
        self.figure = plt.gcf()
        
        self.figure.set_size_inches(8.5, 6.5)
        plt.savefig(imgDir, dpi=100)
        
        f.write("\n(necesario para la lectura del archivo) \nCurva de calibración:")
        f.write(self.curva)
        f.write("\nDatos utlizados:\n")
        myTable = PrettyTable(["PELÍCULA", "DOSIS", "INTENSIDAD (ROJO)", "DESVIACIÓN ESTÁNDAR (I)", "DO"]) # lo siguiente será para insertar una tabla con los datos usados y obtenidos del programa.
        for a in self.desvStd:
            contador = contador + 1
        for i in range (0,contador):
            if i == 0:
                myTable.add_row([str(i), str(i), str(self.pelicula0), str(self.desvStd[i]), "n/a"])
            else: 
                myTable.add_row([str(i), str(self.D[i-1]), str(self.I[i-1]), str(self.desvStd[i]), str(self.DO[i-1])])
        f.write(str(myTable))
        
        f.write("\nCreación del archivo:")
        f.write(str(date))
        
#%% botón "CURVA DE CALIBRACIÓN A UTILIZAR"
    """
    Este botón es para seleccionar la curva previamente guardada que se utilizará para evaluar una película
    de dosis desconocida. Leerá el archivo seleccionado, y obtendrá la información necesaria para identificar la curva
    de calibración guardada.
    """
    def AbrirCurva(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', "", #getSaveNameFile pythonspot pyqt5 file dialog
                                            "Archivo de texto (*txt)")
        f = open(fileName, "r")
        linea = f.readline()

        contador = 0 #La información guardada en el archivo es una str, por lo que se usará un contador para quitar los corchetes de lo que se lee de la primera linea del archivo para posteriormente convertirlo a float
        arrcasi = str()
        for char in linea: 
            contador = contador + 1
        for i in range (1, contador-2): #se quitan los corchetes de la primera linea
            arrcasi = arrcasi + linea[i]
        arr = arrcasi.split() #se crea un arreglo con los contenidos de la primera linea, diferenciandolos por un espacio
        longitud = len(arr) #se obtiene la longitud del arreglo creado para ahora hacerlo un arreglo de float's
        self.arrFin = [] #arreglo que se utilizará al final
        for i in range (0,longitud): 
            j = arr[i]
            if i<longitud-1:
                j = j[:-1]
                self.arrFin.append(float(j)) #llenamos el arreglo que nos tiene los coeficientes de la curva
            self.pelicula0 = float(j) #recordamos la intensidad 0 para obtener la DO.
        longitud = len(self.arrFin)
        if longitud == 5:
            a = str("{:.3e}".format(self.arrFin[0])) + "x^4 (+) "
            b = str("{:.3e}".format(self.arrFin[1])) + "x^3 (+) "
            c = str("{:.3e}".format(self.arrFin[2])) + "x^2 (+) " 
            d = str("{:.3e}".format(self.arrFin[3])) + "x (+) "
            e = str("{:.3e}".format(self.arrFin[4]))
            curva =  "Curva: " + a + b + c + d + e
            self.label_8.setText(curva)
            self.ran = np.poly1d(self.arrFin) 
            x = np.linspace(0,1) #rango X para graficar
            plt.plot(x, self.ran(x))
            plt.xlabel("Densidad óptica")
            plt.ylabel("Dosis [cGy]")
            plt.grid()
            
            self.figure = plt.gcf()
            
            self.figure.set_size_inches(8.5, 6.5)
            plt.savefig("curva.png", dpi=100)
            
            self.pix = QPixmap()
            self.pix.load("curva.png")
            self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
            self.scene = QtWidgets.QGraphicsScene(self)
            self.scene.addItem(self.item)
            self.IMGCURVA.setScene(self.scene)
            self.IMGCURVA.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        elif longitud == 4:
            a = str("{:.3e}".format(self.arrFin[0])) + "x^3 (+) "
            b = str("{:.3e}".format(self.arrFin[1])) + "x^2 (+) "
            c = str("{:.3e}".format(self.arrFin[2])) + "x (+) " 
            d = str("{:.3e}".format(self.arrFin[3])) 
            self.ran = np.poly1d(self.arrFin) 
            x = np.linspace(0,1) #rango X para graficar
            plt.plot(x, self.ran(x))
            plt.xlabel("Densidad óptica")
            plt.ylabel("Dosis [cGy]")
            plt.grid()
            
            self.figure = plt.gcf()
            
            self.figure.set_size_inches(8.5, 6.5)
            plt.savefig("curva.png", dpi=100)
            
            self.pix = QPixmap()
            self.pix.load("curva.png")
            self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
            self.scene = QtWidgets.QGraphicsScene(self)
            self.scene.addItem(self.item)
            self.IMGCURVA.setScene(self.scene)
            self.IMGCURVA.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
            curva =  "Curva: " + a + b + c + d 
            self.label_8.setText(curva)
        

#%%Botón "OBTENER DOSIS"
    """
    Este botón es para evaluar una dosis desconocida con una curva de calibración determinada
    """
    def evaluarDosis(self):
        self.textEdit.setEnabled(True)
        DO = math.log10(self.pelicula0/self.pelAnz)
        longitud = len(self.arrFin)
        if longitud == 5:
            DOSIS = (self.arrFin[0]*DO**4+self.arrFin[1]*DO**3+
                     self.arrFin[2]*DO**2+self.arrFin[3]*DO+
                     self.arrFin[4])
            self.ran = np.poly1d(self.arrFin) 
            x = np.linspace(0,1) #rango X para graficar
            plt.plot(x, self.ran(x))
            plt.xlabel("Densidad óptica")
            plt.ylabel("Dosis [cGy]")
            plt.scatter(DO,DOSIS, color = 'red', marker = '.')
            plt.grid()
            
            self.figure = plt.gcf()
            
            self.figure.set_size_inches(8.5, 6.5)
            plt.savefig("curva.png", dpi=100)
            
            self.pix = QPixmap()
            self.pix.load("curva.png")
            self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
            self.scene = QtWidgets.QGraphicsScene(self)
            self.scene.addItem(self.item)
            self.IMGCURVA.setScene(self.scene)
            self.IMGCURVA.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        elif longitud == 4: 
            DOSIS = (self.arrFin[0]*DO**3+self.arrFin[1]*DO**2+
                     self.arrFin[2]*DO+self.arrFin[3])
            self.ran = np.poly1d(self.arrFin) 
            x = np.linspace(0,1) #rango X para graficar
            plt.plot(x, self.ran(x))
            plt.xlabel("Densidad óptica")
            plt.ylabel("Dosis [cGy]")
            plt.scatter(DO,DOSIS, color = 'red', marker = '.')
            plt.grid()
            
            self.figure = plt.gcf()
            
            self.figure.set_size_inches(8.5, 6.5)
            plt.savefig("curva.png", dpi=100)
            
            self.pix = QPixmap()
            self.pix.load("curva.png")
            self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
            self.scene = QtWidgets.QGraphicsScene(self)
            self.scene.addItem(self.item)
            self.IMGCURVA.setScene(self.scene)
            self.IMGCURVA.fitInView(self.scene.sceneRect(),Qt.KeepAspectRatio)
        DOSIS = str(DOSIS) + " cGy"
        self.textEdit.setText(str(DOSIS))
    
#%%Botón "CAPTURA DE PANTALLA"
    """
    Botón para tomar una captura de pantalla de la dosis obtenida
    """
    def SS(self):
        screenshot = QApplication.primaryScreen().grabWindow(0)
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName= QFileDialog.getSaveFileName(self, 'Seleccionar Dirección', "", #getSaveNameFile pythonspot pyqt5 file dialog
                                            "All Files (*);;PNG Files (*png)")
        self.imName=fileName[0]
        screenshot.save(f'{self.imName}.png')

#%%
## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()

    sys.exit(app.exec_())
