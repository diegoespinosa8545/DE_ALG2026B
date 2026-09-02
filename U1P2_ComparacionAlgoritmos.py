import matplotlib.pyplot as plt
import tkinter as tk
import random
import time

# ===   ALGORITMOS DE ORDENAMIENTO     ===

# Algoritmo de ordenamiento 1:  Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Algoritmo de ordenamiento 2:  Bubble Sort
def bubble_sort_brute_force(arr):
    n = len(arr)
    # Ciclo externo corre n veces de forma fija
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ===   GENERACIÓN DE NUMEROS ALEATORIOS Y GRÁFICA     ===

def ejecucion_programa():
    inicio = int(entryInicio.get())
    fin = int(entryFin.get())
    incremento = int(entryIncremento.get())

    tiemposBubble = []
    tiemposSelection = []

    # Generación de números aleatorios en arreglos
    arrayTamanhos = range(inicio, fin + 1, incremento)
    for n in arrayTamanhos:
        array = [random.randint(0, 1000) for _ in range(n)]

        inicioBubble = time.perf_counter()
        bubble_sort_brute_force(array)
        finBubble = time.perf_counter()

        tiempoBubble = finBubble - inicioBubble
        tiemposBubble.append(tiempoBubble)

        inicioSelection = time.perf_counter()
        selection_sort(array)
        finSelection = time.perf_counter()

        tiempoSelection = finSelection - inicioSelection
        tiemposSelection.append(tiempoSelection)

    # Gráfica
    plt.cla()
    plt.plot(list(arrayTamanhos), tiemposBubble, marker="o", label="Bubble Sort")
    plt.plot(list(arrayTamanhos), tiemposSelection, marker="o", label="Selection Sort")
    plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid()
    plt.show()


# ===   VENTANA GUI     ===
#   Ventana, título y tamaño
root = tk.Tk()
root.title("Comparación de Algoritmos: Bubble y Selection")
root.geometry("480x272")

#   Apariencia
root.configure(bg="#121314")

#   Etiquetas y entradas de texto
lblInicio = tk.Label(root, text = "Inicio", fg="#FFFFFF", bg="#121314", font=("Arial", 12))
lblInicio.pack(pady = 10)
entryInicio = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 12))
entryInicio.pack(pady = 5)

lblIncremento = tk.Label(root, text = "Incremento", fg="#FFFFFF", bg="#121314", font=("Arial", 12))
lblIncremento.pack(pady = 10)
entryIncremento = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 12))
entryIncremento.pack(pady = 5)

lblFin = tk.Label(root, text = "Fin", fg="#FFFFFF", bg="#121314", font=("Arial", 12))
lblFin.pack(pady = 10)
entryFin = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 12))
entryFin.pack(pady = 5)

#   Botón
btn = tk.Button(root, text = "Ejecutar programa", command=ejecucion_programa, fg="#FFFFFF", bg="#007ACC", activeforeground="#FFFFFF", activebackground="#005999", relief="flat", bd=0, cursor="hand2", width=15, height=2)
btn.pack(pady = 10)

#   Loop constante
root.mainloop()