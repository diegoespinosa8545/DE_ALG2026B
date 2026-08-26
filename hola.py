import tkinter as tk                    # Importación de la librería

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Diego"
    lbl.config(text=f"Hola, {nombre}")

root = tk.Tk()                          # Creamos un objeto Tk()
root.title("Saludador de Compas")       # Título de la ventana
root.geometry("360x220")                # Tamaño de la ventana

# Crear etiqueta
lbl = tk.Label(root, text="Hola, escribe tu nombre y presiona el botón")
lbl.pack(pady = 10)

# Entrada de texto
entrada = tk.Entry(root)
entrada.pack(pady = 5)

# Creación de botón
btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady = 10)

root.mainloop()                         # Ejecutar la ventana en un loop constante