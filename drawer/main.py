import tkinter as tk
from tkinter import colorchooser
from PIL import Image


class Drawer:
    """
    Desenhador
    """

    def __init__(self):
        """
        Construtor.
        """

        self.window = tk.Tk()
        self.window.title("Pinterest")
        self.window.minsize(width=1280, height=720)
        self.window.resizable(0, 0)

        bar_menu = tk.Frame(
            self.window,
            background="#3b3b3b",
            height=50
        )
        bar_menu.pack(fill="x")

        tk.Label(
            bar_menu,
            text="  Cores:  ",
            background="#3b3b3b",
            foreground="white"
        ).pack(side="left")

        colors = ("black", "gray", "white", "red", "green", "blue", "purple", "orange", "yellow")
        for color in colors:
            tk.Button(
                bar_menu,
                background=color,
                width=3,
                height=2,
                command=lambda param=color: self.__select_colors(color=param)
            ).pack(side="left")

        tk.Label(bar_menu, text="  Cor:  ", foreground="white", background="#3b3b3b").pack(side="left")
        square_img = tk.PhotoImage(file="drawer/icons/square.png")
        tk.Button(
            bar_menu,
            border=0,
            image=square_img,
            command=self.__chooser_color
        ).pack(side="left")

        tk.Label(
            bar_menu,
            text=" Tamanho: ",
            foreground="white",
            background="#3b3b3b"
        ).pack(side="left")

        self.pen_size = tk.Spinbox(
            bar_menu,
            from_=5,
            to=50
        )
        self.pen_size.pack(side="left")

        self.pick_colors = "black"
        self.pick_brush = "oval"

        tk.Label(
            bar_menu,
            text="Pinceis:  ",
            background="#3b3b3b",
            foreground="white"
        ).pack(side="left")

        line_img = tk.PhotoImage(file="drawer/icons/line.png")
        tk.Button(
            bar_menu,
            image=line_img,
            border=0,
            height=40,
            width=40,
            command=lambda: self.__select_brush("line")
        ).pack(side="left")

        oval_img = tk.PhotoImage(file="drawer/icons/oval.png")
        tk.Button(
            bar_menu,
            image=oval_img,
            border=0,
            height=40,
            width=40,
            command=lambda: self.__select_brush("oval")
        ).pack(side="left")

        tk.Button(
            bar_menu,
            image=square_img,
            border=0,
            height=40,
            width=40,
            command=lambda: self.__select_brush("square")
        ).pack(side="left")

        erase_img = tk.PhotoImage(file="drawer/icons/eraser.png")
        tk.Button(
            bar_menu,
            image=erase_img,
            border=0,
            height=40,
            width=40,
            command=lambda: self.__select_brush("erase")
        ).pack(side="left")

        tk.Label(
            bar_menu,
            text=" Opções: ",
            foreground="white",
            background="#3b3b3b"
        ).pack(side="left")

        save_img = tk.PhotoImage(file="drawer/icons/save.png")
        tk.Button(
            bar_menu,
            image=save_img,
            border=0,
            height=40,
            width=40,
            command=self.__save
        ).pack(side="left")

        new_img = tk.PhotoImage(file="drawer/icons/new.png")
        tk.Button(
            bar_menu,
            image=new_img,
            border=0,
            height=40,
            width=40,
            command=self.__clean
        ).pack(side="left")

        self.area_drawer = tk.Canvas(
            self.window,
            height=720,
            background="gainsboro"
        )
        self.area_drawer.pack(fill="both")
        # Evento de movimentar o mouse
        self.area_drawer.bind("<B1-Motion>", self.__draw)
        # Adicionar atalhos
        self.window.bind("<Escape>", self.__clean)
        self.window.bind("<Return>", self.__save)

        self.window.mainloop()

    def __draw(self, event: tk.Event) -> None:
        """
        Realiza o desenho a partir do movimento do mouse.
        """

        x0, y0 = event.x, event.y
        x1, y1 = event.x, event.y

        if self.pick_brush == "oval":
            self.area_drawer.create_oval(
                x0, y0, x1, y1,
                fill=self.pick_colors,
                outline=self.pick_colors,
                width=self.pen_size.get()
            )
        elif self.pick_brush == "line":
            self.area_drawer.create_line(
                x0 - 5, y0 - 5, x1, y1,
                fill=self.pick_colors,
                width=self.pen_size.get()
            )
        elif self.pick_brush == "square":
            self.area_drawer.create_rectangle(
                x0, y0, x1, y1,
                fill=self.pick_colors,
                outline=self.pick_colors,
                width=self.pen_size.get()
            )
        else:
            # Apagar
            self.area_drawer.create_oval(
                x0, y0, x1, y1,
                fill="gainsboro",
                outline="gainsboro",
                width=self.pen_size.get()
            )

    def __select_colors(self, color: str) -> None:
        """
        Seleciona a cor.
        """

        self.pick_colors = color

    def __chooser_color(self):
        """
        Seleciona a cor da paleta de cores
        """

        color = colorchooser.askcolor()
        self.pick_colors = color[1]

    def __select_brush(self, brush: str) -> None:
        """
        Seleciona o tipo de pincel.
        """

        self.pick_brush = brush

    def __clean(self, event: tk.Event = None):
        """
        Limpar tela
        """

        self.area_drawer.delete("all")

    def __save(self, event: tk.Event = None):
        """
        Salva a imagem do desenho, para funcionar precisa instalar
        sudo apt-get install ghostscript
        """

        self.area_drawer.postscript(file="drawer/desenho.eps")
        img = Image.open("drawer/desenho.eps")
        img.save("drawer/desenho.png", "png")


if __name__ == '__main__':
    Drawer()
