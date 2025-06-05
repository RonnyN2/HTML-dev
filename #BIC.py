#BIC
 
#La entrada debe captar 2 numeros enteros y pasarlos a binario y operar una resta sucesiva,
#la resta se tiene que hacer en binario mediante el complemente del numero digitado mostrando cada interaccion.
 
## Example   Entrada   9 div 2  Salida  9 - 2 = 7      1001 - 0010 = 0111                   /iteración 1
##                                                     7 - 2 = 5      0111 - 0010 = 0101    /iteración 2
##                                                     3 - 2 = 1      0011 - 0010 = 0001    /iteración 4
##                                                     Resultado  4 sobra 1.

#librerias
import tkinter as tk
from tkinter import *

# Función para convertir un número a binario 
def a_binario(num, longitud):
    return format(num, f'0{longitud}b')

# Función / realizar la resta  sucesiva
def resta_binaria(num1, num2):
    num1_bin = a_binario(num1, 4)
    num2_bin = a_binario(num2, 4)
    
    iteraciones = []
    while num1 >= num2:
        num1 -= num2
        num1_bin = a_binario(num1, 4)
        iteraciones.append(f"{num1 + num2} - {num2} = {num1}\t{a_binario(num1 + num2, 4)} - {a_binario(num2, 4)} = {num1_bin}")
    
    return iteraciones, num1

# Función para devolver el resultado a la etiqueta
def resultado():
    num1 = int(Entry1.get())
    num2 = int(Entry2.get())
    iteraciones, sobrante = resta_binaria(num1, num2)
    
    resultado_texto = "\n".join(iteraciones)
    resultado_texto += f"\nResultado: {num1 // num2} sobra {sobrante}."
    resultado_label.config(text=resultado_texto)

# Opciones de ventana
window = tk.Tk()
window.title("Binary-Decimal Calculator")
window.geometry("1050x770")
window.configure(bg="black")

#Diseño de interfaz
tittle_1 = tk.Label(window, text = "Binary-Decimal Calculator")
tittle_1.pack(side = "top", anchor = "w", pady = 6)
tittle_1.config(fg="green",bg="black",font=("Researcher Regular",24))
tittle_2 = tk.Label(window, text = "Digita dos valores en las entradas ")
tittle_2.pack(side = "top", anchor = "w", pady = 10)
tittle_2.config(fg="green",bg="black",font=("Researcher Regular",20))

#Etiquetas y botones

Entry1 = tk.Entry(window)
Entry1.pack(pady=10)
Entry1.config(fg="green",bg="black",font=("Researcher Regular",20))
Entry2 = tk.Entry(window)
Entry2.pack(pady=10)
Entry2.config(fg="green",bg="black",font=("Researcher Regular",20))

boton = tk.Button(window, text="Calcular", command = resultado)
boton.pack(pady=10)

#label del resultado
resultado_label = Label(window, text="", font=("Arial", 12, "bold"), fg="blue")
resultado_label.pack(pady=10)

window.mainloop()