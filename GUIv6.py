# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 20:47:48 2022

@author: Cristian
"""
import csv
import os.path
import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mss

#Ventana principal
ventana = Tk()
ventana.geometry("400x300")
ventana.title("Monster Fight")

#Ubicación de las imágenes de los monsters
Dir ="C:/Users/MAF/OneDrive - ALVAREZ AUTOMOTRIZ/Python Scripts/Proyecto AiLab/"
Im1 = Image.open(Dir+"aquarder.png")
Im2 = Image.open(Dir+"firesor.png")
Im3 = Image.open(Dir+"electder.png")
Im4 = Image.open(Dir+"mousebug.png")
Im5 = Image.open(Dir+"splant.png")
Im6 = Image.open(Dir+"rockdog.png")


#Modificamos la imagen a un tamaño predeterminado
newsize = (100,100)
Im_1 = Im1.resize(newsize)
Im_2 = Im2.resize(newsize)
Im_3 = Im3.resize(newsize)
Im_4 = Im4.resize(newsize)
Im_5 = Im5.resize(newsize)
Im_6 = Im6.resize(newsize)

#Generar la imagen para Tk
im1 = ImageTk.PhotoImage(Im_1)
im2 = ImageTk.PhotoImage(Im_2)
im3 = ImageTk.PhotoImage(Im_3)
im4 = ImageTk.PhotoImage(Im_4)
im5 = ImageTk.PhotoImage(Im_5)
im6 = ImageTk.PhotoImage(Im_6)
Arreglo_im = [im1,im2,im3,im4,im5,im6]

#Frames para intercambiar
frame_inicio = Frame(ventana)
frame_inicio.pack()
frame_nuevo = Frame(ventana)
frame_sesion = Frame(ventana)
frame_modo = Frame(ventana)
frame_seleccion = Frame(ventana)
frame_batalla = Frame(ventana)
frame_ataques = Frame(frame_batalla)
frame_ataques.columnconfigure(0, weight=1)
frame_terminaste = Frame(ventana)

#Funciones
def Reg():

    frame_inicio.forget()
    frame_sesion.forget()
    frame_nuevo.pack()
    print("Reg")
     
def Log():
    frame_inicio.forget()
    frame_nuevo.forget()
    frame_sesion.pack()
    print("Log")

def Loggin():

    with open("usuario.csv") as archivo:
        lector = csv.reader(archivo,
                            delimiter=",",
                            quotechar=",",
                            quoting=csv.QUOTE_MINIMAL)
        for fila in lector:
            if len(fila)!=0:
                if(fila[0]==E4.get() and fila[1]==E5.get()):
                    bandera_sesion = 1
                    break
                elif(fila[0]==E4.get() and fila[1]!=E5.get()):
                    bandera_sesion = 2
                    break
                else:
                    bandera_sesion = 0
        
        if bandera_sesion == 1:
            mss.showinfo(title="Inicio Sesión",message="Datos válidos")
            frame_sesion.forget()
            frame_modo.pack()
        elif bandera_sesion == 2:
            mss.showerror(title="Contraseña incorrecta", message="Ha ingresado una contraseña incorrecta, favor de verificar.")
            
        else:
            respuesta=mss.askyesno(message="El usuario no existe ¿Desea crear un usuario?",title="Usuario")
            if respuesta == True:
                Reg()
                
def Save():


    with open("usuario.csv") as archivo:
        lector = csv.reader(archivo,
                            delimiter=",",
                            quotechar=",",
                            quoting=csv.QUOTE_MINIMAL)
        for fila in lector:
            if len(fila)!=0:
                if fila[0]==E1.get():
                    bandera_sesion = 1
                    break
                else:
                    bandera_sesion = 0
        
        if bandera_sesion == 1:
            mss.showerror(title="Registro usuario",message="El usuario ya existe en el registro")
        else:
            if E2.get() == E3.get():
                
                datos = [[E1.get(),E2.get()]]
                archivo = open("usuario.csv","a")
                with archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerows(datos)
                    print("Escritura exitosa")
                        
                Log()
                print("Iniciando sesión")
            else:
                mss.showerror(title="Contraseña incorrecta", message="Las constraseñas ingresadas no coinciden, favor de verificar.")
   
def Training():
    print("Modo entrenamiento")
    global modo
    modo = 1
    frame_modo.forget()
    frame_seleccion.pack()

def Story():
    global modo
    modo = 2    
    print("Modo historia")
    contador = 0
    memoria = 0
    arreglo = []
    with open("usuario.csv") as archivo:
        lector = csv.reader(archivo,
                            delimiter=",",
                            quotechar=",",
                            quoting=csv.QUOTE_MINIMAL)
        for fila in lector:
            if len(fila)!=0:
                if(fila[0]==E4.get()):
                    memoria =contador
                contador = contador+1
                arreglo.append(fila)

    if(len(arreglo[memoria])==4):
        texto = "1.- Presione Sí para reiniciar partida en el nivel "+str(int(arreglo[memoria][2])+1)+"\n2.- Presione No para cambiar el modo de juego"
        if(mss.askyesno(title="Continuar partida",message=texto)):
            
            Prueba(modo,int(arreglo[memoria][3])-1, int(arreglo[memoria][2]))
    else:
        frame_modo.forget()
        frame_seleccion.pack()
    
def Aquarder():
    global hum
    global modo
    global cpu
    
    if(hum==0 and modo == 1):
        B7.configure(bg="blue")
        mss.showinfo(title="Selección",message="Seleccione el contrincante")
        time.sleep(1)
        hum = 1
    elif(hum==0 and modo == 2):
        B7.configure(bg="blue")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        hum = 1            
    elif (hum!=0 and modo == 1):
        B7.configure(bg="red")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        cpu = 1

def Firesor():
    global hum
    global modo
    global cpu
    
    if(hum==0 and modo == 1):
        B8.configure(bg="blue")
        mss.showinfo(title="Selección",message="Seleccione el contrincante")
        time.sleep(1)
        hum = 2
    elif(hum==0 and modo == 2):
        B8.configure(bg="blue")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        hum = 2            
    elif (hum!=0 and modo == 1):
        B8.configure(bg="red")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        cpu = 2
       
def Electder():
    global hum
    global modo
    global cpu
    
    if(hum==0 and modo == 1):
        B9.configure(bg="blue")
        mss.showinfo(title="Selección",message="Seleccione el contrincante")
        time.sleep(1)
        hum = 3
    elif(hum==0 and modo == 2):
        B9.configure(bg="blue")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        hum = 3            
    elif (hum!=0 and modo == 1):
        B9.configure(bg="red")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        cpu = 3

def Mousebug():
    global hum
    global modo
    global cpu
    
    if(hum==0 and modo == 1):
        B10.configure(bg="blue")
        mss.showinfo(title="Selección",message="Seleccione el contrincante")
        time.sleep(1)
        hum = 4
    elif(hum==0 and modo == 2):
        B10.configure(bg="blue")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        hum = 4            
    elif (hum!=0 and modo == 1):
        B10.configure(bg="red")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        cpu = 4

def Splant():
    global hum
    global modo
    global cpu
    
    if(hum==0 and modo == 1):
        B11.configure(bg="blue")
        mss.showinfo(title="Selección",message="Seleccione el contrincante")
        time.sleep(1)
        hum = 5
    elif(hum==0 and modo == 2):
        B11.configure(bg="blue")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        hum = 5            
    elif (hum!=0 and modo == 1):
        B11.configure(bg="red")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        cpu = 5
    
def Rockdog():
    global hum
    global modo
    global cpu
    
    if(hum==0 and modo == 1):
        B12.configure(bg="blue")
        mss.showinfo(title="Selección",message="Seleccione el contrincante")
        time.sleep(1)
        hum = 6
    elif(hum==0 and modo == 2):
        B12.configure(bg="blue")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        hum = 6            
    elif (hum!=0 and modo == 1):
        B12.configure(bg="red")
        mss.showinfo(title="Iniciemos",message="Ya estás listo, presiona INICIAR")
        time.sleep(1)
        cpu = 6
        
def Detalle_1():
    print("Detalle")
    win = Toplevel(ventana)
    win.geometry("325x325")
    L6 = Label(win,image=im1)
    L6.pack(side="top")
    L7 = Label(win,text="Aquarder: tipo agua")
    L7.pack(side="top")
    L8 = Label(win,text="Ventaja con: Roca, Fuego")
    L8.pack(side="top")
    L9 = Label(win,text="Desventaja con: Eléctrico, Planta")
    L9.pack(side="top")
    L10 = Label(win,text="Normal con: Agua, Escarabajo")
    L10.pack(side="top")
    #L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|\nAqua-jef  |3 pt|  5 pt | 2 pt  |  5 pt  |  7 pt  |  4 pt  |\nCola-Ferr |2 pt|\nCabezazo  |2 pt|\nLluvia    | Potenciador de campo, 1 vez cada 3 turnos.\n          | tiene una duración de 2 turnos.",anchor="w")
    L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|")
    L11.pack(side=TOP,anchor="w")
    L12 = Label(win,text="Aqua-jet.  | 3 pt  |   5 pt   |   2 pt   |     5 pt     |    7 pt    |     4 pt   |")
    L12.pack(side=TOP,anchor="w")
    L13 = Label(win,text="Cola-Ferr. | 2 pt  |",anchor="w")
    L13.pack(side=TOP,anchor="w")
    L14 = Label(win,text="Cabezazo. | 2 pt  |",anchor="w")
    L14.pack(side=TOP,anchor="w")
    L15 = Label(win,text="Lluvia.       | Potenciador de campo, 1 vez cada 3 turnos.",anchor="w")
    L15.pack(side=TOP,anchor="w")
    L16 = Label(win,text="                  | tiene una duración de 2 turnos.",anchor="w")
    L16.pack(side=TOP,anchor="w")
        
def Detalle_2():
    print("Detalle")
    win = Toplevel(ventana)
    win.geometry("330x325")
    L6 = Label(win,image=im2)
    L6.pack(side="top")
    L7 = Label(win,text="Firesor: Tipo fuego")
    L7.pack(side="top")
    L8 = Label(win,text="Ventaja con: Planta, Escarabajo")
    L8.pack(side="top")
    L9 = Label(win,text="Desventaja con: Agua, Roca")
    L9.pack(side="top")
    L10 = Label(win,text="Normal con: Eléctrico, Fuego")
    L10.pack(side="top")
    #L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|\nAqua-jef  |3 pt|  5 pt | 2 pt  |  5 pt  |  7 pt  |  4 pt  |\nCola-Ferr |2 pt|\nCabezazo  |2 pt|\nLluvia    | Potenciador de campo, 1 vez cada 3 turnos.\n          | tiene una duración de 2 turnos.",anchor="w")
    L11 = Label(win,text="Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|")
    L11.pack(side=TOP,anchor="w")
    L12 = Label(win,text="Llamarada  | 3 pt  |   5 pt   |   2 pt   |     5 pt     |    7 pt    |     4 pt   |")
    L12.pack(side=TOP,anchor="w")
    L13 = Label(win,text="Embestida  | 2 pt  |",anchor="w")
    L13.pack(side=TOP,anchor="w")
    L14 = Label(win,text="Mordisco   | 2 pt  |",anchor="w")
    L14.pack(side=TOP,anchor="w")
    L15 = Label(win,text="Día sol        | Potenciador de campo, 1 vez cada 3 turnos.",anchor="w")
    L15.pack(side=TOP,anchor="w")
    L16 = Label(win,text="                    | tiene una duración de 2 turnos.",anchor="w")
    L16.pack(side=TOP,anchor="w")
        
def Detalle_3():
    print("Detalle")
    win = Toplevel(ventana)
    win.geometry("330x325")
    L6 = Label(win,image=im3)
    L6.pack(side="top")
    L7 = Label(win,text="Electder: Tipo eléctrico")
    L7.pack(side="top")
    L8 = Label(win,text="Ventaja con: Agua, Escarabajo")
    L8.pack(side="top")
    L9 = Label(win,text="Desventaja con: Roca, Planta")
    L9.pack(side="top")
    L10 = Label(win,text="Normal con: Eléctrico, Fuego")
    L10.pack(side="top")
    #L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|\nAqua-jef  |3 pt|  5 pt | 2 pt  |  5 pt  |  7 pt  |  4 pt  |\nCola-Ferr |2 pt|\nCabezazo  |2 pt|\nLluvia    | Potenciador de campo, 1 vez cada 3 turnos.\n          | tiene una duración de 2 turnos.",anchor="w")
    L11 = Label(win,text="Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|")
    L11.pack(side=TOP,anchor="w")
    L12 = Label(win,text="Trueno       | 3 pt  |   5 pt   |   2 pt   |     5 pt     |    7 pt    |     4 pt   |")
    L12.pack(side=TOP,anchor="w")
    L13 = Label(win,text="Arañazo     | 3 pt  |",anchor="w")
    L13.pack(side=TOP,anchor="w")
    L14 = Label(win,text="Mordisco   | 3 pt  |",anchor="w")
    L14.pack(side=TOP,anchor="w")
    L15 = Label(win,text="Campo m  | Potenciador de campo, 1 vez cada 3 turnos.",anchor="w")
    L15.pack(side=TOP,anchor="w")
    L16 = Label(win,text="                    | tiene una duración de 2 turnos.",anchor="w")
    L16.pack(side=TOP,anchor="w")
        
def Detalle_4():
    print("Detalle")
    win = Toplevel(ventana)
    win.geometry("330x325")
    L6 = Label(win,image=im4)
    L6.pack(side="top")
    L7 = Label(win,text="Mousebug: Tipo escarabajo")
    L7.pack(side="top")
    L8 = Label(win,text="Ventaja con: Planta, Roca")
    L8.pack(side="top")
    L9 = Label(win,text="Desventaja con: Fuego, Eléctrico")
    L9.pack(side="top")
    L10 = Label(win,text="Normal con: Escarabajo, Agua")
    L10.pack(side="top")
    #L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|\nAqua-jef  |3 pt|  5 pt | 2 pt  |  5 pt  |  7 pt  |  4 pt  |\nCola-Ferr |2 pt|\nCabezazo  |2 pt|\nLluvia    | Potenciador de campo, 1 vez cada 3 turnos.\n          | tiene una duración de 2 turnos.",anchor="w")
    L11 = Label(win,text="Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|")
    L11.pack(side=TOP,anchor="w")
    L12 = Label(win,text="Picotazo      | 3 pt  |   5 pt   |   2 pt   |     5 pt     |    7 pt    |     4 pt   |")
    L12.pack(side=TOP,anchor="w")
    L13 = Label(win,text="Embestida  | 2 pt  |",anchor="w")
    L13.pack(side=TOP,anchor="w")
    L14 = Label(win,text="Cabezazo   | 2 pt  |",anchor="w")
    L14.pack(side=TOP,anchor="w")
    L15 = Label(win,text="Esporas      | Potenciador de campo, 1 vez cada 3 turnos.",anchor="w")
    L15.pack(side=TOP,anchor="w")
    L16 = Label(win,text="                    | tiene una duración de 2 turnos.",anchor="w")
    L16.pack(side=TOP,anchor="w")

def Detalle_5():
    print("Detalle")
    win = Toplevel(ventana)
    win.geometry("330x325")
    L6 = Label(win,image=im5)
    L6.pack(side="top")
    L7 = Label(win,text="Splant: Tipo Planta")
    L7.pack(side="top")
    L8 = Label(win,text="Ventaja con: Roca, Agua, Eléctrico")
    L8.pack(side="top")
    L9 = Label(win,text="Desventaja con: Fuego, Escarabajo")
    L9.pack(side="top")
    L10 = Label(win,text="Normal con: Planta")
    L10.pack(side="top")
    #L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|\nAqua-jef  |3 pt|  5 pt | 2 pt  |  5 pt  |  7 pt  |  4 pt  |\nCola-Ferr |2 pt|\nCabezazo  |2 pt|\nLluvia    | Potenciador de campo, 1 vez cada 3 turnos.\n          | tiene una duración de 2 turnos.",anchor="w")
    L11 = Label(win,text="Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|")
    L11.pack(side=TOP,anchor="w")
    L12 = Label(win,text="Hoja nav     | 3 pt  |   5 pt   |   2 pt   |     5 pt     |    7 pt    |     4 pt   |")
    L12.pack(side=TOP,anchor="w")
    L13 = Label(win,text="Mordisco   | 2 pt  |",anchor="w")
    L13.pack(side=TOP,anchor="w")
    L14 = Label(win,text="Cabezazo   | 2 pt  |",anchor="w")
    L14.pack(side=TOP,anchor="w")
    L15 = Label(win,text="Rayo sol     | Potenciador de campo, 1 vez cada 3 turnos.",anchor="w")
    L15.pack(side=TOP,anchor="w")
    L16 = Label(win,text="                   | tiene una duración de 2 turnos.",anchor="w")
    L16.pack(side=TOP,anchor="w")

def Detalle_6():
    print("Detalle")
    win = Toplevel(ventana)
    win.geometry("330x325")
    L6 = Label(win,image=im6)
    L6.pack(side="top")
    L7 = Label(win,text="Rockdog: Tipo Roca")
    L7.pack(side="top")
    L8 = Label(win,text="Ventaja con: Fuego, Eléctrico")
    L8.pack(side="top")
    L9 = Label(win,text="Desventaja con: Agua, Planta")
    L9.pack(side="top")
    L10 = Label(win,text="Normal con: Roca, Escarabajo")
    L10.pack(side="top")
    #L11 = Label(win,text="Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|\nAqua-jef  |3 pt|  5 pt | 2 pt  |  5 pt  |  7 pt  |  4 pt  |\nCola-Ferr |2 pt|\nCabezazo  |2 pt|\nLluvia    | Potenciador de campo, 1 vez cada 3 turnos.\n          | tiene una duración de 2 turnos.",anchor="w")
    L11 = Label(win,text="Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|")
    L11.pack(side=TOP,anchor="w")
    L12 = Label(win,text="Roca afil.    | 3 pt  |   5 pt   |   2 pt   |     5 pt     |    7 pt    |     4 pt   |")
    L12.pack(side=TOP,anchor="w")
    L13 = Label(win,text="Velocidad  | 2 pt  |",anchor="w")
    L13.pack(side=TOP,anchor="w")
    L14 = Label(win,text="Cola fer      | 2 pt  |",anchor="w")
    L14.pack(side=TOP,anchor="w")
    L15 = Label(win,text="Campo ro  | Potenciador de campo, 1 vez cada 3 turnos.",anchor="w")
    L15.pack(side=TOP,anchor="w")
    L16 = Label(win,text="                    | tiene una duración de 2 turnos.",anchor="w")
    L16.pack(side=TOP,anchor="w")

def Iniciar():
    
    global modo
    global hum
    global cpu
    
    print("Iniciar")
    if(modo==2):
        if(mss.askyesno(message="¿Estás listo?",title="Vamos a la pelea")):
            contador = 0
            memoria = 0
            arreglo = []
            with open("usuario.csv") as archivo:
                lector = csv.reader(archivo,
                                    delimiter=",",
                                    quotechar=",",
                                    quoting=csv.QUOTE_MINIMAL)
                for fila in lector:
                    if len(fila)!=0:
                        if(fila[0]==E4.get()):
                            memoria =contador
                        contador = contador+1
                        arreglo.append(fila)
            
            arreglo[memoria].append(0)
            arreglo[memoria].append(hum)
            print(arreglo)
            archivo=open("usuario.csv","w")
            with archivo:
                escritor=csv.writer(archivo)
                escritor.writerows(arreglo)
            
            
            Prueba(modo, hum-1, 0)
            B7.configure(bg="gray")
            B8.configure(bg="gray")
            B9.configure(bg="gray")
            B10.configure(bg="gray")
            B11.configure(bg="gray")
            B12.configure(bg="gray")
            hum = 0
            
        else:
            B7.configure(bg="gray")
            B8.configure(bg="gray")
            B9.configure(bg="gray")
            B10.configure(bg="gray")
            B11.configure(bg="gray")
            B12.configure(bg="gray")
            time.sleep(1)
            hum = 0
    else:
        if(hum!=0 and cpu != 0):
            if(mss.askyesno(message="¿Estás Listo?",title="Vamos a la pelea")):
                Prueba(modo,hum-1,cpu-1)
                B7.configure(bg="gray")
                B8.configure(bg="gray")
                B9.configure(bg="gray")
                B10.configure(bg="gray")
                B11.configure(bg="gray")
                B12.configure(bg="gray")
                hum = 0
                cpu= 0
        else:
            mss.showinfo(title="Selección",message="Tienes que seleccionar a dos personajes")

def Prueba(modo,humano,compu):

    import random

    
    class monster:
        def __init__(self, nombre, tipo, ataques):
            self.nombre = nombre
            self.tipo = tipo
            self.ataques = ataques
            self.hp = 25
            self.ventaja = 0
    
        def update_hp(self, dato):
            self.hp = dato
    
        def update_ataque(self, dato):
            """actualiza el daño del primer ataque"""
            self.ataques[0][1] = self.ataques[0][1]+dato
    
        def config(self, dato):
            """Si dato es -1 el monster no tiene ventaja\nSi dato es 0 el monster tiene ataque normal/nSi dato es 1 el monster tiene ventaja"""
            if dato == 1:
                self.ventaja = 1
                self.ataques[0][1] = self.ataques[0][1]+2
            elif dato == -1:
                self.ventaja = -1
                self.ataques[0][1] = self.ataques[0][1]-1
    
    
    def fight(hum_mon, cpu_mon):
        """hum_mon es el monster del jugador\ncpu_mon es el monster del CPU"""
        def ataque_1():
            botonpresionado.set(1)
        def ataque_2():
            botonpresionado.set(2)
        def ataque_3():
            botonpresionado.set(3)
        def ataque_4():
            botonpresionado.set(4)
        
        def pruebafuncion():
            print("Empieza la espera")
            result= B20.wait_variable(botonpresionado)
            print(result)
            print("Se termina la espera")
            
        #Este frame es para la pelea
        global hum
        global cpu
        global Arreglo_im
        botonpresionado = IntVar()
        text_mensaje = StringVar()
        text_hp_hum = StringVar()
        text_hp_cpu= StringVar()
        
        bandera_turno = 0
        bandera_pot_hum = 0
        bandera_ganador = 0
    
        bandera_pot_cpu = 0
        cont_pot_hum = 0
        cont_pot_cpu = 0
        
        ataque_hum = 0
        
        

        B20 = Button(frame_ataques,text=hum_mon.ataques[0][0],command=ataque_1)
        B20.pack(side="top")
        B21 = Button(frame_ataques,text=hum_mon.ataques[1][0],command=ataque_2)
        B21.pack(side="top")
        B22 = Button(frame_ataques,text=hum_mon.ataques[2][0],command=ataque_3)
        B22.pack(side="top")
        B23 = Button(frame_ataques,text=hum_mon.ataques[3][0],command=ataque_4)
        B23.pack(side="top")
        frame_ataques.grid(column=0,row=0,sticky="we")
        L6 = Label(frame_batalla,image=Arreglo_im[hum-1])
        L6.grid(column=1,row=0)
        L7 = Label(frame_batalla,image=Arreglo_im[cpu-1])
        L7.grid(column=2,row=0)
        L8 = Label(frame_batalla,text=hum_mon.nombre)
        L8.grid(column=1,row=1)
        L9 = Label(frame_batalla,text=cpu_mon.nombre)
        L9.grid(column=2,row=1)
        textohphum = str(hum_mon.hp)+" HP"
        text_hp_hum.set(textohphum)
        L10 = Label(frame_batalla,textvariable=text_hp_hum)
        L10.grid(column=1,row=2)
        textohpcpu = str(cpu_mon.hp)+" HP"
        text_hp_cpu.set(textohpcpu)
        L11 = Label(frame_batalla,textvariable=text_hp_cpu)
        L11.grid(column=2,row=2)
        texto = "La batalla será entre "+str(hum_mon.nombre)+" y "+str(cpu_mon.nombre)
        text_mensaje.set(texto)
        L12 = Label(frame_batalla,textvariable=text_mensaje)
        L12.grid(column=0,row=3,sticky="we",columnspan=3)
        
        frame_modo.forget()
        frame_seleccion.forget()
        frame_batalla.pack()
    
        if hum_mon.tipo == "Agua":
            if cpu_mon.tipo == "Roca" or cpu_mon.tipo == "Fuego":
                hum_mon.config(1)
                cpu_mon.config(-1)
            if cpu_mon.tipo == "Eléctrico" or cpu_mon.tipo == "Planta":
                hum_mon.config(-1)
                cpu_mon.config(1)
        elif hum_mon.tipo == "Fuego":
            if cpu_mon.tipo == "Planta" or cpu_mon.tipo == "Escarabajo":
                hum_mon.config(1)
                cpu_mon.config(-1)
            if cpu_mon.tipo == "Agua" or cpu_mon.tipo == "Roca":
                hum_mon.config(-1)
                cpu_mon.config(1)
        elif hum_mon.tipo == "Eléctrico":
            if cpu_mon.tipo == "Agua" or cpu_mon.tipo == "Escarabajo":
                hum_mon.config(1)
                cpu_mon.config(-1)
            if cpu_mon.tipo == "Roca" or cpu_mon.tipo == "Planta":
                hum_mon.config(-1)
                cpu_mon.config(1)
        elif hum_mon.tipo == "Escarabajo":
            if cpu_mon.tipo == "Planta" or cpu_mon.tipo == "Roca":
                hum_mon.config(1)
                cpu_mon.config(-1)
            if cpu_mon.tipo == "Fuego" or cpu_mon.tipo == "Eléctrico":
                hum_mon.config(-1)
                cpu_mon.config(1)
        elif hum_mon.tipo == "Planta":
            if cpu_mon.tipo == "Roca" or cpu_mon.tipo == "Agua" or cpu_mon.tipo == "Eléctrico":
                hum_mon.config(1)
                cpu_mon.config(-1)
            if cpu_mon.tipo == "Fuego" or cpu_mon.tipo == "Escarabajo":
                hum_mon.config(-1)
                cpu_mon.config(1)
        elif hum_mon.tipo == "Roca":
            if cpu_mon.tipo == "Fuego" or cpu_mon.tipo == "Eléctrico":
                hum_mon.config(1)
                cpu_mon.config(-1)
            if cpu_mon.tipo == "Agua" or cpu_mon.tipo == "Planta":
                hum_mon.config(-1)
                cpu_mon.config(1)
        


        
        while(hum_mon.hp > 0 and cpu_mon.hp > 0):
            time.sleep(1)
            if bandera_turno == 0:
                # 0 va primero humano y 1 va primero cpu
                turno = random.randint(0, 1)
                if turno == 0:
                    texto = "Va primero el humano... agarráte CPU"
                else:
                    texto = "Va primero el CPU... agarráte humano"
                bandera_turno = 1
                text_mensaje.set(texto)
            time.sleep(1)
            if turno == 0:
    
                text_mensaje.set("Va el humano de elegir")
                time.sleep(1)
                
                frame_ataques.wait_variable(botonpresionado)
                
                ataque_hum=botonpresionado.get()-1
                move_hum = hum_mon.ataques[ataque_hum]
                texto = "Humano eligió ataque... " + move_hum[0]
                text_mensaje.set(texto)
                if ataque_hum == 3:
                    if bandera_pot_hum == 0:
                        hum_mon.update_ataque(2)
                        bandera_pot_hum = bandera_pot_hum+1
                    else:
                        while (ataque_hum == 3):
                            texto = "Selecciona otro ataque, te falta " + str((4-cont_pot_hum)) +" turno(s) para usarlo de nuevo"
                            text_mensaje.set(texto)
                            time.sleep(1)
                            frame_ataques.wait_variable(botonpresionado)
                            ataque_hum=botonpresionado.get()-1
                        move_hum = hum_mon.ataques[ataque_hum]
                        texto = "Humano eligió ataque... " + str(move_hum[0]) 
                        text_mensaje.set(texto)
                        cpu_mon.update_hp(cpu_mon.hp-move_hum[1])
                        text_hp_cpu.set(str(cpu_mon.hp)+" HP")
    
                else:
                    # move_hum = hum_mon.ataques[ataque_hum]
                    cpu_mon.update_hp(cpu_mon.hp-move_hum[1])
                    text_hp_cpu.set(str(cpu_mon.hp)+" HP")
                
                time.sleep(1)
                text_mensaje.set("Va el CPU de elegir")
                time.sleep(1)
    
                ataque_cpu = random.randint(0, 3)
                move_cpu = cpu_mon.ataques[ataque_cpu]
                texto = "CPU eligió ataque... " + str(move_cpu[0])
                text_mensaje.set(texto)
    
                if ataque_cpu == 3:
                    if bandera_pot_cpu == 0:
                        cpu_mon.update_ataque(2)
                        bandera_pot_cpu = bandera_pot_cpu+1
                    else:
                        while(ataque_cpu == 3):
                            texto = "Selecciona otro ataque, te falta " + str((4-cont_pot_cpu)) +" turno(s) para usarlo de nuevo"
                            text_mensaje.set(texto)
                            time.sleep(1)
                            ataque_cpu = random.randint(0, 3)
                        move_cpu = cpu_mon.ataques[ataque_cpu]
                        texto = "CPU eligió ataque..." + str(move_cpu[0])
                        text_mensaje.set(texto)
                        hum_mon.update_hp(hum_mon.hp-move_cpu[1])
                        text_hp_hum.set(str(hum_mon.hp) + " HP")
                        time.sleep(1)
    
                else:
                   #move_cpu = cpu_mon.ataques[ataque_cpu]
                    hum_mon.update_hp(hum_mon.hp-move_cpu[1])
                    text_hp_hum.set(str(hum_mon.hp) + " HP")
    
                time.sleep(1)
    
            else:
                text_mensaje.set("Va el CPU de elegir")
                time.sleep(1)
                ataque_cpu = random.randint(0, 3)
                move_cpu = cpu_mon.ataques[ataque_cpu]
                texto = "CPU eligió ataque..." + str(move_cpu[0])
                text_mensaje.set(texto)
                if ataque_cpu == 3:
                    if bandera_pot_cpu == 0:
                        cpu_mon.update_ataque(2)
                        bandera_pot_cpu = bandera_pot_cpu+1
                    else:
                        while(ataque_cpu == 3):
                            texto = "Selecciona otro ataque, te falta " + str((4-cont_pot_cpu)) +" turno(s) para usarlo de nuevo"
                            text_mensaje.set(texto)
                            time.sleep(0.5)
                            ataque_cpu = random.randint(0, 3)
                        move_cpu = cpu_mon.ataques[ataque_cpu]
                        texto = "CPU eligió ataque..." + str(move_cpu[0])
                        text_mensaje.set(texto)
                        hum_mon.update_hp(hum_mon.hp-move_cpu[1])
                        text_hp_hum.set(str(hum_mon.hp) + " HP")
                       
    
                else:
                   #move_cpu = cpu_mon.ataques[ataque_cpu]
                    hum_mon.update_hp(hum_mon.hp-move_cpu[1])
                    text_hp_hum.set(str(hum_mon.hp) + " HP")
                time.sleep(1)
                text_mensaje.set("Va el humano de elegir")
                time.sleep(1)
                
            
                frame_ataques.wait_variable(botonpresionado)
                frame_ataques.update()
                
                ataque_hum=botonpresionado.get()-1
                move_hum = hum_mon.ataques[ataque_hum]
                texto = "Humano eligió ataque..." + move_hum[0]
                text_mensaje.set(texto)
                if ataque_hum == 3:
                    if bandera_pot_hum == 0:
                        hum_mon.update_ataque(2)
                        bandera_pot_hum = bandera_pot_hum+1
                    else:
                        while (ataque_hum == 3):
                            texto = "Selecciona otro ataque, te falta " + str((4-cont_pot_hum)) +" turno(s) para usarlo de nuevo"
                            text_mensaje.set(texto)
                            frame_ataques.wait_variable(botonpresionado)
                            frame_ataques.update()
                            
                            
                            ataque_hum=botonpresionado.get()-1
                        move_hum = hum_mon.ataques[ataque_hum]
                        texto = "Humano eligió ataque... " + str(move_hum[0]) 
                        text_mensaje.set(texto)
                        cpu_mon.update_hp(cpu_mon.hp-move_hum[1])
                        text_hp_cpu.set(str(cpu_mon.hp)+" HP")
    
                else:
                    # move_hum = hum_mon.ataques[ataque_hum]
                    cpu_mon.update_hp(cpu_mon.hp-move_hum[1])
                    text_hp_cpu.set(str(cpu_mon.hp)+" HP")
                    
                time.sleep(1)
    
            if bandera_pot_hum == 1:
                if cont_pot_hum < 2:
                    cont_pot_hum = cont_pot_hum+1
                elif cont_pot_hum == 2:
                    hum_mon.update_ataque(-2)
                    cont_pot_hum = cont_pot_hum+1
                else:
                    bandera_pot_hum = 0
                    cont_pot_hum = 0
    
            if bandera_pot_cpu == 1:
                if cont_pot_cpu < 2:
                    cont_pot_cpu = cont_pot_cpu+1
                elif cont_pot_cpu == 2:
                    cpu_mon.update_ataque(-2)
                    cont_pot_cpu = cont_pot_cpu+1
                else:
                    bandera_pot_cpu = 0
                    cont_pot_cpu = 0
    
        time.sleep(1)
        if(hum_mon.hp > 0):
            texto = "Pelea terminada... El ganador es el humano con el monster: " + hum_mon.nombre
            text_mensaje.set(texto)
            bandera_ganador = 1 #1 si gana humano y 2 si gana CPU
        else:
            texto = "Pelea terminada... El ganador es el humano con el monster: " + cpu_mon.nombre
            text_mensaje.set(texto)
            bandera_ganador = 2
        time.sleep(1)
        
        
        return bandera_ganador       
    
    
    def monsters(dato):
        if dato == 0:
            salida = monster("Aquarder", "Agua", [["Aqua-jet", 3], ["Cola férrea", 2],["Cabezazo", 2], ["Lluvia", "Potenciador"]])
        elif dato == 1:
            salida = monster("Firesor", "Fuego", [["Llamarada", 3], ["Embestida", 2], ["Mordisco", 2], ["Día soleado", "Potenciador"]])
        elif dato == 2:
            salida = monster("Electder", "Eléctrico", [["Trueno", 3], ["Arañazo", 3], ["Mordisco", 3], ["Campo magnético", "Potenciador"]])
        elif dato == 3:
            salida = monster("Mousebug", "Escarabajo", [["Picotazo", 3], ["Embestida", 2], ["Cabezazo", 2], ["Esporas", "Potenciador"]])
        elif dato == 4:
            salida = monster("Splant", "Planta", [["Hoja navaja", 3], ["Mordisco", 2], ["Cabezazo", 2], ["Rayo solar", "Potenciador"]])
        elif dato == 5:
            salida = monster("Rockdog", "Roca", [["Roca afilada", 3], ["Velocidad", 2], ["Cola ferrea", 2], ["Campo rocoso", "Potenciador"]])
        else:
            print("Error no existe este monster")
        return salida
    
    """
    aquarder = monster("Aquarder", "Agua", [["Aqua-jet", 3], ["Cola férrea", 2],["Cabezazo", 2], ["Lluvia", "Potenciador"]])
    firesor = monster("Firesor", "Fuego", [["Llamarada", 3], ["Embestida", 2], ["Mordisco", 2], ["Día soleado", "Potenciador"]])
    electder = monster("Electder", "Eléctrico", [["Trueno", 3], ["Arañazo", 3], ["Mordisco", 3], ["Campo magnético", "Potenciador"]])
    mousebug = monster("Mousebug", "Escarabajo", [["Picotazo", 3], ["Embestida", 2], ["Cabezazo", 2], ["Esporas", "Potenciador"]])
    splant = monster("Splant", "Planta", [["Hoja navaja", 3], ["Mordisco", 2], ["Cabezazo", 2], ["Rayo solar", "Potenciador"]])
    rockdog = monster("Rockdog", "Roca", [["Roca afilada", 3], ["Velocidad", 2], ["Cola ferrea", 2], ["Campo rocoso", "Potenciador"]])
    monsters = [aquarder, firesor, electder, mousebug, splant, rockdog]
    """

    
    ganador = 0
    
    if modo == 1:  # 1 es modo entrenamiento y 2 es modo historia
        monster_humano = monsters(humano)
        monster_cpu = monsters(compu)
        fight(monster_humano, monster_cpu)

        frame_batalla.forget()
        frame_seleccion.pack()


    
    elif modo == 2:
        arreglo = []
        memoria = 0
        contador = 0
        with open("usuario.csv") as archivo:
            lector = csv.reader(archivo,
                                delimiter=",",
                                quotechar=",",
                                quoting=csv.QUOTE_MINIMAL)
            for fila in lector:
                if len(fila)!=0:
                    if(fila[0]==E4.get()):
                        memoria =contador
                    contador = contador+1
                    arreglo.append(fila)
        print(arreglo)
        print(memoria)
        print(E4.get())

                        
        for i in range(compu,5):
            
            while(ganador!=1):
                monster_humano = monsters(humano)
                monster_cpu = monsters(i)
                ganador = fight(monster_humano, monster_cpu)

            ganador = 0
            arreglo[memoria][2] = i+1
            archivo=open("usuario.csv","w")
            with archivo:
                escritor=csv.writer(archivo)
                escritor.writerows(arreglo)
                
            
        print("Felicidades ganaste el modo historia")
        frame_batalla.forget()
        frame_terminaste.pack()
        os.remove("usuario.csv")
        

modo = 0
hum = 0
cpu = 0

#Funcionalidad si no existe el archivo. Lo crea y agrega los headers
if not os.path.isfile("usuario.csv"):
    archivo=open("usuario.csv","w")
    with archivo:
        datos = [["Usuario","Contraseña","Nivel","Monster"]]
        escritor=csv.writer(archivo)
        escritor.writerows(datos)

#Este frame se usa para seleccionar iniciar sesión o registrar usuario
L1 = Label(frame_inicio, text="Monster Fight")
L1.pack(side="top")

B1 = Button(frame_inicio, text="Iniciar Sesión", command=Log)
B1.pack(side="top")

B2 = Button(frame_inicio, text="Usuario Nuevo", command=Reg)
B2.pack(side="top")

#Este frame es para dar de alta un usuario
L2 = Label(frame_nuevo, text="Usuario")
L2.pack(side="top")
E1 = Entry(frame_nuevo)
E1.pack(side="top")
L3 = Label(frame_nuevo, text="Contraseña")
L3.pack(side="top")   
E2 = Entry(frame_nuevo,show="*")
E2.pack(side="top")
L4 = Label(frame_nuevo, text="Re-Contraseña")
L4.pack(side="top")     
E3 = Entry(frame_nuevo,show="*")
E3.pack(side="top")
B3 = Button(frame_nuevo, text="Guardar",command=Save)
B3.pack(side="top")

#Este frame es para iniciar sesión
L5 = Label(frame_sesion, text="Usuario")
L5.pack(side="top")
E4 = Entry(frame_sesion)
E4.pack(side="top")
L5 = Label(frame_sesion, text="Contraseña")
L5.pack(side="top")  
E5 = Entry(frame_sesion,show="*")
E5.pack(side="top")
L5 = Label(frame_sesion)
L5.pack(side="top")
B4 = Button(frame_sesion, text="Iniciar Sesión",command=Loggin)
B4.pack(side="top")

#Este frame es para seleccionar el modo de juego
B5 = Button(frame_modo, text="Modo entrenamiento",command=Training)
B5.pack(side="left")
B6 = Button(frame_modo, text="Modo historia",command=Story)
B6.pack(side="right")


#Este frame es para la selección de personajes
B7= Button(frame_seleccion,text="Aquarder", command = Aquarder, bg="gray")
B7.grid(column=1,row=1)
B7.config(image=im1)
B13 = Button(frame_seleccion,text="Detalle", command = Detalle_1)
B13.grid(column=1,row=2)

B8= Button(frame_seleccion,text="Firesor", command = Firesor, bg="gray")
B8.grid(column=2,row=1)
B8.config(image=im2)
B14 = Button(frame_seleccion,text="Detalle", command = Detalle_2)
B14.grid(column=2,row=2)

B9= Button(frame_seleccion,text="Electder", command = Electder, bg="gray")
B9.grid(column=3,row=1)
B9.config(image=im3)
B15 = Button(frame_seleccion,text="Detalle", command = Detalle_3)
B15.grid(column=3,row=2)

B10= Button(frame_seleccion,text="Mousebug", command = Mousebug, bg="gray")
B10.grid(column=1,row=3)
B10.config(image=im4)
B16 = Button(frame_seleccion,text="Detalle", command = Detalle_4)
B16.grid(column=1,row=4)

B11= Button(frame_seleccion,text="Splant", command = Splant, bg="gray")
B11.grid(column=2,row=3)
B11.config(image=im5)
B17 = Button(frame_seleccion,text="Detalle", command = Detalle_5)
B17.grid(column=2,row=4)

B12= Button(frame_seleccion,text="Rockdog", command = Rockdog, bg="gray")
B12.grid(column=3,row=3)
B12.config(image=im6)
B18 = Button(frame_seleccion,text="Detalle", command = Detalle_6)
B18.grid(column=3,row=4)

B19 = Button(frame_seleccion,text="INICIAR",command = Iniciar)
B19.grid(column=2,row=5)

L6 = Label(frame_terminaste,text="¡FELICIDADES! TERMINASTE")
L6.pack(anchor="center")


ventana.mainloop()