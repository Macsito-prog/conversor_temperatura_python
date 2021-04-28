import tkinter as tk

def fahrenheit_to_celsius():
    '''
    Convierte el valor de fahrenheit a Celsius
    '''
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

frm_entry = tk.Frame(master = ventana)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row = 0, column = 0, sticky = "e")
lbl_temp.grid(row = 0, column = 1, sticky = "w")


btn_convert = tk.Button(
    master=ventana,
    text ="Convertir",
    command = fahrenheit_to_celsius 
)
lbl_result = tk.Label(master=ventana, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)



ventana.mainloop()