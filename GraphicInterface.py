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



title = Label(window, text="Calculadora de corriente", bg="#595358", fg="white")
title.config(font=("Arial", 20))
title.grid(column = 0, row = 0, columnspan = 5, sticky = "we")
#title.pack(fill=X)



voltage = Entry(window, font="Arial 20")
voltage.grid(row = 1, column = 2 )
#voltage.pack()
vtitle = Label(window, text="Voltaje", bg="#3891A6", fg="BLACK")
vtitle.config(font=("Arial", 20))
vtitle.grid(row = 1, column = 1)




resistance = Entry(window, font="Arial 20")
resistance.grid(row = 2, column = 2 )
#resistance.pack()
rtitle = Label(window, text="Resistencia", bg="#3891A6", fg="BLACK")
rtitle.config(font=("Arial", 20))
rtitle.grid(row = 2, column = 1)



power = Entry(window, font="Arial 20")
power.grid(row = 3, column = 2 )
#power.pack()
ptitle = Label(window, text="Poder", bg="#3891A6", fg="BLACK")
ptitle.config(font=("Arial", 20))
ptitle.grid(row = 3, column = 1)



error = Entry(window, font="Arial 20")
error.grid(row = 4, column = 2 )
#error.pack()
etitle = Label(window, text="Error", bg="#3891A6", fg="BLACK")
etitle.config(font=("Arial", 20))
etitle.grid(row = 4, column = 1)



result = Label(window)
result.grid(row = 6, column = 2 )
#result.pack()
rstitle = Label(window, text="Resultado", bg="#3891A6", fg="BLACK")
rstitle.config(font=("Arial", 20))
rstitle.grid(row = 6, column = 1)


photo= PhotoImage (file = r"C:\Users\crade\Dropbox\Ingenieria Mecatronica\Cuarto Año     - 2021\Primer Semestre\Digital 2\Labs\Github\Metodos\Microproject1NM\circuit.png")
imagen= Button(window, image=photo, padx = 50, pady =50)
imagen.grid(row =8, column = 2)

clear_button = Button(window, text="Reiniciar", padx=20, pady=10, command=clear, bg="#99c24d")
clear_button.config(font=("Arial", 15))
clear_button.grid(row = 11, column = 2 )
#clear_button.pack(side="bottom")




calculate_button = Button(window, text="Calcular", padx=20, pady=10, command=calculate, bg="#99c24d")
calculate_button.config(font=("Arial", 15))
calculate_button.grid(row = 12, column = 2 )
#calculate_button.pack(side="bottom")


window.geometry("745x600")
window.config(bg="#B2CEDE")
window.mainloop()




