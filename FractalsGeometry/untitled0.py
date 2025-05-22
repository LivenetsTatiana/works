import numpy as np
import pandas as pd
import glob
from tkinter import *
from openpyxl import load_workbook

file_SPF = 'SPF_template.xlsx'
file_1 = '1.asc'
file_2 = '2.asc'
file_3 = '3.asc'
file_4 = '4.asc'

df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)
df3 = pd.read_csv(file_3)
df4 = pd.read_csv(file_4)

df1.to_excel(file_SPF, sheet_name = 'Лист1', index=False)
df2.to_excel(file_SPF, sheet_name = 'Лист2', index=False)
df3.to_excel(file_SPF, sheet_name = 'Лист3', index=False)
df4.to_excel(file_SPF, sheet_name = 'Лист4', index=False)


workbook = loadworkbook (filename="SPF_template.xlsx")
sheet = workbook['Лист5']
SPF_value = sheet["R2"].value


window = Tk()
window.title("Расчет значений SPF от Арбанаса Стефана")  
lbl = Label(window, text="Здраствуйте, SPF = ", SPF_value)  
lbl.grid(column=0, row=0)  
window.mainloop()


print(SPF_value)