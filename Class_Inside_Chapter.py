import customtkinter as ctk


class InsideChapter:
    def __init__(self,
                 master: any,
                 name_chapter: str,
                 id_chapter: int,
                 arg_func: any,
                 arg_func_2: any):
        self.name_chapter = name_chapter
        self.id_chapter = id_chapter
        self.arg_func = arg_func
        self.arg_func_2 = arg_func_2

        from suportive_function import list_open_tabs_for_chapters

        condition = ""

        for x in list_open_tabs_for_chapters:
            if self.id_chapter in x:
                condition = "disabled"
                break
        else:
            condition = "normal"

        # кнопка создания статьи🗑
        self.button_add_small_chapter = ctk.CTkButton(master, text="➕\nДобавьте статью",
                                                                font=("Tahoma", 18), width=120, height=35,
                                                                fg_color="#32CD32", text_color="black",
                                                                hover_color="#00FF7F", border_width=2,
                                                                border_color="#ADFF2F", corner_radius=8,
                                                                command=self.event)
        self.button_add_small_chapter.grid(row=0, column=0, padx=10, pady=7, sticky="we")

        # фрейм для названия раздела
        self.info_frame = ctk.CTkFrame(master, fg_color="#E6E6FA")
        self.info_frame.grid(row=0, column=1, padx=60, pady=10, sticky="nw")
        # название раздела
        self.info_label = ctk.CTkLabel(self.info_frame, text=name_chapter,
                                       font=("Tahoma", 20))
        self.info_label.grid(row=0, column=0, padx=25, pady=10, sticky="nw")

        self.button_delete_chapter = ctk.CTkButton(master, text="🗑",
                                                      font=("Tahoma", 18), width=50, height=45,
                                                      fg_color="red", text_color="black", border_color="red",
                                                      border_width=2, corner_radius=8, state=condition,
                                                      command=self.event_2)
        self.button_delete_chapter.grid(row=0, column=2, padx=10, pady=7, sticky="we")

    def event(self):
        self.arg_func(self.name_chapter, self.id_chapter)

    def event_2(self):
        self.arg_func_2(self.id_chapter)
