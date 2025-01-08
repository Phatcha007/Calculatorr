import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)

        self.display_var = tk.StringVar()
        self.display = tk.Entry(self, textvariable=self.display_var, font=("Arial", 20), bd=5, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        row_value = 1
        col_value = 0
        for button in buttons:
            tk.Button(self, text=button, width=6, height=2, font=("Arial", 15),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_value, column=col_value, pady=5, padx=5)

            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

    def on_button_click(self, button_text):
        if button_text == "C":
            self.display_var.set("")
        elif button_text == "=":
            try:
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except Exception:
                self.display_var.set("Error")
        else:
            current_text = self.display_var.get()
            self.display_var.set(current_text + button_text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
