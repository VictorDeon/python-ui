import tkinter as tk


class Calculator:
    """
    Calculadora.
    """

    def __init__(self):
        """
        Construtor.
        """

        self.window = tk.Tk()
        self.window.title("Calculadora")
        self.window.resizable(width=0, height=0)

        self.screen_numbers = tk.Entry(
            self.window,
            font="Arial 20 bold",
            background="#1d2f38",
            foreground="white",
            width=25  # Limita a quantidade de caracteres
        )
        self.screen_numbers.pack()

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.__create_btn('(', 0, 0, lambda: self.__display("("))
        self.__create_btn('C', 0, 1, self.__clean)
        self.__create_btn('Back', 0, 2, self.__back)
        self.__create_btn('=', 0, 3, self.__calculate)
        self.__create_btn('7', 1, 0, lambda: self.__display("7"))
        self.__create_btn('8', 1, 1, lambda: self.__display("8"))
        self.__create_btn('9', 1, 2, lambda: self.__display("9"))
        self.__create_btn('/', 1, 3, lambda: self.__display("/"))
        self.__create_btn('4', 2, 0, lambda: self.__display("4"))
        self.__create_btn('5', 2, 1, lambda: self.__display("5"))
        self.__create_btn('6', 2, 2, lambda: self.__display("6"))
        self.__create_btn('x', 2, 3, lambda: self.__display("*"))
        self.__create_btn('1', 3, 0, lambda: self.__display("1"))
        self.__create_btn('2', 3, 1, lambda: self.__display("2"))
        self.__create_btn('3', 3, 2, lambda: self.__display("3"))
        self.__create_btn('-', 3, 3, lambda: self.__display("-"))
        self.__create_btn(')', 4, 0, lambda: self.__display(")"))
        self.__create_btn('0', 4, 1, lambda: self.__display("0"))
        self.__create_btn(',', 4, 2, lambda: self.__display("."))
        self.__create_btn('+', 4, 3, lambda: self.__display("+"))

        self.window.mainloop()

    def __create_btn(self, text: str, row: int, column: int, command) -> tk.Button:
        """
        Cria os botões da calculadora.
        """

        button = tk.Button(
            self.frame,
            background="orange",
            text=text,
            border=0,
            font="Arial 20 bold",
            foreground="white",
            width=5,
            height=3,
            command=command
        )
        button.grid(row=row, column=column)
        return button

    def __display(self, value: str):
        """
        Mostra os dados no display
        """

        self.screen_numbers.insert(tk.END, value)

    def __clean(self):
        """
        Limpa tudo.
        """

        self.screen_numbers.delete(0, tk.END)

    def __back(self):
        """
        Remove o ultimo caracter
        """

        current_text = self.screen_numbers.get()
        if current_text:
            self.screen_numbers.delete(len(current_text) - 1, tk.END)

        self.screen_numbers.delete(tk.END)

    def __calculate(self):
        """
        Realiza o calculo.
        """

        txt = self.screen_numbers.get()
        result = eval(txt)
        final_result = round(result, 2)
        self.screen_numbers.delete(0, tk.END)
        self.screen_numbers.insert(0, str(final_result))


if __name__ == '__main__':
    calc = Calculator()
