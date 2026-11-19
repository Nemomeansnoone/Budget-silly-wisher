import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

import time
import random
import os

from scripts import gambling

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

fivestarlim: dict[str] = [
    "Yelan"
]

fourstarlim: dict[str] = [
    "Yanfei",
    "Fischl",
    "Xingqiu"
]

txt_entry = None
pulls_entry = None
pullsleft = 20
currentbanner = "standard"
currentbannerimg = "standard.png"
invcurrentsel = str()

THEME_BG = "#1e1e1e"
THEME_FONT = ("Helvetica, 10")

def pull1():
    print("Lets go gambling!")
def pull10():
    print("Lets go gambling more!")

def changeset(set):
    global bannerselectionvar
    bannerselectionvar.set(set)
    pullscreen()

def changebanner(id):
    print(id)

class ScrollableFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._canvas = tk.Canvas(self, highlightthickness=0, bg="#1e1e1e")
        self._bar = tk.Scrollbar(self, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._bar.set)
        self._bar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)
        self.body = tk.Frame(self._canvas, bg="#1e1e1e")
        self._window = self._canvas.create_window((0, 0), window=self.body, anchor="nw")
        self.body.bind("<Configure>", self._on_body)

    def _on_body(self, _event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

def pullscreen():
    global currentbanner
    global bannerselectionvar
    for widget in main_frame.winfo_children():
        widget.destroy()

    selectbanner = ScrollableFrame(main_frame, bg="#1e1e1e")
    selectbanner.place(x=0, y=130, width=120, height=270)

    bannerframe = tk.Frame(main_frame, relief="groove", bd=2, bg="#1e1e1e")
    bannerframe.place(x=120, y=0, width=480, height=400)

    pullsleftlbl = tk.Label(bannerframe, text=f"Pulls left: {pullsleft}", fg="#ffffff", bg="#1e1e1e", font=THEME_FONT)
    pullsleftlbl.place(x=300, y=10, width=100, height=20)

    bannerimgpath = os.path.join(BASE_DIR, "assets", "bannerimages", currentbannerimg)
    main_frame.bannerimage_image = ImageTk.PhotoImage(Image.open(bannerimgpath).resize((440, 290)))
    bannerimage = tk.Label(bannerframe, image=main_frame.bannerimage_image)
    bannerimage.place(x=20, y=40, width=440, height=290)

    pull10btn = tk.Button(bannerframe, text="Pull 10", command=pull10, fg="#1e1e1e")
    pull10btn.place(x=364, y=350, width=96, height=32)

    pull1btn = tk.Button(bannerframe, text="Pull 1", command=pull1, fg="#1e1e1e")
    pull1btn.place(x=252, y=350, width=96, height=32)

    getmorepullsbtn = tk.Button(bannerframe, text="Get more pulls", command=getmorepulls, fg="#1e1e1e", font=THEME_FONT)
    getmorepullsbtn.place(x=20, y=362, width=100, height=20)

    bannersetselection = tk.OptionMenu(main_frame, bannerselectionvar, "Version 1", "Version 2", "Version 3", command=changeset)
    bannersetselection.place(x=15, y=50, width=90, height=30)

    backbutton = tk.Button(main_frame, text="Back", command=intro, fg="#1e1e1e", bg="#ffffff", font=THEME_FONT)
    backbutton.place(x=12, y=10, width=96, height=32)

    standard = tk.Button(main_frame, text="Standard", command=lambda: changebanner("standard"), fg="#1e1e1e", bg="#ffffff", font=THEME_FONT)
    standard.place(x=12, y=90, width=96, height=32)

    selectbanner.body.configure(width=104, height=400)

    if bannerselectionvar.get().strip() == "Version 1":
        ver1011 = tk.Button(selectbanner.body, text="1.0 Phase 1", command=lambda: changebanner("1011"), fg="#1e1e1e", bg="#ffffff", font=THEME_FONT).pack(pady=5)
        ver1021 = tk.Button(selectbanner.body, text="1.0 Phase 2", command=lambda: changebanner("1021"), fg="#1e1e1e", bg="#ffffff", font=THEME_FONT).pack(pady=5)
        ver1111 = tk.Button(selectbanner.body, text="1.1 Phase 1", command=lambda: changebanner("1111"), fg="#1e1e1e", bg="#ffffff", font=THEME_FONT).pack(pady=5)
    elif bannerselectionvar.get().strip() == "Version 2":
        print(bannerselectionvar)
    elif bannerselectionvar.get().strip() == "Version 3":
        print(bannerselectionvar)





def addpulls():
    global pulls_entry
    global pullsleft
    addpulls = pulls_entry.get().strip()
    pullsleft += int(addpulls)
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text=f'charging $' + str(addpulls*2) + f' to your credit card...').pack(pady=10)
    root.update()
    time.sleep(3)
    for widget in main_frame.winfo_children():
        widget.destroy
    root.update()
    tk.Label(main_frame, text=f'{addpulls} pulls have been added to your balance!').pack(pady=10)
    root.update()
    time.sleep(3)
    intro()

def pullsinvalid():
    global pulls_entry
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="How many pulls would you like?", font=("Arial", 11, "bold")).pack(pady=10)
    pulls_entry = tk.Entry(main_frame, width=24, font=("Arial", 12), fg="#1e1e1e", bg="#ffffff")
    pulls_entry.pack(pady=10)
    tk.Button(main_frame, text="Confirm", font=("Arial", 11, "bold"), command=checkifpullsvalid).pack(pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 11, "bold"), command=getmorepulls)
    tk.Label(main_frame, text="Invalid number of pulls! Please enter a valid number", font=("Arial", 9), fg="red").pack(pady=10)

    

def checkifpullsvalid():
    global pulls_entry
    try:
        entered = int(pulls_entry.get().strip())
        addpulls()
    except ValueError:
        pullsinvalid()

def howmany():
    global pulls_entry
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="How many pulls would you like?", font=("Arial", 11, "bold")).pack(pady=10)
    pulls_entry = tk.Entry(main_frame, width=24, font=("Arial", 12), fg="#1e1e1e", bg="#ffffff")
    pulls_entry.pack(pady=10)
    tk.Button(main_frame, text="Confirm", font=("Arial", 11, "bold"), command=checkifpullsvalid).pack(pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 11, "bold"), command=getmorepulls).pack(pady=10)

def cardinvalid():
    global txt_entry
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="Please input your credit card number", font=("Arial", 11, "bold")).pack(pady=10)
    txt_entry = tk.Entry(main_frame, width=24, font=("Arial", 12), fg="#1e1e1e", bg="#ffffff")
    txt_entry.pack(pady=10)
    tk.Button(main_frame, text="Confirm", font=("Arial", 11, "bold"), command=checkifcardvalid).pack(pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 11, "bold"), command=intro).pack(pady=10)
    tk.Label(main_frame, text="Invalid card number! Enter a valid card number", font=("Arial", 9), fg="red").pack(pady=10)

def checkifcardvalid():
    global txt_entry
    try:
        entered = int(txt_entry.get().strip())
        howmany()
    except ValueError:
        cardinvalid()


def getmorepulls():
    global txt_entry
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="Please input your credit card number", font=("Arial", 11, "bold")).pack(pady=10)
    txt_entry = tk.Entry(main_frame, width=24, font=("Arial", 12), fg="#1e1e1e", bg="#ffffff")
    txt_entry.pack(pady=10)
    tk.Button(main_frame, text="Confirm", font=("Arial", 11, "bold"), command=checkifcardvalid).pack(pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 11, "bold"), command=intro).pack(pady=10)

def balance():
    global pullsleft
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text=f'You have {pullsleft} pulls left', font=("Arial", 12, "bold"), fg="#ffffff").pack(pady=10)
    tk.Button(main_frame, text="Get more pulls", fg="blue", font=("Arial", 11, "bold"), bg="#ffffff", command=getmorepulls).pack(pady=10)
    tk.Button(main_frame, text="Back", fg="blue", font=("Arial", 11, "bold"), bg="#ffffff", command=intro).pack(pady=10)

def gambled(fivestarlim, fourstarlim):
    result = gambling.pull(fivestarlim, fourstarlim)
    print(result)

def intro():
    global bannerselectionvar
    bannerselectionvar = tk.StringVar()
    bannerselectionvar.set("Version 1")
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="Budget silly wisher", font=("Arial", 14, "bold"), fg="#ffffff").pack(pady=10)
    tk.Button(main_frame, text="Pull", fg="blue", font=("Arial", 11, "bold"), command=pullscreen).pack(pady=10)
    tk.Button(main_frame, text="Inventory", fg="blue", font=("Arial", 11, "bold"), command=lambda: gambled(fivestarlim, fourstarlim)).pack(pady=10)
    tk.Button(main_frame, text="Get more pulls", fg="blue", font=("Arial", 11, "bold"), command=getmorepulls).pack(pady=10)
    tk.Button(main_frame, text="Balance", fg="blue", font=("Arial", 11, "bold"), command=balance).pack(pady=10)

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="#1e1e1e")
root.title("Budget silly wisher")
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand = True)

intro()
root.mainloop()
