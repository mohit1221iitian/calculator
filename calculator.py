from tkinter import *
from PIL import Image,ImageTk
import os

first_number=second_number=operator=None

def get_digit(digit):
	current=result_label['text']
	new=current+str(digit)
	result_label.config(text=new)
def clear():
	result_label.config(text='')
def get_operator(op):
	global first_number,operator
	first_number=int(result_label['text'])
	operator=op
	result_label.config(text='')
def get_result():
	global first_number,second_number,operator
	second_number=int(result_label['text'])
	if operator=='+':
		result_label.config(text=str(first_number+second_number))
	elif operator=='-':
		result_label.config(text=str(first_number-second_number))
	elif operator=='*':
		result_label.config(text=str(first_number*second_number))
	else :
		if second_number==0:
			result_label.config(text='ERROR')
		else:	
			result_label.config(text=str(first_number/second_number))


root=Tk()
root.title('CALCULATOR')
# root.minsize(500,700)
# root.maxsize(500,700)
root.geometry('306x406')
root.resizable(0,0)
root.configure(background='light blue') 
result_label=Label(root,text='',bg='light blue',fg='orange')
result_label.configure(font=('arial',35,'bold'))
result_label.grid(row=0,column=0,columnspan=1000,sticky='w',pady=(10,40))


btn7=Button(root,text='7',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text='8',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text='9',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text='+',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)



btn4=Button(root,text='4',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text='5',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text='6',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text='-',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)

btn1=Button(root,text='1',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text='2',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text='3',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn_multiply=Button(root,text='*',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_operator('*'))
btn_multiply.grid(row=3,column=3)

btn_clear=Button(root,text='C',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=clear)
btn_clear.grid(row=4,column=0)
btn0=Button(root,text='0',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn_equals=Button(root,text='=',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=get_result)
btn_equals.grid(row=4,column=2)
btn_divide=Button(root,text='/',bg='light green',fg='black',font=('bold',28),width=3,height=1,command=lambda:get_operator('/'))
btn_divide.grid(row=4,column=3)
root.mainloop()