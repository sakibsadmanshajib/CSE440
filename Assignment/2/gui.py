from tkinter import*
from PIL import ImageTk,Image
    class Adapter(self):
        G1_pos
        G2_pos
        G3_pos
        T_pos
        __init__(self,g1_pos,g2_pos,g3_pos,t_pos):
            self.G1_pos=g1_pos
            self.G2_pos=g2_pos
            self.G3_pos=g3_pos
            self.T_pos=t_pos


#from bagh_bakhri import Animal,Goat,Tiger
root = Tk()
root.config(bg="")
root.title("Baag-Bakhri")



goat_img_URL='image/goat.png'
tiger_img_URL='image/tiger.png'
default_img_URL='image/default.png'


def click():
    print("Hellow world!")
# ver_strip_image = PhotoImage(file='image/rsz_ver_strip.png')
# LDRU-> Left down right up
diagonal_arrow_img_LDRU = ImageTk.PhotoImage(Image.open('image/ldru.png'))
diagonal_arrow_lbl_LDRU_1=Label(image= diagonal_arrow_img_LDRU)
diagonal_arrow_lbl_LDRU_2=Label(image= diagonal_arrow_img_LDRU)
diagonal_arrow_lbl_LDRU_3=Label(image= diagonal_arrow_img_LDRU)
diagonal_arrow_lbl_LDRU_4=Label(image= diagonal_arrow_img_LDRU)

diagonal_arrow_lbl_LDRU_1.grid(row=1,column=4)
diagonal_arrow_lbl_LDRU_2.grid(row=3,column=2)
diagonal_arrow_lbl_LDRU_3.grid(row=1,column=8)
diagonal_arrow_lbl_LDRU_4.grid(row=3,column=6)
 
#RULD-> Right up left down
diagonal_arrow_img_RULD = ImageTk.PhotoImage(Image.open('image/ruld.png'))
diagonal_arrow_lbl_RULD_1=Label(image= diagonal_arrow_img_RULD)
diagonal_arrow_lbl_RULD_2=Label(image= diagonal_arrow_img_RULD)
diagonal_arrow_lbl_RULD_3=Label(image= diagonal_arrow_img_RULD)
diagonal_arrow_lbl_RULD_4=Label(image= diagonal_arrow_img_RULD)

diagonal_arrow_lbl_RULD_1.grid(row=1,column=2)
diagonal_arrow_lbl_RULD_2.grid(row=3,column=4)
diagonal_arrow_lbl_RULD_3.grid(row=1,column=6)
diagonal_arrow_lbl_RULD_4.grid(row=3,column=8)


ver_arrow_img = ImageTk.PhotoImage(Image.open('image/ver_arrow.png'))
vertical_arrow_lable_1 = Label(image=ver_arrow_img)
vertical_arrow_lable_2 = Label(image=ver_arrow_img)
vertical_arrow_lable_3 = Label(image=ver_arrow_img)
vertical_arrow_lable_4 = Label(image=ver_arrow_img)
vertical_arrow_lable_5 = Label(image=ver_arrow_img)
vertical_arrow_lable_6 = Label(image=ver_arrow_img)
vertical_arrow_lable_7 = Label(image=ver_arrow_img)
vertical_arrow_lable_8 = Label(image=ver_arrow_img)
vertical_arrow_lable_9 = Label(image=ver_arrow_img)


vertical_arrow_lable_1.grid(row=1,column=0)
vertical_arrow_lable_2.grid(row=2,column=0)
vertical_arrow_lable_3.grid(row=3,column=0)
vertical_arrow_lable_4.grid(row=1,column=5)
vertical_arrow_lable_5.grid(row=2,column=5)
vertical_arrow_lable_6.grid(row=3,column=5)
vertical_arrow_lable_7.grid(row=1,column=9)
vertical_arrow_lable_8.grid(row=2,column=9)
vertical_arrow_lable_9.grid(row=3,column=9)

default_image = PhotoImage(file='')
goat_image = PhotoImage(file=goat_img_URL)
tiger_image = PhotoImage(file="")

def click_A0(self, animal):
    pass

def click_A2(self, animal):
    pass

def click_A4(self, animal):
    pass

def click_B1(self,animal):
    pass

def click_B3(self, animal):
    pass

def click_C0(self, animal):
    pass

def click_C2(self, animal):
    pass

def click_C3(self, animal):
    pass

button_A0 = Button(root, border=0, image=goat_image, command=click_A0).grid(row=0,column=0)
button_A2 = Button(root, border=0, image=goat_image, command=click_A2).grid(row=4,column=0)
button_A4 = Button(root, border=0, image=goat_image, command=click_A4).grid(row=2,column=3)
button_B1 = Button(root, border=0, image=default_image, command=click_B1).grid(row=0,column=5)
button_B3 = Button(root, border=0, image=default_image, command=click_B3).grid(row=4,column=5)
button_C0 = Button(root, border=0, image=tiger_image, command=click_C0).grid(row=2,column=7)
button_C2 = Button(root, border=0, image=default_image, command=click_C2).grid(row=0,column=9)
button_C4 = Button(root, border=0, image=default_image, command=click_C3).grid(row=4,column=9)



def command():
    print("hellow world!")


root.mainloop()