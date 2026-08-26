import tkinter as tk
while True:
    pencere = tk.Tk()
    pencere.attributes("-toolwindow", True)
    pencere.attributes("-fullscreen", True)
    pencere.config(bg="blue")
    for i in range(10000):
        yeni = tk.Toplevel()
        yeni.resizable(False, False)
        yeni.config(bg="blue")
        yeni.title(f"Pencere {i + 1}")
        yeni.geometry(f"2000x2000+{100 * i}+{100 * i}")
    pencere.mainloop()



