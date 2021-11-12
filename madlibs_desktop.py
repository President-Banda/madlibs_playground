# Python 3.8
# Coding: UTF-8

try:
    import main

except ImportError:
    print("Main not found!s")

try:
    from tkinter import *  # any package really

except ImportError:
    pip.main['install', 'tk']
    from tkinter import *

try:
    from tkinter import messagebox

except ImportError:
    pip.main['install', 'tk']
    from tkinter import messagebox

try:
    from PIL import ImageTk  # any package really

except ImportError:
    pip.main['install', 'PIL']
    from PIL import ImageTk

class madlibsMain:
    # This is the default login function, all login logic should and will be implemented here
    def __init__(self, root):
        self.root = root
        self.root.title("Madlibs Desktop by Team Macie")
        self.root.geometry("840x620+250+50")
        self.root.resizable(width=False, height=False)
        #self.root.iconbitmap(r'/badminton.png')
        self.frames = {}

        # =====================This is to set my background image=================
        bg_label = Label(self.root, background="white").pack()

        # =============Top Frame==================================================
        self.top_frame = Frame(self.root)
        self.top_frame.place(x=230, y=100, width=420, height=380)
        self.top_frame.configure(bg="#ffffff")

        # ============Bottom Frame===========================================================
        self.bottom_frame = Frame(self.root)
        self.bottom_frame.place(x=230, y=490, width=420, height=110)
        self.bottom_frame.configure(bg="#ffffff")

        # =================Title=============================================================
        self.title = Label(self.top_frame)
        self.title.place(x=10, y=10, relwidth=1)
        self.title.configure(text="Welcome to Madlibs")
        self.title.configure(font=("Arial", 28, "bold"))
        self.title.configure(bg="#ffffff")
        self.title.configure(fg="#259b29")
        self.title.configure(bd=0)
        self.title.configure(relief=SUNKEN)
        self.title.configure(justify="center")


root = Tk()
test_object = madlibsMain(root)
root.mainloop()