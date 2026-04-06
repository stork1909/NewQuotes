import tkinter as tk

root = tk.Tk()              # создание окна
root.title("Моё приложение")
root.geometry("400x300")   # размер окна

label = tk.Label(root, text="Привет!")
label.pack()

root.mainloop()            # запуск программы