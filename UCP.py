#UNIT Conversion Program. Beta 5.0
#Librerias
import tkinter as tk
from tkinter import *
#><
# WN rceacion inicial
principal_WN = tk.Tk() #wn creation
principal_WN.title("UCP Beta 5.0")
principal_WN.geometry("1050x770") # x,y
principal_WN.configure(bg="lightgray")

# variables globales
sistema_entrada = None
sistema_salida = None

# Funcion de conversion 1
def convertir():
    if not sistema_entrada or not sistema_salida:
        resultado_label.config(text="Porfavor, selecciona un sistema :3.")
        return
    
    numero = entry_valor.get()
    try:
        bases = {"Binario": 2, "Octal": 8, "Hexadecimal": 16, "Decimal": 10}
        
        if sistema_entrada == "Decimal":
            decimal = int(numero)
        else:
            decimal = base_a_decimal(numero, bases[sistema_entrada])
        
        if sistema_salida == "Decimal":
            resultado = str(decimal)
        else:
            resultado = decimal_a_base(decimal, bases[sistema_salida])
        
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Entrada no válida para el sistema seleccionado.")
        
#Funcion Decimal-Base  
def decimal_a_base(decimal, base):
    if decimal == 0:
        return "0"
    
    num = decimal
    resultado = ""
    digitos = "0123456789ABCDEF"
    pasos = []
    while num > 0:
        cociente = num // base
        residuo = num % base
        pasos.append(f"{num} ÷ {base} = {cociente}, residuo = {residuo} ({digitos[residuo]})")
        resultado = digitos[residuo] + resultado
        num = cociente
    
    #impresion de la operacion en consola
    print("Operaciones:")
    for paso in pasos:
        print(paso)
    print(f"Total de la operacion: {resultado}")
    return resultado

#Funcion Base-decimal
def base_a_decimal(numero, base):
    digitos = "0123456789ABCDEF"
    decimal = 0
    potencia = 0
    pasos = []
    
    for digito in reversed(numero.upper()):
        valor = digitos.index(digito)
        if valor >= base:
            raise ValueError(f"Digito{digito} invalido para esta base{base}")
        decimal += valor * (base ** potencia)
        potencia += 1
    
        termino = valor * (base ** potencia)
        pasos.append(f"{digito} × {base}^{potencia} = {valor} × {base ** potencia} = {termino}")
        decimal += termino
        potencia += 1
    
    #Impresion de la operacion en consola
    print("Operaciones:")
    for paso in pasos:
        print(paso)
    print(f"Total de la operacion = {decimal}")
    return decimal

#Funcion de entrada y salida (Valor actualizable)
def mostrar_entrada(sistema):
    global sistema_entrada  
    sistema_entrada = sistema 
    label_ingreso.config(text=f"Ingrese un número en {sistema}:")
    entry_valor.pack(side ="top", anchor = "w", padx = 10)
    btn_convertir.pack(pady=10)
    
def seleccionar_salida(sistema):
    global sistema_salida 
    sistema_salida = sistema
    
#Menu de opciones
#Configuracion del Titulo principal
tittle_n1 = tk.Label(principal_WN, text = "UNIT CONVERSION PROGRAM", font = ("Arial", 15, "bold"))
tittle_n1.pack(side = "top", anchor = "w", pady = 6)
tittle_n2 = tk.Label(principal_WN, text = "Calculadora de sistemas numericos ;)", font = ("Arial", 15, "bold"))
tittle_n2.pack(side = "top", anchor = "w", pady = 10)
textone = tk.Label(principal_WN, text = "Selecciona un sistema numerico para empezar",  font = ("Arial", 15, "bold"), bg="Gray")
textone.pack(side = "top", anchor = "w", pady = 10, padx = 10)

#funcion para el cambio de color de los botones (Boton precionado = SN a usar) V.A
def cambiar_color_botonA(Press_buttonA):
    for button in botones_s1:
        button.config(bg="white")
    Press_buttonA.config(bg="green")
    
#frame de los botones v.A
frame_buttonA = tk.Frame(principal_WN, bg="lightgray",)
frame_buttonA.pack()
texttwo = tk.Label(principal_WN, text = "Selecciona un sistema para convertir", font = ("Arial", 15, "bold"),  bg="gray")
texttwo.pack(side = "top", anchor = "w", pady = 5, padx = 5)

#Botones s1
botones_s1 = []
button1 = Button(frame_buttonA, text="Hexadecimal",bg="white", width=15, command=lambda: [mostrar_entrada("Hexadecimal"),cambiar_color_botonA(button1)])
button1.pack(side="top", anchor = "nw", padx = 10)
botones_s1.append(button1)
button2 = Button(frame_buttonA, text="Binary",bg="white", width=12, command=lambda: [mostrar_entrada("Binario"),cambiar_color_botonA(button2)])
button2.pack(side="top", anchor = "nw", padx = 10)
botones_s1.append(button2)
button3 = Button(frame_buttonA, text="Octal",bg="white", width=12, command=lambda: [mostrar_entrada("Octal"), cambiar_color_botonA(button3)])
button3.pack(side="top", anchor = "nw", padx = 10)
botones_s1.append(button3)
button4 = Button(frame_buttonA, text="Decimal",bg="white", width=12, command=lambda: [mostrar_entrada("Decimal"), cambiar_color_botonA(button4)])
button4.pack(side="top", anchor = "nw", padx = 10)
botones_s1.append(button4)

#funcion para el cambio de color de los botones (Boton precionado = SN a usar) V.B
def cambiar_color_botonB(Press_buttonB):
    for button in botones_s2:
        button.config(bg="white")
    Press_buttonB.config(bg="green")
    
#frame de los botones v.B
frame_buttonB = tk.Frame(principal_WN, bg="lightgray",)
frame_buttonB.pack()  
  
#Botones s2
botones_s2 = []  
button5 = Button(frame_buttonB, text="Hexadecimal",bg="white", width=15, command=lambda: [seleccionar_salida("Hexadecimal"), cambiar_color_botonB(button5)])
button5.pack(side="top", anchor = "nw", padx = 10)
botones_s2.append(button5)
button6 = Button(frame_buttonB, text="Binary",bg="white", width=12, command=lambda: [seleccionar_salida("Binario"),cambiar_color_botonB(button6)])
button6.pack(side="top", anchor = "nw", padx = 10)
botones_s2.append(button6)
button7 = Button(frame_buttonB, text="Octal",bg="white", width=12, command=lambda: [seleccionar_salida("Octal"),cambiar_color_botonB(button7)])
button7.pack(side="top", anchor = "nw", padx = 10)
botones_s2.append(button7)
button8 = Button(frame_buttonB, text="Decimal",bg="white", width=12, command=lambda: [seleccionar_salida("Decimal"),cambiar_color_botonB(button8)])
button8.pack(side="top", anchor = "nw", padx = 10)
botones_s2.append(button8)

#Etiqueta y boton de conversion
label_ingreso = tk.Label(principal_WN, text="", font=("Arial", 12))
label_ingreso.pack(side ="top", anchor = "w", pady = 30, padx = 10)

entry_valor = tk.Entry(principal_WN, font=("Arial", 14), width=10)

btn_convertir = Button(principal_WN, text="Convertir", font=("Arial", 12), command=convertir)
btn_convertir.pack(pady=20)
resultado_label = Label(principal_WN, text="", font=("Arial", 12, "bold"), fg="blue")
resultado_label.pack(pady=10)


#Mantener ventana abierta 
principal_WN.mainloop()