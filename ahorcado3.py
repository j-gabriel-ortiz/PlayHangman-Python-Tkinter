import random 
import tkinter as tk 
from tkinter import messagebox 

palabras = ["perro", "gato", "raton", "elefante", "jirafa", "leon"]
intentos = 7
letras_adivinadas = []
partidas_ganadas = 0
partidas_perdidas = 0
partidas_totales = 0

def jugar():

    global intentos, letras_adivinadas, partidas_totales, partidas_ganadas, partidas_perdidas

    palabra = random.choice(palabras)
    letras_adivinadas = []

    ventana_juego = tk.Toplevel(root) 
    ventana_juego.title("Juego del Ahorcado") 
    ventana_juego.geometry("300x250") 
    ventana_juego.config(bg="#F2DC9B")

    etiqueta_titulo= tk.Label(ventana_juego, bg="#D99036",fg="#260B1D",
                               font=("Calibri", 18, "bold"), text="Adivina el Animal")
    etiqueta_titulo.pack(ipadx=60)

    etiqueta_intentos= tk.Label(ventana_juego, bg="#F2DC9B",fg="#260B1D",
                                 font=("Calibri", 12), text="Tienes 7 intentos para adivinar\n el animal oculto")
    etiqueta_intentos.pack(pady=5)

    etiqueta_palabra = tk.Label(ventana_juego, bg="#F2DC9B",fg="#260B1D",
                                 font=("Calibri", 15, "bold"), text="Palabra: {}".format("".join([c if c in letras_adivinadas else "_" for c in palabra])))
    etiqueta_palabra.pack(pady=5)

    entry_letra = tk.Entry(ventana_juego)
    entry_letra.pack() 


    boton_adivinar = tk.Button(ventana_juego, text="Adivinar",bg="#A66060", fg="#260B1D", 
                     borderwidth=5, width=15, font=("Calibri",12,"bold"), command=lambda: verificar_letra(palabra, entry_letra.get()))
    boton_adivinar.pack(pady=30)

    def verificar_letra(palabra, letra):
        global intentos, letras_adivinadas, partidas_totales, partidas_ganadas, partidas_perdidas

        entry_letra.delete(0, tk.END)

        if letra in letras_adivinadas:
            messagebox.showinfo("Error", "Ya has adivinado esa letra. Intenta con otra.")
            return
        
        if letra in palabra:
            letras_adivinadas.append(letra)
            if len(letras_adivinadas) == len(set(palabra)):
                messagebox.showinfo("Resultado", "¡Ganaste! La palabra era: {}".format(palabra))
                partidas_ganadas += 1
                partidas_totales += 1
                ventana_juego.destroy()
                return
        else:
            intentos -= 1
            if intentos == 0:
                messagebox.showinfo("Resultado", "¡Perdiste! La palabra era: {}".format(palabra))
                partidas_perdidas += 1
                partidas_totales += 1
                ventana_juego.destroy()
            else:
                messagebox.showinfo("Error", "Letra incorrecta. Te quedan {} intentos.".format(intentos))
        
        etiqueta_palabra.config(text="Palabra: {}".format("".join([c if c in letras_adivinadas else "_" for c in palabra])))

def reiniciar_resultados():
    global partidas_ganadas, partidas_perdidas, partidas_totales
    partidas_ganadas = 0
    partidas_perdidas = 0
    partidas_totales = 0
    

def ver_resultados():
    ventana_resultados = tk.Toplevel(root)
    ventana_resultados.title("Resultados")
    ventana_resultados.geometry("250x250")
    ventana_resultados.config(background="#F2DC9B")

    etiqueta_resultados = tk.Label(ventana_resultados, text="Resultados Generales",bg="#D99036",fg="#260B1D", font=("Calibri",18,"bold"), pady=10)
    etiqueta_resultados.pack(ipadx=60)

    etiqueta_resultados = tk.Label(ventana_resultados, bg="#F2DC9B",fg="#260B1D", font=("Calibri",12,"bold"), text="Partidas ganadas: {}\nPartidas perdidas: {}\nPartidas totales: {}".format(partidas_ganadas, partidas_perdidas, partidas_totales))
    etiqueta_resultados.pack(pady=20)

    boton_reiniciar = tk.Button(ventana_resultados, text="Reiniciar",bg="#A66060", fg="#260B1D", 
                     borderwidth=5, width=15, font=("Calibri",12,"bold"), command=reiniciar_resultados)
    boton_reiniciar.pack(pady=25)


root = tk.Tk()
root.title("Ahorcado")
root.geometry("400x350")
root.config(background="#F2DC9B")

tk.Label(root, text="Bienvenidos al Juego del Ahorcado",
      bg="#D99036",fg="#260B1D", font=("Calibri",20,"bold"), pady=10).pack(ipadx=60)

jugar_button = tk.Button(root, text="Jugar",bg="#A66060", fg="#260B1D",
                     borderwidth=5, font=("Calibri",15,"bold"), width=20, command=jugar)
jugar_button.pack(pady=50)

ver_resultados_button = tk.Button(root, text="Ver resultados", bg="#A66060", fg="#260B1D",
                     borderwidth=5, width=20, font=("Calibri",15,"bold"), command=ver_resultados)
ver_resultados_button.pack(pady=20)

root.mainloop()