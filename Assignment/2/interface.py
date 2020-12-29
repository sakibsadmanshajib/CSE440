from tkinter import*
from PIL import ImageTk,Image
root = Tk()
root.config(bg="")
root.title("Baag-Bakhri")


def click():
    print("Hellow world!")
# ver_strip_image = PhotoImage(file='image/rsz_ver_strip.png')
diagonal_arrow_img_LDRU = ImageTk.PhotoImage(Image.open('image/ldru.png'))
diagonal_arrow_lbl_LDRU_1=Label(image= diagonal_arrow_img_LDRU)
diagonal_arrow_lbl_LDRU_2=Label(image= diagonal_arrow_img_LDRU)
diagonal_arrow_lbl_LDRU_3=Label(image= diagonal_arrow_img_LDRU)
diagonal_arrow_lbl_LDRU_4=Label(image= diagonal_arrow_img_LDRU)

diagonal_arrow_lbl_LDRU_1.grid(row=1,column=4)
diagonal_arrow_lbl_LDRU_2.grid(row=3,column=2)
diagonal_arrow_lbl_LDRU_3.grid(row=1,column=8)
diagonal_arrow_lbl_LDRU_4.grid(row=3,column=6)
 

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

default_image = PhotoImage(file='image/default.png')
goat_image = PhotoImage(file="image/goat.png")
tiger_image = PhotoImage(file="image/tiger.png")

button_A1 = Button(root, border=0, image=goat_image, command=click).grid(row=0,column=0)
button_C1 = Button(root, border=0, image=goat_image, command=click).grid(row=4,column=0)
button_B2 = Button(root, border=0, image=goat_image, command=click).grid(row=2,column=3)
button_A3 = Button(root, border=0, image=default_image, command=click).grid(row=0,column=5)
button_C3 = Button(root, border=0, image=default_image, command=click).grid(row=4,column=5)
button_B4 = Button(root, border=0, image=tiger_image, command=click).grid(row=2,column=7)
button_A5 = Button(root, border=0, image=default_image, command=click).grid(row=0,column=9)
button_C5 = Button(root, border=0, image=default_image, command=click).grid(row=4,column=9)

def command():
    print("hellow world!")


root.mainloop()