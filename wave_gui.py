import os,sys

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import numpy as np
import matplotlib.pyplot as plt

# 参照ボタンのイベント
# button1クリック時の処理
def select_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    load_file.set(filepath)

data_list=[]
def load_clicked():
    data_path=load_file.get()
    data_name=data_path.split("/")[-1].split(".")[0]
    data_list.append(data_name)
    globals()[data_name]=np.loadtxt(data_path,delimiter=",")
    print(globals()[data_name])
    wave['values']=(data_list)

def table_clicked():
    pass

def display_clicked():
    print(globals()[wave_name.get()])
    plt.plot(globals()[wave_name.get()])
    plt.show()

def analyze_clicked():
    pass

def save_csv_clicked():
    save_name =  filedialog.asksaveasfilename(initialdir = "./",title = "Save as",filetypes =  [("CSV file","*.csv")])
    save_name = save_name.split(".")[0]+".csv"
    
    if save_name==".csv":
        print("Input file_name")
        pass
    else:
        print (f"Save:{save_name}")
        np.savetxt(save_name,globals()[wave_name.get()])

#コンボボックスを押した時の反応用関数
def select_wave(event):
    print(wave_name.get())

def analyze_wave(event):
    print(analyze_name.get())

if __name__ == "__main__":
    # mainの作成
    main = tk.Tk()
    main.title('Main')
    # main.geometry("1000x1000")
    main.resizable(False, False)

    # Frame1の作成
    frame1 = tk.Frame(main,borderwidth = 5)
    frame1.grid()

    # Frame2の作成
    frame2 = tk.Frame(main,borderwidth = 5)
    frame2.grid(row=1,sticky=tk.E)

    # Frame3の作成
    frame3 = tk.Frame(main,borderwidth = 5)
    frame3.grid(row=2)

    # Frame4の作成
    frame4 = tk.Frame(main,borderwidth = 5)
    frame4.grid(row=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = tk.StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ボタンの作成
    select_button = ttk.Button(frame1, text=u'参照', command=select_clicked)
    select_button.grid(row=0, column=3)

    # 参照ファイルパス表示ラベルの作成
    load_file = tk.StringVar()
    load_file_entry = ttk.Entry(frame1, textvariable=load_file, width=50)
    load_file_entry.grid(row=0, column=2)

    # Cancelボタンの作成
    quit_button = ttk.Button(frame2, text='Quit', command=quit)
    # quit_button.grid(row=1, column=3)
    quit_button.pack(side=tk.RIGHT)

    # Loadボタンの作成
    load_button = ttk.Button(frame2, text='Load', command=load_clicked)
    # load_button.grid(row=1, column=2)
    load_button.pack(side=tk.RIGHT)
    
    # Tableボタンの作成
    table_button = ttk.Button(frame4, text='Table', command=table_clicked)
    table_button.pack(side=tk.LEFT)
    # Displayボタンの作成
    display_button = ttk.Button(frame4, text='Display', command=display_clicked)
    display_button.pack(side=tk.LEFT)
    # analyzeボタンの作成
    analyze_button = ttk.Button(frame4, text='Analyze', command=analyze_clicked)
    analyze_button.pack(side=tk.LEFT)
    # save_csvボタンの作成
    save_csv_button = ttk.Button(frame4, text='Save_CSV', command=save_csv_clicked)
    save_csv_button.pack(side=tk.LEFT)

    # ラベルの作成
    # 「wave」ラベルの作成
    wave_s = tk.StringVar()
    wave_s.set('wave>>')
    wave_label = ttk.Label(frame3, textvariable=wave_s)
    wave_label.grid(row=0, column=0)
    #コンボボックス
    wave_name = tk.StringVar()
    wave = ttk.Combobox(frame3, textvariable=wave_name)
    wave.bind('<<ComboboxSelected>>' , select_wave)
    wave.grid(row=0, column=1)
    wave.grid_configure(padx=5, pady=5)

    # ラベルの作成
    # 「analyze」ラベルの作成
    analyze_s = tk.StringVar()
    analyze_s.set('analyze>>')
    analyze_label = ttk.Label(frame3, textvariable=analyze_s)
    analyze_label.grid(row=0, column=3)
    #コンボボックス
    analyze_name = tk.StringVar()
    analyze = ttk.Combobox(frame3, textvariable=analyze_name)
    analyze.bind('<<ComboboxSelected>>' , analyze_wave)
    analyze.grid(row=0, column=4)
    analyze.grid_configure(padx=5, pady=5)

    main.mainloop()
