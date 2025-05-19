[9:02 AM, 5/14/2025] Gael: import tkinter as tk
def  e():
 nombre = etiqueta_nombre.get()
 num = etiqueta_num.get()
 calif = etiqueta_calif.get()
 sexo = etiqueta_sexo.get()
 etiqueta_resultado.config(ventana,text="los datos del estudiante son {estudiante}, {num}, {calif}, {sexo}")
ventana = tk.Tk ()
ventana.title("diccionario")
ventana.geometry("900x400")
etiqueta = tk.Label(ventana, text="introduszca el numero de estudiante")
etiqueta.pack()
etiqueta_nombre = tk.Label(ventana, text="introduzca el nombre")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.get()
etiqueta_num = tk.Label(ventana, text="introduzca el numero de estudiante")
etiqueta_num.pack()
entrada_num = tk.Entry(ventana)
entrada_num.get()
etiqueta_calif = tk.Label(ventana, text="introduzca la ca…
[8:50 AM, 5/19/2025] Gael: import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def interfaz_uno():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="recive un saludo", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("saludo", "hola")).pack()

def interfaz_dos():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="datos del alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="ingrese el nombre del alumno").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="selección su grupo:").pack()
    opcion_elegida = tk.StringVar(value="grupo 1")
    tk.Radiobutton(area_dinamica, text="grupo 1", variable=opcion_elegida, value="grupo 1").pack()
    tk.Radiobutton(area_dinamica, text="grupo 2", variable=opcion_elegida, value="grupo 2").pack()

    tk.Label(area_dinamica, text="Numero de lista:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    def accion_guardar():
        valor = campo_texto_uno.get()
        messagebox.showinfo("Revisión", f"nombre: {valor}\ngrupo: {opcion_elegida.get()}\nNumero de Lista: {combo.get()}")

    tk.Button(area_dinamica, text="guardar datos", command=accion_guardar).pack(pady=10)

def interfaz_tres():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "red", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def interfaz_cuatro():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="inicio", command=interfaz_uno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos del alumno", command=interfaz_dos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="cambio de fondo", command=interfaz_tres, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Preguntas", command=interfaz_cuatro, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

interfaz_uno()
ventana_principal.mainloop()