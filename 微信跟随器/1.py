import tkinter as tk

class FollowWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 0.5)
        self.root.geometry("200x600+2000+0")
        self.root.lift()
        self.root.wm_attributes("-topmost", True)

        self.follow_window()

    def follow_window(self):
        wx = self.root.winfo_screenwidth()
        wy = self.root.winfo_screenheight()
        ww = self.root.winfo_width()
        wh = self.root.winfo_height()
        x = wx - ww - 10 # 距离屏幕右边缘10像素
        y = 0
        self.root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.root.after(100, self.follow_window)

if __name__ == "__main__":
    FollowWindow().root.mainloop()
