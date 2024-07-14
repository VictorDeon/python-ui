import tkinter
from menu import new_file, save, read, update

window = tkinter.Tk()
window.title("Notapad")
window.minsize(width=1280, height=720)
window.maxsize(width=1280, height=720)

frame = tkinter.Frame(window, height=30)
frame.pack(fill="x")

font_text = tkinter.Label(frame, text=" Fonte: ")
font_text.pack(side="left")
spin_font = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spin_font.pack(side="left")

font_size = tkinter.Label(frame, text=" Tamanho da fonte: ")
font_size.pack(side="left")
spin_size = tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side="left")

text_area = tkinter.Text(window, font="Arial 20 bold", width=1280, height=720)
text_area.pack()

button = tkinter.Button(frame, text="Atualizar", command=lambda: update(
    text_area=text_area,
    spin_size=spin_size,
    spin_font=spin_font
))
button.pack(side="right")

menu = tkinter.Menu(window)
# Submenus que realizam ações do menu de arquivo
file_menu = tkinter.Menu(menu, tearoff=0)
file_menu.add_command(label="Novo", command=lambda: new_file(text_area))
file_menu.add_command(label="Abrir", command=lambda: read(text_area))
file_menu.add_command(label="Salvar", command=lambda: save(text_area))
file_menu.add_command(label="Sair", command=window.quit)
# Abre um menu de opções
menu.add_cascade(label="Arquivo", menu=file_menu)
window.config(menu=menu)

window.mainloop()
