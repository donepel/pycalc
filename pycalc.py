#*****************************
# Calculadora en python
# author: don_epel
#***************************
import tkinter as tk
from tkinter import ttk, messagebox
import math
from PIL import Image, ImageTk


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("pyCalc by Don_Epel")
        self.root.geometry("400x700")
        self.root.resizable(False, False)

        # Frame para cambiar entre modos
        self.frame_modos = tk.Frame(root)
        self.frame_modos.pack(pady=10)

        tk.Button(self.frame_modos, text="Básica", command=self.mostrar_basica).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_modos, text="Electrónica", command=self.mostrar_electronica).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_modos, text="Resistencias", command=self.mostrar_resistencias).pack(side=tk.LEFT, padx=5)

        # Frame donde se mostrarán las operaciones
        self.frame_operaciones = tk.Frame(root, relief="groove", bd=2, padx=10, pady=10)
        self.frame_operaciones.pack(pady=10, fill=tk.BOTH, expand=True)

        # Etiqueta para mostrar resultados
        self.label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 14))
        self.label_resultado.pack(pady=20)

        # Cargar vista inicial (básica)
        self.mostrar_basica()

    def limpiar_frame(self):
        for widget in self.frame_operaciones.winfo_children():
            widget.destroy()

    def mostrar_basica(self):
        self.limpiar_frame()
        resultado=0
        self.label_resultado.config(text=f"Resultado: {resultado}")

        titulo = tk.Label(self.frame_operaciones, text="Operaciones Básicas", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        # Entrada para los números
        self.entry_num1 = tk.Entry(self.frame_operaciones, font=("Arial", 12), justify="center")
        self.entry_num1.pack(pady=5)
        self.entry_num1.insert(0, "Número 1")

        self.entry_num2 = tk.Entry(self.frame_operaciones, font=("Arial", 12), justify="center")
        self.entry_num2.pack(pady=5)
        self.entry_num2.insert(0, "Número 2")

        # Botones para operaciones
        operaciones = [
            ("+", lambda: self.calcular('+')),
            ("-", lambda: self.calcular('-')),
            ("*", lambda: self.calcular('*')),
            ("/", lambda: self.calcular('/')),
            ("%", lambda: self.calcular('%')),
            ("^", lambda: self.calcular('^')),
        ]

        for op, command in operaciones:
            btn = tk.Button(self.frame_operaciones, text=op, width=5, font=("Arial", 12), command=command)
            btn.pack(side=tk.LEFT, padx=5, pady=5)

    def mostrar_electronica(self):
        self.limpiar_frame()
        resultado=0
        self.label_resultado.config(text=f"Resultado: {resultado}")
        titulo = tk.Label(self.frame_operaciones, text="Cálculos Electrónicos", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        opciones = [
            ("Potencia (P=V*I)", lambda: self.calcular_electronica("potencia")),
            ("Corriente (I=P/V)", lambda: self.calcular_electronica("corriente")),
            ("Voltaje (V=P/I)", lambda: self.calcular_electronica("voltaje")),
        ]

        for texto, comando in opciones:
            btn = tk.Button(self.frame_operaciones, text=texto, font=("Arial", 12), command=comando)
            btn.pack(pady=5)

        # Entradas
        self.entry_valor1 = tk.Entry(self.frame_operaciones, font=("Arial", 12), justify="center")
        self.entry_valor1.pack(pady=5)
        self.entry_valor1.insert(0, "Valor 1")

        self.entry_valor2 = tk.Entry(self.frame_operaciones, font=("Arial", 12), justify="center")
        self.entry_valor2.pack(pady=5)
        self.entry_valor2.insert(0, "Valor 2")

    def mostrar_resistencias(self):
        self.limpiar_frame()
        resultado=0
        self.label_resultado.config(text=f"Valor: {resultado}")

        titulo = tk.Label(self.frame_operaciones, text="Cálculo de Resistencias", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        # Imagen de resistencia
        try:
            imagen = Image.open("resistencia.png")
            self.imagen_resistencia = ImageTk.PhotoImage(imagen)
            tk.Label(self.frame_operaciones, image=self.imagen_resistencia).pack(pady=5)
        except Exception as e:
            tk.Label(self.frame_operaciones, text=f"Error al cargar la imagen: {e}").pack()

        # Combobox para colores
        colores = ["Negro", "Marrón", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]
        tolerancias = ["Dorado", "Plateado"]

        self.band1 = ttk.Combobox(self.frame_operaciones, values=colores, state="readonly")
        self.band1.set("Seleccione color banda 1")
        self.band1.pack(pady=5)

        self.band2 = ttk.Combobox(self.frame_operaciones, values=colores, state="readonly")
        self.band2.set("Seleccione color banda 2")
        self.band2.pack(pady=5)

        self.band3 = ttk.Combobox(self.frame_operaciones, values=colores, state="readonly")
        self.band3.set("Seleccione color banda 3")
        self.band3.pack(pady=5)

        self.band4 = ttk.Combobox(self.frame_operaciones, values=tolerancias, state="readonly")
        self.band4.set("Seleccione tolerancia")
        self.band4.pack(pady=5)

        # Botón calcular
        tk.Button(self.frame_operaciones, text="Calcular", command=self.calcular_resistencia).pack(pady=10)

    def calcular(self, operacion):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())

            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            elif operacion == '%':
                resultado = num1 % num2
            elif operacion == '^':
                resultado = num1 ** num2
            else:
                resultado = "Operación inválida"

            self.label_resultado.config(text=f"Resultado: {resultado}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def calcular_electronica(self, tipo):
        try:
            valor1 = float(self.entry_valor1.get())
            valor2 = float(self.entry_valor2.get())

            if tipo == "potencia":
                resultado = valor1 * valor2
            elif tipo == "corriente":
                if valor2 == 0:
                    raise ZeroDivisionError
                resultado = valor1 / valor2
            elif tipo == "voltaje":
                if valor2 == 0:
                    raise ZeroDivisionError
                resultado = valor1 / valor2
            else:
                resultado = "Operación inválida"

            self.label_resultado.config(text=f"Resultado: {resultado}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def calcular_resistencia(self):
        colores = {
            "Negro": 0, "Marrón": 1, "Rojo": 2, "Naranja": 3,
            "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7,
            "Gris": 8, "Blanco": 9
        }
        tolerancias = {"Dorado": 5, "Plateado": 10}

        try:
            b1 = colores[self.band1.get()]
            b2 = colores[self.band2.get()]
            b3 = colores[self.band3.get()]
            tol = tolerancias[self.band4.get()]

            valor = (b1 * 10 + b2) * (10 ** b3)
            self.label_resultado.config(text=f"Valor: {valor} Ω ±{tol}%")
        except KeyError:
            messagebox.showerror("Error", "Seleccione todos los colores.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
