import	tkinter as tk

ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('350x600')
ventana.resizable(False,False)
ventana.configure(background='grey')

#FUNCIONES
operacion = ' '
resultado = StringVar()

def borrar():
	global operacion
	global resultado
	operacion = ' '
	pantalla.delete(0,END)

def pulsar(valor):
	global operacion
	global resultado
	operacion = operacion + str(valor)
	pantalla.delete(0,END)
	pantalla.insert(0,operacion)

def calcular():
	global operacion
	global resultado
	try:
		resultado = str(eval(operacion))
	except:
		resultado = "Error"
	finally:
		pantalla.delete(0,END)
		pantalla.insert(0,resultado)
		operacion = resultado

def resultado():
	global operacion
	global resultado
	pantalla.delete(0,END)
	pantalla.insert(0,operacion)

#INTERFAZ CALCULADORA

#campo de texto
pantalla = Entry(ventana,font={'arial',20,'bold'},borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3,pady=10,padx=5)

#Boton reiniciar operación
boton_reset = Button(ventana,text='AC',width=5,height=2,command=lambda:borrar())
boton_reset.grid(row=0,column=3,pady=10,padx=5)

ancho = 5
alto = 3

#BOTON primera fila
boton_uno = Button(ventana,text='1',width=ancho,height=alto,command=lambda:pulsar(1))
boton_uno.grid(row=1,column=0,pady=5,padx=5)

boton_dos = Button(ventana,text='2',width=ancho,height=alto,command=lambda:pulsar(2))
boton_dos.grid(row=1,column=1,pady=5,padx=5)

boton_tres = Button(ventana,text='3',width=ancho,height=alto,command=lambda:pulsar(3))
boton_tres.grid(row=1,column=2,pady=5,padx=5)

boton_suma = Button(ventana,text='+',width=ancho,height=alto,command=lambda:pulsar('+'))
boton_suma.grid(row=1,column=3,pady=5,padx=5)

#BOTON segunda fila
boton_cuatro = Button(ventana,text='4',width=ancho,height=alto,command=lambda:pulsar(4))
boton_cuatro.grid(row=2,column=0,pady=5,padx=5)

boton_cinco = Button(ventana,text='5',width=ancho,height=alto,command=lambda:pulsar(5))
boton_cinco.grid(row=2,column=1,pady=5,padx=5)

boton_seis = Button(ventana,text='6',width=ancho,height=alto,command=lambda:pulsar(6))
boton_seis.grid(row=2,column=2,pady=5,padx=5)

boton_resta = Button(ventana,text='-',width=ancho,height=alto,command=lambda:pulsar('-'))
boton_resta.grid(row=2,column=3,pady=5,padx=5)

#BOTON tercera fila
boton_siete = Button(ventana,text='7',width=ancho,height=alto,command=lambda:pulsar(7))
boton_siete.grid(row=3,column=0,pady=5,padx=5)

boton_ocho = Button(ventana,text='8',width=ancho,height=alto,command=lambda:pulsar(8))
boton_ocho.grid(row=3,column=1,pady=5,padx=5)

boton_nueve = Button(ventana,text='9',width=ancho,height=alto,command=lambda:pulsar(9))
boton_nueve.grid(row=3,column=2,pady=5,padx=5)

boton_multip = Button(ventana,text='*',width=ancho,height=alto,command=lambda:pulsar('*'))
boton_multip.grid(row=3,column=3,pady=5,padx=5)

#BOTON cuarta fila
boton_punto = Button(ventana,text='.',width=ancho,height=alto,command=lambda:pulsar('.'))
boton_punto.grid(row=4,column=0,pady=5,padx=5)

boton_cero = Button(ventana,text='0',width=ancho,height=alto,command=lambda:pulsar(0))
boton_cero.grid(row=4,column=1,pady=5,padx=5)

boton_divide = Button(ventana,text='/',width=ancho,height=alto,command=lambda:pulsar('/'))
boton_divide.grid(row=4,column=2,pady=5,padx=5)

boton_calcula = Button(ventana,text='=',width=ancho,height=alto,command=lambda:calcular())
boton_calcula.grid(row=4,column=3,pady=5,padx=5)


ventana.mainloop()
