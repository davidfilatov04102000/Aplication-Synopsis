import customtkinter as ctk
import pprint
from suportive_function import add_in_logging_last_press, delete_tabs_from_lists_open_tabs, \
    read_name_article_for_open_tabs, read_name_chapter_for_open_tabs, delete_all_from_lists_for_open_tabs, \
    clear_logging_last_press, search_string_in_sub_lists


class TabsAndDoubleButton(ctk.CTkFrame):
    def __init__(self,
                 master: any,
                 name_article: str,
                 id_article: int,
                 arg_func: any,
                 name_chapter: str,
                 id_chapter: int,
                 func_open_new_art: any,
                 func_open_menu_chapter: any):
        super().__init__(master, corner_radius=8)

        self.arg_func = arg_func
        self.name_article = name_article
        self.id_article = id_article
        self.name_chapter = name_chapter
        self.id_chapter = id_chapter
        self.func_open_new_article = func_open_new_art
        self.func_open_menu_chapter = func_open_menu_chapter

        self.button_1 = ctk.CTkButton(self, text=self.name_article, font=("Arial Bold", 11), border_spacing=1,
                                      width=40, height=20, fg_color="#4682B4",
                                      command=self.transition_on_tabs)
        self.button_1.grid(row=0, column=0, sticky="w")

        self.button_2 = ctk.CTkButton(self, text="❌", font=("Arial Bold", 10), width=10, height=20,
                                      fg_color="#4682B4", command=self.delete_tabs)
        self.button_2.grid(row=0, column=1, sticky="w")

    def transition_on_tabs(self):
        add_in_logging_last_press(self.name_article, self.name_chapter, self.id_chapter, self.id_article)
        self.arg_func(self.name_article, self.name_chapter, self.id_chapter, self.id_article)
        from suportive_function import list_open_tabs_for_articles, list_open_tabs_for_chapters, \
            logging_last_press
        pprint.pprint(list_open_tabs_for_articles)
        pprint.pprint(list_open_tabs_for_chapters)
        print(logging_last_press)
        print("\n\n")

    def delete_tabs(self):
        from suportive_function import logging_last_press
        if logging_last_press[0] != self.name_article:
            self.destroy()
            # print(f"Работает данное условие {self.name_article}, {self.name_chapter}")
            delete_tabs_from_lists_open_tabs(self.name_article, self.name_chapter)
            # ar = read_name_article_for_open_tabs()
            # br = read_name_chapter_for_open_tabs()
            # print(ar)
        else:
            a = read_name_article_for_open_tabs()[0]
            b = read_name_chapter_for_open_tabs()[0]
            a_id = read_name_article_for_open_tabs()[1]
            b_id = read_name_chapter_for_open_tabs()[1]
            ind_art_in_list = a.index(self.name_article)
            # print(a)
            if len(a) == 1:
                delete_all_from_lists_for_open_tabs()
                clear_logging_last_press()
                self.func_open_menu_chapter(self.name_chapter, self.id_chapter)
                self.destroy()
            else:
                if ind_art_in_list == (len(a)-1):
                    access = ind_art_in_list - 1
                    name_new_art = a[access]
                    name_chap_for_his = b[access]
                    id_article = a_id[access]
                    id_chapter = b_id[access]
                    delete_tabs_from_lists_open_tabs(self.name_article, self.name_chapter)
                    self.func_open_new_article(name_new_art, name_chap_for_his, id_chapter, id_article)
                    self.destroy()
                else:
                    access = ind_art_in_list + 1
                    name_new_art = a[access]
                    name_chap_for_his = b[access]
                    id_article = a_id[access]
                    id_chapter = b_id[access]
                    delete_tabs_from_lists_open_tabs(self.name_article, self.name_chapter)
                    self.func_open_new_article(name_new_art, name_chap_for_his, id_chapter, id_article)
                    self.destroy()

    def configure_text(self, new_name):
        from suportive_function import list_open_tabs_for_articles, list_open_tabs_for_chapters, \
            logging_last_press
        pprint.pprint(list_open_tabs_for_articles)
        pprint.pprint(list_open_tabs_for_chapters)
        print(logging_last_press)

        local_list_open_tabs_for_articles = list_open_tabs_for_articles.copy()
        ind_sub_lists = search_string_in_sub_lists(self.name_article, local_list_open_tabs_for_articles)
        list_open_tabs_for_articles[ind_sub_lists].pop(0)
        list_open_tabs_for_articles[ind_sub_lists].insert(0, new_name)

        self.name_article = new_name
        self.button_1.configure(text=new_name)

        add_in_logging_last_press(new_name, self.name_chapter, self.id_chapter, self.id_article)