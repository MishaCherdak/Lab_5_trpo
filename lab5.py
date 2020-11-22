import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()  # toolbar

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить студента', command=self.open_dialog, bg='#d7d8e0', bd=5,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)  # Кнопка добавить

        # Отображение на экране
        self.tree = ttk.Treeview(self, columns=('ID', "name", "surname", "patronymic", "faculty", "group",
                                                "course", "direction_of_work"), height=18, show='headings')
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("name", width=70, anchor=tk.CENTER)
        self.tree.column("surname", width=70, anchor=tk.CENTER)
        self.tree.column("patronymic", width=70, anchor=tk.CENTER)
        self.tree.column("faculty", width=70, anchor=tk.CENTER)
        self.tree.column("group", width=50, anchor=tk.CENTER)
        self.tree.column("course", width=40, anchor=tk.CENTER)
        self.tree.column("direction_of_work", width=85, anchor=tk.CENTER)

        # Подписи колонок
        self.tree.heading("ID", text='ID')
        self.tree.heading("name", text="Имя")
        self.tree.heading("surname", text="Фамилия")
        self.tree.heading("patronymic", text="Отчество")
        self.tree.heading("faculty", text="Факультет")
        self.tree.heading("group", text="Группа")
        self.tree.heading("course", text="Курс")
        self.tree.heading("direction_of_work", text="Направление работы")

        self.tree.pack()

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):  # Создание окна добавить
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):  # Параметры окна добавить
        self.title('Добавить студента')
        self.geometry('330x300+400+300')
        self.resizable(False, False)

        # Заголовки добавляемых данных
        lable_name = ttk.Label(self, text="Имя:")
        lable_name.place(x=50, y=30)
        lable_surname = ttk.Label(self, text="Фамилия:")
        lable_surname.place(x=50, y=60)
        lable_patronymic = ttk.Label(self, text="Отчество:")
        lable_patronymic.place(x=50, y=90)
        lable_select_fac = ttk.Label(self, text="Факультет:")
        lable_select_fac.place(x=50, y=120)
        lable_group = ttk.Label(self, text="Группа:")
        lable_group.place(x=50, y=150)
        lable_course = ttk.Label(self, text="Курс:")
        lable_course.place(x=50, y=180)
        lable_direction_of_work = ttk.Label(self, text="Нап. работы:")
        lable_direction_of_work.place(x=50, y=210)

        # Добавляемые данные
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=150, y=30)

        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=150, y=60)

        self.entry_patronymic = ttk.Entry(self)
        self.entry_patronymic.place(x=150, y=90)

        self.combobox = ttk.Combobox(self, values=[u"Биологии и биотехники (ИББ)",
                                                   u"Институт географии (ИНГЕО)",
                                                   u"Колледж АГУ (СПО)",
                                                   u"Исторический (ИИМО)",
                                                   u"Институт психологии (ИП)",
                                                   u"Искусств и дизайна (ИИД)",
                                                   u"Институт социальных наук (ИСН)",
                                                   u"Исторический (ИИМО)"])
        self.combobox.current(0)
        self.combobox.place(x=135, y=120)

        self.entry_group = ttk.Entry(self)
        self.entry_group.place(x=150, y=150)

        self.combobox = ttk.Combobox(self, values=[u"Первый", u"Второй", u"Третий", u"Четвертый", u"Пятый"])
        self.combobox.current(0)
        self.combobox.place(x=135, y=180)

        self.combobox = ttk.Combobox(self, values=[u"Научное студенческое общество",
                                                   u"Социальная поддержка",
                                                   u"Спорт",
                                                   u"Культура и творчество",
                                                   u"Штаб трудовых дел"])
        self.combobox.current(0)
        self.combobox.place(x=135, y=210)

        btn_cansel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cansel.place(x=220, y=260)  # Кнопка закрыть

        btn_ok = ttk.Button(self, text="Добавить")  # Кнопка добавить
        btn_ok.place(x=140, y=260)
        btn_ok.bind('<button-1>')

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":  # Создание окна
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Домашние финансы")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
