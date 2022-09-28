#=================PURE GLITCH=====================#
#LICENSE: MIT
#AUTHOR: Akash Bora

import tkinter
import customtkinter
import awesometkinter
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

try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(0)
except:
    pass

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
    customtkinter.set_default_color_theme(resource("Assets/Pure_Glitch_theme.json"))
    
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
        self.iconphoto(False, self.icopath)
        
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
                self.button_next.configure(fg_color=customtkinter.ThemeManager.theme["color"]["button"])
                self.entry.configure(text_color="gray50")
                
            forget_everything()
            self.recipe.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky="wn")
            self.recipe_bar.grid(row=0, column=0, columnspan=2, padx=15, pady=40, sticky="wn")
            self.bar.place(x=455,y=90)
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
            global ofile
            ofile = tkinter.filedialog.askopenfilename(filetypes =[('Image File', ['*.png','*.jpg','*.bmp','*.webp','*jpeg','*gif']),('All Files', '*.*')])
            if ofile:
                self.button_next.configure(fg_color=customtkinter.ThemeManager.theme["color"]["button"])
                self.entry.configure(textvariable=var1.set(str(ofile)), text_color="gray50")
                self.entry2.configure(textvariable=var2.set(os.path.dirname(ofile)+"/"))
                
        def output_folder():
            global ffile
            ffile = tkinter.filedialog.askdirectory()
            if ffile:
                self.entry2.configure(textvariable=var2.set(ffile+"/"))
                
        def viewer():
            global image1, sfile
            if not os.path.exists(self.entry.get()):
                return
            forget_everything()
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            filename, extension = os.path.splitext(sfile)
            filename = filename.split("\\")[-1] if platform.system == "Windows" else filename.split("/")[-1]
            outPath = f"{var2.get()}{filename}_mode={self.optionmenu_2.get()}_seed={int(self.slider_1.get())}_amount={int(self.slider_2.get())}_byte={int(self.slider_3.get())}_repeat={int(self.slider_4.get())}{extension}"
            try:
                if os.path.exists(outPath):
                    image_label.set_image(image=None)
                    image1 = ImageTk.PhotoImage(Image.open(outPath).resize((self.frame_right.winfo_width(), self.frame_right.winfo_height()), Image.Resampling.LANCZOS))
                    image_label.configure(image=image1)
                    image_label.grid()
                    if extension==".png":
                        self.label_oops.configure(text="Currently this image viewer is in beta stage and \ncannot display broken PNG images!")
                        self.label_oops.place(x=12,y=150)
            except:
                self.label_oops.configure(text="Unable to display this file!")
                self.label_oops.place(x=200,y=150)
                
        def glitch_it():
            if not os.path.exists(var2.get()):
                self.entry2.configure(text_color="orange")
                return
            else:
                self.entry2.configure(text_color="gray50")
                
            self.button_glitch.configure(state=tkinter.DISABLED)
            self.bar.set(0)
            self.bar.start(10)
            
            try:
                threading.Thread(target=process).start()
            except:
                self.button_glitch.configure(state=tkinter.NORMAL)
                self.bar.set(0)
                self.bar.percent_label.config(text="OOPS!")
                self.string_log.set("Something went wrong!")
                self.label_log.place(x=20,y=320)
                self.bar.stop()
                
        def process():
            self.label_log.place_forget()     
            global ofile, var2, sfile
            
            if not self.optionmenu_1.get()=="Copy":
                self.bar.stop()
                self.bar.start(200)
                try:
                    ifile = ofile[:-4]+"_intermediate."+self.optionmenu_1.get().lower()
                    Image.open(ofile).convert('RGB').save(ifile)
                except:
                    self.button_glitch.configure(state=tkinter.NORMAL)
                    self.bar.set(0)
                    self.bar.percent_label.config(text="OOPS!")
                    self.bar.stop()
                    self.string_log.set("Conversion error!")
                    self.label_log.place(x=20,y=320)
                    return
                sfile = ifile
                self.bar.stop()
                self.bar.start(10)
            else:
                sfile=ofile
               
            def writeFile(fileByteList, fileNum, iteration, bytesTochange, seed):
                global var2, outPath
                filename, extension = os.path.splitext(sfile)
                filename = filename.split("\\")[-1] if platform.system == "Windows" else filename.split("/")[-1]
                outPath = f"{var2.get()}{filename}_mode={self.optionmenu_2.get()}_seed={int(self.slider_1.get())}_amount={int(self.slider_2.get())}_byte={int(self.slider_3.get())}_repeat={int(self.slider_4.get())}{extension}"
                try:
                    if os.path.isfile(outPath):
                        os.remove(outPath)
                    open(outPath, "wb").write(bytes(fileByteList))
                except:
                    self.button_glitch.configure(state=tkinter.NORMAL)
                    self.bar.set(0)
                    self.bar.percent_label.config(text="OOPS!")
                    self.bar.stop()
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
                bytesToChange = random.randint(minBytes, maxBytes)
                repeatWidth = random.randint(minRepeating, maxRepeating)
                messWithFile(originalByteList, iterations, bytesToChange, repeatWidth, 1)

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
                self.bar.set(100)
                self.bar.stop()
                self.bar.percent_label.config(text="Done!")
                if len(outPath)>=75:
                    showname = outPath[:60]+"..."+outPath[-12:]
                else:
                    showname = outPath 
                self.string_log.set("Image saved: "+str(showname))
                self.label_log.place(x=20,y=320)
            
        def randomizer():
            self.slider_1.set(random.randint(1,10))
            self.slider_2.set(random.randint(1,10))
            self.slider_3.set(random.randint(1,10))
            self.slider_4.set(random.randint(1,10))
            self.optionmenu_2.set(random.choice(self.optionmenu_2.values))
            
        def web_help():
            webbrowser.open_new_tab("https://github.com/Akascape/Pure-Glitch")
            
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=50, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left, image=ImageTk.PhotoImage(Image.open(resource("Assets/new.png")).resize((32, 32), Image.Resampling.LANCZOS))
                                                ,text="", width=50, height=50, corner_radius=0, fg_color=None, hover_color="gray10", command=place_front)
        self.button_1.grid()
        self.button_2 = customtkinter.CTkButton(master=self.frame_left, image=ImageTk.PhotoImage(Image.open(resource("Assets/gear.png")).resize((40, 40), Image.Resampling.LANCZOS))
                                                ,text="", width=50, height=50, corner_radius=0, fg_color=None, hover_color="gray10", command=place_process)
        self.button_2.grid()
        self.button_3 = customtkinter.CTkButton(master=self.frame_left, image=ImageTk.PhotoImage(Image.open(resource("Assets/view.png")).resize((35, 40), Image.Resampling.LANCZOS))
                                                ,text="", width=50, height=50, corner_radius=0, fg_color=None, hover_color="gray10", command=viewer)
        self.button_3.grid()
        
        var1=tkinter.StringVar()
        var1.set("Import File")
        
        self.entry = customtkinter.CTkEntry(master=self.frame_right,text_color="gray50", width=540, height=30, textvariable=var1)
        
        self.button_browse = customtkinter.CTkButton(master=self.frame_right, text="...", width=20, height=30, corner_radius=10, fg_color=customtkinter.ThemeManager.theme["color"]["entry_border"][1],
                                                hover_color="gray10", command=open_function)
        
        self.logo = customtkinter.CTkButton(master=self.frame_right, image=ImageTk.PhotoImage(Image.open(resource("Assets/LOGO.png")).resize((350, 256), Image.Resampling.LANCZOS)),
                                                width=256, height=256, text="", bg="grey", fg_color=None, hover_color=None)
        
        self.recipe = customtkinter.CTkLabel(master=self.frame_right,text="GLITCH RECIPE", width=5, fg_color=None)
        
        self.recipe_bar = customtkinter.CTkProgressBar(master=self.frame_right, width=580, height=5, corner_radius=10, fg_color="white")
        self.recipe_bar.set(100)
                
        self.bar = awesometkinter.RadialProgressbar(self.frame_right, fg=customtkinter.ThemeManager.theme["color"]["button"][1], parent_bg=customtkinter.ThemeManager.theme["color"]["frame_low"][1], size=120)

        self.optionmenu_1 = customtkinter.CTkComboBox(master=self.frame_right, fg_color="#4d4d4d",width=160, height=25,
                                                values=["Copy","JPG","PNG","WEBP","GIF","PCX","BMP","TIFF"])
        
        self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.frame_right, fg_color="#4d4d4d",width=160,button_color=customtkinter.ThemeManager.theme["color"]["combobox_border"][1],
                                                button_hover_color=customtkinter.ThemeManager.theme["color"]["combobox_button_hover"][1], height=25,
                                                values=["change","reverse","repeat","remove","zero","insert","replace","move"])
        
        self.dynamiclabel_1 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1, fg_color=None)
        self.dynamiclabel_2 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1, fg_color=None)
        self.dynamiclabel_3 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1, fg_color=None)
        self.dynamiclabel_4 = customtkinter.CTkLabel(master=self.frame_right,text="10", width=5, height=1, fg_color=None)

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1, to=10, number_of_steps=9, command=dynamic1)
        self.slider_1.set(random.randint(1,10))
        self.label1 = customtkinter.CTkLabel(master=self.frame_right,text="seed", width=5, height=1, fg_color=None)
        
        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1, to=10, number_of_steps=9, command=dynamic2)
        self.slider_2.set(random.randint(1,10))
        self.label2 = customtkinter.CTkLabel(master=self.frame_right,text="amount", width=5, height=1, fg_color=None)
        
        self.slider_3 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1,to=10, number_of_steps=9, command=dynamic3)
        self.slider_3.set(random.randint(1,10))
        self.label3 = customtkinter.CTkLabel(master=self.frame_right,text="bytes", width=5, height=1, fg_color=None)
        
        self.slider_4 = customtkinter.CTkSlider(master=self.frame_right, width=400, from_=1, to=10, number_of_steps=9, command=dynamic4)
        self.slider_4.set(random.randint(1,10))
        self.label4 = customtkinter.CTkLabel(master=self.frame_right,text="repeat width", width=5, height=1, fg_color=None)
        
        global var2
        var2=tkinter.StringVar()
        var2.set(" ")
        
        self.entry2 = customtkinter.CTkEntry(master=self.frame_right, width=540, height=30,text_color="gray50", placeholder_text="Output Folder", textvariable=var2)

        self.button_browse2 = customtkinter.CTkButton(master=self.frame_right, text="...", width=20, height=30, corner_radius=10, fg_color=customtkinter.ThemeManager.theme["color"]["entry_border"][1],
                                                hover_color="gray10", command=output_folder)

        self.button_glitch = customtkinter.CTkButton(master=self.frame_right, text="GLITCH IT!", width=150, height=30, corner_radius=10, fg_color="gray10",hover_color="gray20", command=glitch_it)

        self.button_next = customtkinter.CTkButton(master=self.frame_right, text="NEXT!", fg_color="gray30", width=150, height=35, corner_radius=10, command=place_process)

        image_label = customtkinter.CTkButton(master=self.frame_right, image=None, text="", hover_color=None, fg_color=None, corner_radius=30)
        
        self.label_oops = customtkinter.CTkLabel(master=self.frame_right, text="", fg_color="Black", bg_color=None)
        
        self.button_random = customtkinter.CTkButton(master=self.frame_right, image=ImageTk.PhotoImage(Image.open(resource("Assets/random.png")).resize((25, 25), Image.Resampling.LANCZOS)),
                                                text="", width=5, height=5, corner_radius=0, fg_color=None, hover_color=None, command=randomizer)  

        self.string_log = tkinter.StringVar()
        self.string_log.set("")
        
        self.label_log = customtkinter.CTkLabel(master=self.frame_right, textvariable=self.string_log, fg_color=None, anchor="w", width=1, text_color="grey70")

        self.label_version = customtkinter.CTkLabel(master=self.frame_right, fg_color=None, text="v0.1", text_color="grey70", width=1)

        self.help_button =  customtkinter.CTkButton(master=self.frame_left, text="?", fg_color=None,width=10, hover_color=None, height=35, text_color="grey50", corner_radius=10, command=web_help)
        self.help_button.place(x=10, y=355)
        
        place_front()
        
    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
