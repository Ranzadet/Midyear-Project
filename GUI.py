from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Hello"
              ).grid(row=0, column=0, columnspan=2, sticky=W)


# main
root = Tk()
root.title("This is a test")
app = Application(root)
root.mainloop()
