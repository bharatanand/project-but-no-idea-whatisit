# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:33:53 2022

@author: User
"""
# ------------------------------------------------------------------------------
#                        list and dictonary -button backend
# ------------------------------------------------------------------------------

from tkinter import *

class list_working_function:

    def __init__(self, String):
        list_temp = []  # empty list
        l1 = list(String.split(" "))
        for i in l1:
            list_temp.append(int(i))
        self.list_temp = list_temp

    def display(self):
        str1 = str(self.list_temp)
        return str1

    def search(self, index):
        self.index = index
        index1 = []
        for x in range(len(self.list_temp)):
            if index == self.list_temp[x]:
                print(x)
                index1.append(x)
        return str(index1)

    def sort(self):

        def partition(array, low, high):

            pivot = array[high]
            i = low - 1

            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)

        data = self.list_temp
        size = len(data)
        quickSort(data, 0, size - 1)
        return str(data)

class Dicitionaries_working_function:

    def __init__(self, String):
        self.String = String
        l1 = list(String.split(" "))
        dicitionary_temp = {}
        for i in range(len(l1)):
            dicitionary_temp[i] = int(l1[i])
        self.dicitionary_temp = dicitionary_temp

    def display(self):
        str2 = str(self.dicitionary_temp)
        return str2

    def search(self, index):
        self.index = index
        index1 = []
        for x in range(len(self.dicitionary_temp)):
            if index == self.dicitionary_temp[x]:
                index1.append(x)
        return str(index1)

    def sort(self):
        list = []
        for i in self.dicitionary_temp:
            list.append(self.dicitionary_temp[i])
# algo starts here
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1

            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)

        data = list
        size = len(data)
        quickSort(data, 0, size - 1)
        dicti = {}

        for i in range(len(data)):
            dicti[i] = data[i]

        return str(dicti)

# ------------------------------------------------------------------------------
#               list button and dictionary button
# ------------------------------------------------------------------------------


def List_Button():
    global flag
    flag = 1  # list selected
    window.destroy()
    return 0


def Dictionary_Button():
    global flag
    flag = 2
    window.destroy()
    return 0


# ------------------------------------------------------------------------------
#               code execution from here
# ------------------------------------------------------------------------------
flag = 0
action = 0
window = Tk()

window.geometry('500x500')
window.title("Project 1")
l = Label(window, text="Choose the starting Data Type list or Dicitionary",font=("Arial", 15)).place(x=30, y=50)
button = Button(window, text="List", bd=10, width=25,command=List_Button).place(x=100, y=150)
but = Button(window, text="Dicitionary", bd=10, width=25,command=Dictionary_Button).place(x=100, y=250)
window.mainloop()  # window will stay open until we destroy it


# ------------------------------------------------------------------------------
#                        common data entry page
# ------------------------------------------------------------------------------


def data_entry_page(string):
    def submit_button():
        global input_string
        input_string = Entr.get()
        windo.destroy()

    windo = Tk()
    windo.geometry('800x500')
    windo.title("Project 1")
    l = Label(windo, text=string,font=("Arial", 15)).place(x=100, y=100)
    Entr = Entry(windo, width=50)
    Entr.pack(padx=100, pady=140)
    button = Button(windo, text='Submit',command=submit_button).place(x=150, y=200)
    windo.mainloop()


data_entry_page("Please enter the data")

global l1, d1
def action_flag_set1():
    global action
    action=1
    wino.destroy()
def action_flag_set2():
    global action
    action=2
    wino.destroy()

string1 = input_string
from tkinter import *

vstring1=input_string
from tkinter import *
wino = Tk()
wino.geometry('500x400')
wino.title("Project 1")
if flag==1:
    l1=list_working_function(string1)
    la1=Label(wino,text="The submitted list is ....",font=("Arial", 15)).place(x=100,y=50)
    la2=Label(wino,text=l1.display(),font=("Arial", 15)).place(x=100,y=100)

else:
    d1=Dicitionaries_working_function(string1)
    la1=Label(wino,text="The submitted Dicitionary is ....",font=("Arial", 15)).place(x=100,y=50)
    la2=Label(wino,text=d1.display(),font=("Arial", 12)).place(x=100,y=100)
button1 = Button(wino, text="Sorting", bd=10,width=25,command=action_flag_set2).place(x=40,y=200)
button2 = Button(wino, text="Searching", bd=10,width=25,command=action_flag_set1).place(x=250,y=200)
wino.mainloop()



def exit_function():
    global action
    action=0
    wino.destroy()
while action != 0:
    if action == 1 and flag==1:
        print("do searching ")
        data_entry_page("Please enter the number you want to search in list")
        data=int(input_string)
        print(data)
        print(l1.search(data))
        from tkinter import *
        wino = Tk()
        wino.geometry('500x400')
        wino.title("Project 1")
        la1 = Label(wino, text="The Searched list element is at ....", font=("Arial", 15)).place(x=100, y=50)
        la2 = Label(wino, text=l1.search(data)+" indexs", font=("Arial", 12)).place(x=100, y=100)
        button1 = Button(wino, text="Sorting", bd=10, width=25, command=action_flag_set2).place(x=40, y=200)
        button2 = Button(wino, text="Exit", bd=10, width=25, command=exit_function).place(x=250, y=200)
        wino.mainloop()



    elif action == 2 and flag==1:
        print("do sortinging in list")
        from tkinter import *
        wino = Tk()
        wino.geometry('500x400')
        wino.title("Project 1")
        la1 = Label(wino, text="The Sorted list is .......", font=("Arial", 15)).place(x=100, y=50)
        la2 = Label(wino, text=l1.sort()+" indexs", font=("Arial", 12)).place(x=100, y=100)
        button1 = Button(wino, text="searching", bd=10, width=25, command=action_flag_set1).place(x=40, y=200)
        button2 = Button(wino, text="Exit", bd=10, width=25, command=exit_function).place(x=250, y=200)
        wino.mainloop()




    elif action == 1 and flag==2:
        print("do searching in dicitionary")
        data_entry_page("Please enter the number you want to search in Dicitionary")
        data=int(input_string)
        from tkinter import *
        wino = Tk()
        wino.geometry('500x400')
        wino.title("Project 1")
        la1 = Label(wino, text="The Searched list element is at ....", font=("Arial", 15)).place(x=100, y=50)
        la2 = Label(wino, text=d1.search(data)+" indexs", font=("Arial", 12)).place(x=100, y=100)
        button1 = Button(wino, text="Sorting", bd=10, width=25, command=action_flag_set2).place(x=40, y=200)
        button2 = Button(wino, text="Exit", bd=10, width=25, command=exit_function).place(x=250, y=200)
        wino.mainloop()

    elif action == 2 and flag==2:
        print("do sorting in dicitionary")
        from tkinter import *
        wino = Tk()
        wino.geometry('500x400')
        wino.title("Project 1")
        la1 = Label(wino, text="The Searched list element is at ....", font=("Arial", 15)).place(x=100, y=50)
        la2 = Label(wino, text=d1.sort()+" indexs", font=("Arial", 12)).place(x=100, y=100)
        button1 = Button(wino, text="Searching", bd=10, width=25, command=action_flag_set1).place(x=40, y=200)
        button2 = Button(wino, text="Exit", bd=10, width=25, command=exit_function).place(x=250, y=200)
        wino.mainloop()









