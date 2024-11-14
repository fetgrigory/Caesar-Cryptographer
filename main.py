from tkinter import Tk, Frame, Label, Entry, Button, Menu, messagebox as mb


class BaseWindow(Frame):
    """AI is creating summary for BaseWindow

    Args:
        Frame ([type]): [description]
    """
    def __init__(self, master, title, bg_color, geo):
        super().__init__(master)
        self.master = master
        # Set the window's title, background color, and geometry.
        self.master.title(title)
        self.master.configure(bg=bg_color)
        self.master.geometry(geo)
        # Disable resizing of the window.
        self.master.resizable(width=False, height=False)
        # Pack the frame to fill the parent.
        self.pack(side="top", fill="both")


class ConfigurationMixin:
    """AI is creating summary for
    """
    def __init__(self, title, bg_color, geo):
        self.title = title
        self.bg_color = bg_color
        self.geometry = geo

    def configure_window(self, master):
        """AI is creating summary for configure_window

        Args:
            master ([type]): [description]
        """
        # Apply configuration settings to the given master window.
        master.title(self.title)
        master.configure(bg=self.bg_color)
        master.geometry(self.geometry)
        master.resizable(width=False, height=False)


class CipherBase(BaseWindow, ConfigurationMixin):
    """AI is creating summary for CipherBase

    Args:
        BaseWindow ([type]): [description]
        ConfigurationMixin ([type]): [description]
    """
    def __init__(self, master, title, bg_color, geo):
        ConfigurationMixin.__init__(self, title, bg_color, geo)
        # Initialize the base window with given parameters.
        super().__init__(master, title, bg_color, geo)
        self.configure_window(master)


class CaesarCipherMixin:
    """AI is creating summary for

    Returns:
        [type]: [description]
    """
    # Russian alphabet used in cipher.
    LETTERS = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

    def caesar_cipher(self, message, key, encrypt=True):
        """AI is creating summary for caesar_cipher

        Args:
            message ([type]): [description]
            key ([type]): [description]
            encrypt (bool, optional): [description]. Defaults to True.

        Returns:
            [type]: [description]
        """
        translation = ""
        length = len(self.LETTERS)
        shift = key if encrypt else -key

        for character in message:
            # Check if character is in the defined alphabet.
            if character.lower() in self.LETTERS:
                index = self.LETTERS.find(character.lower())
                index = (index + shift) % length
                translation += self.LETTERS[index]
            else:
                # Leave non-alphabetic characters unchanged.
                translation += character

        return translation


class CipherApp(CipherBase, CaesarCipherMixin):
    """Main application class for the Caesar cipher."""

    def __init__(self, master):
        # Set up the main application window with title, background color, and size.
        super().__init__(master, "Шифр Цезаря", "#008000", "600x500")
        self.create_widgets()

    def create_widgets(self):
        """Create and position widgets in the application window."""
        # Title label.
        Label(
            self.master,
            text="Шифр Цезаря",
            width=20,
            background="#008000",
            font="Arial 16 italic",
        ).place(x=200, y=30)

        # Label and entry for message input.
        Label(
            self.master,
            text="Введите сообщение: ",
            width=20,
            background="#008000",
            font="Arial 16 italic",
        ).place(x=50, y=130)

        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=130)
        # Label and entry for key input.
        Label(
            self.master,
            text="Введите ключ: ",
            width=20,
            background="#008000",
            font="Arial 16 italic",
        ).place(x=20, y=190)

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=190)

        # Button for encrypting the message.
        Button(
            self.master,
            text="Зашифровать",
            command=self.encrypt,
            background="#DAA520"
        ).place(x=220, y=250)

        # Button for decrypting the message.
        Button(
            self.master,
            text="Расшифровать",
            command=self.decrypt,
            background="#DAA520"
        ).place(x=350, y=250)

        # Result label and display field.
        Label(
            self.master,
            text="Результат:",
            background="#008000",
            font="Arial 16 italic"
        ).place(x=100, y=300)

        self.result = Entry(self.master, width=30)
        self.result.place(x=270, y=300)

    def encrypt(self):
        """Encrypt and display the result."""
        try:
            # Get the key value and message, perform encryption.
            key = int(self.ent2.get())
            message = self.ent1.get()
            encrypted_message = self.caesar_cipher(message, key, encrypt=True)
            # Display the encrypted message in the result entry.
            self.result.delete(0, "end")
            self.result.insert(0, encrypted_message)
        except ValueError:
            # Show error if key is not a number.
            mb.showerror("Ошибка", "Ключ должен быть числом")

    def decrypt(self):
        """Decrypt and display the result."""
        try:
            # Get the key value and message, perform decryption.
            key = int(self.ent2.get())
            message = self.ent1.get()
            decrypted_message = self.caesar_cipher(message, key, encrypt=False)
            # Display the decrypted message in the result entry.
            self.result.delete(0, "end")
            self.result.insert(0, decrypted_message)
        except ValueError:
            # Show error if key is not a number.
            mb.showerror("Ошибка", "Ключ должен быть числом")


def show_info():
    """Display info about the program."""
    mb.showinfo("О программе", "Феткулин Григорий - Шифр Цезаря, 2022")


if __name__ == "__main__":
    root = Tk()
    app = CipherApp(root)

    # Create a menu with information about the program.
    main_menu = Menu(root)
    about_menu = Menu(main_menu, tearoff=0)
    about_menu.add_command(label="О программе", command=show_info)
    main_menu.add_cascade(label="Справка", menu=about_menu)
    root.config(menu=main_menu)

    # Run the main application loop.
    root.mainloop()
