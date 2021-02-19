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



title = Label(window, text="Calculadora de corriente", bg="darkgreen", fg="white")
title.config(font=("Arial", 20))
title.grid(column = 0, row = 0, columnspan = 5, sticky = "we")
#title.pack(fill=X)



voltage = Entry(window, font="Arial 20")
voltage.grid(row = 1, column = 2 )
#voltage.pack()
vtitle = Label(window, text="Voltage", bg="turquoise", fg="Black")
vtitle.config(font=("Arial", 20))
vtitle.grid(row = 1, column = 1)




resistance = Entry(window, font="Arial 20")
resistance.grid(row = 2, column = 2 )
#resistance.pack()
rtitle = Label(window, text="Resistance", bg="turquoise", fg="Black")
rtitle.config(font=("Arial", 20))
rtitle.grid(row = 2, column = 1)



power = Entry(window, font="Arial 20")
power.grid(row = 3, column = 2 )
#power.pack()
ptitle = Label(window, text="Power", bg="turquoise", fg="Black")
ptitle.config(font=("Arial", 20))
ptitle.grid(row = 3, column = 1)



error = Entry(window, font="Arial 20")
error.grid(row = 4, column = 2 )
#error.pack()
etitle = Label(window, text="Error", bg="turquoise", fg="Black")
etitle.config(font=("Arial", 20))
etitle.grid(row = 4, column = 1)



result = Label(window)
result.grid(row = 6, column = 2 )
#result.pack()
rstitle = Label(window, text="Result", bg="turquoise", fg="Black")
rstitle.config(font=("Arial", 20))
rstitle.grid(row = 6, column = 1)



clear_button = Button(window, text="Reiniciar", padx=20, pady=10, command=clear)
clear_button.config(font=("Arial", 15))
clear_button.grid(row = 8, column = 2 )
#clear_button.pack(side="bottom")




calculate_button = Button(window, text="Calcular", padx=20, pady=10, command=calculate)
calculate_button.config(font=("Arial", 15))
calculate_button.grid(row = 9, column = 2 )
#calculate_button.pack(side="bottom")


window.geometry("745x400")
window.config(bg="BLUE")
window.mainloop()



##circuit = Tk()
#circuit.title("Circuito a Calcular")
#circuit.geometry("203x169")
#picture= PhotoImage(file="circuit.jpeg")
#background=Label(circuit,image=picture).place(x=0, y=0)
#circuit.mainloop()
