'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/09/01
Ending 2022/11/05

'''
from tkinter import *
from tkinter import messagebox as mb
class Sezar(Frame):
    LETTERS = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, pencere):
        Frame.__init__(self, pencere)
        self.pencere = pencere
        Label(pencere, text="Шифр Цезаря",  width=20, background="#008000",font='Arial 16 italic').place(x=200, y=30)
        Label(pencere, text="Введите сообщение: ",  width=20, background="#008000",font='Arial 16 italic').place(x=50, y=130)
        self.Ent1 = Entry(pencere, width=30)
        self.Ent1.place(x=300, y=130)
        Label(pencere, text="Введите ключ: ", width=20, background="#008000", font='Arial 16 italic').place(x=20, y=190)
        self.Ent2 = Entry(pencere, width=30)
        self.Ent2.place(x=300, y=190)
        Button(pencere, text="Зашифровать",  command=self.Encrypt,background='#DAA520').place(x=220, y=250)
        Button(pencere, text="Расшифровать", command=self.Decrypt, background='#DAA520').place(x=350, y=250)
        Label(pencere, text= "Результат:", background="#008000",font='Arial 16 italic').place(x=100, y=300)
        self.RESULT = Entry(pencere, width=30)
        self.RESULT.place(x=270, y=300)
# Функция кнопки "Зашифровать"
    def Encrypt(self):
        key = int(self.Ent2.get())
        length = len(self.LETTERS)

        translation = ''

        for character in self.Ent1.get():
            if character.lower() in self.LETTERS:
                sayı = self.LETTERS.find(character.lower())
                sayı = (sayı + key) % length
                translation += self.LETTERS[sayı]
            else:
                translation += character

        self.RESULT.delete(0, END)
        self.RESULT.insert(0, translation)
# Функция кнопки "Расшифровать"
    def Decrypt(self):
        key = int(self.Ent2.get())
        length = len(self.LETTERS)

        translation = ''

        for character in self.Ent1.get():
            if character.lower() in self.LETTERS:
                sayı = self.LETTERS.find(character.lower())
                sayı = (sayı - key) % length
                translation += self.LETTERS[sayı]
            else:
                translation += character

        self.RESULT.delete(0, END)
        self.RESULT.insert(0, translation)

if __name__ == "__main__":
   # Создание главного окна
    root = Tk()
    root.title("Шифр Цезаря")
    root["bg"]="#008000"
    root.geometry("600x500")
    root.resizable(width=False, height=False)
    Sezar(root).pack(side="top", fill="both")

def show_info():
    mb.showinfo("О программе", "Феткулин Григорий - Шифр Цезаря, 2022")
main_menu = Menu()
file_menu = Menu()
about_menu = Menu()
about_menu.add_command(label="О программе", command=show_info)
main_menu.add_cascade(label="Справка", menu=about_menu)
root.config(menu=main_menu)
root.mainloop()
