logging_last_press = []


def clear_logging_last_press():
    logging_last_press.clear()


def add_in_logging_last_press(name_article, name_chapter, id_chapter, id_article):
    # print("Функция add_in_logging_last_press работает")
    global logging_last_press
    if len(logging_last_press) > 0:
        logging_last_press.clear()
        logging_last_press = [x for x in (name_article, name_chapter, id_chapter, id_article)]
    else:
        logging_last_press = [x for x in (name_article, name_chapter, id_chapter, id_article)]
        # print(logging_last_press)


list_open_tabs_for_articles = []
list_open_tabs_for_chapters = []


def record_name_in_lists_open_tabs(name_article, name_chapter, id_chapter, id_article):
    list_open_tabs_for_articles.append([x for x in (name_article, id_article)])
    list_open_tabs_for_chapters.append([y for y in (name_chapter, id_chapter)])


def delete_tabs_from_lists_open_tabs(name_article, name_chapter):
    for art, chap in zip(list_open_tabs_for_articles, list_open_tabs_for_chapters):
        if art[0] == name_article and chap[0] == name_chapter:
            index_for_remove_1 = list_open_tabs_for_articles.index(art)
            index_for_remove_2 = list_open_tabs_for_chapters.index(chap)
            list_open_tabs_for_articles.pop(index_for_remove_1)
            list_open_tabs_for_chapters.pop(index_for_remove_2)


def read_name_article_for_open_tabs():
    return [x[0] for x in list_open_tabs_for_articles], [x[1] for x in list_open_tabs_for_articles]


def read_name_chapter_for_open_tabs():
    return [y[0] for y in list_open_tabs_for_chapters], [y[1] for y in list_open_tabs_for_chapters]


def delete_all_from_lists_for_open_tabs():
    list_open_tabs_for_articles.clear()
    list_open_tabs_for_chapters.clear()


def return_value_logging_last_press():
    return logging_last_press[0]


def search_string_in_sub_lists(string, where_search):
    for x in where_search:
        if x[0] == string:
            return where_search.index(x)


#Эта функция возвращает измененный номер строки для кнопок разделов, что бы кнопки были на разных строках
def function_for_offset_down(arg_count):
    if arg_count == 0:
        return 1
    else:
        return arg_count + 1


def function_for_offset_down_for_chapter_article(num):
    i, row, column = 0, 0, 0
    while i < num:
        row += 1
        for y in [0, 1, 2]:
            i += 1
            if i == num:
                column = y
                break
    return row, column