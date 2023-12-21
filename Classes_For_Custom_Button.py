import customtkinter as ctk


class CustomButton(ctk.CTkButton):
    def __init__(self,
                 master: any,
                 name_button: str,
                 id_chapter: int,
                 arg_func: any):
        self.name_button = name_button
        self.id_chapter = id_chapter
        self.arg_func = arg_func
        # кнопка
        super().__init__(master, text=name_button, fg_color="#FFFBF0", text_color="black",
                         font=("Tahoma", 15), width=180, border_color="#C0C0C0",
                         border_width=1, hover_color="#FFDAB9",
                         # передаём название раздела в функцию которая создаёт
                         # содержимое основной рабочей облати
                         command=self.event)

    def event(self):
        self.arg_func(self.name_button, self.id_chapter)


class ToolBarButton(ctk.CTkButton):
    def __init__(self,
                 master: any,
                 command: any,
                 name: str,
                 font_size: int,
                 btn_color: str):
        super().__init__(master, text=name, font=("Arial Bold", font_size),
                         width=60, height=30, fg_color=btn_color, text_color="black",
                         border_color="#808080", border_width=1, corner_radius=9,
                         command=command)