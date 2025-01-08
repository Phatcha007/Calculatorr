import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        # ตัวแสดงผลของเครื่องคิดเลข
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(self, textvariable=self.display_var, font=("Arial", 20), justify="right", state="readonly")
        self.display.pack(fill=tk.BOTH, padx=10, pady=10)

        # เฟรมสำหรับปุ่ม
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        # กำหนดปุ่มและตำแหน่ง
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("CE", 5, 1),
        ]

        # สร้างปุ่มและจัดวางในกริด
        for (text, row, col) in buttons:
            button = ttk.Button(self.button_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # ปรับแต่งขนาดแถวและคอลัมน์ในกริด
        for i in range(6):
            self.button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.columnconfigure(j, weight=1)

    def on_button_click(self, button_text):
        """ฟังก์ชันจัดการเมื่อคลิกปุ่ม"""
        if button_text in "0123456789.":
            # เพิ่มตัวเลขหรือจุดลงในช่องแสดงผล
            current_text = self.display_var.get()
            self.display_var.set(current_text + button_text)
        elif button_text in "+-*/":
            # เพิ่มเครื่องหมายลงในช่องแสดงผล
            current_text = self.display_var.get()
            if current_text and current_text[-1] not in "+-*/":
                self.display_var.set(current_text + button_text)
        elif button_text == "=":
            # คำนวณผลลัพธ์
            try:
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except Exception:
                self.display_var.set("Error")
        elif button_text == "C":
            # ลบตัวอักษรสุดท้ายในช่องแสดงผล
            current_text = self.display_var.get()
            self.display_var.set(current_text[:-1])
        elif button_text == "CE":
            # ลบทุกอย่างในช่องแสดงผล
            self.display_var.set("")


def main():
    app = Calculator()
    app.mainloop()


if __name__ == "__main__":
    main()
