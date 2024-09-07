import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import functions
import pandas as pd
def select_file_and_execute():
    io = filedialog.askopenfilename(title='Select your file')
    if io:
        # 如果成功选择文件，创建新窗口并在其中放置 "run" 按钮
        execute_window = tk.Toplevel(window)
        execute_window.title('Perform iteration')
        execute_window.geometry('550x200')
        w_box = 600
        h_box = 350
        canvas = tk.Canvas(execute_window, bg='white', height=150, width=500)
        pil_image = Image.open(r'glucose.gif')
        pil_image_resized = functions.resize(150, 150, pil_image)
        tk_image = ImageTk.PhotoImage(pil_image_resized) 
        image = canvas.create_image(250, 0, anchor='n', image=tk_image)
        canvas.pack()
        btn_execute = tk.Button(execute_window, text='Run', command=lambda:functions.execute_after_select(io))
        btn_execute.place(x=210, y=160)
        execute_window.mainloop()
window = tk.Tk() # 实例化一个窗口
window.title('select data')
window.geometry('550x200')

w_box = 600
h_box = 350
canvas = tk.Canvas(window, bg='white', height=150, width=500)
pil_image = Image.open(r'fructose.gif') # 获得合适大小的图片
pil_image_resized = functions.resize(150, 150, pil_image)
tk_image = ImageTk.PhotoImage(pil_image_resized) 
image = canvas.create_image(250, 0, anchor='n', image=tk_image)
canvas.pack()
btn_Run = tk.Button(window, text='select your file', command=select_file_and_execute)
btn_Run.place(x=210, y=160)
window.mainloop()