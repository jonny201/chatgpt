import tkinter as tk
import tcp_client3
class ChatWindow:
    def __init__(self, master):
        self.master = master
        master.title("Chat Window")

        # 聊天记录框
        self.chat_history = tk.Text(master, height=20, width=50)
        self.chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.chat_history.config(state=tk.DISABLED)

        # 输入框和发送按钮
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.send_button = tk.Button(self.input_frame, text="发送", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        message = self.input_entry.get()
        if message:
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"You: {message}\n")
            self.chat_history.config(state=tk.DISABLED)
            self.chat_history.see(tk.END)
            self.input_entry.delete(0, tk.END)
            tcp_client3.TCPClient()

root = tk.Tk()
chat_window = ChatWindow(root)
root.mainloop()
