import os
import django
from tkinter import Tk, Listbox, Button

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from Libros.models import Libro

def cargar_libros():
    libros = Libro.objects.all()
    lista.delete(0, 'end')
    for libro in libros:
        lista.insert('end', f"{libro.titulo} - {libro.autor}")

# Crear la interfaz de Tkinter
ventana = Tk()
ventana.title("Sistema de Biblioteca")

lista = Listbox(ventana, width=50, height=15)
lista.pack()

btn_cargar = Button(ventana, text="Cargar Libros", command=cargar_libros)
btn_cargar.pack()
def cargar_libros():
    try:
        libros = Libro.objects.all()  # Obtén todos los libros de la base de datos
        lista.delete(0, 'end')  # Limpia la lista
        for libro in libros:
            lista.insert('end', f"{libro.titulo} - {libro.autor}")  # Muestra cada libro
        print("Conexión exitosa: datos cargados correctamente.")
    except Exception as e:
        print(f"Error de conexión: {e}")

ventana.mainloop()