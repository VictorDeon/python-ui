import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Frame, Button, Scale, Label
from ttkthemes import ThemedTk
import pygame
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

        pygame.mixer.init()
        self.music_folder = ""

        add_img = tk.PhotoImage(file="player/add.png")
        next_img = tk.PhotoImage(file="player/next.png")
        self.pause_img = tk.PhotoImage(file="player/pause.png")
        self.play_img = tk.PhotoImage(file="player/play.png")
        previous_img = tk.PhotoImage(file="player/previous.png")
        remove_img = tk.PhotoImage(file="player/remove.png")

        self.playing = False

        self.list = tk.Listbox(
            self.window,
            background="#333333",
            height=13,
            foreground="white"
        )
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
            command=self.__previous_music
        ).grid(row=0, column=0)

        self.play_btn = Button(
            bigger_btn_frame,
            image=self.play_img,
            command=self.__play_music
        )
        self.play_btn.grid(row=0, column=1)

        Button(
            bigger_btn_frame,
            image=next_img,
            command=self.__next_music
        ).grid(row=0, column=2)

        self.volume = Scale(self.window, from_=0, to=1, command=self.__config_volume)
        self.volume.pack(fill="x", padx=10)

        self.window.mainloop()

    def __select_music(self):
        """
        Seleciona a musica.
        """

        folder = filedialog.askdirectory()
        self.music_folder = folder
        files = os.listdir(folder)
        for file in files:
            self.list.insert(tk.END, str(file))

    def __remove_music(self):
        """
        Removendo item da lista.
        """

        self.list.delete(tk.ANCHOR)

    def __next_music(self):
        """
        Passar para a próxima musica.
        """

        try:
            music_index = self.list.curselection()[0]
            next_music_index = music_index + 1
            self.list.select_clear(0, tk.END)
            self.list.activate(next_music_index)
            self.list.select_set(next_music_index)
            self.list.yview(next_music_index)
        except Exception as error:
            print(str(error))
            self.__error_window("Não existe músicas para avançar.")

    def __previous_music(self):
        """
        Volta para a música anterior.
        """

        try:
            music_index = self.list.curselection()[0]
            previous_music_index = music_index - 1
            self.list.select_clear(0, tk.END)
            self.list.activate(previous_music_index)
            self.list.select_set(previous_music_index)
            self.list.yview(previous_music_index)
        except Exception as e:
            print(str(e))
            self.__error_window("Não existe músicas para voltar.")

    def __play_music(self):
        """
        Toca a música.
        """

        try:
            if self.playing:
                pygame.mixer.music.pause()
                self.play_btn.config(image=self.play_img)
                self.playing = False
            else:
                music_path = str(self.music_folder) + "/" + str(self.list.get(tk.ANCHOR))
                print(music_path)
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play()
                self.play_btn.config(image=self.pause_img)
                self.playing = True
        except Exception as error:
            print(str(error))
            self.__error_window("Não foi selecionada nenhuma música para execução.")

    def __config_volume(self, *args, **kwargs):
        """
        Configura o volume da musica.
        """

        pygame.mixer.music.set_volume(self.volume.get())

    def __error_window(self, message: str) -> None:
        """
        Janela de notificação de error.
        """

        window = tk.Toplevel()
        window.title("Error")
        window.geometry("300x300+300+300")
        window.resizable(0, 0)
        window.config(bg="#444444")

        Label(window, text=str(message)).pack(expand=tk.YES)
        Button(window, text="OK", command=window.destroy).pack(pady=10)


if __name__ == '__main__':
    Player()
