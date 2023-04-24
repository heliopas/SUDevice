import tkinter as tk
import datetime
#import configuracao, help

from PIL import Image, ImageTk

def drawApp():
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    root.title('SmartMeter HQA V:1.00')

    window_width = 310
    window_height = 360

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # set windows size
    global draWindow
    draWindow = tk.Canvas(root)
    draWindow.grid(columnspan=1, rowspan=1)

    # set backgroung logo
    logo = Image.open('files/logo/landisLogo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, columnspan=2, row=1, rowspan=5, padx=0, pady=0)

    # software instructions
    instructions = tk.Label(draWindow, text="HQA SMARTMETER CONTROL", font="Raleway")
    instructions.grid(columnspan=1, row=10, column=0, padx=10, pady=10)

    # Button iniciar teste
    StartTSTbtnTXT = tk.StringVar()
    StartTSTbtn = tk.Button(draWindow, textvariable=StartTSTbtnTXT, command=lambda: cadastroSkinApp.cadastro(), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    StartTSTbtnTXT.set("Iniciar")
    StartTSTbtn.grid(column=0, row=0)

    # Button pausar teste
    PauseTSTbtnTXT = tk.StringVar()
    PauseTSTbtn = tk.Button(draWindow, textvariable=PauseTSTbtnTXT, command=lambda: cadastroSkinApp.buscar(), font="Raleway",
                        background="#8b9484", foreground="White", height=1, width=20)
    PauseTSTbtnTXT.set("Pausar")
    PauseTSTbtn.grid(column=0, row=1)

    # Button cancelar teste
    CancelarTSTbtnTXT = tk.StringVar()
    CancelarTSTbtn = tk.Button(draWindow, textvariable=CancelarTSTbtnTXT, command=lambda: cadastroSkinApp.deletar(), font="Raleway",
                           background="#8b9484", foreground="White", height=1, width=20)
    CancelarTSTbtnTXT.set("Cancelar")
    CancelarTSTbtn.grid(column=0, row=2)

    # Button alterar material
    ConfigTSTbtnTXT = tk.StringVar()
    ConfigTSTbtn = tk.Button(draWindow, textvariable=ConfigTSTbtnTXT, command=lambda: configuracao.drawConfig(), font="Raleway",
                        background="#8b9484", foreground="White", height=1, width=20)
    ConfigTSTbtnTXT.set("Configurações")
    ConfigTSTbtn.grid(column=0, row=3)

    # Button help
    helpbtnTXT = tk.StringVar()
    helpbtn = tk.Button(draWindow, textvariable=helpbtnTXT, command=lambda: help.drawHelp(), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    helpbtnTXT.set("Help")
    helpbtn.grid(column=0, row=4)

    # Button Close
    closebtnTXT = tk.StringVar()
    closebtn = tk.Button(draWindow, textvariable=closebtnTXT, command=lambda: exitsw(root), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    closebtnTXT.set("Close App")
    closebtn.grid(column=0, row=6)

    root.mainloop()

def exitsw(root):
    root.destroy()