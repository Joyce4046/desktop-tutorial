import tkinter as tk
import random


win = tk.Tk()
win.geometry('500x300')
win.config(bg = '#323232')

def test1(i):
    global number
    if number < 3:    
        number += 1
    temp = questions[i]
    answer[temp] = 1
    i += 1
    if i <= 3:
        question.config(text = questions[i])
        
    print(answer)
    

def test2(i):
    global number
    if number < 3:    
        number += 1
    answer[questions[i]] = 0
    i += 1
    if i <= 3:    
        question.config(text = questions[i])
        
    print(answer)
    

def test3():
    global number
    if number > 0:
        number -= 1
        answer[questions[number]] = ''
        question.config(text = questions[number])
    
    print(answer)

questions = ['想要親人的貓', '想要親貓的貓', '喜歡肉感的貓', '是否接受需要特殊醫療的貓']
number = 0
question = tk.Label(text = questions[number], bg = 'gray', fg = 'white', font = '微軟正黑體 25')
question.place(anchor = 'center', relx = 0.5, rely = 0.45)



answer = {}
ans_btn1 = tk.Button(text = '是', height = 1, width = 5, font = '微軟正黑體 20', command = lambda: test1(number))
ans_btn2 = tk.Button(text = '否', height = 1, width = 5, font = '微軟正黑體 20', command = lambda: test2(number))
ans_btn1.place(anchor = 'center', relx = 0.3, rely = 0.8)
ans_btn2.place(anchor = 'center', relx = 0.7, rely = 0.8)

back_btn = tk.Button(text = '上一題', font = '微軟正黑體 15', command = test3)
back_btn.place(anchor = 'center', relx = 0.9, rely = 0.9)

win.mainloop()