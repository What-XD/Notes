from rgbprint import gradient_print, Color
import os

class Messages:
    def __init__(self):
        self.commands_list = [
            {"title": "Открыть заметки", "function": self.list_note},
            {"title": "Создать заметку", "function": self.create_note},
            {"title": "Удалить заметку", "function": self.del_note},
            {"title": "Найти заметку", "function": self.find_note},
            {"title": "Выйти", "function": exit},
        ]

    def print_logo(self) -> None:
        """
        Displays the logo on the screen
        """

        gradient_print(""" /$$   /$$             /$$              
| $$$ | $$            | $$              
| $$$$| $$  /$$$$$$  /$$$$$$    /$$$$$$ 
| $$ $$ $$ /$$__  $$|_  $$_/   /$$__  $$
| $$  $$$$| $$  \\ $$  | $$    | $$$$$$$$
| $$\\  $$$| $$  | $$  | $$ /$$| $$_____/
| $$ \\  $$|  $$$$$$/  |  $$$$/|  $$$$$$$
|__/  \\__/ \\______/    \\___/   \\_______/""", start_color="#00c6ff", end_color="#0072ff", end="\n\n")

    def open_menu(self) -> None:
        """
        Opens the menu (The data is taken from the variable self.commands_list)
        """

        self.print_logo()

        # Output all functions
        for count, value in enumerate(self.commands_list, 1):
            print(f"[{Color.red}{count}{Color.reset}] {value['title']}")

        user_resp = input("> ")

        if not user_resp.isnumeric():
            self.print_error("Вы ввели не число!")
        else:
            user_resp = int(user_resp)
            if user_resp > len(self.commands_list) or user_resp <= 0:
                self.print_error("Этот параметр не подходит!")

        # Execute the function
        self.clear_console()
        self.commands_list[user_resp - 1]['function']()

    def print_error(self, text: str, exit_: bool = True) -> None:
        """
        Displays the error on the screen

        :param text: Text message
        :param exit_: Go to the menu?
        """
        
        print(f"\n[{Color.red}ОШИБКА{Color.reset}] {text}")

        if exit_:
            input(f"\n{Color.orange}Нажмите пробел что-бы вернуться в меню{Color.reset}")
            self.start()

    def print_success(self, text: str) -> None:
        """
        Display a successful message

        :param text: Text message
        """

        print(f"\n[{Color.green}УСПЕХ{Color.reset}] {text}")

    def print_notes(self, notes: list) -> None:
        """
        Display all notes on the screen

        :param notes: Notes from the database
        """

        for note in notes:
            print(f"""{Color.gold}#{note[0]}
{Color.aqua}Заголовок: {Color.reset}{note[1]}
{Color.aqua}Содержание: {Color.reset}{note[2]}\n\n""")

    def clear_console(self) -> None:
        """
        Clears the screen
        """

        os.system("cls")
