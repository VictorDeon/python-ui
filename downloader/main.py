import tkinter as tk
from tkinter import filedialog
import youtube_dl
import os


class Downloader:
    """
    Faz download de qualquer video do youtube.
    """

    def __init__(self):
        """
        Construtor.
        """

        self.window = tk.Tk()
        self.window.title("Youtube Downloader")
        self.window.resizable(0, 0)
        # Inicializar a janela mais para o meio
        self.window.geometry("1280x720+300+200")

        img_logo = tk.PhotoImage(file='downloader/youtube.png')
        img_audio = tk.PhotoImage(file='downloader/audio.png')
        img_video = tk.PhotoImage(file='downloader/video.png')
        img_audio_video = tk.PhotoImage(file='downloader/audio-video.png')

        frame = tk.Frame(self.window, background="#3b3b3b", pady=80)
        frame.pack(fill="x")

        tk.Label(frame, image=img_logo, background="#3b3b3b").pack()

        entry_frame = tk.Frame(self.window, pady=20)
        entry_frame.pack()

        tk.Label(entry_frame, text="  Insira o link do youtube:  ", font="Arial 12").pack(side="left")
        link = tk.Entry(entry_frame, font="Arial 20", width=50)
        link.pack(side="left")
        tk.Button(
            entry_frame,
            background="red",
            text=">",
            width=3,
            height=2,
            border=0,
            foreground="white",
            command=lambda: self.__download(link.get())
        ).pack(side="left")

        btn_frame = tk.Frame(self.window)
        btn_frame.pack()

        self.audio = False
        self.video = False

        tk.Radiobutton(
            btn_frame,
            image=img_audio,
            value=0,
            command=self.__validate_audio
        ).pack(side="left")

        tk.Radiobutton(
            btn_frame,
            image=img_video,
            value=1,
            command=self.__validate_video
        ).pack(side="left")

        tk.Radiobutton(
            btn_frame,
            image=img_audio_video,
            value=2,
            command=self.__validate_all
        ).pack(side="left")

        self.window.mainloop()

    def __validate_audio(self):
        """
        Valida se vai baixar o audio
        """

        self.audio = True
        self.video = False

    def __validate_video(self):
        """
        Valida se vai baixar o video
        """

        self.audio = False
        self.video = True

    def __validate_all(self):
        """
        Quero baixar tudo.
        """

        self.audio = True
        self.video = True

    def __download(self, link):
        """
        Realiza o download do video.        
        """

        folder = filedialog.askdirectory()
        print(folder)

        os.system("youtube-dl " + str(link))  # Faz download do video.
        self.__complete()

    def __msn(self):
        window = tk.Toplevel()
        window.title('E R R O')
        window.resizable(0, 0)
        window.geometry('300x200')

        text = tk.Label(window, text='O Link não é válido', font='arial 20 bold', pady=30)
        text.pack()

        button_exit = tk.Button(window, text='OK', bg='lightblue', command=window.destroy)
        button_exit.pack()

    def __complete(self):
        window = tk.Toplevel()
        window.title('Efetuado')
        window.resizable(0, 0)
        window.geometry('300x200')
 
        text = tk.Label(window, text='Download Efetuado', pady=30)
        text.pack()

        button_exit = tk.Button(window, text='OK', command=window.destroy)
        button_exit.pack()


if __name__ == '__main__':
    Downloader()
