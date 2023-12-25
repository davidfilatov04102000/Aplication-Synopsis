import customtkinter as ctk
from Classes_For_Custom_Button import ToolBarButton
from working_with_data import Connection
from tkinter.messagebox import askyesno, showerror
from suportive_function import add_in_logging_last_press


class InsideArticleAndToolBar:
    def __init__(self,
                 master: any,
                 name_article_for_info_label: str,
                 id_article: int,
                 arg_func_home: any,
                 name_chapter: str,
                 id_chapter: int,
                 arg_func_for_delete_tabs,
                 func_for_rename_tabs):
        self.size_font_for_scale = 25
        self.name_article_for_info_label = name_article_for_info_label
        self.id_article = id_article
        self.arg_func_home = arg_func_home
        self.name_chapter = name_chapter
        self.id_chapter = id_chapter
        self.arg_func_for_delete_tabs = arg_func_for_delete_tabs
        self.func_for_rename_tabs = func_for_rename_tabs
        self.tool_bar_frame = ctk.CTkFrame(master, corner_radius=10, fg_color="#A0A0A4")
        self.tool_bar_frame.grid(row=0, column=0, padx=5, pady=3, sticky="w")

        self.home_btn = ToolBarButton(master=self.tool_bar_frame, name="⬅", font_size=16,
                                      btn_color="#FF4500", command=self.to_menu_chapter)
        self.home_btn.grid(row=0, column=0, padx=22, pady=5, sticky="w")

        self.btn_edit = ToolBarButton(master=self.tool_bar_frame, name="🖍", font_size=19,
                                      btn_color="#A6CAF0", command=self.do_text_box_edit)
        self.btn_edit.grid(row=0, column=1, padx=22, pady=5, sticky="w")

        self.btn_save = ToolBarButton(master=self.tool_bar_frame, name="✔", font_size=15,
                                      btn_color="#00FF00", command=self.save_change_in_article)
        self.btn_save.grid(row=0, column=2, padx=22, pady=5, sticky="w")

        self.scale_up_btn = ToolBarButton(master=self.tool_bar_frame, name="М⬆", font_size=16, btn_color="#FF4500",
                                          command=self.scale_up)
        self.scale_up_btn.grid(row=0, column=3, padx=22, pady=5, sticky="w")

        self.scale_down_btn = ToolBarButton(master=self.tool_bar_frame, name="М⬇", font_size=16, btn_color="#A6CAF0",
                                            command=self.scale_down)
        self.scale_down_btn.grid(row=0, column=4, padx=22, pady=5, sticky="w")

        self.btn_rename_article = ToolBarButton(master=self.tool_bar_frame, name="ReNaMe", font_size=10,
                                                btn_color="#FF0000", command=self.rename_article)
        self.btn_rename_article.grid(row=0, column=6, padx=22, pady=5, sticky="w")

        self.btn_delete_article = ToolBarButton(master=self.tool_bar_frame, name="🗑", font_size=18,
                                                btn_color="#FF0000", command=self.delete_article)
        self.btn_delete_article.grid(row=0, column=7, padx=22, pady=5, sticky="w")

        self.frame_for_name_article = ctk.CTkFrame(master=self.tool_bar_frame, corner_radius=10)
        self.frame_for_name_article.grid(row=0, column=5, padx=5, pady=5)

        self.text_label = ctk.CTkLabel(master=self.frame_for_name_article, text=self.name_article_for_info_label,
                                       font=("Tahoma", 15))
        self.text_label.grid(row=0, column=0, padx=20, pady=5)

        self.text_box = ctk.CTkTextbox(master, width=1100, height=640, corner_radius=10,
                                       font=("Tahoma", 20), border_spacing=15)
        self.text_box.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        D_B = Connection()
        result = D_B.read_text_article(self.id_article)
        D_B.close_connect()
        result_str = ""
        for xx in result:
            result_str += xx
        self.text_box.insert("0.0", result_str)
        self.text_box.configure(state="disabled")

    def to_menu_chapter(self):
        self.arg_func_home(self.name_chapter, self.id_chapter, 1)

    def scale_up(self):
        self.size_font_for_scale += 1
        self.text_box.configure(font=("Arial Bold", self.size_font_for_scale))

    def scale_down(self):
        self.size_font_for_scale -= 1
        self.text_box.configure(font=("Arial Bold", self.size_font_for_scale))

    def do_text_box_edit(self):
        self.text_box.configure(state="normal")

    def save_change_in_article(self):
        self.text_from_article = self.text_box.get("0.0", "end")
        D_B = Connection()
        D_B.create_write_text_article(self.id_article, self.text_from_article)
        D_B.close_connect()
        self.text_box.configure(state="disabled")

    def delete_article(self):
        ask_window = askyesno("Подтверждение операции", "Вы действительно хотите\nбезвозвратно удалить эту статью?")
        if ask_window is True:
            D_B = Connection()
            D_B.delete_article(self.id_article)
            D_B.close_connect()
            self.arg_func_home(self.name_chapter, self.id_chapter)
            self.arg_func_for_delete_tabs(self.name_article_for_info_label, self.name_chapter)
        else:
            pass

    def rename_article(self):
        dialog_window = ctk.CTkInputDialog(text="Введите новое название статьи",
                                                     title="Переименовать статью")
        value_dialog_window = dialog_window.get_input()
        if value_dialog_window is None:
            pass
        else:
            if value_dialog_window == "":
                showerror(message="Ошибка", title="Ошибка")
            elif value_dialog_window.isspace() is True:
                showerror(message="Ошибка", title="Ошибка")
            else:
                D_B = Connection()
                D_B.rename_article(old_name=self.name_article_for_info_label, new_name=value_dialog_window)
                D_B.close_connect()
                self.func_for_rename_tabs(value_dialog_window)
                add_in_logging_last_press(value_dialog_window, self.name_chapter, self.id_chapter, self.id_article)

        self.save_change_in_article()
