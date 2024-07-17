# -*- coding: utf-8 -*-
"""
Created Tue Jul 9 16:00:14 2024

@author: Isabel_Fuentes
"""


import tkinter as tk
from tkinter import messagebox

def dms_to_dd():
    try:
        grados = int(entry_lat_grados.get())
        minutos = int(entry_lat_minutos.get())
        segundos = float(entry_lat_segundos.get())
        min1 = segundos / 60 * minutos
        grados1 = round((min1 / 60 + grados), 4)
        messagebox.showinfo("Resultado Latitud", f"Respuesta: {grados1}°")

        grados = int(entry_lon_grados.get())
        minutos = int(entry_lon_minutos.get())
        segundos = float(entry_lon_segundos.get())
        min1 = segundos / 60 * minutos
        grados1 = round((min1 / 60 + grados), 4)
        messagebox.showinfo("Resultado Longitud", f"Respuesta: {grados1}°")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def dd_to_dms():
    try:
        grados = float(entry_lat_dd.get())
        grados2 = grados * 60
        minutos = int(entry_lat_minutos_dd.get())
        min2 = minutos * 60
        messagebox.showinfo("Resultado Latitud", f"Respuesta: {grados}° {grados2} {min2}''")

        grados = float(entry_lon_dd.get())
        grados2 = grados * 60
        minutos = int(entry_lon_minutos_dd.get())
        min2 = minutos * 60
        messagebox.showinfo("Resultado Longitud", f"Respuesta: {grados}° {grados2} {min2}''")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversión de Coordenadas")
ventana.geometry("800x600")

ventana.configure(bg ='lightgreen')

# Sección de DMS a DD
tk.Label(ventana, text="Esta es una aplicación para conversión de coordenadas").pack()

tk.Label(ventana, text="Primero convertiremos de DMS a DD").pack()

tk.Label(ventana, text="Ingrese los datos de la Latitud").pack()
tk.Label(ventana, text="Grados:").pack()
entry_lat_grados = tk.Entry(ventana)
entry_lat_grados.pack()
tk.Label(ventana, text="Minutos:").pack()
entry_lat_minutos = tk.Entry(ventana)
entry_lat_minutos.pack()
tk.Label(ventana, text="Segundos:").pack()
entry_lat_segundos = tk.Entry(ventana)
entry_lat_segundos.pack()

tk.Label(ventana, text="Ingrese los datos de la Longitud").pack()
tk.Label(ventana, text="Grados:").pack()
entry_lon_grados = tk.Entry(ventana)
entry_lon_grados.pack()
tk.Label(ventana, text="Minutos:").pack()
entry_lon_minutos = tk.Entry(ventana)
entry_lon_minutos.pack()
tk.Label(ventana, text="Segundos:").pack()
entry_lon_segundos = tk.Entry(ventana)
entry_lon_segundos.pack()

tk.Button(ventana, text="Convertir DMS a DD", command=dms_to_dd).pack()

# Sección de DD a DMS
tk.Label(ventana, text="Ahora convertiremos de DD a DMS").pack()

tk.Label(ventana, text="Ingrese los datos de la Latitud").pack()
tk.Label(ventana, text="Grados con el punto decimal:").pack()
entry_lat_dd = tk.Entry(ventana)
entry_lat_dd.pack()
tk.Label(ventana, text="Minutos:").pack()
entry_lat_minutos_dd = tk.Entry(ventana)
entry_lat_minutos_dd.pack()

tk.Label(ventana, text="Ingrese los datos de la Longitud").pack()
tk.Label(ventana, text="Grados con el punto decimal:").pack()
entry_lon_dd = tk.Entry(ventana)
entry_lon_dd.pack()
tk.Label(ventana, text="Minutos:").pack()
entry_lon_minutos_dd = tk.Entry(ventana)
entry_lon_minutos_dd.pack()

tk.Button(ventana, text="Convertir DD a DMS", command=dd_to_dms).pack()

ventana.mainloop()
