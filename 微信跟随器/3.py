import tkinter as tk
import win32gui

class FollowWeChatWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Follow WeChat")
        self.attributes("-topmost", True)  # 窗口置于最上层
        self.geometry("300x400")  # 设置窗口大小
        self.update()  # 刷新窗口，以获取当前坐标
        self.update_idletasks()
        self.move_window_to_right()  # 将窗口移动到右侧

    def move_window_to_right(self):
        wechat_hwnd = win32gui.FindWindow(None, "微信")
        if wechat_hwnd != 0:
            wechat_rect = win32gui.GetWindowRect(wechat_hwnd)
            wechat_width = wechat_rect[2] - wechat_rect[0]
            wechat_height = wechat_rect[3] - wechat_rect[1]
            self_width = self.winfo_width()
            self_height = self.winfo_height()
            x = wechat_rect[2]
            y = wechat_rect[1]
            self.geometry("{}x{}+{}+{}".format(self_width, self_height, x, y))
            self.after(1000, self.move_window_to_right)  # 每隔1秒更新一次窗口位置
        else:
            self.after(1000, self.move_window_to_right)

if __name__ == '__main__':
    FollowWeChatWindow().mainloop()
