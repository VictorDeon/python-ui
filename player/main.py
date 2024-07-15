import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Frame, Button, Scale
from ttkthemes import ThemedTk
import os


class Player:
    """
    Faz download de qualquer video do youtube.
    """

    def __init__(self):
        """
        Construtor.
        """

        self.window = ThemedTk(theme="black")
        self.window.title("Music Player")
        self.window.resizable(0, 0)
        # Inicializar a janela mais para o meio
        self.window.geometry("300x430+800+200")
        self.window.config(background="#444444")

        add_img = tk.PhotoImage(file="player/add.png")
        next_img = tk.PhotoImage(file="player/next.png")
        pause_img = tk.PhotoImage(file="player/pause.png")
        play_img = tk.PhotoImage(file="player/play.png")
        previous_img = tk.PhotoImage(file="player/previous.png")
        remove_img = tk.PhotoImage(file="player/remove.png")

        self.list = tk.Listbox(self.window, background="#333333", height=13, foreground="white")
        self.list.pack(fill="x", padx=10, pady=10)

        btn_frame = Frame(self.window)
        btn_frame.pack(pady=10)

        Button(
            btn_frame,
            image=remove_img,
            command=self.__remove_music
        ).grid(row=0, column=0, padx=10)

        Button(
            btn_frame,
            image=add_img,
            command=self.__select_music
        ).grid(row=0, column=1, padx=10)

        bigger_btn_frame = Frame(self.window)
        bigger_btn_frame.pack(pady=10)

        Button(
            bigger_btn_frame,
            image=previous_img,
            command=None
        ).grid(row=0, column=0)

        Button(
            bigger_btn_frame,
            image=play_img,
            command=None
        ).grid(row=0, column=1)

        Button(
            bigger_btn_frame,
            image=next_img,
            command=None
        ).grid(row=0, column=2)

        Scale(self.window).pack(fill="x", padx=10)

        self.window.mainloop()

    def __select_music(self):
        """
        Seleciona a musica.
        """

        folder = filedialog.askdirectory()
        files = os.listdir(folder)
        for file in files:
            self.list.insert(tk.END, str(file))

    def __remove_music(self):
        """
        Removendo item da lista.
        """

        self.list.delete(tk.ANCHOR)


if __name__ == '__main__':
    Player()
