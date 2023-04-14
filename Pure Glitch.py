#=================PURE GLITCH=====================#
#LICENSE: MIT
#AUTHOR: Akash Bora
#Version: 0.2

import tkinter
import customtkinter
import tkdial
from PIL import Image, ImageTk, ImageFile
import random
import os
import copy
import math
import platform
import random
import re
import time
import sys
import threading
import webbrowser

class App(customtkinter.CTk):
    
    WIDTH = 700
    HEIGHT = 400
    
    global resource
    def resource(relative_path):
        base_path = getattr(
            sys,
            '_MEIPASS',
            os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    customtkinter.set_appearance_mode("Dark") 
    customtkinter.set_default_color_theme("green")
    
    def __init__(self):
        
        super().__init__()
        global ofile, sfile
        
        ofile=""
        sfile=""
        self.title("Pure Glitch")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<1>", lambda event: event.widget.focus_set())
        self.icopath = ImageTk.PhotoImage(file=resource("Assets/icon2.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.icopath)
        
        if sys.platform.startswith("win"):
            try:
                import ctypes
                ctypes.windll.shcore.SetProcessDpiAwareness(0)
                HWND = ctypes.windll.user32.GetParent(self.winfo_id())
                ctypes.windll.dwmapi.DwmSetWindowAttribute(HWND, 35, ctypes.byref(ctypes.c_int(0x00292929)), ctypes.sizeof(ctypes.c_int))
            except:
                pass
            
        def forget_everything():
            self.entry.place_forget()
            self.button_browse.place_forget()
            self.logo.place_forget()
            self.recipe.grid_forget()
            self.recipe_bar.grid_forget()
            self.optionmenu_1.place_forget()
            self.optionmenu_2.place_forget()
            self.bar.place_forget()
            self.slider_1.grid_forget()
            self.slider_2.grid_forget()
            self.slider_3.grid_forget()
            self.slider_4.grid_forget()
            self.label1.place_forget()
            self.label2.place_forget()
            self.label3.place_forget()
            self.label4.place_forget()
            self.dynamiclabel_1.place_forget()
            self.dynamiclabel_2.place_forget()
            self.dynamiclabel_3.place_forget()
            self.dynamiclabel_4.place_forget()
            self.button_glitch.place_forget()
            self.entry2.place_forget()
            self.replace.place_forget()
            self.button_browse2.place_forget()
            self.button_next.place_forget()
            image_label.grid_forget()
            self.label_oops.place_forget()
            self.button_random.place_forget()
            self.label_log.place_forget()
            self.label_version.place_forget()
            
        def place_front():
            forget_everything()
            self.entry.place(x=20,y=270)
            self.button_browse.place(x=565,y=270)
            self.logo.place(x=130,y=0)
            self.button_next.place(x=220,y=315)
            self.label_version.place(x=570,y=5)
            
        def place_process():
            if not os.path.exists(self.entry.get()):
                self.button_next.configure(fg_color="gray30")
                self.entry.configure(text_color="orange")
                return
            else:
                self.button_next.configure(fg_color=customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
                self.entry.configure(text_color="gray50")
                
            forget_everything()
            self.recipe.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky="wn")
            self.recipe_bar.grid(row=0, column=0, columnspan=2, padx=15, pady=40, sticky="wn")
            self.bar.place(x=440,y=75)
            self.optionmenu_1.place(x=20,y=65)
            self.optionmenu_2.place(x=250,y=65)
            self.slider_1.grid(row=0, column=0, columnspan=2, padx=15, pady=120, sticky="wn")
            self.slider_2.grid(row=0, column=0, columnspan=2, padx=15, pady=160, sticky="wn")
            self.slider_3.grid(row=0, column=0, columnspan=2, padx=15, pady=200, sticky="wn")
            self.slider_4.grid(row=0, column=0, columnspan=2, padx=15, pady=240, sticky="wn")
            self.label1.place(x=369,y=103)
            self.label2.place(x=355,y=143)
            self.label3.place(x=368,y=183)
            self.label4.place(x=330,y=223)
            self.dynamiclabel_1.place(x=20,y=103)
            self.dynamiclabel_2.place(x=20,y=143)
            self.dynamiclabel_3.place(x=20,y=183)
            self.dynamiclabel_4.place(x=20,y=223)
            self.button_glitch.place(x=440,y=230)
            self.entry2.place(x=20,y=280)
            self.replace.place(x=520, y=325)
            self.button_browse2.place(x=565,y=280)
            self.button_random.place(x=560,y=60)
            if self.string_log.get()!="":
                self.label_log.place(x=20,y=320)
                
        def dynamic1(value):
            self.dynamiclabel_1.configure(text= str(int(value)))
        def dynamic2(value):
            self.dynamiclabel_2.configure(text= str(int(value)))
        def dynamic3(value):
            self.dynamiclabel_3.configure(text= str(int(value)))
        def dynamic4(value):
            self.dynamiclabel_4.configure(text= str(int(value)))
            
        def open_function():
            global ofile, ffile
            ofile = tkinter.filedialog.askopenfilename(filetypes =[('Image File', ['*.png','*.jpg','*.bmp','*.webp','*jpeg','*gif']),('All Files', '*.*')])
            if ofile:
                self.button_next.configure(fg_color=customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
                self.entry.configure(text_color="gray50")
                var1.set(ofile)
                self.extension = ofile[-3:]
                s=1
                ffile = ofile[:-4]+"_glitched."+self.extension
                while os.path.exists(ffile):
                    ffile = ofile[:-4]+"_glitched_"+str(s)+"."+self.extension
                    s+=1
                var2.set(ffile)
                
        def output_folder():
            global ffile
            ffile = tkinter.filedialog.asksaveasfilename(filetypes =[('Image', ['*.png','*.jpg','*.bmp','*.webp','*jpeg','*gif'])],
                                                         initialfile=os.path.basename(ofile)[:-4]+"_glitched."+self.extension,
                                                         defaultextension=self.extension)
            if ffile==ofile:
                return
            if ffile:
                var2.set(ffile)
            
        def viewer():
            global image1, sfile
            if not sfile:
                return
            try:
                forget_everything()
                ImageFile.LOAD_TRUNCATED_IMAGES = True
                
                if os.path.exists(outPath):
                    image_label.configure(image=None)
                    image1 = customtkinter.CTkImage(Image.open(outPath), size=((self.frame_right.winfo_width(), self.frame_right.winfo_height())))
                    image_label.configure(image=image1)
                    image_label.grid()
                    if self.extension=="png":
                        self.label_oops.configure(text="Currently this image viewer is in beta stage and \ncannot display broken PNG images!")
                        self.label_oops.place(x=200,y=150)

            except:
                self.label_oops.configure(text="Unable to display this file!")
                self.label_oops.place(x=220,y=150)
                
        def glitch_it():        
            self.button_glitch.configure(state=tkinter.DISABLED)
            self.bar.set(0)
        
            try:
                threading.Thread(target=process).start()
            except:
                self.button_glitch.configure(state=tkinter.NORMAL)
                self.bar.set(0)
                self.bar.configure(text="OOPS!")
                self.string_log.set("Something went wrong!")
                self.label_log.place(x=20,y=320)
                
        def process():
            self.label_log.place_forget()     
            global ofile, var2, sfile

            self.after(100, self.bar.set(10))
            if not self.optionmenu_1.get()=="Copy":
                try:
                    ifile = ofile[:-4]+"_intermediate."+self.optionmenu_1.get().lower()
                    Image.open(ofile).convert('RGB').save(ifile)
                except:
                    self.button_glitch.configure(state=tkinter.NORMAL)
                    self.bar.set(0)
                    self.bar.configure(text="OOPS!")
                    self.string_log.set("Conversion error!")
                    self.label_log.place(x=20,y=320)
                    return
                sfile = ifile
            else:
                sfile=ofile
            
            def writeFile(fileByteList, fileNum, iteration, bytesTochange, seed):
                global var2, outPath
                outPath = var2.get()
                try:
                    if os.path.isfile(outPath):
                        os.remove(outPath)
                    open(outPath, "wb").write(bytes(fileByteList))
                except:
                    self.button_glitch.configure(state=tkinter.NORMAL)
                    self.bar.set(0)
                    self.bar.configure(text="OOPS!")
                    self.string_log.set("Save error!")
                    self.label_log.place(x=20,y=320)
                    return
                    
            def messWithFile(originalByteList, iterations, bytesToChange, repeatWidth, fileNum):
                newByteList = copy.copy(originalByteList)
                iteration = 1
                seed = int(self.slider_1.get()) or random.randrange(sys.maxsize)
                random.seed(seed)
                for i in range(iterations):
                    iteration = i+1
                    if (self.optionmenu_2.get() == "repeat"):
                        newByteList = repeatBytes(newByteList, bytesToChange, repeatWidth)
                    else:
                        newByteList = transforms[self.optionmenu_2.get()](newByteList, bytesToChange)
                writeFile(newByteList, fileNum, iteration, bytesToChange, seed)

            def changeBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList) - bytesToChange)
                chunk = [random.randint(0, 255) for i in range(bytesToChange)]
                byteList[pos:pos+bytesToChange] = chunk
                return byteList

            def reverseBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList) - bytesToChange)
                chunk = byteList[pos:pos+bytesToChange][::-1]
                byteList[pos:pos+bytesToChange] = chunk
                return byteList

            def repeatBytes(byteList, bytesToChange, repeatWidth):
                pos = random.randint(0, len(byteList) - bytesToChange)
                chunk = []
                for i in range(math.ceil(bytesToChange/repeatWidth)):
                    chunk.extend(byteList[pos:pos+repeatWidth])
                byteList[pos:pos+bytesToChange] = chunk[:bytesToChange]
                return byteList

            def removeBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList) - bytesToChange)
                byteList[pos:pos+bytesToChange] = []
                return byteList

            def zeroBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList) - bytesToChange)
                byteList[pos:pos+bytesToChange] = [0] * bytesToChange
                return byteList

            def insertBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList))
                chunk = [random.randint(0, 255) for i in range(bytesToChange)]
                byteList[pos:pos] = chunk
                return byteList

            def replaceBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList) - bytesToChange)
                chunk = byteList[pos:pos+bytesToChange]
                old = random.randint(0, 255)
                new = random.randint(0, 255)
                chunk = [new if b == old else b for b in chunk]
                byteList[pos:pos+bytesToChange] = chunk
                return byteList

            def moveBytes(byteList, bytesToChange):
                pos = random.randint(0, len(byteList) - bytesToChange)
                chunk = byteList[pos:pos+bytesToChange]
                byteList[pos:pos+bytesToChange] = []
                newPos = random.randint(0, len(byteList))
                byteList[newPos:newPos] = chunk
                return byteList

            def main():
                self.after(100, self.bar.set(40))
                minChanges = 1
                maxChanges = 1
                if (int(self.slider_2.get()) and re.match(r"[0-9]+-[0-9]+", str(int(self.slider_2.get())))):
                    parts = int(self.slider_2.get()).split("-")
                    minChanges = int(parts[0])
                    maxChanges = int(parts[1])
                elif (int(self.slider_2.get())):
                    minChanges = int(self.slider_2.get())
                    maxChanges = int(self.slider_2.get())
                minBytes = 1
                maxBytes = 1
                if (int(self.slider_3.get()) and re.match(r"[0-9]+-[0-9]+", str(int(self.slider_3.get())))):
                    parts = int(self.slider_3.get()).split("-")
                    minBytes = int(parts[0])
                    maxBytes = int(parts[1])
                elif (int(self.slider_3.get())):
                    minBytes = int(self.slider_3.get())
                    maxBytes = int(self.slider_3.get())
                minRepeating = 1
                maxRepeating = 1
                if (int(self.slider_4.get()) and re.match(r"[0-9]+-[0-9]+", str(int(self.slider_4.get())))):
                    parts = int(self.slider_4.get()).split("-")
                    minRepeating = int(parts[0])
                    maxRepeating = int(parts[1])
                elif (int(self.slider_4.get())):
                    minRepeating = int(self.slider_4.get())
                    maxRepeating = int(self.slider_4.get())
                    
                originalByteList = list(open(sfile, "rb").read())
                iterations = random.randint(minChanges, maxChanges)
                self.after(100, self.bar.set(50))
                bytesToChange = random.randint(minBytes, maxBytes)
                self.after(100, self.bar.set(60))
                repeatWidth = random.randint(minRepeating, maxRepeating)
                self.after(100, self.bar.set(70))
                messWithFile(originalByteList, iterations, bytesToChange, repeatWidth, 1)
                self.after(100, self.bar.set(80))
                
            transforms = {
                "change": changeBytes,
                "reverse": reverseBytes,
                "repeat": repeatBytes,
                "remove": removeBytes,
                "zero": zeroBytes,
                "insert": insertBytes,
                "replace": replaceBytes,
                "move": moveBytes
            }
            main()
            
            try:
                if os.path.exists(ifile):
                    os.remove(ifile)
            except:
                pass
            
            if os.path.exists(outPath):   
                time.sleep(1)
                self.button_glitch.configure(state=tkinter.NORMAL)
                self.after(100, self.bar.set(90))
                self.after(100, self.bar.set(100))
                self.bar.configure(text="Done!")
                self.string_log.set("Image Saved!")
                self.label_log.place(x=20,y=320)
                if not self.replace_file:
                    s=1
                    while os.path.exists(var2.get()):
                        ffile = ofile[:-4]+"_glitched_"+str(s)+"."+self.extension
                        s+=1
                        var2.set(ffile)
                        
        def randomizer():
            x, y, w, z = random.sample(range(1,10),4)
            self.slider_1.set(x)
            self.dynamiclabel_1.configure(text=x)
            self.slider_2.set(y)
            self.dynamiclabel_2.configure(text=y)
            self.slider_3.set(w)
            self.dynamiclabel_3.configure(text=w)
            self.slider_4.set(z)
            self.dynamiclabel_4.configure(text=z)
            self.optionmenu_2.set(random.choice(self.optionmenu_2._values))
            
        def web_help():
            webbrowser.open_new_tab("https://github.com/Akascape/Pure-Glitch")

        def change_ext(e):
            if e=="Copy":
                e = ofile[-3:]
            self.extension = e.lower()
            var2.set(ffile[:-3]+self.extension)

        def change_file_mode():
            if self.replace.get()==1:
                self.replace_file = True
            else:
                self.replace_file = False

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=50, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left, image=customtkinter.CTkImage(Image.open(resource("Assets/new.png")),size=(32, 32)),
                                                text="", width=50, height=50, corner_radius=0, fg_color="transparent", hover_color="gray10", command=place_front)
        self.button_1.grid()
        self.button_2 = customtkinter.CTkButton(master=self.frame_left, image=customtkinter.CTkImage(Image.open(resource("Assets/gear.png")),size=(40, 40)), 
                                                text="", width=50, height=50, corner_radius=0, fg_color="transparent", hover_color="gray10", command=place_process)
        self.button_2.grid()
        self.button_3 = customtkinter.CTkButton(master=self.frame_left, image=customtkinter.CTkImage(Image.open(resource("Assets/view.png")),size=(35, 40)), 
                                                text="", width=50, height=50, corner_radius=0, fg_color="transparent", hover_color="gray10", command=viewer)
        self.button_3.grid()
        
        var1=tkinter.StringVar()
        var1.set("Import File")
        
        self.entry = customtkinter.CTkEntry(master=self.frame_right,text_color="gray50", width=540, height=30, textvariable=var1)
        
        self.button_browse = customtkinter.CTkButton(master=self.frame_right, text="...", width=20, height=30, corner_radius=10, fg_color="grey30",
                                                hover_color="gray10", command=open_function)
        
        self.logo = customtkinter.CTkLabel(master=self.frame_right, image=customtkinter.CTkImage(Image.open(resource("Assets/LOGO.png")),size=(350, 256)),
                                                width=256, height=256, text="")
        
        self.recipe = customtkinter.CTkLabel(master=self.frame_right,text="GLITCH RECIPE", width=5, fg_color=None)
        
        self.recipe_bar = customtkinter.CTkProgressBar(master=self.frame_right, width=580, height=5, corner_radius=10, fg_color="white")
        self.recipe_bar.set(100)
                
        self.bar = tkdial.ScrollKnob(self.frame_right ,width=150, height=150, fg=self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"]),
                                    bg=self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"]),
                                    text=" ", steps=10, radius=200, bar_color="#242424", 
                                    progress_color=self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"]),
                                    outer_color=self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"]), outer_length=10, 
                                    border_width=30, start_angle=270, inner_width=0, outer_width=5, 
                                    text_color="white")

        self.optionmenu_1 = customtkinter.CTkComboBox(master=self.frame_right, fg_color="#4d4d4d",width=160, height=25, state="readonly",
                                                values=["Copy","JPG","PNG","WEBP","GIF","PCX","BMP","TIFF"], command=change_ext)
        self.optionmenu_1.set("Copy")
        self.optionmenu_2 = customtkinter.CTkComboBox(master=self.frame_right, fg_color="#4d4d4d",width=160, height=25, state="readonly",
                                                values=["change","reverse","repeat","remove","zero","insert","replace","move"])
        self.optionmenu_2.set("change")
        
        self.dynamiclabel_1 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1)
        self.dynamiclabel_2 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1)
        self.dynamiclabel_3 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1)
        self.dynamiclabel_4 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1)

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1, to=10, number_of_steps=9, command=dynamic1)
        self.slider_1.set(random.randint(1,10))
        self.label1 = customtkinter.CTkLabel(master=self.frame_right,text="seed", width=5, height=1)
        
        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1, to=10, number_of_steps=9, command=dynamic2)
        self.slider_2.set(random.randint(1,10))
        self.label2 = customtkinter.CTkLabel(master=self.frame_right,text="amount", width=5, height=1)
        
        self.slider_3 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1,to=10, number_of_steps=9, command=dynamic3)
        self.slider_3.set(random.randint(1,10))
        self.label3 = customtkinter.CTkLabel(master=self.frame_right,text="bytes", width=5, height=1)
        
        self.slider_4 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1, to=10, number_of_steps=9, command=dynamic4)
        self.slider_4.set(random.randint(1,10))
        self.label4 = customtkinter.CTkLabel(master=self.frame_right,text="repeat width", width=5, height=1)
        
        global var2
        var2 = tkinter.StringVar()
        var2.set("")
        
        self.entry2 = customtkinter.CTkEntry(master=self.frame_right, width=540, height=30,text_color="gray50", placeholder_text="Output Folder",
                                             state="readonly", textvariable=var2)

        self.button_browse2 = customtkinter.CTkButton(master=self.frame_right, text="...", width=20, height=30, corner_radius=10, fg_color="grey30",
                                                hover_color="gray10", command=output_folder)

        self.button_glitch = customtkinter.CTkButton(master=self.frame_right, text="GLITCH IT!", width=150, height=30, corner_radius=10, fg_color="gray10",
                                                     hover_color="gray20", command=glitch_it)

        self.button_next = customtkinter.CTkButton(master=self.frame_right, text="NEXT!", fg_color="gray30", width=150, height=35, corner_radius=10, command=place_process)

        image_label = customtkinter.CTkLabel(master=self.frame_right, image=None, text="", corner_radius=30)
        
        self.label_oops = customtkinter.CTkLabel(master=self.frame_right, text="", fg_color="Black")
        
        self.button_random = customtkinter.CTkButton(master=self.frame_right, image=customtkinter.CTkImage(Image.open(resource("Assets/random.png")),size=(25, 25)),
                                                text="", width=5, height=5, corner_radius=0, fg_color="transparent", hover=False, command=randomizer)  

        self.string_log = tkinter.StringVar()
        self.string_log.set("")

        self.replace = customtkinter.CTkCheckBox(master=self.frame_right, text="Replace", command=change_file_mode)
        self.replace.toggle()
        
        self.label_log = customtkinter.CTkLabel(master=self.frame_right, textvariable=self.string_log, anchor="w", width=1, text_color="grey70")

        self.label_version = customtkinter.CTkLabel(master=self.frame_right, text="v0.2", text_color="grey70", width=1)

        self.help_button = customtkinter.CTkButton(master=self.frame_left, text="?", fg_color="transparent", width=10, hover=False,
                                                   height=35, text_color="grey50", corner_radius=10, command=web_help)
        self.help_button.place(x=10, y=355)
        
        place_front()
        
    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
