import customtkinter as ctk
import random
import textwrap
from working_with_data import Connection


#Класс создает кнопки-ссылки на статью
class ButtonReferenceOnArticle(ctk.CTkButton):
    def __init__(self, master: any,
                 name_article: str,
                 name_chapter: str,
                 id_chapter: int,
                 id_article: int,
                 arg_func: any):
        self.name_article = name_article
        self.name_chapter = name_chapter
        self.id_chapter = id_chapter
        self.id_article = id_article
        self.arg_func = arg_func
        list_random_color = [["#D02090", "#B03060", "#DB7093"], ["#FF7F50", "#D2691E", "#FFA07A"],
                             ["#F5DEB3", "#D2B48C", "#F5F5DC"], ["#FFD700", "#DAA520", "#FFFF00"],
                             ["#00FF00", "#228B22", "#00FF7F"], ["#00FFFF", "#008080", "#40E0D0"],
                             ["#6A5ACD", "#87CEEB", "#6495ED"], ["#A0A0A4", "#778899", "#696969"],
                             ["#FAEBD7", "#FFDAB9", "#FFFAFA"]]
        color_list = random.choice(list_random_color)
        list_random_emoji = ["🔤", "🔡", "♾", "💲", "💱", "®", "👁", "‍🗨", "➿", "➰", "〰", "🔺"]

        emoji = random.choice(list_random_emoji)

        size_font = 20
        final_string = name_article
        if len(name_article) > 14:
            validation_size = len(name_article) - 14
            if validation_size <= 3:
                size_font -= validation_size
            else:
                size_font -= 3
                final_string = textwrap.fill(name_article, 17)

        super().__init__(master, text=f"{emoji*2}\n{final_string}",
                         font=("Tahoma", size_font), width=200, height=150,
                         fg_color=color_list[0], text_color="black",
                         hover_color=color_list[1], border_width=2,
                         border_color=color_list[2], corner_radius=20,
                         command=self.event)
        D_B = Connection()
        D_B.create_void_record_for_article(id_article=self.id_article)
        D_B.close_connect()

    def event(self):
        self.arg_func(self.name_article, self.name_chapter, self.id_chapter, self.id_article)
