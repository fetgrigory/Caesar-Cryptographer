from tkinter import Tk, Frame, Label, Entry, Button, Menu, END, messagebox as mb


class BaseWindow(Frame):
    """AI is creating summary for BaseWindow

    Args:
        Frame ([type]): [description]
    """
    def __init__(self, master, title, bg_color, geo):
        # Initialize the base frame and configure the window's basic properties
        super().__init__(master)
        self.master = master
        self.master.title(title)
        self.master.configure(bg=bg_color)
        self.master.geometry(geo)
        self.master.resizable(width=False, height=False)


class CipherApp(BaseWindow):
    """AI is creating summary for CipherApp

    Args:
        BaseWindow ([type]): [description]
    """
    def __init__(self, master):
        # Initialize the main application window with custom settings
        super().__init__(master, "Шифр Цезаря", "#008000", "600x500")
        self.create_widgets()

    def create_widgets(self):
        """AI is creating summary for create_widgets
        """
        # Create and place labels, entries, and buttons for Caesar cipher functionality
        Label(
            self.master,
            text="Шифр Цезаря",
            width=20,
            background="#008000",
            font="Arial 16 italic",
        ).place(x=200, y=30)

        Label(
            self.master,
            text="Введите сообщение: ",
            width=20,
            background="#008000",
            font="Arial 16 italic",
        ).place(x=50, y=130)

        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=130)
        Label(
            self.master,
            text="Введите ключ: ",
            width=20,
            background="#008000",
            font="Arial 16 italic",
        ).place(x=20, y=190)
        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=190)
        Button(
            self.master,
            text="Зашифровать",
            command=self.encrypt,
            background="#DAA520"
        ).place(x=220, y=250)
        Button(
            self.master,
            text="Расшифровать",
            command=self.decrypt,
            background="#DAA520"
        ).place(x=350, y=250)
        Label(
            self.master,
            text="Результат:",
            background="#008000",
            font="Arial 16 italic"
        ).place(x=100, y=300)
        self.result = Entry(self.master, width=30)
        self.result.place(x=270, y=300)

    def encrypt(self):
        """AI is creating summary for encrypt
        """
        # Encrypt the message using the Caesar cipher
        key = int(self.ent2.get())
        # Get the length of the letters used for encryption
        length = len(Sezar.LETTERS)
        translation = ""
        for character in self.ent1.get():
            if character.lower() in Sezar.LETTERS:
                # Find the character's position in the LETTERS and shift it by the key
                sayı = Sezar.LETTERS.find(character.lower())
                sayı = (sayı + key) % length
                translation += Sezar.LETTERS[sayı]
            else:
                # If character is not in LETTERS, keep it unchanged
                translation += character

        # Display the encrypted result
        self.result.delete(0, END)
        self.result.insert(0, translation)

    def decrypt(self):
        """AI is creating summary for decrypt
        """
        # Decrypt the message using the Caesar cipher
        key = int(self.ent2.get())
        # Get the length of the letters used for decryption
        length = len(Sezar.LETTERS)
        translation = ""
        for character in self.ent1.get():
            if character.lower() in Sezar.LETTERS:
                # Find the character's position in the LETTERS and reverse shift it by the key
                sayı = Sezar.LETTERS.find(character.lower())
                sayı = (sayı - key) % length
                translation += Sezar.LETTERS[sayı]
            else:
                # If character is not in LETTERS, keep it unchanged
                translation += character

        # Display the decrypted result
        self.result.delete(0, END)
        self.result.insert(0, translation)


class Sezar:
    """AI is creating summary for
    """
    # Russian alphabet for Caesar cipher
    LETTERS = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def show_info():
    """AI is creating summary for show_info
    """
    # Display information about the program and its author
    mb.showinfo("О программе", "Феткулин Григорий - Шифр Цезаря, 2022")


if __name__ == "__main__":
    root = Tk()
    app = CipherApp(root)
    app.pack(side="top", fill="both")

    # Create a menu with information about the program
    main_menu = Menu()
    about_menu = Menu()
    about_menu.add_command(label="О программе", command=show_info)
    main_menu.add_cascade(label="Справка", menu=about_menu)
    root.config(menu=main_menu)

    # Run the main application loop
    root.mainloop()
