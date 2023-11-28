import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, OptionMenu, Text
class CurrencyConverter:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Currency Converter")
        self.ir=tk.Label(self.root, text="Indian Rupee", )
        self.ir.grid(column=1,row=1)
        self.sc=tk.Label(self.root, text="Select Country")
        self.sc.grid(column=1,row=2)
        self.convert=tk.Button(self.root, text="Convert",command=self.cc)
        self.convert.grid(column=1,row=3)
        self.clear=tk.Button(self.root, text="Clear All", command=self.clear)
        self.clear.grid(column=1,row=4)
        self.result=tk.Text(self.root, height=2, width=30)
        self.result.grid(column=2,row=3)
        self.e1=tk.Entry(self.root,width=35)
        self.e1.grid(column=2,row=1)
        self.options={
            "USD": 0.014,
            "AUS": 0.021,
            "CHINESE YUAN": 0.097,
            "UAED": 0.051,
            "JAPANESE YEN": 1.52,
            "RUSSIAN RUBBLE": 0.89
        }
        self.country_name = StringVar(self.root)
        self.country_name.set(None)
        self.menu=OptionMenu(self.root,self.country_name,*self.options)
        self.menu.grid(column=2,row=2)
        self.root.mainloop()
    def cc(self):
            try:
                self.amount_rs=self.e1.get()
                selected_country=self.country_name.get()
                selec_contry_val=self.options.get(selected_country)
                try:
                    self.currency=float(selec_contry_val)
                    self.amount=float(self.amount_rs)
                    self.converted=self.currency*self.amount
                    self.result.delete(1.0,tk.END)
                    self.result.insert(tk.INSERT,self.converted)
                except TypeError as error:
                    print('please select a country', error)
            except ValueError as error:
                print(error)
    def clear(self):
        self.e1.delete(0,tk.END)
        self.result.delete(1.0,tk.END)
        self.country_name.set(None)
        

if __name__ == "__main__":
    CurrencyConverter()
