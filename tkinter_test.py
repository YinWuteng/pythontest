from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # # 创建标题
        # self.helloLabel = Label(self, text='Hello world!')
        # self.helloLabel.pack()
        # # 创建一个quit按钮
        # self.quitbutton = Button(self, text='Quit', command=self.quit())
        # self.quitbutton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello,%s' % name)


app = Application()
# 设置窗口标题
app.master.title('Hello world!')
# 主消息循环
app.mainloop()
