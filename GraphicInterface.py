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
        result["text"] = "Entrada no correcta"


def clear():
    voltage.delete(0, END)
    resistance.delete(0, END)
    power.delete(0, END)
    error.delete(0, END)
    result["text"] = ""


window = Tk()
window.columnconfigure(0, minsize=100)
window.columnconfigure(1, minsize=100)
window.columnconfigure(2, minsize=100)
window.columnconfigure(3, minsize=100)
window.columnconfigure(4, minsize=100)

window.rowconfigure(0, minsize=30)
window.rowconfigure(1, minsize=30)
window.rowconfigure(2, minsize=30)
window.rowconfigure(3, minsize=30)
window.rowconfigure(4, minsize=30)
window.rowconfigure(5, minsize=30)
window.rowconfigure(6, minsize=30)
window.rowconfigure(7, minsize=30)

title = Label(window, text="Calculadora de corriente", bg="#595358", fg="white")
title.config(font=("Arial", 20))
title.grid(column=0, row=0, columnspan=5, sticky="we")

voltage = Entry(window, font="Arial 20")
voltage.grid(row=1, column=2)
v_title = Label(window, text="Voltaje", bg="#3891A6", fg="BLACK")
v_title.config(font=("Arial", 20))
v_title.grid(row=1, column=1)

resistance = Entry(window, font="Arial 20")
resistance.grid(row=2, column=2)
r_title = Label(window, text="Resistencia", bg="#3891A6", fg="BLACK")
r_title.config(font=("Arial", 20))
r_title.grid(row=2, column=1)

power = Entry(window, font="Arial 20")
power.grid(row=3, column=2)
p_title = Label(window, text="Poder", bg="#3891A6", fg="BLACK")
p_title.config(font=("Arial", 20))
p_title.grid(row=3, column=1)

error = Entry(window, font="Arial 20")
error.grid(row=4, column=2)
e_title = Label(window, text="Error", bg="#3891A6", fg="BLACK")
e_title.config(font=("Arial", 20))
e_title.grid(row=4, column=1)

result = Label(window)
result.grid(row=6, column=2)
rstitle = Label(window, text="Resultado", bg="#3891A6", fg="BLACK")
rstitle.config(font=("Arial", 20))
rstitle.grid(row=6, column=1)

# Change file location of image
photo = PhotoImage(
    file=r"./circuit.png")
imagen = Button(window, image=photo, padx=50, pady=50)
imagen.grid(row=8, column=2)

clear_button = Button(window, text="Reiniciar", padx=20, pady=10, command=clear, bg="#99c24d")
clear_button.config(font=("Arial", 15))
clear_button.grid(row=11, column=2)


calculate_button = Button(window, text="Calcular", padx=20, pady=10, command=calculate, bg="#99c24d")
calculate_button.config(font=("Arial", 15))
calculate_button.grid(row=12, column=2)


window.geometry("745x600")
window.config(bg="#B2CEDE")
window.mainloop()
