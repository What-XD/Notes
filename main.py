from modules import DataBase, Messages
from rgbprint import Color


class Note(DataBase, Messages):
    def __init__(self):
        super().__init__()
        Messages.__init__(self)

    def create_note(self) -> None:
        """
        Create a note
        """

        title = input("Введите заголовок заметки: ")
        context = input("Введите содержимое заметки: ")

        self.add_note_db(title, context)
        self.print_success("Заметка успешно создана!")

    def list_note(self) -> None:
        """
        Get a list of notes
        """

        notes = self.get_notes_db()

        if len(notes) == 0:
            self.print_error("У вас нет заметок!")

        self.print_notes(notes)

    def del_note(self) -> None:
        """
        Delete the note
        """

        note_id = input("Введите ID заметки которую хотите удалить: ")

        if not note_id.isnumeric():
            self.print_error("Вы ввели не число!")

        if self.get_note_db(int(note_id)):
            self.del_note_db(int(note_id))
            self.print_success("Заметка успешно удалена!")
        else:
            self.print_error("Такой заметки нет!")

    def find_note(self) -> None:
        """
        Find a note
        """

        word = input("Введите фразу или слово для поиска: ")

        notes = self.find_note_db(word)

        if len(notes) == 0:
            self.print_error("Заметки не найдены!")

        self.print_notes(notes)

    def start(self) -> None:
        """
        Start program
        """

        while True:
            self.clear_console()
            self.open_menu()
            input(f"\n{Color.orange}Нажмите пробел что-бы вернуться в меню{Color.reset}")


if __name__ == '__main__':
    note = Note()
    note.start()
