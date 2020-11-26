import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()  # toolbar
        self.db = db
        self.view_records()  # Отображение данных БД

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить студента', command=self.open_dialog, bg='#d7d8e0', bd=5,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)  # Кнопка добавить

        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=5, compound=tk.TOP,
                                    command=self.open_update_dialog)  # Кнопка редактировать

        btn_edit_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', "name", "surname", "patronymic", "faculty", "gruppa",
                                                "course", "direction_of_work"), height=18, show='headings')

        # Отображение на экране
        self.tree.column("ID", width=40, anchor=tk.CENTER)
        self.tree.column("name", width=80, anchor=tk.CENTER)
        self.tree.column("surname", width=80, anchor=tk.CENTER)
        self.tree.column("patronymic", width=80, anchor=tk.CENTER)
        self.tree.column("faculty", width=180, anchor=tk.CENTER)
        self.tree.column("gruppa", width=60, anchor=tk.CENTER)
        self.tree.column("course", width=60, anchor=tk.CENTER)
        self.tree.column("direction_of_work", width=200, anchor=tk.CENTER)

        # Подписи колонок
        self.tree.heading("ID", text='ID')
        self.tree.heading("name", text="Имя")
        self.tree.heading("surname", text="Фамилия")
        self.tree.heading("patronymic", text="Отчество")
        self.tree.heading("faculty", text="Факультет")
        self.tree.heading("gruppa", text="Группа")
        self.tree.heading("course", text="Курс")
        self.tree.heading("direction_of_work", text="Направление работы")

        self.tree.pack()

    def records(self, name, surname, patronymic, faculty, gruppa, course,
                direction_of_work):  # Передача данных в INSERT INTO
        self.db.insert_data(name, surname, patronymic, faculty, gruppa, course, direction_of_work)
        self.view_records()

    def update_record(self, name, surname, patronymic, faculty, gruppa, course,
                      direction_of_work):  # Обновление данных БД
        self.db.c.execute('''UPDATE students SET name=?, surname=?, patronymic=?, 
        faculty=?, gruppa=?, course=?, direction_of_work=? WHERE ID=?''',
                          (name, surname, patronymic, faculty, gruppa, course, direction_of_work,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):  # Отображение БД на экране
        self.db.c.execute('''SELECT * FROM students''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):  # Child "Добавить студента"
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):  # Создание окна добавить
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

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
        lable_gruppa = ttk.Label(self, text="Группа:")
        lable_gruppa.place(x=50, y=150)
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

        self.combobox_faculty = ttk.Combobox(self, values=[u"Биологии и биотехники (ИББ)",
                                                           u"Институт географии (ИНГЕО)",
                                                           u"Колледж АГУ (СПО)",
                                                           u"Исторический (ИИМО)",
                                                           u"Институт психологии (ИП)",
                                                           u"Искусств и дизайна (ИИД)",
                                                           u"Институт социальных наук (ИСН)",
                                                           u"Исторический (ИИМО)"])
        self.combobox_faculty.current(0)
        self.combobox_faculty.place(x=135, y=120)

        self.entry_gruppa = ttk.Entry(self)
        self.entry_gruppa.place(x=150, y=150)

        self.combobox_course = ttk.Combobox(self, values=[u"Первый", u"Второй", u"Третий", u"Четвертый", u"Пятый"])
        self.combobox_course.current(0)
        self.combobox_course.place(x=135, y=180)

        self.combobox_direction_of_work = ttk.Combobox(self, values=[u"Научное студенческое общество",
                                                                     u"Социальная поддержка",
                                                                     u"Спорт",
                                                                     u"Культура и творчество",
                                                                     u"Штаб трудовых дел"])
        self.combobox_direction_of_work.current(0)
        self.combobox_direction_of_work.place(x=135, y=210)

        btn_cansel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cansel.place(x=220, y=260)  # Кнопка закрыть

        self.btn_ok = ttk.Button(self, text="Добавить")  # Кнопка добавить
        self.btn_ok.place(x=140, y=260)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(),
                                                                       self.entry_surname.get(),
                                                                       self.entry_patronymic.get(),
                                                                       self.combobox_faculty.get(),
                                                                       self.entry_gruppa.get(),
                                                                       self.combobox_course.get(),
                                                                       self.combobox_direction_of_work.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):  # Кнопка редактировать
        self.title('Редактировать запись')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=120, y=260)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_name.get(),
                                                                          self.entry_surname.get(),
                                                                          self.entry_patronymic.get(),
                                                                          self.combobox_faculty.get(),
                                                                          self.entry_gruppa.get(),
                                                                          self.combobox_course.get(),
                                                                          self.combobox_direction_of_work.get()))
        self.btn_ok.destroy()


class DB:  # База данных
    def __init__(self):
        self.conn = sqlite3.connect("students.db")  # Создаем/подключаемся
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS students 
            (id integer primary key, name text, surname text, 
            patronymic text, faculty text, gruppa integer, 
            course text, direction_of_work text)''')
        self.conn.commit()

    def insert_data(self, name, surname, patronymic, faculty, gruppa, course, direction_of_work):  # Добавление данных
        self.c.execute('''INSERT INTO students(name, surname, patronymic, faculty, gruppa, course, direction_of_work) 
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, surname, patronymic, faculty, gruppa, course, direction_of_work))
        self.conn.commit()


if __name__ == "__main__":  # Создание окна
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Лига студентов")
    root.geometry("800x450+300+200")
    root.resizable(False, False)
    root.mainloop()
