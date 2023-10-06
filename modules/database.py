import sqlite3


class DataBase:
    def __init__(self):
        self._con = sqlite3.connect("db.db")
        self._cur = self._con.cursor()

        self._create_table()

    def _create_table(self) -> None:
        """
        Creating default tables in the database
        """

        self._cur.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, "
                          "content TEXT)")

    def add_note_db(self, title: str, content: str) -> None:
        """
        Adding a note to the database

        :param title: Title note
        :param content: Content note
        """

        self._cur.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        self._con.commit()

    def get_notes_db(self) -> list:
        """
        Get all notes from the database
        """

        self._cur.execute("SELECT * from notes")
        return self._cur.fetchall()

    def get_note_db(self, id_: int) -> list:
        """
        Get note by ID from the database

        :param id_: ID note
        """

        self._cur.execute("SELECT * FROM notes WHERE id = ?", (id_, ))
        return self._cur.fetchone()

    def del_note_db(self, id_: int) -> None:
        """
        Delete a note by ID from the database

        :param id_: ID note
        """

        self._cur.execute("DELETE FROM notes WHERE id = ?", (id_, ))
        self._con.commit()

    def find_note_db(self, word: str) -> list:
        """
        Search for a note by keyword from the database

        :param word: keyword
        """

        args = (f'%{word.lower()}%', f'%{word.lower()}%',)
        self._cur.execute("SELECT * FROM notes WHERE LOWER(title) LIKE ? OR LOWER(content) LIKE ?", args)
        return self._cur.fetchall()
