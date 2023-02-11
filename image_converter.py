 
import tkinter as tk 
from tkinter import filedialog,StringVar,OptionMenu,messagebox,Checkbutton
import glob,os
import windnd,tkinter
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

#================================================================
filename = ""
fileDir = ""
name =""
extension = ""
r=255
g=255
b=255
root = tk.Tk()
root['bg'] = "white"
root.title('image converter')
# root.iconbitmap('C:/Users/User/Documents/education/py/yt_project/image_file_converter/man_ico.ico')
root.geometry('500x350')
root.resizable(width = False, height = False) 
#================================================================

option = ["png","jpeg","ico","pdf","jpg","svg"]
def convert_to():
    global img_export
    img_export = StringVar(root) 
    img_export.set(option[0])
    question_menu = OptionMenu(root, img_export , *option)
    question_menu.pack()

def transparent_colour():
    global name
    name = str(entry_field.get())
    return name  

def dragged_files(files):
    clear_history()
    global fileDir
    fileDir = '\n'.join((item.decode('gbk') for item in files))
    global filename
    filename = os.path.basename(fileDir)  

    # saperate files and extension
    (files, ext) = os.path.splitext(filename)
    global extension
    extension = ext.replace('.', '')
    print(extension)

    print(fileDir)
    x = fileDir
    img = Image.open(x) 
    img = img.resize((100, 100), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img) 
    panel = tk.Label(root, image = img) 
    panel.image = img
    # place image in frame
    label1 = tk.Label(frame, image=img)
    label1.pack()

    # show file name
    label2 = tk.Label(frame, text=filename,fg="black")    
    label2.pack()

    # get the inserted color code
    exp = str(img_export.get())
    if extension == ("png") and exp == ("png"):
        transparent_colour() 

# remove everything in frame
def clear_history():    
    for widget in frame.winfo_children():
        widget.destroy() 

def convert_now():
    # using try, exccept, else is to display message box
    # try = all the operation stored there

    try:
        
        global exp
        exp = str(img_export.get())
        # remove background color condition
        if extension == ("png") and exp == ("png"):
            img = Image.open(fileDir) 
            rgba = img.convert("RGBA") 
            datas = rgba.getdata() 
            
            # convert to the list
            list = transparent_colour()
            list1 = list.split (",") # seperate by comma

            # convert each element as integers
            li = []
            for i in list1:
                li.append(int(i))

            global r,g,b
            r = (li[0])
            g = (li[1])
            b = (li[2])
            print(r,g,b)
            newData = [] 
            for item in datas: 
                # get_rgb()
                # if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value 
                # if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding white colour by its RGB value 
                if item[0] == r and item[1] == g and item[2] == b:  # finding white colour by its RGB value 

                    # storing a transparent value when we find a black colour 
                    newData.append((255, 255, 255, 0)) 
                else: 
                    newData.append(item)  # other colours remain unchanged 
            
            rgba.putdata(newData) 
            name = os.path.splitext(fileDir)[0] # remove the current file extension
            name = name+".png"   # save as new name
            print(name)
            rgba.save(name, "PNG") 

        else:
            im = Image.open(fileDir)   # open file
            rgb_im = im.convert('RGB')
            rgb_im.save(fileDir.replace(extension,exp),quality = 95) # convert current  file according to the selected operation

    except:
        # error occur
        result="failed"
        messagebox.showinfo(result)

    else:
        result = "sucess"
        messagebox.showinfo("result",result)
    print(fileDir)

tk.Label(text="",bg="white").pack()
a = tk.Label(text=" convert to png and select png image to remove plane bg color",bg="white",fg="grey", font=('Helvectia',12))
a.pack()

b = tk.Label(text="fill the blank with the background color code ",bg="white",fg="grey", font=('Helvectia',11))
b.pack()

tk.Label(text="convert to").pack()
convert_to()

entry_field = tk.Entry()
entry_field.pack() 

b = tk.Label(text="Drop your image here ",bg="white",fg="grey")
b.pack()

dragged_files
windnd.hook_dropfiles(root,func= dragged_files)

frame = tk.Frame(root, bg="#988c89") # create frame to insert selected picture
frame.place()
frame.pack()

convert = tk.Button(root, text="convert now", padx = 10, pady = 5, fg ="white",bg="#263D42",command=convert_now)
convert.pack()

root.mainloop()
print(r,g,b)
print(b)
print(g)

