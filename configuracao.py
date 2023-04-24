import tkinter as tk
import datetime
import messagePipe, serialLayer

def sendParamMeter(param1):
    for aux in param1:
        if aux.__contains__('0'):
            continue
        else:
            serialLayer.sedDataReadMeterWT210(aux)
    return 0

def drawConfig():
    opt = tk.Toplevel()
    opt.wm_attributes("-topmost", True)
    opt.title('Configuração')
    window_width = 700
    window_height = 600
    # get the screen dimension

    screen_width = opt.winfo_screenwidth()
    screen_height = opt.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    opt.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    draWindowoptions = tk.Canvas(opt, height=300, width=200)

    #check1, check2, check3, check4 = tkinter.IntVar()

    global aUnit, aGrand, bUnit, bGrand, cUnit, cGrand
    aUnit  = tk.StringVar(value=0)

    bUnit  = tk.StringVar(value=0)

    cUnit  = tk.StringVar(value=0)
    cGrand = tk.StringVar(value=0)

    #draw check box chanel A
    chaLbl = tk.Label(opt, text='Configuração canal A:', font="Raleway 12", anchor='w')
    chaLbl.grid(column=0, row=0)
    a1 = tk.Checkbutton(opt, text='V', variable=aUnit, onvalue=':DISPlay1:FUNCtion V', offvalue=None)
    a2 = tk.Checkbutton(opt, text='A', variable=aUnit, onvalue=':DISPlay1:FUNCtion A', offvalue=None)
    a3 = tk.Checkbutton(opt, text='W', variable=aUnit, onvalue=':DISPlay1:FUNCtion W', offvalue=None)
    # a4 = tk.Checkbutton(opt, text='m', justify='left')
    # a5 = tk.Checkbutton(opt, text='k', justify='left')
    # a6 = tk.Checkbutton(opt, text='M', justify='left')
    a7 = tk.Checkbutton(opt, text='VA', variable=aUnit, onvalue=':DISPlay1:FUNCtion VA', offvalue=None)
    a8 = tk.Checkbutton(opt, text='VAR', variable=aUnit, onvalue=':DISPlay1:FUNCtion VAR', offvalue=None)
    a9 = tk.Checkbutton(opt, text='TIME', variable=aUnit, onvalue=':DISPlay1:FUNCtion TIME', offvalue=None)
    a1.grid(row=1, column=0); a2.grid(row=1, column=1); a3.grid(row=1, column=2);
    # a4.grid(row=2, column=0); a5.grid(row=2, column=1); a6.grid(row=2, column=2);
    a7.grid(row=3, column=0); a8.grid(row=3, column=1); a9.grid(row=3, column=2);

    #draw check box chanel B
    chbLbl = tk.Label(opt, text='Configuração canal B:', font="Raleway 12", anchor='w')
    chbLbl.grid(column=0, row=4)
    b1 = tk.Checkbutton(opt, text='V', variable=bUnit, onvalue=':DISPlay2:FUNCtion V', offvalue=None)
    b2 = tk.Checkbutton(opt, text='A', variable=bUnit, onvalue=':DISPlay2:FUNCtion A', offvalue=None)
    b3 = tk.Checkbutton(opt, text='W', variable=bUnit, onvalue=':DISPlay2:FUNCtion W', offvalue=None)
    # b4 = tk.Checkbutton(opt, text='m')
    # b5 = tk.Checkbutton(opt, text='k')
    # b6 = tk.Checkbutton(opt, text='M')
    b7 = tk.Checkbutton(opt, text='PF', variable=bUnit, onvalue=':DISPlay2:FUNCtion PF', offvalue=None)
    b8 = tk.Checkbutton(opt, text='DEGRee', variable=bUnit, onvalue=':DISPlay2:FUNCtion DEGRee', offvalue=None)
    #b9 = tk.Checkbutton(opt, text='%')
    b1.grid(row=5, column=0); b2.grid(row=5, column=1); b3.grid(row=5, column=2);
    # b4.grid(row=6, column=0); b5.grid(row=6, column=1); b6.grid(row=6, column=2);
    b7.grid(row=7, column=0); b8.grid(row=7, column=1); #b9.grid(row=7, column=2);

    #draw check box chanel C
    chcLbl = tk.Label(opt, text='Configuração canal C:', font="Raleway 12", anchor='w')
    chcLbl.grid(column=0, row=8)
    c1 = tk.Checkbutton(opt, text='V', variable=cUnit, onvalue=':DISPlay3:FUNCtion V', offvalue=None)
    c2 = tk.Checkbutton(opt, text='A', variable=cUnit, onvalue=':DISPlay3:FUNCtion A', offvalue=None)
    c3 = tk.Checkbutton(opt, text='W', variable=cUnit, onvalue=':DISPlay3:FUNCtion W', offvalue=None)
    # c4 = tk.Checkbutton(opt, text='m')
    # c5 = tk.Checkbutton(opt, text='k')
    # c6 = tk.Checkbutton(opt, text='M')
    c7 = tk.Checkbutton(opt, text='VHZ', variable=cGrand, onvalue=':DISPlay3:FUNCtion VHZ', offvalue=None)
    c8 = tk.Checkbutton(opt, text='AH', variable=cGrand, onvalue=':DISPlay3:FUNCtion AH', offvalue=None)
    # c9 = tk.Checkbutton(opt, text=':DISPlay3:FUNCtion V')
    c1.grid(row=9, column=0); c2.grid(row=9, column=1); c3.grid(row=9, column=2);
    # c4.grid(row=10, column=0); c5.grid(row=10, column=1); c6.grid(row=10, column=2);
    c7.grid(row=11, column=0); c8.grid(row=11, column=1); #c9.grid(row=11, column=2);

    #draw btnTST

    # Button Start test
    tstbtnTXT = tk.StringVar()
    tsttbtn = tk.Button(opt, textvariable=tstbtnTXT, command=lambda: sendParamMeter([aUnit.get(), bUnit.get(), cUnit.get(), cGrand.get()]), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=15)
    tstbtnTXT.set("Suite TST")
    tsttbtn.grid(row=12, column=0)

    return True

