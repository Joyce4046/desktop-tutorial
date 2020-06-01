import tkinter as tk
from PIL import Image, ImageTk

class Showing3Cats(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.title_words()
        self.images()
        self.infos()
        self.main_page_btn()

    def title_words(self):
        self.title = tk.Label(self, height = 3, text='最適合你的貓咪', font=('Times', 20, 'bold'), bg='green')
        self.title.grid(row = 0, column = 0, columnspan=3, sticky = tk.NE + tk.SW)

    def resize(self, w_box, h_box, pil_image):  
        w, h = pil_image.size
        f1 = 1.0*w_box/w  
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_image.resize((width, height), Image.ANTIALIAS) 

    def images(self):
        w = 100
        h = 300
        wt = 200
        ht = 200
        img1 = Image.open('src\\cats\\Dodo.jpg')
        img1_resized = self.resize(wt, ht, img1)
        img2 = Image.open('src\\cats\\Lulu.jpg')
        img2_resized = self.resize(wt, ht, img2)
        img3 = Image.open('src\\cats\\Peter.jpg')
        img3_resized = self.resize(wt, ht, img3)

        self.photo1 = ImageTk.PhotoImage(img1_resized)
        self.photo2 = ImageTk.PhotoImage(img2_resized)
        self.photo3 = ImageTk.PhotoImage(img3_resized)

        self.image1 = tk.Label(self, image = self.photo1, height = h, width = w, bg='red')
        self.image2 = tk.Label(self, image = self.photo2, height = h, width = w, bg='blue')
        self.image3 = tk.Label(self, image = self.photo3, height = h, width = w, bg='purple')

        self.image1.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.image2.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.image3.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)

    def infos(self):
        w = 37
        self.info1 = tk.Label(self, height = 10, width = w, text = 'name: \nage: \nothers: \nurl: ', anchor="w", justify = 'left')
        self.info2 = tk.Label(self, height = 10, width = w, text = 'name: \nage: \nothers: \nurl:', anchor="w", justify = 'left')
        self.info3 = tk.Label(self, height = 10, width = w, text = 'name: \nage: \nothers: \nurl: ', anchor="w", justify = 'left')

        self.info1.grid(row = 2, column = 0, sticky = tk.W)
        self.info2.grid(row = 2, column = 1, sticky = tk.W)
        self.info3.grid(row = 2, column = 2, sticky = tk.W)

    def main_page_btn(self):
        self.main_page = tk.Button(self, height = 2, text='Main Page')
        self.main_page.grid(row=3, column=0, columnspan=3, sticky = tk.NE + tk.SW)

window = Showing3Cats()
window.master.title('cats')
window.master.geometry('800x600')
window.configure(background='white')
window.mainloop()
