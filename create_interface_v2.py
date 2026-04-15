import tkinter as tk
import pickle

"""ШАГ 1. Главный класс (контроллер)"""
class App(tk.Tk):
    # Вызываем конструктор класса и передаем ему наши данные о формах в виде списка
    def __init__(self, forms):
        # Вызываем конструктор родительского класса в данном случае Tk
        super().__init__()

        #Название и размер формы
        self.title("Формы")
        self.geometry("900x600")

        # Переписываем наш список форм в свойство класса
        self.forms = forms
        # Задаем начальный индекс
        self.current_index = 0

        # Создаем внутри нашего окна контейнер в виде Frame
        self.container = tk.Frame(self)
        # Растягиваем его на весь экран и делаем масштабируемым
        self.container.pack(fill='both', expand=True)

        # Создаем внутри нашего окна контейнер страницу нашей формы,
        # В качестве параметров передаем свой контейнер и себя как контроллер
        self.form_page = FormPage(self.container, self)
        # Растягиваем нашу страницу на весь экран и делаем масштабируемой
        self.form_page.pack(fill="both", expand=True)

        # Вызываем функцию, которая показывает следующую страницу
        self.show_next_form()

    def show_next_form(self):
        """Функция, которая показывает следующую страницу"""
        # Если наш индекс выходит за пределы длинны списка форма пишем сообщение
        # и завершаем функцию (возвращаем ничего)
        if self.current_index >= len(self.forms):
            print("Все формы обработаны")
            return

        # Если не сработал предыдущий блок кода, то берем данные формы
        # в списке форм и сохраняем их в переменную form_data
        form_data = self.forms[self.current_index]
        # Обращаемся к нашей странице для вызова функции загрузки формы,
        # передавая ей в качестве аргументу настройки формы
        self.form_page.load_form(form_data)

        self.current_index += 1

"""ШАГ 2. Скроллируемая форма"""
class FormPage(tk.Frame):
    # Вызываем конструктор нашего класса. В качестве параметров передаем ему
    # родителя (наш контейнер) и наш контроллер (класс Tk, главную программу)
    def __init__(self, parent, controller):
        # Вызываем конструктор родительского класса в данном случае контейнера,
        # который представлен объектом класса Frame
        super().__init__(parent)

        self.controller = controller

        # Canvas + Scrollbar
        # Canvas это холст, который будет размещаться на нашей страницы.
        # Для этого передаем ему в качестве аргумента объект нашей страницы.
        # На нем будем рисовать наши объекты (метки, поля ввода, кнопки)
        canvas = tk.Canvas(self)
        # Стандартная полоса прокрутки (расположение вертикальное, вызывает
        # функцию объекта canvas под именем yview )
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)

        # Создаем на нашем холсте, еще одну рамку формы
        self.scroll_frame = tk.Frame(canvas)

        # Функция bind объекта scroll_frame (класс Frame) записывает события типа
        # "<Configure>" и выполняет lambda функцию. Данная функция принимает событие
        # ('e') (в нашем случае видимо настройка окна scroll_frame) и меняет
        # позицию всех объектов которые попадают в рамки нашего холста.
        # Если вкратце: “каждый раз, когда меняется содержимое → пересчитать размер прокрутки”
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # “помести Frame внутрь Canvas в левый верхний угол,
        # чтобы его можно было прокручивать”
        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        # Сообщаем холсту, что он должен обновлять ползунок
        canvas.configure(yscrollcommand=scrollbar.set)

        #Размещаем холст и полосу прокрутки в контейнере
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    """ШАГ 3. Загрузка формы (динамика)"""
    # Функция получает список под названием form_data, который содержит словари полей
    def load_form(self, form_data):

        # очистка старой формы
        # Метод winfo_children() — это стандартный инструмент в Tkinter,
        # который позволяет «заглянуть внутрь» любого контейнера
        # (окна, фрейма или холста) и получить список всех элементов,
        # которые в нем находятся.
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # -------------------------
        # Заголовок
        # -------------------------
        tk.Label(
            self.scroll_frame,
            text=f"{form_data[0]} {form_data[1]} {form_data[2]}",
            font=("Arial", 16)
        ).pack(pady=10)

        # -------------------------
        # Таблица
        # -------------------------

        entry = tk.Entry(self.scroll_frame)
        entry.pack(pady=10)

        # -------------------------
        # КНОПКА ПРОПУСТИТЬ
        # -------------------------
        tk.Button(
            self.scroll_frame,
            text="Пропустить",
            command=self.skip_form
        ).pack(pady=20)

    def skip_form(self):
        self.controller.show_next_form()

"""ШАГ 4. Тестовые данные (твои формы)"""

with open("samples/forms_v2", "rb") as f:
    forms = pickle.load(f)

# Запуск
if __name__ == "__main__":
    app = App(forms)
    app.mainloop()