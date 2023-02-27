import tkinter as tk


class ChatWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        # 创建聊天记录显示框
        self.chat_log = tk.Text(self, height=20, state=tk.DISABLED)
        self.chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 创建滚动条
        self.scrollbar = tk.Scrollbar(self.chat_log)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 绑定聊天记录框和滚动条
        self.chat_log.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.chat_log.yview)

        # 创建发送消息框和按钮
        self.send_frame = tk.Frame(self)
        self.send_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.send_entry = tk.Entry(self.send_frame)
        self.send_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.send_entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.send_frame, text='发送', command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        # 获取输入框中的文本
        message = self.send_entry.get()

        # 将消息添加到聊天记录中
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, message + '\n')
        self.chat_log.config(state=tk.DISABLED)

        # 清空发送框
        self.send_entry.delete(0, tk.END)

root = tk.Tk()
app = ChatWindow(master=root)
app.mainloop()
