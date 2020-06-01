import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

class Helper():
	def __init__(self, root):
		self.root = root
		self.root.config()  # ?
		self.root.title('Cat Adopting Helper')
		self.root.geometry('1000x600')
		initface(self.root)


class initface():
	def __init__(self, root):
		self.root = root
		self.initface = tk.Canvas(self.root,width=1000,height=500,bd=0, highlightthickness=0) # 設定畫布大小
		self.ft = tkFont.Font(family='内海フォント-Bold', size=15, weight=tkFont.BOLD)  #　設定文字字體、大小、粗細
		self.photo = ImageTk.PhotoImage(file = '圖片3.png')
		self.initface.create_image(400, 285, image=self.photo)  # 設定圖片在畫布上的位置
		self.initface.grid(sticky = tk.NE)
		self.btn1 = tk.Button(self.initface,text='小幫手Part 1',font = self.ft,bg="white",fg = 'pink',anchor = tk.Ｓ,command=self.change1)
		self.btn1.grid()
		self.btn2 = tk.Button(self.initface,text='小幫手Part 2',font = self.ft,bg="white",fg = 'pink',anchor = tk.Ｓ,command=self.change2)
		self.btn2.grid()
		self.initface.create_window(800, 330, width=200, height=40,window = self.btn1)  # 設定按鈕的位置、長寬
		self.initface.create_window(800, 380, width=200, height=40,window = self.btn2)


	def change1(self):
		self.initface.destroy()
		face1(self.root)
	def change2(self):
		self.initface.destroy()
		face2(self.root)

if __name__ == '__main__':  # ?
	root = tk.Tk()
	Helper(root)
	root.mainloop()