# encoding: utf-8
"""
    GraphicInterface.py

    Displays the circuit calculator graphically

    Dario Marroquin 18269 (dariomarroquin)
    Pablo Ruiz 18259 (PingMaster99)

    Version 1.0
    Updated February 19, 2020
"""
from tkinter import *
import CalculationMethods as Cm
import matplotlib.pyplot as plt
import numpy as np

# Constants
TITLE_SIZE = 15


def calculate():
    """
    Calculates the current based on the user's inputs
    """
    try:
        # Parsing inputs
        v = float(voltage.get())
        r = float(resistance.get())
        p = float(power.get())
        e = float(error.get())
        i = float(initial_point.get())

        # Current calculation
        current = Cm.calculate_circuit(v, r, p, e, i)

        if current is not None:
            current = round(float(current), 7)
            result["text"] = str(current) + " A"

        else:
            # Calculation resulted in a null solution
            current = "Revise estimación y gráfica"
            result["text"] = current

            # We plot the graph to make a new estimate or discard the circuit
            plt.clf()
            plt.close()
            fig, ax = plt.subplots(num="Resultado")
            x = np.linspace(-1, 20, 1000)
            ax.plot(x, r * x ** 2 - v * x + p)
            ax.axhline(y=0, color='k')
            ax.axvline(x=0, color='k')
            plt.show()

    except ValueError:
        result["text"] = "Entrada no correcta"


def clear():
    """
    Clears the input fields.
    Note that the initial estimation is preloaded with '1'
    """
    initial_point.delete(0, END)
    initial_point.insert(0, "1")
    voltage.delete(0, END)
    resistance.delete(0, END)
    power.delete(0, END)
    error.delete(0, END)
    result["text"] = ""


"""
    GUI window with grid layout
"""
window = Tk()
window.columnconfigure(0, minsize=100)
window.columnconfigure(1, minsize=100)
window.columnconfigure(2, minsize=100)
window.columnconfigure(3, minsize=100)
window.columnconfigure(4, minsize=50)

window.rowconfigure(0, minsize=30)
window.rowconfigure(1, minsize=30)
window.rowconfigure(2, minsize=30)
window.rowconfigure(3, minsize=30)
window.rowconfigure(4, minsize=30)
window.rowconfigure(5, minsize=30)
window.rowconfigure(6, minsize=30)
window.rowconfigure(7, minsize=30)


"""
    Titles and input fields
"""
title = Label(window, text="Calculadora de corriente", bg="#595358", fg="white")
title.config(font=("Arial", 20))
title.grid(column=0, row=0, columnspan=5, sticky="we")

voltage = Entry(window, font="Arial 20")
voltage.grid(row=1, column=2, pady=(20, 0))
v_title = Label(window, text="Voltaje (V)", bg="#3891A6", fg="BLACK")
v_title.config(font=("Arial", TITLE_SIZE))
v_title.grid(row=1, column=1, pady=(20, 0))

resistance = Entry(window, font="Arial 20")
resistance.grid(row=2, column=2)
r_title = Label(window, text="Resistencia (Ohms)", bg="#3891A6", fg="BLACK")
r_title.config(font=("Arial", TITLE_SIZE))
r_title.grid(row=2, column=1, padx=(0, 5))

power = Entry(window, font="Arial 20")
power.grid(row=3, column=2)
p_title = Label(window, text="Potencia (W)", bg="#3891A6", fg="BLACK")
p_title.config(font=("Arial", TITLE_SIZE))
p_title.grid(row=3, column=1)

error = Entry(window, font="Arial 20")
error.grid(row=4, column=2)
e_title = Label(window, text="Error esperado (%)", bg="#3891A6", fg="BLACK")
e_title.config(font=("Arial", TITLE_SIZE))
e_title.grid(row=4, column=1)

initial_point = Entry(window, font="Arial 20")
initial_point.grid(row=5, column=2)
i_title = Label(window, text="Punto inicial", bg="#3891A6", fg="BLACK")
i_title.config(font=("Arial", TITLE_SIZE))
i_title.grid(row=5, column=1)
initial_point.insert(0, "1")

result = Label(window)
result.grid(row=6, column=2)
rs_title = Label(window, text="Resultado", bg="#3891A6", fg="BLACK")
rs_title.config(font=("Arial", TITLE_SIZE))
rs_title.grid(row=6, column=1)

"""
    Circuit picture
"""
photo = PhotoImage(file=r"./circuit.png")
image = Button(window, image=photo, padx=0, pady=0)
image.grid(row=8, column=1, pady=(0, 20))

"""
    Buttons
"""
calculate_button = Button(window, text="Calcular", padx=20, pady=10, command=calculate, bg="#99c24d")
calculate_button.config(font=("Arial", 15))
calculate_button.grid(row=8, column=2, pady=(20, 150))

clear_button = Button(window, text="Reiniciar", padx=20, pady=10, command=clear, bg="#99c24d")
clear_button.config(font=("Arial", 15))
clear_button.grid(row=8, column=2, pady=(75, 0))

"""
    Window display
"""
window.geometry("700x520")
window.config(bg="#B2CEDE")
window.mainloop()
