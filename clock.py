import tkinter as tk
import datetime

class MillisecondClock:
    def __init__(self, root):
        self.root = root
        self.root.title("实时时钟（精确到毫秒）")

        # 创建一个 Label 显示时间
        self.label = tk.Label(
            root,
            font=("Helvetica", 36),
            fg="#00FF00",           # lime 的十六进制等价色
            bg="black",
            padx=20,
            pady=20
        )
        self.label.pack(expand=True)

        # 启动更新时间循环
        self.update_time()

    def update_time(self):
        now = datetime.datetime.now()
        time_string = now.strftime("%H:%M:%S.%f")[:-3]  # 显示到毫秒
        self.label.config(text=time_string)

        # 每 10 毫秒更新一次（精度更高就用更小的间隔，但 10ms 是 UI可接受上限）
        self.root.after(10, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x200")  # 设置窗口大小
    clock = MillisecondClock(root)
    root.mainloop()