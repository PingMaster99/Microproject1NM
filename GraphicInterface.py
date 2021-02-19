from tkinter import *
import CalculationMethods as Cm


def calculate():
    try:
        v = float(voltage.get())
        r = float(resistance.get())
        p = float(power.get())
        e = float(error.get())
        current = Cm.calculate_circuit(v, r, p, e)
        if current is not None:
            current = round(float(current), 4)
        else:
            current = "El circuito no es posible"
        result["text"] = current


    except ValueError:
        print("Entrada no correcta")





def clear():
    print("Clear")

window = Tk()
title = Label(window, text="Calculadora de corriente", bg="darkgreen", fg="white")
title.config(font=("Arial", 20))
title.pack(fill=X)

voltage = Entry(window, font="Arial 20")
voltage.pack()

resistance = Entry(window, font="Arial 20")
resistance.pack()

power = Entry(window, font="Arial 20")
power.pack()

error = Entry(window, font="Arial 20")
error.pack()

result = Label(window)
result.pack()

clear_button = Button(window, text="Reiniciar", padx=20, pady=10, command=clear)
clear_button.pack(side="bottom")

calculate_button = Button(window, text="Calcular", padx=20, pady=10, command=calculate)
calculate_button.pack(side="bottom")




window.geometry("700x700")
window.config(bg="black")
window.mainloop()


