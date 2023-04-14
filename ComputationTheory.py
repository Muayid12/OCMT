# libraries 
import tkinter as tk # Note require to install this library to use the code >> pip install tk
from tkinter import * 
import re # regular expression

#============================================================       

# finite automata function      
def check_nfa(user_text):
    
    if set(user_text) - set(['a', 'b']): #(Checking if user input contain only our alphabet)
        return False
    elif len(user_text) < 4: #(Checking if our string contain 4 or more character from our alphabet if its less then false because cant be there 4th character in string)
        return False
    else:
        temp = list(user_text)
        if temp[-4] == 'b': #("checking if user input the input fourth before last is b")
            return True
        else:
            return False
        
#   Regular expresion 
def regular_expresion(user_text):
    if set(user_text) - set(['a', 'b']): #(Checking if user input is same as our alphabet)
        return False
    else:
        pattern = "^(b|aaa(a)*)*$" #(regular expression for the question)
        return bool(re.match(pattern, user_text)) #("to check if the user input suit this regular expression or not so it will return for us true or false")

# Functions for label changes 
#==============================================================
    
def checkup():
    userinput1 = input1.get()
    if check_nfa(userinput1): #if this function return true then put tick 
        result_label.config(text="✓",fg="green")
    else: #if this function return false then put X  
        result_label.config(text="X",fg="Red")
        
def checkup1():
    userinput2 = input2.get() 
    if regular_expresion(userinput2): #if this function return true then put tick 
        result_label1.config(text="✓",fg="green")
    else: #if this function return false then put X  
        result_label1.config(text="X",fg="Red")
    
#GUI section
#============================================================================
# Frame settings 
root = tk.Tk()
root.geometry("420x140")
root.title("Assingment competition theory")

# Labels section
first_label = Label(root, text="        All string such the fourth to last symbol is always a 'b': ")
first_label.grid(row=0 , column=0,columnspan=4) 
second_label = Label(root, text="Enter the text: ")
second_label.grid(row=1 , column=0,pady=5) 
third_label = Label(root, text="        All strings in which every run of ‘a’ has length at least 3: ")
third_label.grid(row=2 , column=0,columnspan=4,pady=10) 
forth_label = Label(root, text="Enter the text: ")
forth_label.grid(row=5 , column=0,pady=5) 
result_label = Label(root,text="",font=18)
result_label.grid(row=1,column=3)
result_label1 = Label(root,text="",font=18)
result_label1.grid(row=5,column=3)

# Entry section
input1 = Entry(root, width=25)
input1.grid(row=1, column=1)
input2 = Entry(root, width=25)
input2.grid(row=5, column=1)

# Buttons section 
checking_button = tk.Button(root, text="check",state="normal",width=10,command=checkup)
checking_button.grid(row=1,column=4)
checking_button2 = tk.Button(root, text="check",state="normal",width=10,command=checkup1)
checking_button2.grid(row=5,column=4)

#Execute gui
root.mainloop()






