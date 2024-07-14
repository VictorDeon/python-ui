import tkinter
from menu import new_file, save, read

window = tkinter.Tk()
window.title("Notapad")
window.minsize(width=1280, height=720)
window.maxsize(width=1280, height=720)

text_area = tkinter.Text(window, font="Arial 20 bold", width=1280, height=720)
text_area.pack()

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
