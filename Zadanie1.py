from tkinter import *
from tkinter import ttk
import requests
import sys
import json
from requests.exceptions import ConnectionError
#from requests.exceptions import ValueError

try:
    table = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/")
    table_json = table.json()
except ConnectionError:
    with open('API.txt') as json_file:
        data = json.load(json_file)
else:
    with open('API.txt', 'w') as outfile:
        json.dump(table_json, outfile)
    
    with open('API.txt') as json_file:
        data = json.load(json_file)



rates = data[0]["rates"]

dictionary = {}

for i in range(len(rates)):
    dictionary["{} ({})". format(rates[i]["currency"],rates[i]["code"])] = rates[i]["mid"]


currency_list = []
for key in (dictionary):
    currency_list.append(key)



def counting():

    """
        * Function which count the value if type of data is correct
          and create a window on a canvas.  
    """
    
    if from_currency.get() == to_currency.get():
        
        note = Label(root, text = "Converting a currency into the same is ridiculous, isn't it?")
        note.config(font=('courier 15 bold'))
        #canvas1.create_window(400, 400, window = note)
        
    else:
        
        try:
            amount = float(money.get())
            
        except ValueError:
            note = Label(root, text = "Counting string is ridiculous, isn't it?")
            note.config(font=('courier 15 bold'))
            
        else:   
            from_rate = dictionary[from_currency.get()]
            to_rate = dictionary[to_currency.get()]
            
            note = Label(root, text = "It is {}.".format(round((from_rate/to_rate)*amount, 2)))
            note.config(font=('courier 15 bold'))
        
    canvas1.create_window(400, 400, window = note)
    
root= Tk()
root.title("Currency converter")
canvas1 = Canvas(root, width = 800, height = 600,  relief = 'raised')
canvas1.pack()

head_label = Label(root, text='Convert one currency to another one!')
head_label.config(font=('courier 25 bold'), fg = "black", bg = "pink",)
canvas1.create_window(400, 80, window=head_label)

from_label = Label(root, text='From:')
from_label.config(font=('courier 20 bold'))
canvas1.create_window(250, 150, window=from_label)

to_label = Label(root, text='To:')
to_label.config(font=('courier 20 bold'))
canvas1.create_window(550, 150, window=to_label)


from_currency = ttk.Combobox(root, values = currency_list)
from_currency.set("Choose a currency")
from_currency.config(font=('courier 13 bold'))
canvas1.create_window(250, 200, window = from_currency)

to_currency = ttk.Combobox(root, values = currency_list)
to_currency.set("Choose a currency")
to_currency.config(font=('courier 13 bold'))
canvas1.create_window(550, 200, window = to_currency)

amount_label = Label(root, text = "Type the amount:")
amount_label.config(font=('courier 20 bold'))
canvas1.create_window(400, 300, window = amount_label)

money = Entry(root, width = 20)
money.insert(0,'Amount')
money.config(font=('courier 13 bold'))
canvas1.create_window(400, 350, window = money)

    
button1 = Button(root, text='CONVERT', command = counting, bg='pink', fg='white', font=('courier 20 bold'), activebackground = 'grey')
canvas1.create_window(400, 450, window=button1)

quitt = Button(root, text = "Quit", command = root.destroy, bg='red', fg='white', font=('courier 20 bold'), activebackground = 'grey')
canvas1.create_window(400,525, window = quitt)

root.mainloop()

