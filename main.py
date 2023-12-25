from tkinter.messagebox import askyesno, showerror
import customtkinter as ctk
from working_with_data import Connection
from Classes_For_Custom_Button import CustomButton
from Class_Inside_Chapter import InsideChapter
from Class_Button_Reference_On_Article import ButtonReferenceOnArticle
from Class_Inside_Article_And_Tool_Bar import InsideArticleAndToolBar
from Class_For_Tabs import TabsAndDoubleButton
from suportive_function import function_for_offset_down, function_for_offset_down_for_chapter_article, \
     add_in_logging_last_press, record_name_in_lists_open_tabs, read_name_article_for_open_tabs, \
     delete_tabs_from_lists_open_tabs, delete_all_from_lists_for_open_tabs, change_value_configuration_app_now


#Переменная которая хранит количество вкладок и используется в качестве аргумента для размещения на фрейме вкладок
count_for_offset_Tabs = 1


#Функция которая увеличивает значение переменной выше на 1
def change_offset_tabs():
    global count_for_offset_Tabs
    count_for_offset_Tabs += 1


#основной класс с пользовательским интерфейсом
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.width_win = 1400
        self.height_win = 788
        self.title("Synopsis")
        self.geometry(f"{self.width_win}x{self.height_win}")
        #
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        change_value_configuration_app_now(0)

        """Рамка для боковой панели слева"""
        self.art_left = ctk.CTkFrame(self, width=self.width_win - 1070, corner_radius=0)
        self.art_left.grid(row=0, column=0, rowspan=4, sticky="nsew")

        """Рамка для вспомогательных виджетов"""
        self.help_widget_frame = ctk.CTkFrame(self.art_left, corner_radius=0)
        self.help_widget_frame.grid(row=0, column=0)

        """Лейбл Synopsis"""
        self.main_label = ctk.CTkLabel(self.help_widget_frame, text="Synopsis",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=70, pady=(20, 10))

        """Кнопка для добавления нового раздела"""
        self.button_add = ctk.CTkButton(self.help_widget_frame, text="+", width=30, height=20,
                                        font=ctk.CTkFont(size=18), command=self.create_button)
        self.button_add.grid(row=1, column=0, padx=40, pady=(0, 10), sticky="w")

        """Прокручиваемый фрейм для кнопок разделов"""
        self.scroll_frame_for_chapter = ctk.CTkScrollableFrame(self.art_left, height=650, corner_radius=0)
        self.scroll_frame_for_chapter.grid(row=1, column=0)

        """Рамка для основного рабочего поля"""
        self.main_field_frame = ctk.CTkFrame(self, height=(self.height_win - 95), corner_radius=10)
        self.main_field_frame.grid(row=0, column=1, padx=20, pady=10, sticky="new", rowspan=4)

        """Прокручиваемый фрейм для вкладок"""
        self.frame_for_tabs = ctk.CTkScrollableFrame(self, height=25, corner_radius=5,
                                                     orientation="horizontal")
        self.frame_for_tabs.grid(row=2, column=1, padx=20, pady=10, sticky="wse")

        """Вызов функции которая считывает и создает кнопки разделов"""
        self.create_exist_chapters()
        """Функция которая полностью чистит файлы для учета открытых файлов """
        delete_all_from_lists_for_open_tabs()

    """Функция удаляет всплывающие виджеты для создания нового раздела"""
    def delete_time_widget(self):
        self.time_label.destroy()
        self.time_entry.destroy()
        self.time_btn_ok.destroy()
        self.time_btn_non.destroy()
        self.button_add.configure(state="normal")

    """Функция для сохранения нового раздела"""
    def create_chapter(self):
        D_B = Connection()
        offset_down = function_for_offset_down(D_B.return_count_chapters())

        name_new_chapter = self.time_entry.get()

        if name_new_chapter.isspace() is True or name_new_chapter == "":
            self.delete_time_widget()
        else:

            D_B.save_name_chapter(name_new_chapter)

            new_chapter = CustomButton(master=self.scroll_frame_for_chapter, name_button=name_new_chapter,
                                       id_chapter=D_B.return_id_chapter(name_new_chapter),
                                       arg_func=self.distribution_function)
            new_chapter.grid(row=offset_down, column=0, padx=10, pady=10, sticky="we")

            D_B.close_connect()

            self.delete_time_widget()

            self.button_add.configure(state="normal")

    def delete_chapter(self, id_chapter):
        showerror(title="Предупреждение",
                               message="Если вы удалите этот раздел, вместе с ним "
                                       "удаляться все статьи из этого раздела")
        result_pool = askyesno(title="Удаление раздела", message="Вы действительно хотите безвозвратно "
                                                                 "удалить этот раздел")
        if result_pool is False:
            pass
        else:
            D_B = Connection()
            D_B.delete_chapter(id_chapter)
            D_B.close_connect()

            for widget in self.main_field_frame.winfo_children():
                widget.destroy()
            for widget_2 in self.scroll_frame_for_chapter.winfo_children():
                widget_2.destroy()
            self.create_exist_chapters()



    """Функция создает всплывающие виджеты для создания нового раздела"""
    def create_button(self):
        """Сделаем кнопку плюсика неактивной"""
        self.button_add.configure(state="disabled")

        """Подпись к полю для ввода"""
        self.time_label = ctk.CTkLabel(self.help_widget_frame, text="Имя нового раздела", font=("Tahoma", 12))
        self.time_label.grid(row=2, column=0, padx=45, pady=0, sticky="nw")

        """Поле для ввода названия нового раздела"""
        self.time_entry = ctk.CTkEntry(self.help_widget_frame, width=160)
        self.time_entry.grid(row=2, column=0, padx=35, pady=(22, 7), sticky="sw")
        """фокус"""
        self.time_entry.focus()

        """Кнопка сохранения нового раздела"""
        self.time_btn_ok = ctk.CTkButton(self.help_widget_frame, text="✅", width=16, fg_color="green",
                                                   font=("Arial Bold", 12), command=self.create_chapter)
        self.time_btn_ok.grid(row=1, column=0, padx=60, pady=0, sticky="n")

        """Кнопка удаления всплывающих виджетов для создания раздела"""
        self.time_btn_non = ctk.CTkButton(self.help_widget_frame, text="❌", width=16, fg_color="red",
                                                    font=("Arial Bold", 12), command=self.delete_time_widget)
        self.time_btn_non.grid(row=1, column=0, padx=40, pady=0, sticky="ne")

    """Функция создает всплывающую рамку с виджетами для создания статьи"""
    def create_widget_for_create_article(self, name_chapter, id_chapter):
        D_B = Connection()
        """получаем колличество статей из текст файла"""
        count_article = D_B.return_count_articles(id_chapter)
        """ Создаем вспывающее окно которое спрашивает название новой статьи"""
        self.time_window_for_create_article = ctk.CTkInputDialog(text="Название статьи",
                                                                 title="Создание новой статьи")
        """Получем значение из этого окна"""
        self.name_new_article = self.time_window_for_create_article.get_input()
        """Проверям если занчение пустое, то есть процесс отменен"""
        if self.name_new_article is None:
            pass
        elif self.name_new_article.isspace() is True or self.name_new_article == "":
            pass
        # Если нет, то ...
        else:
            values_for_offset = function_for_offset_down_for_chapter_article(count_article + 1)
            D_B.save_name_article(id_chapter, self.name_new_article)
            id_article = D_B.return_id_article(self.name_new_article)
            D_B.close_connect()
            self.new_article = ButtonReferenceOnArticle(master=self.main_field_frame, name_article=self.name_new_article,
                                                        name_chapter=name_chapter, id_chapter=id_chapter,
                                                        id_article=id_article, arg_func=self.create_inside_article)
            self.new_article.grid(row=values_for_offset[0], column=values_for_offset[1], padx=70, pady=30)
            """Передаем имя раздела и имя статьи в функцию которая сохраняет их в файл"""

    #Функиция которая создает содержимое внутри статьи
    def create_inside_article(self, name_article, name_chapter, id_chapter, id_article):
        # Список открытых статей
        list_open_tabs = read_name_article_for_open_tabs()[1]
        # Проверка
        if id_article in list_open_tabs:
            self.open_article(name_article, name_chapter, id_chapter, id_article)
        else:
            self.open_article(name_article, name_chapter, id_chapter, id_article)
            self.create_tabs(name_article, name_chapter, id_chapter, id_article)

        # Дубликат функции которая создает содержимое внутри статьи
    def create_inside_article_duplicate(self, name_article, name_chapter, id_chapter, id_article):
        # цикл удаляющий все содержимое основной рабочей области
        for widget in self.main_field_frame.winfo_children():
            widget.destroy()
        # Создание объекта класса который создает текстовое поле и панель инструментов
        self.text_box = InsideArticleAndToolBar(master=self.main_field_frame, name_article_for_info_label=name_article,
                                                id_article=id_article, arg_func_home=self.distribution_function,
                                                name_chapter=name_chapter, id_chapter=id_chapter,
                                                arg_func_for_delete_tabs=self.delete_tabs_in_time_delete_article,
                                                func_for_rename_tabs=self.rename_tabs_article)
        change_value_configuration_app_now(2)
        add_in_logging_last_press(name_article, name_chapter, id_chapter, id_article)

    # Функция которая создает содержимое статьи она будет вызываться в create_inside_article()
    def open_article(self, name_article, name_chapter, id_chapter, id_article):
        for widget in self.main_field_frame.winfo_children():
            widget.destroy()
        # объект класса который созадет и текстовое поле и панель инструментов
        self.text_box = InsideArticleAndToolBar(master=self.main_field_frame, name_article_for_info_label=name_article,
                                                id_article=id_article, arg_func_home=self.distribution_function,
                                                name_chapter=name_chapter, id_chapter=id_chapter,
                                                arg_func_for_delete_tabs=self.delete_tabs_in_time_delete_article,
                                                func_for_rename_tabs=self.rename_tabs_article)
        change_value_configuration_app_now(2)

    # Функция которая создает вкладку статьи
    def create_tabs(self, name_article, name_chapter, id_chapter, id_article):
        # создание объекта класса который создает вкладку статьи
        self.one_tabs = TabsAndDoubleButton(self.frame_for_tabs, name_article, id_article,
                                            self.create_inside_article_duplicate, name_chapter, id_chapter,
                                            self.create_inside_article_duplicate,
                                            self.distribution_function,
                                            self.info_about_object_article)
        # размещение
        self.one_tabs.grid(row=0, column=count_for_offset_Tabs)
        # функция которая меняет число для отступа вкладки
        change_offset_tabs()
        # добавление названия статьи и раздела в файл для учета открытых вкладок
        record_name_in_lists_open_tabs(name_article, name_chapter, id_chapter, id_article)
        # вызов функции регистрации последнего нажатия на вкладку либо статью
        add_in_logging_last_press(name_article, name_chapter, id_chapter, id_article)

    def delete_tabs_in_time_delete_article(self, name_article, name_chapter):
        list_open_tabs = read_name_article_for_open_tabs()[0]
        index_tabs_for_delete = list_open_tabs.index(name_article)
        i = -1
        for widget in self.frame_for_tabs.winfo_children():
            i += 1
            if i == index_tabs_for_delete:
                widget.destroy()
        delete_tabs_from_lists_open_tabs(name_article, name_chapter)

    """Функция которая меняет название именно вкладки
        внутри функции open_article() она передается в качестве аргумента 
        объекту класса InsideArticleAndToolBar и там же будет вызываться"""
    def rename_tabs_article(self, new_name_article):
        self.one_tabs.configure_text(new_name_article)

    """Функция считывает и создает кнопки разделов"""
    def create_exist_chapters(self):
        """получаем список существующих разделов"""
        D_B = Connection()
        count_chapters = D_B.return_count_chapters()
        if count_chapters == 0:
            pass
        else:
            list_exist_chapters = D_B.return_name_and_id_chapters()[0]
            list_exist_chapters_id = D_B.return_name_and_id_chapters()[1]
            D_B.close_connect()
            """счетчик воссозданных разделов"""
            count_chapters = 0
            """проверка пустой ли список разделов"""
            if len(list_exist_chapters) != 0:
                """цикл воссоздания разделов"""
                for name, k in zip(list_exist_chapters, list_exist_chapters_id):
                    count_chapters += 1
                    new_chapter = CustomButton(master=self.scroll_frame_for_chapter, name_button=name, id_chapter=k,
                                               arg_func=self.distribution_function)
                    new_chapter.grid(row=count_chapters, column=0, padx=10, pady=10, sticky="we")

    """Функция считывает и создает список статей"""
    def create_exist_article(self, name_chapter, id_chapter):
        """получаем колличество существующих статей"""
        D_B = Connection()
        count_article = D_B.return_count_articles(id_chapter)
        """проверка пустой ли список статей"""
        if count_article == 0:
            pass
        else:
            """получение списка статей"""
            D_B = Connection()
            list_name_article = D_B.return_name_and_id_article(id_chapter)[0]
            list_id_article = D_B.return_name_and_id_article(id_chapter)[1]
            D_B.close_connect()
            """счетчик для отступов кнопок статей"""
            count_article_for_offset = 0
            """цикл воссоздания кнопок статей"""
            for i, k in zip(list_name_article, list_id_article):
                count_article_for_offset += 1
                values_for_offset = function_for_offset_down_for_chapter_article(count_article_for_offset)
                """Создание обьекта класса кнопки ссылки на статью"""
                self.exist_article = ButtonReferenceOnArticle(master=self.main_field_frame, name_article=i,
                                                              name_chapter=name_chapter, id_chapter=id_chapter,
                                                              id_article=k, arg_func=self.create_inside_article)
                self.exist_article.grid(row=values_for_offset[0], column=values_for_offset[1], padx=70, pady=30)

    def info_about_object_article(self):
        return self.text_box

    """Функция создает содержимое основной рабочей области"""

    def distribution_function(self, name_chapter, id_chapter, save_article=None):
        from suportive_function import list_open_tabs_for_articles, configuration_app_now
        if save_article is not None:
            self.text_box.save_change_in_article()
        elif len(list_open_tabs_for_articles) != 0:
            if configuration_app_now[0] == 2:
                self.text_box.save_change_in_article()

        change_value_configuration_app_now(1)

        # цикл удаляющий все содержимое основной рабочей области
        for widget in self.main_field_frame.winfo_children():
            widget.destroy()
        # создание объекта класса содержимого внутри раздела
        self.small_chapter = InsideChapter(self.main_field_frame, name_chapter, id_chapter,
                                           self.create_widget_for_create_article, self.delete_chapter)
        # отрисовка кписка существующих статей
        self.create_exist_article(name_chapter, id_chapter)


if __name__ == "__main__":
    main_obj = App()
    main_obj.mainloop()
