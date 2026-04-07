import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Excel Form Interface")
        self.geometry("800x600")

        # Контейнер для страниц
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Регистрируем страницы
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


# -------------------------
# Главная страница
# -------------------------
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Выберите форму", font=("Arial", 16))
        label.pack(pady=20)

        btn1 = tk.Button(self, text="Производитель 1",
                         command=lambda: controller.show_frame(Page1))
        btn1.pack(pady=10)

        btn2 = tk.Button(self, text="Производитель 2",
                         command=lambda: controller.show_frame(Page2))
        btn2.pack(pady=10)


# -------------------------
# Страница 1 (пример формы)
# -------------------------
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Форма: Производитель 1", font=("Arial", 14)).pack(pady=10)

        # Поля ввода
        tk.Label(self, text="Цена:").pack()
        self.price = tk.Entry(self)
        self.price.pack()

        tk.Label(self, text="Количество:").pack()
        self.quantity = tk.Entry(self)
        self.quantity.pack()

        # Результат (расчет)
        tk.Label(self, text="Итого:").pack()
        self.total = tk.Label(self, text="0")
        self.total.pack()

        # Кнопка расчета
        tk.Button(self, text="Рассчитать",
                  command=self.calculate).pack(pady=10)

        # Навигация
        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame(StartPage)).pack()

    def calculate(self):
        try:
            price = float(self.price.get())
            quantity = float(self.quantity.get())
            total = price * quantity
            self.total.config(text=str(total))
        except:
            self.total.config(text="Ошибка")


# -------------------------
# Страница 2 (другая форма)
# -------------------------
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Форма: Производитель 2", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Вес:").pack()
        self.weight = tk.Entry(self)
        self.weight.pack()

        tk.Label(self, text="Цена за кг:").pack()
        self.price_per_kg = tk.Entry(self)
        self.price_per_kg.pack()

        tk.Label(self, text="Стоимость:").pack()
        self.result = tk.Label(self, text="0")
        self.result.pack()

        tk.Button(self, text="Рассчитать",
                  command=self.calculate).pack(pady=10)

        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame(StartPage)).pack()

    def calculate(self):
        try:
            w = float(self.weight.get())
            p = float(self.price_per_kg.get())
            self.result.config(text=str(w * p))
        except:
            self.result.config(text="Ошибка")


# -------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()