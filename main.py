from caesarCryptograph import CaesarCryptograph
from gronsfeldCryptograph import GronsfeldCryptograph
from tritemiusCryptograph import TritemiusCryptographer
import tkinter as tk
import pyperclip

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        def encrypt(event):
            textbox2.delete('1.0', 'end')
            x = ''
            variable = var.get()

            key = entry.get()
            text = textbox1.get('1.0', 'end')
            if variable == 1:
                x = CaesarCryptograph.encrypt(text, key)
            elif variable == 2:
                x = GronsfeldCryptograph.encrypt(text, key)
            elif variable == 3:
                x = TritemiusCryptographer.encrypt(text, key)
            if x != '':
                textbox2.insert('1.0', x)

        def decrypt(event):
            textbox2.delete('1.0', 'end')
            x = ''
            variable = var.get()

            key = entry.get()
            text = textbox1.get('1.0', 'end')
            if variable == 1:
                x = CaesarCryptograph.decrypt(text, key)
            elif variable == 2:
                x = GronsfeldCryptograph.decrypt(text, key)
            elif variable == 3:
                x = TritemiusCryptographer.decrypt(text, key)
            if x != '':
                textbox2.insert('1.0', x)

        def copy1(event):
            pyperclip.copy(textbox1.get('1.0', 'end'))

        def copy2(event):
            pyperclip.copy(textbox2.get('1.0', 'end'))

        def paste(event):
            copied_text = pyperclip.paste()
            if textbox1.get('1.0', 'end') != '':
                textbox1.delete('1.0', 'end')
            textbox1.insert('1.0', copied_text)

        frame1 = tk.Frame(root, bg='white')
        frame2 = tk.Frame(root, bg='white')
        frame3 = tk.Frame(root, bg='white')

        textbox1 = tk.Text(frame2, font='Arial 14', bd=2, wrap='word')
        textbox2 = tk.Text(frame3, font='Arial 14', bd=2, wrap='word')

        label1 = tk.Label(frame2, font='Arial 10', text='Введите ваше сообщение:', bg='white')
        label2 = tk.Label(frame3, font='Arial 10', text='(Рас/За)шифрованное сообщение:', bg='white')
        label3 = tk.Label(frame1, font='Arial 10', text='Код/функция:', bg='white')

        btn = tk.Button(frame3, text='Зашифровать', font='Arial 10', bd=2)
        btn2 = tk.Button(frame3, text='Расшифровать', font='Arial 10', bd=2)
        btn3 = tk.Button(frame2, text='Скопировать', font='Arial 10', bd=2)
        btn4 = tk.Button(frame2, text='Вставить', font='Arial 10', bd=2)
        btn5 = tk.Button(frame3, text='Скопировать', font='Arial 10', bd=2)

        entry = tk.Entry(frame1, font='Arial 10', bd=2)

        var = tk.IntVar()
        var.set(1)

        rbut1 = tk.Radiobutton(frame1, text='шифр Цезаря', font='Arial 12', variable=var, value=1, bg='white')
        rbut2 = tk.Radiobutton(frame1, text='шифр Гронсфельда', font='Arial 12', variable=var, value=2, bg='white')
        rbut3 = tk.Radiobutton(frame1, text='шифр Тридемиуса', font='Arial 12', variable=var, value=3, bg='white')

        rbut1.place(x=10, y=40)
        rbut2.place(x=10, y=80)
        rbut3.place(x=10, y=120)

        frame1.place(x=200, y=100, anchor="c", height=200, width=400)
        frame2.place(x=200, y=300, anchor="c", height=200, width=400)
        frame3.place(x=200, y=500, anchor="c", height=200, width=400)

        entry.place(x=110, y=160, height=23, width=100)
        label3.place(x=10, y=160, height=23, width=100)

        textbox1.place(x=200, y=100, anchor="c", height=100, width=300)
        label1.place(x=33, y=25, height=20, width=200)
        textbox2.place(x=200, y=100, anchor="c", height=100, width=300)
        label2.place(x=37, y=25, height=20, width=210)

        btn.place(x=180, y=160, height=30, width=100)
        btn.bind('<Button-1>', encrypt)
        btn2.place(x=290, y=160, height=30, width=100)
        btn2.bind('<Button-1>', decrypt)
        btn3.place(x=290, y=160, height=30, width=100)
        btn3.bind('<Button-1>', copy1)
        btn4.place(x=180, y=160, height=30, width=100)
        btn4.bind('<Button-1>', paste)
        btn5.place(x=70, y=160, height=30, width=100)
        btn5.bind('<Button-1>', copy2)



if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Cryptographer')
    root.geometry('400x600')
    root.resizable(False, False)
    root.mainloop()

