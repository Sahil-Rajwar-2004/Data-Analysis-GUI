# Essential Libraries
from tkinter import *
from tkinter import (
    filedialog as fd,
    messagebox as msg,
    ttk
)
from chemaphy import (
    LoadData,
    Statistics as stats
)
from sklearn import (
    linear_model,
    model_selection,
    preprocessing,
    metrics
)
from matplotlib import (
    pyplot as plt,
    style
)
from info import (
    author,
    version,
    homepage
)
from pandas_datareader import data as web
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import webbrowser

# Backend Programmes
def about_me():
    about = Toplevel()
    about.geometry("670x310")
    about.resizable(False,False)
    about.title("About Me")
    about.config(bg = "gray")

    content = (
        f"""author: {author}
version: {version}
homepage: {homepage}
        """
    )
    txt_frame = Frame(about)
    txt_frame.pack(fill = BOTH,padx = 5,pady = 5)
    txt = Text(txt_frame,height = 10,state = NORMAL,font = ("cascadia code",13))
    txt.pack(fill = BOTH,padx = 5,pady = 5)
    txt.insert(INSERT,content)
    txt.config(state = DISABLED)

    btn_frame = Frame(about)
    btn_frame.pack(fill = BOTH,padx = 5)
    btn = Button(btn_frame,text = "Exit",font = ("cascadia code",13),command = about.destroy)
    btn.pack(padx = 5,pady = 5,ipadx = 5,ipady = 5)
    about.mainloop()

def home():
    url = "https://github.com/Sahil-Rajwar-2004/Data-Analysis-GUI"
    webbrowser.open(url)

def statistics():
    pass

def plot():
    pass

def scatter():
    pass

def clear():
    global dataname
    data_text.config(state = "normal")
    data_text.delete("1.0","end")
    data_text.config(state = "disabled")
    dataname = ""
    data_heading_label.config(text = "data: "+dataname)

def go():
    def load():
        global data,dataname
        clear()
        input_data = data_box.get()
        if input_data == "":
            msg.showerror("Error","Invalid Dataname")
        else:
            data = LoadData.load_data(input_data)
            dataname = input_data
            data_heading_label.config(text = "data: "+dataname)
            data_text.config(state = "normal")
            data_text.insert(INSERT,data.to_string())
            data_text.config(state = "disabled")
        load_win.destroy()
        source.current(0)

    def ticker():
        global data,dataname
        clear()
        input_ticker = ticker_entry.get()
        if input_ticker != "":
            try:
                data = web.get_data_yahoo(input_ticker,start = dt.datetime(2010,1,1),end = dt.datetime.now())
                dataname = input_ticker.upper()
                data_heading_label.config(text = "data: "+dataname)
                data_text.config(state = "normal")
                data_text.insert(INSERT,data.to_string())
                data_text.config(state = "disabled")
            except Exception as error:
                msg.showerror("Error",error)
        else:
            msg.showerror("Error","Invalid Ticker")
        load_win.destroy()
        source.current(0)

    src = source.get()
    if src == "None":
        msg.showerror("Error","Invalid Input")

    elif src == "Chemaphy":
        load_win = Toplevel()
        load_win.geometry("600x280")
        load_win.title("Load Data")
        load_win.resizable(False,False)
        frame = Frame(load_win)
        frame.pack(fill = BOTH,padx = 5,pady = 5)
        label = Label(frame,text = "Dataset Name: ",font = ("cascadia code",13))
        label.grid(row = 0,column = 0,padx = 5,pady = 5)
        data_var = StringVar()
        data_box = ttk.Combobox(frame,textvariable = data_var,state = "readonly",font = ("cascadia code",13))
        data_box.grid(row = 0,column = 1,padx = 5,pady = 5)
        data_box["values"] = LoadData.data_name()
        btn_frame = Frame(load_win)
        btn_frame.pack(fill = BOTH,padx = 5,pady = 5)
        btn = Button(btn_frame,text = "Load",font = ("cascadia code",13),command = load)
        btn.pack(padx = 5,pady = 5)
        load_win.mainloop()

    elif src == "Ticker":
        load_win = Toplevel()
        load_win.geometry("400x110")
        load_win.title("Load Data")
        load_win.resizable(False,False)
        frame = Frame(load_win)
        frame.pack(fill = BOTH,padx = 5,pady = 5)
        label = Label(frame,text = "Ticker: ",font = ("cascadia code",13))
        label.grid(row = 0,column = 0,padx = 5,pady = 5)
        ticker_var = StringVar()
        ticker_entry = Entry(frame,textvariable = ticker_var,width = 25,font = ("cascadia code",13))
        ticker_entry.grid(row = 0,column = 1,padx = 5,pady = 5)
        btn_frame = Frame(load_win)
        btn_frame.pack(fill = BOTH,padx = 5,pady = 5)
        btn = Button(btn_frame,text = "Load",font = ("cascadia code",13),command = ticker)
        btn.pack(padx = 5,pady = 5)
        load_win.mainloop()

    elif src == "System":
        global data,dataname
        clear()
        full_path = fd.askopenfilename(initialdir = "C:\\Users\\a\\OneDrive\\Desktop\\",title = "Open",filetypes = (
            ("CSV","*csv"),
            ("EXCEL","*xlsx"),
            ("DATA","*data")
            ))
        split_name = full_path.split("/")
        file_name = split_name[len(split_name)-1]
        try:
            data = pd.read_csv(full_path)
            dataname = file_name
            data_heading_label.config(text = "data: "+dataname)
            data_text.config(state = "normal")
            data_text.insert(INSERT,data.to_string())
            data_text.config(state = "disabled")
        except Exception:
            data = pd.read_excel(full_path)
            dataname = file_name
            data_heading_label.config(text = "data: "+dataname)
            data_text.config(state = "normal")
            data_text.insert(INSERT,data.to_string())
            data_text.config(state = "disabled")


# Frontend Programmes
main_app = Tk()
main_app.geometry("1200x600")
main_app.title("Stock App")
main_app.resizable(False,False)

main_menu = Menu(main_app)
main_app.config(menu = main_menu)
graphs_menu = Menu(main_menu,tearoff = 0)
main_menu.add_command(label = "Statistics",command = statistics)
main_menu.add_cascade(label = "Graphs",menu = graphs_menu)
graphs_menu.add_command(label = "Plot",command = plot)
graphs_menu.add_command(label = "Scatter",command = scatter)
main_menu.add_command(label = "About",command = about_me)
main_menu.add_command(label = "Home",command = home)

head_frame = Frame(main_app)
head_frame.pack(fill = BOTH,padx = 5)
head_label = Label(head_frame,text = "Source: ",font = ("cascadia code",13))
head_label.grid(row = 0,column = 0,padx = 5)
source_var = StringVar()
source = ttk.Combobox(head_frame,textvariable = source_var,state = "readonly",font = ("cascadia code",13))
source.grid(row = 0,column = 1,padx = 5)
source["values"] = (
    "None",
    "Chemaphy",
    "System",
    "Ticker"
)
source.current(0)
go_btn = Button(head_frame,text = "Go",font = ("cascadia code",13),command = go)
go_btn.grid(row = 0,column = 2,padx = 5,ipadx = 5)
clear_data_btn = Button(head_frame,text = "Clear",font = ("cascadia code",13),command = clear)
clear_data_btn.grid(row = 0,column = 3,padx = 5, ipadx = 5)
dataname = ""
data_heading_label = Label(head_frame,text = "data: "+dataname,font = ("cascadia code",16))
data_heading_label.grid(row = 0,column = 4,padx = 20)

data_content_frame = Frame(main_app)
data_content_frame.pack(fill = BOTH,padx = 5,pady = 5)
vertical_scrollbar = Scrollbar(data_content_frame)
vertical_scrollbar.pack(side = RIGHT,fill = Y)
horizontal_scrollbar = Scrollbar(data_content_frame,orient = HORIZONTAL)
horizontal_scrollbar.pack(side = BOTTOM,fill = X)
data_text = Text(data_content_frame,font = ("cascadia code",11),height = 30,state = "disabled",wrap = NONE,yscrollcommand = vertical_scrollbar.set,xscrollcommand = horizontal_scrollbar.set)
data_text.pack(fill = BOTH,padx = 5)
vertical_scrollbar.config(command = data_text.yview)
horizontal_scrollbar.config(command = data_text.xview)

main_app.mainloop()



