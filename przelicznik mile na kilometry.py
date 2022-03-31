import tkinter as tk
import tkinter.font as tk_font

km_miles_label: tk.Label # km and miles label
m_s_label: tk.Label  # meters per second
input_field: tk.Entry

miles_as_km = 1.60934
miles_as_ms = 0.44704

def km_click():
    text = input_field.get()
    kilometers = round(float(input_field.get()) * miles_as_km, 2) # miles to kilometers
    m_s = round(float(input_field.get()) * miles_as_km / 3.6, 2)  # kilometers to meters
    km_miles_label.configure(text=str(kilometers) + " Kilometry")
    m_s_label.configure(text=str(m_s) + " Metry na sekundę z km/h")


def miles_click():
    text = input_field.get()
    miles = round(float(input_field.get()) / miles_as_km, 2)  # kilometers to miles
    m_s_m = round((float(input_field.get()) / miles_as_km) * miles_as_ms, 2) # miles to meters ; m/s = mile * 0.44704
    km_miles_label.configure(text=str(miles) + " Mile")
    m_s_label.configure(text=str(m_s_m) + " Metry na sekundę z mil")

root = tk.Tk()
root.title("Przelicznik km na mile i odwrotnie") # title
# Ustawienie okienka
width = 400
height = 160
half_screen_width = root.winfo_screenwidth()//2 - width//2
half_screen_height = root.winfo_screenheight()//2 - height//2
root.geometry(f"{width}x{height}+{half_screen_width}+{half_screen_height}")  # miejsce lewego górnego rogu
root.resizable(width=False, height=False)
root["bg"] = "snow2"

km_miles_label = tk.Label(root)
km_miles_label["text"] = " Wartość na km / h: "
font = tk_font.Font(family='Bahnschrift', size=15, weight="normal")
km_miles_label["font"] = font
km_miles_label["anchor"] = "center"
km_miles_label["bg"] = "gray82"
km_miles_label.place(x=10, y=45)

m_s_label = tk.Label(root)
m_s_label["text"] = " Wartość na metry na sekundę: "
font = tk_font.Font(family='Bahnschrift', size=15, weight="normal")
m_s_label["font"] = font
m_s_label.place(x=10, y=98)
m_s_label["anchor"] = "center"
m_s_label["bg"] = "misty rose"

input_field = tk.Entry(root, justify="right")
input_field.place(x=10, y=10, width=165, height=25)

to_km_button = tk.Button()
to_km_button["text"] = "Zamień na km/h"
to_km_button.place(x=190, y=10)
to_km_button["command"] = km_click

to_miles_button = tk.Button(root)
to_miles_button["text"] = "Zamień na mile"
to_miles_button.place(x=295, y=10)
to_miles_button["command"] = miles_click

root.mainloop()

