import tkinter


def new_file(text_area: tkinter.Text) -> None:
    """
    Cria um novo arquivo.
    """

    print("Criando um novo arquivo.")
    text_area.delete(1.0, "end")


def save(text_area: tkinter.Text) -> None:
    """
    Salvando o arquivo.
    """

    print("Salvando o arquivo...")
    content = text_area.get(1.0, "end")
    with open("notepad/notepad.txt", "w") as file:
        file.write(content)


def read(text_area: tkinter.Text) -> None:
    """
    Salvando o arquivo como...
    """

    print("Abrindo arquivo...")
    with open("notepad/notepad.txt", "r") as file:
        content = file.read()

    text_area.insert(1.0, content)