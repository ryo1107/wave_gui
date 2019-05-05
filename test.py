import os
import tkinter
from tkinter import filedialog
import numpy as np

data=np.array([1,2,3])
root = tkinter.Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "./",title = "Save as",filetypes =  [("CSV file","*.csv")])
root.filename=root.filename.split(".")[0]+".csv"
print (root.filename)
np.savetxt(root.filename,data)