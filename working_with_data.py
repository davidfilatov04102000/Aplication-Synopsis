import sqlite3
import pprint


"""names_of_chapters(id INTEGER PRIMARY KEY AUTOINCREMENT, name_chapter)"""
"""names_of_articles_with_id_chapters(id_chapter, name_article, id INTEGER PRIMARY KEY AUTOINCREMENT)"""
"""names_of_articles_and_their_text(id_article, text_article)"""


class Connection:
    def __init__(self):
        self.connect = sqlite3.connect("database_for_synopsis.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS names_of_chapters(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            "name_chapter TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS names_of_articles_with_id_chapters(id_chapter INTEGER, "
                            "name_article TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS names_of_articles_and_their_text(id_article INTEGER, "
                            "text_article TEXT)")

    def return_count_chapters(self):
        self.cursor.execute("SELECT * FROM names_of_chapters")
        return len(self.cursor.fetchall())

    def return_count_articles(self, id_chapter):
        self.cursor.execute(f"SELECT * FROM names_of_articles_with_id_chapters WHERE id_chapter={id_chapter}")
        return len(self.cursor.fetchall())

    def return_name_and_id_article(self, id_chapter):
        self.cursor.execute(f"SELECT * FROM names_of_articles_with_id_chapters WHERE id_chapter={id_chapter}")
        self.result_read = self.cursor.fetchall()
        return [x[1] for x in self.result_read], [y[2] for y in self.result_read]

    def return_name_and_id_chapters(self):
        self.cursor.execute("SELECT * FROM names_of_chapters")
        self.result_read = self.cursor.fetchall()
        return [x[1] for x in self.result_read], [y[0] for y in self.result_read]

    def save_name_chapter(self, name):
        self.cursor.execute("INSERT INTO names_of_chapters(name_chapter) VALUES (?)", (name,))
        self.connect.commit()

    def save_name_article(self, id_chapter, name):
        self.cursor.execute("INSERT INTO names_of_articles_with_id_chapters(id_chapter, name_article) VALUES (?,?)",
                            (id_chapter, name))
        self.connect.commit()

    def return_id_chapter(self, name):
        self.cursor.execute(f"SELECT * FROM names_of_chapters WHERE name_chapter='{name}'")
        return self.cursor.fetchall()[0][0]

    def return_id_article(self, name):
        self.cursor.execute(f"SELECT * FROM names_of_articles_with_id_chapters WHERE name_article='{name}'")
        return self.cursor.fetchall()[0][2]

    def create_write_text_article(self, id_article, text_article):
        self.cursor.execute(f"SELECT * FROM names_of_articles_and_their_text WHERE id_article={id_article}")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("INSERT INTO names_of_articles_and_their_text(id_article, text_article) VALUES (?,?)",
                                (id_article, text_article))
            self.connect.commit()
        else:
            self.cursor.execute("UPDATE names_of_articles_and_their_text SET text_article= ? WHERE id_article= ?",
                                (text_article, id_article))
            self.connect.commit()

    def create_void_record_for_article(self, id_article):
        self.cursor.execute("INSERT INTO names_of_articles_and_their_text(id_article, text_article) VALUES (?,?)",
                            (id_article, "  "))
        self.connect.commit()

    def read_text_article(self, id_article):
        self.cursor.execute(f"SELECT * FROM names_of_articles_and_their_text WHERE id_article={id_article}")
        return self.cursor.fetchall()[0][1]

    def delete_article(self, id_article):
        self.cursor.execute(f"DELETE FROM names_of_articles_and_their_text WHERE id_article={id_article}")
        self.connect.commit()
        self.cursor.execute(f"DELETE FROM names_of_articles_with_id_chapters WHERE id={id_article}")
        self.connect.commit()

    def delete_chapter(self, id_chapter):
        """table"""
        """names_of_chapters(id INTEGER PRIMARY KEY AUTOINCREMENT, name_chapter)"""
        """names_of_articles_with_id_chapters(id_chapter, name_article, id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        """names_of_articles_and_their_text(id_article, text_article)"""
        count_articles_in_chapter = self.return_count_articles(id_chapter=id_chapter)

        self.cursor.execute(f"DELETE FROM names_of_chapters WHERE id={id_chapter}")
        self.connect.commit()
        if count_articles_in_chapter > 0:
            id_articles = self.cursor.execute(f"SELECT * FROM names_of_articles_with_id_chapters "
                                              f"WHERE id_chapter={id_chapter}")
            list_only_article = [x[2] for x in id_articles]
            self.cursor.execute(f"DELETE FROM names_of_articles_with_id_chapters WHERE id_chapter={id_chapter}")
            self.connect.commit()
            for y in list_only_article:
                self.cursor.execute(f"DELETE FROM names_of_articles_and_their_text WHERE id_article={y}")
                self.connect.commit()

    def rename_article(self, old_name, new_name):
        self.cursor.execute(f"UPDATE names_of_articles_with_id_chapters SET name_article='{new_name}'"
                            f"WHERE name_article='{old_name}'")
        self.connect.commit()

    def close_connect(self):
        self.cursor.close()
        self.connect.close()


# class Operation:
#     def __init__(self):
#         self.conn = sqlite3.connect("database_for_synopsis.db")
#         self.cursor = self.conn.cursor()
#
#     def create_table(self):
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS names_of_chapters(id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                             "name_chapter TEXT)")
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS names_of_articles_with_id_chapters(id_chapter INTEGER, "
#                             "name_article TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)")
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS names_of_articles_and_their_text(id_article INTEGER, "
#                             "text_article TEXT)")
#
#     def show_table(self, name_table):
#         self.cursor.execute(f"SELECT * FROM {name_table}")
#         pprint.pprint(self.cursor.fetchall())
#
#     def remove_any_table(self, name_table):
#         self.cursor.execute(f"DROP TABLE {name_table}")
#
#     def close_connection(self):
#         self.cursor.close()
#         self.conn.close()


# ert = Operation()
# ert.show_table(name_table="names_of_articles_with_id_chapters")
# ert.show_table(name_table="names_of_articles_and_their_text")
# ert.close_connection()




