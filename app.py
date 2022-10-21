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

def exit_():
    ask = msg.askyesno("Info","Are you sure?")
    if ask == True:
        exit()
    elif ask == False:
        pass
    else:
        msg.showerror("Error","You did something wrong!")

def statistics():
    pass

def plot():
    global data,dataname
    def plotting():
        x = x_axis_box.get()
        y = y_axis_box.get()
        marker = marker_box.get()
        color = color_box.get()
        xlabel = x_axis_name_entry.get()
        ylabel = y_axis_name_entry.get()
        title = title_entry.get()
        grid = grid_box.get()
        style_ = style_box.get()
        log_ = log_box.get()
        width = int(linewidth_box.get())
        style.use(style_)
        plt.plot(data[x],data[y],color = color,marker = marker,linewidth = width)
        if log_ == "xscale":
            plt.xscale("log")
        elif log_ == "yscale":
            plt.yscale("log")
        plt.grid(grid)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    graph_win = Toplevel()
    graph_win.geometry("600x550")
    graph_win.title("Details")
    graph_win.resizable(False,False)
    heading_frame = Frame(graph_win)
    heading_frame.pack(fill = BOTH,padx = 5,pady = 5)
    heading_label = Label(heading_frame,text = "data: "+dataname,font = ("cascadia code",16))
    heading_label.pack(fill = BOTH,padx = 5,pady = 5)
    main_frame = Frame(graph_win)
    main_frame.pack(fill = BOTH,padx = 5,pady = 5)
    x_axis_label = Label(main_frame,text = "x-axis: ",font = ("cascadia code",13))
    x_axis_label.grid(row = 0,column = 0,padx = 5,pady = 5)
    x_axis = StringVar()
    x_axis_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = x_axis,state = "readonly",width = 28)
    x_axis_box.grid(row = 0,column = 1,padx = 5,pady = 5)
    x_axis_box["values"] = tuple(data.columns)
    y_axis_label = Label(main_frame,text = "y-axis: ",font = ("cascadia code",13))
    y_axis_label.grid(row = 1,column = 0,padx = 5,pady = 5)
    y_axis = StringVar()
    y_axis_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = y_axis,state = "readonly",width = 28)
    y_axis_box.grid(row = 1,column = 1,padx = 5,pady = 5)
    y_axis_box["values"] = tuple(data.columns)
    color_label = Label(main_frame,text = "color: ",font = ("cascadia code",13))
    color_label.grid(row = 2,column = 0,padx = 5,pady = 5)
    color = StringVar()
    color_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = color,state = "readonly",width = 28)
    color_box.grid(row = 2,column = 1,padx = 5,pady = 5)
    color_box["values"] = (
            "blue",
            "orange",
            "red",
            "green",
            "yellow"
            )
    color_box.current(0)
    marker_label = Label(main_frame,text = "marker: ",font = ("cascadia code",13))
    marker_label.grid(row = 3,column = 0,padx = 5,pady = 5)
    marker = StringVar()
    marker_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = marker,state = "readonly",width = 28)
    marker_box.grid(row = 3,column = 1,padx = 5,pady = 5)
    marker_box["values"] = ("None","o","*","^",".","x","X","v","<",">","1","2","3","4","8","s","p","h","H","+","D","d","|","_")
    marker_box.current(0)
    x_axis_name_label = Label(main_frame,text = "x-axis name: ",font = ("cascadia code",13))
    x_axis_name_label.grid(row = 4,column = 0,padx = 5,pady = 5)
    xname = StringVar()
    x_axis_name_entry = Entry(main_frame,font = ("cascadia code",13),textvariable = xname,width = 30)
    x_axis_name_entry.grid(row = 4,column = 1,padx = 5,pady = 5)
    y_axis_name_label = Label(main_frame,text = "y-axis name: ",font = ("cascadia code",13))
    y_axis_name_label.grid(row = 5,column = 0,padx = 5,pady = 5)
    yname = StringVar()
    y_axis_name_entry = Entry(main_frame,font = ("cascadia code",13),textvariable = yname,width = 30)
    y_axis_name_entry.grid(row = 5,column = 1,padx = 5,pady = 5)
    title_label = Label(main_frame,text = "title: ",font = ("cascadia code",13))
    title_label.grid(row = 6,column = 0,padx = 5,pady = 5)
    title = StringVar()
    title_entry = Entry(main_frame,font = ("cascadia code",13),textvariable = title,width = 30)
    title_entry.grid(row = 6,column = 1,padx = 5,pady = 5)
    grid_label = Label(main_frame,text = "grid: ",font = ("cascadia code",13))
    grid_label.grid(row = 7,column = 0,padx = 5,pady = 5)
    is_grid = StringVar()
    grid_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = is_grid,state = "readonly",width = 28)
    grid_box.grid(row = 7,column = 1,padx = 5,pady = 5)
    grid_box["values"] = (True,False)
    style_label = Label(main_frame,text = "style: ",font = ("cascadia code",13))
    style_label.grid(row = 8,column = 0,padx = 5,pady = 5)
    styles = StringVar()
    style_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = styles,state = "readonly",width = 28)
    style_box.grid(row = 8,column = 1,padx = 5,pady = 5)
    style_box["values"] = tuple(style.available)
    style_box.current(5)
    log_label = Label(main_frame,text = "log: ",font = ("cascadia code",13))
    log_label.grid(row = 9,column = 0,padx = 5,pady = 5)
    value = StringVar()
    log_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = value,state = "readonly",width = 28)
    log_box.grid(row = 9,column = 1,padx = 5,pady = 5)
    log_box["values"] = (None,"xscale","yscale")
    log_box.current(0)
    linewidth_label = Label(main_frame,text = "size: ",font = ("cascadia code",13))
    linewidth_label.grid(row = 10,column = 0,padx = 5,pady = 5)
    sizes = StringVar()
    linewidth_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = sizes,state = "readonly",width = 28)
    linewidth_box.grid(row = 10,column = 1,padx = 5,pady = 5)
    linewidth_box["values"] = (1,2,3,4,5,6,7,8,9,10,11,12,13)
    linewidth_box.current(0)
    btn_frame = Frame(graph_win)
    btn_frame.pack(fill = BOTH,padx = 5,pady = 5)
    show_btn = Button(btn_frame,text = "plot",font = ("cascadia code",13),command = plotting)
    show_btn.grid(row = 0,column = 0,padx = 5,pady = 5)
    close_btn = Button(btn_frame,text = "close",font = ("cascadia code",13),command = graph_win.destroy)
    close_btn.grid(row = 0,column = 1,padx = 5,pady = 5)
    graph_win.mainloop()

def scatter():
    global data,dataname
    def plotting():
        x = x_axis_box.get()
        y = y_axis_box.get()
        marker = marker_box.get()
        color = color_box.get()
        xlabel = x_axis_name_entry.get()
        ylabel = y_axis_name_entry.get()
        title = title_entry.get()
        grid = grid_box.get()
        style_ = style_box.get()
        log_ = log_box.get()
        ms = int(ms_box.get())
        style.use(style_)
        plt.scatter(data[x],data[y],color = color,marker = marker,s = ms)
        if log_ == "xscale":
            plt.xscale("log")
        elif log_ == "yscale":
            plt.yscale("log")
        plt.grid(grid)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    graph_win = Toplevel()
    graph_win.geometry("600x550")
    graph_win.title("Details")
    graph_win.resizable(False,False)
    heading_frame = Frame(graph_win)
    heading_frame.pack(fill = BOTH,padx = 5,pady = 5)
    heading_label = Label(heading_frame,text = "data: "+dataname,font = ("cascadia code",16))
    heading_label.pack(fill = BOTH,padx = 5,pady = 5)
    main_frame = Frame(graph_win)
    main_frame.pack(fill = BOTH,padx = 5,pady = 5)
    x_axis_label = Label(main_frame,text = "x-axis: ",font = ("cascadia code",13))
    x_axis_label.grid(row = 0,column = 0,padx = 5,pady = 5)
    x_axis = StringVar()
    x_axis_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = x_axis,state = "readonly",width = 28)
    x_axis_box.grid(row = 0,column = 1,padx = 5,pady = 5)
    x_axis_box["values"] = tuple(data.columns)
    y_axis_label = Label(main_frame,text = "y-axis: ",font = ("cascadia code",13))
    y_axis_label.grid(row = 1,column = 0,padx = 5,pady = 5)
    y_axis = StringVar()
    y_axis_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = y_axis,state = "readonly",width = 28)
    y_axis_box.grid(row = 1,column = 1,padx = 5,pady = 5)
    y_axis_box["values"] = tuple(data.columns)
    color_label = Label(main_frame,text = "color: ",font = ("cascadia code",13))
    color_label.grid(row = 2,column = 0,padx = 5,pady = 5)
    color = StringVar()
    color_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = color,state = "readonly",width = 28)
    color_box.grid(row = 2,column = 1,padx = 5,pady = 5)
    color_box["values"] = (
            "blue",
            "orange",
            "red",
            "green",
            "yellow"
            )
    color_box.current(0)
    marker_label = Label(main_frame,text = "marker: ",font = ("cascadia code",13))
    marker_label.grid(row = 3,column = 0,padx = 5,pady = 5)
    marker = StringVar()
    marker_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = marker,state = "readonly",width = 28)
    marker_box.grid(row = 3,column = 1,padx = 5,pady = 5)
    marker_box["values"] = ("o","*","^",".","x","X","v","<",">","1","2","3","4","8","s","p","h","H","+","D","d","|","_")
    marker_box.current(0)
    x_axis_name_label = Label(main_frame,text = "x-axis name: ",font = ("cascadia code",13))
    x_axis_name_label.grid(row = 4,column = 0,padx = 5,pady = 5)
    xname = StringVar()
    x_axis_name_entry = Entry(main_frame,font = ("cascadia code",13),textvariable = xname,width = 30)
    x_axis_name_entry.grid(row = 4,column = 1,padx = 5,pady = 5)
    y_axis_name_label = Label(main_frame,text = "y-axis name: ",font = ("cascadia code",13))
    y_axis_name_label.grid(row = 5,column = 0,padx = 5,pady = 5)
    yname = StringVar()
    y_axis_name_entry = Entry(main_frame,font = ("cascadia code",13),textvariable = yname,width = 30)
    y_axis_name_entry.grid(row = 5,column = 1,padx = 5,pady = 5)
    title_label = Label(main_frame,text = "title: ",font = ("cascadia code",13))
    title_label.grid(row = 6,column = 0,padx = 5,pady = 5)
    title = StringVar()
    title_entry = Entry(main_frame,font = ("cascadia code",13),textvariable = title,width = 30)
    title_entry.grid(row = 6,column = 1,padx = 5,pady = 5)
    grid_label = Label(main_frame,text = "grid: ",font = ("cascadia code",13))
    grid_label.grid(row = 7,column = 0,padx = 5,pady = 5)
    is_grid = StringVar()
    grid_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = is_grid,state = "readonly",width = 28)
    grid_box.grid(row = 7,column = 1,padx = 5,pady = 5)
    grid_box["values"] = (True,False)
    style_label = Label(main_frame,text = "style: ",font = ("cascadia code",13))
    style_label.grid(row = 8,column = 0,padx = 5,pady = 5)
    styles = StringVar()
    style_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = styles,state = "readonly",width = 28)
    style_box.grid(row = 8,column = 1,padx = 5,pady = 5)
    style_box["values"] = tuple(style.available)
    style_box.current(5)
    log_label = Label(main_frame,text = "log: ",font = ("cascadia code",13))
    log_label.grid(row = 9,column = 0,padx = 5,pady = 5)
    value = StringVar()
    log_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = value,state = "readonly",width = 28)
    log_box.grid(row = 9,column = 1,padx = 5,pady = 5)
    log_box["values"] = (None,"xscale","yscale")
    log_box.current(0)
    ms_label = Label(main_frame,text = "marker size: ",font = ("cascadia code",13))
    ms_label.grid(row = 10,column = 0,padx = 5,pady = 5)
    ms = StringVar()
    ms_box = ttk.Combobox(main_frame,font = ("cascadia code",13),textvariable = ms,state = "readonly",width = 28)
    ms_box.grid(row = 10,column = 1,padx = 5,pady = 5)
    ms_box["values"] = (1,2,3,4,5,6,7,8,9,10,11,12,13)
    btn_frame = Frame(graph_win)
    btn_frame.pack(fill = BOTH,padx = 5,pady = 5)
    show_btn = Button(btn_frame,text = "plot",font = ("cascadia code",13),command = plotting)
    show_btn.grid(row = 0,column = 0,padx = 5,pady = 5)
    close_btn = Button(btn_frame,text = "exit",font = ("cascadia code",13),command = graph_win.destroy)
    close_btn.grid(row = 0,column = 1,padx = 5,pady = 5)
    graph_win.mainloop()

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
        source.current(0)

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
main_menu.add_command(label = "HomePage",command = home)

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
exit_data_btn = Button(head_frame,text = "Exit",font = ("cascadia code",13),command = exit_)
exit_data_btn.grid(row = 0,column = 4,padx = 5,pady = 5)
dataname = ""
data_heading_label = Label(head_frame,text = "data: "+dataname,font = ("cascadia code",16))
data_heading_label.grid(row = 0,column = 5,padx = 20)

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



