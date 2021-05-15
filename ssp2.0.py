




#-----------------------IMPORTING MODULES-----------------------------------------------------------------------------------
#       THIS INTENDATION HAS ALL THE NECESSARY MODULES WHICH ARE BEING USED. ALL THE
#        MODULES USED ARE OPEN-SOURCE, SO THAT THERE ARE NOT ANY COPY WRITE CLAMES.
#-----------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox as mb
import pyttsx3
import random
from datetime import datetime
import wikipedia
import webbrowser
import os
import requests
#-----------------------------------------------------------------------------------------------------------------------------------------









#---------------------WIDGET CLASS----------------------------------------------------------------------------------------------------------------
#          THIS IS THE MAIN AND ONLY CLASS OF THE APPLICATION AND ALSO THE MOST IMPORTANT ONE.
#          IT HAS ALL THE NECESSARY FUCTIONS, LISTS, CONDITION AND INIT FUCTION.
#---------------------------------------------------------------------------------------------------------------------------------------------------------
class Widget():

    



    #------------------------------------------------------KEY WORD LISTS---------------------------------------------------------------------------
    #                THESE ARE ALL THE LIST WHICH CONTAINS IMPORTANT KEYWORDS WHICH THE SSP CAN USE.
    #--------------------------------------------------------------------------------------------------------------------------------------------------------
    greet = ['Hey Whats up! How are you doing', 'Hello Aditya','Hi ! I am your Assistant','Hello, How can I help You']
    how = ['I am Fine Sir, What about You','I am fine as always', 'what you think','just fine!!']
    name = ['You Can call me SSP','My Name Is SSP','you named me SSP','You Should Know this, My name Is SSP']
    creator = ['You made Me','I was Made by Aditya','One And only, Aditya','Best in the World, Aditya']
    can = ['I Can Do Everything .','Just Give Me A Try And Figure This Out.','What you Coded Within Me ;) ','Your Choice']
    c_un = ["I did'nt get that",'What You Said?','I was Unable To Understand','I have some Bugs Because of you']
    here = ['To Help You Out','To Help You To Do Tasks','To Be Your Assistant','You Called me, Thatwise']
    frd = ['I will Feel Lucky To Be Your Friend','Yaa Ofcource']
    me = ['You Told Me Your Name, Aditya','I Think That\'s Aditya','Your Name That I Know Is Aditya']
    thanks = ['My Pleasure','Welcome','Ohh Don\'t amberis me by saying thanks ','So Sweet!!']
    #----------------------------------------------------------------------------------------------------------------------------------------------------------




    #--------------------------------------------ABOUT US FUNCTION---------------------------------------------------------------------------------
    def more(self):
        more = Tk()
        more.configure(bg='powder blue')
        more.geometry('400x250+300+450')

        

        
        Label(more, text='SSP - The Virtual Assistant',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='By: Aditys',bg='powder blue',font=('Arial Black',10,'bold')).pack()
        
        out = 'My Name Is SSP. I Was Created By Aditya. \n He Made Me Using Python Language. I Was Made\n As A Project For Him. But Later I Turned Really Well.\n So He Started Working Really Hard On Me. His\n Progress In Me Was Just Great. So, Now I Am His One\n Of The Dream Project Which He Is Planning\n To Build For Cross-Platform.'
        
        Label(more, text=out,bg='powder blue',font=('Arial Black',10,'bold')).pack()
        
        Label(more, text='Contact us at:\n9803588671',bg='powder blue',font=('Arial Black',10,'bold')).pack(side=LEFT)
        
        
        Button(more, text='Narrate' ,font=('Arial Black',10,'bold'), command=lambda : self.speak(out)).pack(side=RIGHT,padx=10 )

        more.mainloop()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------


        


    #--------------------------------ENGINE FOR SPEAKING--------------------------------------------------------------
    #         THESE VARIABLES ARE  BUILDING AN ENGINE WHICH THE SPEAK FUNCTION IS USING.
    #-----------------------------------------------------------------------------------------------------------------------------
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    #------------------------------------------------------------------------------------------------------------------------------





    #---------------------------PRINTING FUNC---------------------------------------------------
    #       THIS FUCTION PRINTS THE SSP'S RESPONCE TO SCREEN.
    #---------------------------------------------------------------------------------------------------
    def printing_func(self, out):
        self.text_box2.delete(1.0,END)
        self.text_box2.insert(INSERT,  out)
    #----------------------------------------------------------------------------------------------------





    #-----------------SPEAK FUNCTION-------------------------------
    #    THIS FUNCTION SPEAKS THE SSP'S RESPONCE
    #------------------------------------------------------------------------
    def speak(self,s):
        self.engine.say(s)
        self.engine.runAndWait()
    #----------------------------------------------------






    #-----------------------SEND FUNC-----------------------------------------------------------------
    #        THIS FUCTION IS BEING USED TO SEND USER_INPUT TO SSP.
    #--------------------------------------------------------------------------------------------------------
    def send_func(self):
        user_input = self.search_var.get().lower()
        self.search_var.set('')
        self.text_box1.delete(1.0,END)
        self.text_box1.insert(INSERT,user_input)
    #-------------------------------------------------------------------------------------------------------
        
        
        


        #------------------------------------CONDITIONS------------------------------------------------------------------------------------------
        # THESE ARE CONDITIONS WHICH THE SSP CHECKS. HE RESPOND TO THE MOST RELEVENT CONDITION.
        #-------------------------------------------------------------------------------------------------------------------------------------------------


        #----------------ABOUT CONDITION---------------------
        if 'about' in user_input and 'you' in user_input:
            out = 'Ok Let Me Introduce Myself.'
            self.printing_func(out)                                       #|
            self.speak(out)
            self.more()
        #-----------------------------------------------------------------
            

            


        #------YOU CONDITIONS ------------------------
        elif 'you' in user_input:                                           #|
            if 'who' in user_input and 'are' in user_input:
                r = random.randint(0,len(self.name)-1)       #|
                out = self.name[r]                                            #|
                self.printing_func(out)                                       #|
                self.speak(out)
                
            elif 'how are' in user_input:                               #|
                r = random.randint(0,len(self.how)-1)       #|
                out = self.how[r]                                            #|
                self.printing_func(out)                                       #|
                self.speak(out)                                                      #|
                                                                                          #|
            elif 'who made' in user_input:                        #|
                r = random.randint(0,len(self.creator)-1)        #|
                out = self.creator[r]                                              #|
                self.printing_func(out)                                       #|
                self.speak(out)                                                      #|
                                                                                          #|
            elif 'do' in user_input:                                      #|
                r = random.randint(0,len(self.can)-1 )             #|
                out = self.can[r]                                                    #|
                self.printing_func(out)                                       #|
                self.speak(out)                                                      #|
                                                                                          #|
            elif 'name' in user_input:                                #|
                r = random.randint(0,len(self.name)-1)          #|
                out = self.name[r]                                                #|
                self.printing_func(out)                                      #|
                self.speak(out)                                                     #|
                                                                                         #|
            elif 'open' in user_input:                                #|
                out = 'Opening Youtube'                            #|
                self.printing_func(out)                                      #|
                self.speak(out)                                                     #|
                webbrowser.open('youtube.com')             #|

            elif 'here' in user_input:
                r = random.randint(0,len(self.here)-1)            #|
                out = self.here[r]                                                  #|
                self.printing_func(out)                                       #|
                self.speak(out)
                
            else:                                                                               #|
                r = random.randint(0,len(self.c_un)-1)               #|
                out = self.c_un[r]                                                        #|   
                self.printing_func(out)                                               #|
                self.speak(out)                                                            #|        

        #---------------------------------------------------------------------------------------------------------------




        #-----------------GURPARTAP CONDITION-------------------------------------------------------------------
        elif 'SSP singh'  in user_input:
            out = 'SSP Singh Is A Good Friend Of Aditya. He is well Known as SSP'                                                                                               #|   
            self.printing_func(out)                                                                                    #|
            self.speak(out)
        #-----------------------------------------------------------------------------------------------------------------------




                
        #----------------------------MY NAME CONDITION-----------------------------------------------------
        elif 'who' in user_input and 'i' in user_input or 'my' in user_input and 'name' in user_input:
            r = random.randint(0,len(self.me)-1)                                                         #|
            out = self.me[r]                                                                                               #|   
            self.printing_func(out)                                                                                    #|
            self.speak(out)
        #---------------------------------------------------------------------------------------------------------------

        



       #--------------------------THANKS CONDITION-------------------------------------------------------   
        elif 'thank' in user_input:
            r = random.randint(0,len(self.thanks)-1)                                                         #|
            out = self.thanks[r]                                                                                               #|   
            self.printing_func(out)                                                                                    #|
            self.speak(out)
        #-------------------------------------------------------------------------------------------------------------



            
        #-----------------------------GOOD MORNING CONDITION--------------------------------------------------------------------------------
        elif 'good morning' in user_input:
            t = datetime.now().strftime('%H  hours and %M minutes')          #|
            o= t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')

            try:     
                url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Ludhiana'
                json_data = requests.get(url).json()
                format_add = json_data['weather'][0]['main']
                format_temp = json_data['coord']['lat']
                outa = f'Temperture In Your City is {format_temp} Deegre   Celcius, And  Climate is  {format_add}'                    

            except:
                outa = ' Weather Forcast Is Currently Unavailable'
                
                
            out = f'Good Morning Aditya, The Current Time is {time},  And {outa},    Have A Good Day Sir.'
            self.printing_func(out)
            self.speak(out)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------            



                
        #--------------------USES-------------------------------------
        elif 'can' in user_input and 'friend' in user_input:
            r = random.randint(0,len(self.frd)-1)                                                         #|
            out = self.frd[r]                                                                                               #|   
            self.printing_func(out)                                                                                    #|
            self.speak(out)
        #-----------------------------------------------------------




        
        #--------------BORED--------------------------------------------------
        elif 'bored' in user_input:
            out = 'Shall I Play Some Music Or A Game, What You Think?'
            self.printing_func(out)                                                                                    #|
            self.speak(out)
        #--------------------------------------------------------------------------




            
        #-------------------------WEATHER FORCAST---------------------------------------------------------------------------------           
        elif  'weather' in user_input:
            try:
                if 'in' in user_input:
                    u = user_input.split()
                    for i in range(0,len(u)):
                        if u[i] == 'in':
                            city = u[i+1]
                        
                    api='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api+city
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperture In {city} is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
                    
                else:
                    url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Ludhiana'                            
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperture In Your city is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
            except:
                out = 'I Was Unable To Connect To Internet.'
                self.printing_func(out)
                self.speak(out)
        #----------------------------------------------------------------------------------------------------------------------------------------------




        
        #-------------------------------------------LOCATION------------------------------------
        elif 'where' in user_input and 'i' in user_input or 'location' in user_input:
            try:
                r = requests.get('https://ipinfo.io/')
                d = r.text.split()[4]
                out='You Location Is Near To ' + d
                self.printing_func(out)
                self.speak(out)
            except:
                out='I Was Unable To Track Your Location'
                self.printing_func(out)
                self.speak(out)
        #------------------------------------------------------------------------------------------------


                

                

        #-------HELLO CONDITION--------------------
        elif 'hello'  in user_input or 'hi' in user_input:                                   #|
            r = random.randint(0,len(self.greet)-1)              #|
            out = self.greet[r]                                                    #|
            self.printing_func(out)                                          #|
            self.speak(out)                                                         #|
        #-----------------------------------------------------

            



        #----------EXIT CONDITION------------------------
        elif 'exit' in user_input:                                           #|
            out = 'Okk I am going, Have a good Day sir'  #|
            self.printing_func(out)                                             #|
            self.speak(out)                                                             #|
            self.win.destroy()
                                                                                             #|
        #---------------------------------------------------------




        #----------------OPEN CONDITIONS -----------------------------------------
        elif 'open' in user_input:
            if 'google' in user_input:
                out = 'Opening Google'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('google.com')

            elif 'youtube' in user_input:
                out = 'Opening Youtube'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('youtube.com')
                
            elif 'current' in user_input:            
                out='Opening Current Working Directory'                                                     
                self.printing_func(out)
                self.speak(out)
                path = ''
                os.startfile(path)

            elif 'python' in user_input:
                out='Opening Python'
                self.printing_func(out)
                self.speak(out)
                path = 'E:\\'
                os.startfile(path)

            elif 'paint' in user_input:
                out='Opening Paint'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\mspaint.exe'
                os.startfile(path)

            elif 'wordpad' in user_input:
                out='Opening WordPad'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Windows NT\Accessories\wordpad.exe'
                os.startfile(path)

            elif 'notepad' in user_input:
                out='Opening Note Pad'
                self.printing_func(out)
                os.chdir(r'E:\EXE_FILES\Text_editor')
                self.speak(out)
                path = r'E:\EXE_FILES\Text_editor\Text_editor.exe'
                os.startfile(path)

            elif 'code language' in user_input:
                out='Opening Code Language'
                self.printing_func(out)
                os.chdir(r'E:\EXE_FILES\CODE_LANGUAGE\V3.0')
                self.speak(out)
                path = r'E:\EXE_FILES\CODE_LANGUAGE\V3.0\CODE_LANGUAGE V3.0.exe'
                os.startfile(path)

            elif 'snake' in user_input:
                out='Opening Snake Game'
                self.printing_func(out)
                self.speak(out)
                path = r'E:\snake2.py'
                os.startfile(path)

            elif 'positioner' in user_input:
                out='Opening Positioner'
                self.printing_func(out)
                self.speak(out)
                path = r'E:\positioner.py'
                os.startfile(path)

            elif 'vlc' in user_input:
                out = 'Opening VLC'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)

            elif 'calculator' in user_input:
                out = 'Opening Calculator'
                self.printing_func(out)
                os.chdir(r'E:\EXE_FILES\calculator')
                self.speak(out)
                path = r'E:\EXE_FILES\CALCULATOR\CALCULATOR v2.0.exe'
                os.startfile(path)

            elif 'sticky notes' in user_input:
                out = 'Opening Sticky Notes'
                self.printing_func(out)
                os.chdir(r'E:\EXE_FILES')
                self.speak(out)
                path = r'E:\EXE_FILES\STICKY_NOTES.exe'
                os.startfile(path)

            elif 'browser' in user_input or 'chrome' in user_input:
                out = 'Opening Crome Browser'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)

            elif 'wo' in user_input and 'mic' in user_input:
                out = 'Opening Wo Mic Client'
                self.printing_func(out)
                self.speak(out)
                path = r"C:\Program Files\WOMic\WOMicClient.exe"
                os.startfile(path)

            elif 'vsc' in user_input:
                out = 'Opening Visual Studio Code'
                self.printing_func(out)
                self.speak(out)
                path = r"C:\Users\Hardeep Singh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(path)

            elif 'picture' in user_input or 'images' in user_input or 'photo' in user_input:
                out = 'Opening  Images'
                self.printing_func(out)
                self.speak(out)
                path = r'D:\photo\deep'
                os.startfile(path)
         

            elif 'cmd' or 'command prompt' in user_input:
                out='Opening Command Prompt'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\cmd.exe'
                os.startfile(path)
                
            else:                                                                                                                    #|
                r = random.randint(0,len(self.c_un)-1)                                                         #|
                out = self.c_un[r]                                                                                               #|   
                self.printing_func(out)                                                                                    #|
                self.speak(out)                                                                                                   #|        


        #----------------------------------------------------------------------------------------------------------------------





        #------------------------------MEDIA COMMANDS------------------------
        elif 'music' in user_input:
            try:
                out='Playing Music'
                self.printing_func(out)
                self.speak(out)
                mus_dir = r'D:\Top 20 Kuldeep Manak'
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(mus_dir) - 1)
                os.startfile(os.path.join(mus_dir,songs[r]))
            except:
                out='Playing Music'
                self.printing_func(out)
                self.speak(out)
                mus_dir = r'D:\Top 20 Kuldeep Manak'
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(mus_dir) - 1)
                os.startfile(os.path.join(mus_dir,songs[r]))
                
        elif 'movie' in user_input:
            out='Playing Movies'
            self.printing_func(out)
            self.speak(out)
            mov_dir = r'D:\movies'
            songs = os.listdir(mov_dir)
            r = random.randint(0,len(mov_dir) - 2)
            os.startfile(os.path.join(mov_dir,songs[r]))

        elif 'screenshot' in user_input:
            out='Take ScreenShot'
            self.printing_func(out)
            self.speak(out)
            path = r'C:\Windows\system32\SnippingTool.exe'
            os.startfile(path)

        elif 'my' in user_input and 'image' in user_input or 'photo' in user_input or 'picture' in user_input:
            out='Opening Photos'
            self.printing_func(out)
            self.speak(out)
            path = r'D:\photo\deep'
            os.startfile(path)
        #--------------------------------------------------------------------------------



        #--------------GET LOST CONDITION--------------------------------
        elif 'get' in user_input and 'lost' in user_input:
            out = 'You Can\'t Talk To Me Like This \n I Am Going.'
            self.printing_func(out)
            self.speak(out)
            self.win.destroy()
        #-----------------------------------------------------------------------------
        

            
            
            


        #--------------------NONE CONDITION----------------------------------
        elif user_input == '':        
            out = 'You Said Nothing'
            self.printing_func(out)
            self.speak(out)        
         #-------------------------------------------------------------------------------




        #---------------TIME CONDITION-----------------------------------------
        elif 'time' in user_input:                                                                            #|
            t = datetime.now().strftime('%H  hours and %M minutes')          #|
            o= t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')
            out = 'Current time is : ' + time                                                                   #|
            self.printing_func(out)                                                                                 #|
            self.speak(out)                                                                                                 #|        
        #--------------------------------------------------------------------------------




        #--------------------WIKIPEDIA CONDITION-----------------------------
        elif 'wikipedia' in user_input:                                                                    #|
            i_l = list(user_input.split())                                                                   #|
            i_l.remove('wikipedia')                                                                            #|
            to2 = ''.join(i_l)                                                                                          #|
                                                                        
            try:                                                                                                                #|
                out = 'According To Wikipedia ' + wikipedia.summary(to2,2)   #|
                self.printing_func(out)                                                                               #|
                self.speak(out)                                                                                               #|
            except:                                                                                                          #|
                out='cannot find'                                                                                   #|
                self.printing_func(out)                                                                             #|
                self.speak(out)                                                                                              #|
        #---------------------------------------------------------------------------------


        #----------------------------FINE COMMAND-------------------------------
        elif 'fine' in user_input:
            out = 'Great'
            self.printing_func(out)                                                                             #|
            self.speak(out)
        #-----------------------------------------------------------------------------------



        #----------------SHUTDOWN COMMAND----------------------------------------
        elif 'shutdown' in user_input:
            out='Shutting Down The System'                                                                                   #|
            self.printing_func(out)                                                                             #|
            self.speak(out)
            os.system('shutdown -s')
        #-----------------------------------------------------------------------------------------
            
            



        #-------------------ELSE CONDITION----------------------------------------
        else:                                                                                                                    #|

                to_search = user_input
                out='I Can Search That On Google, May I?'                                                                                   #|
                self.printing_func(out)                                                                             #|
                self.speak(out)

                res = mb.askquestion('Google Search','May I Search That On Google.')

                if res == 'yes':
                    out = 'Opening Google Search'
                    self.printing_func(out)
                    self.speak(out)
                    webbrowser.open('https://www.google.co.in/search?q=' + to_search)
                else:
                    out = 'Ok Sir!!'
                    self.printing_func(out)
                    self.speak(out)

        #--------------------------------------------------------------------------------------

                
                
                

                
                 


    #----------------------------------------------------------------------------------





                               
    #------------------------------------------------------------------------------------------------------------------------------------


        
        

        





    
    #----------------------------------------------------CONSTRUCTER  FUNCTION---------------------------------------------------------
    def __init__(self):
        self.win = Tk()
        self.win.geometry('380x300')
        self.win.resizable(0,0)
        self.win.configure(bg='orange')
        
        Label(self.win, text='SSP ASSISTANT',font=('arial black',18),fg='white',width=30,bg='green',bd=5).pack()

        Label(self.win, text='Me' , font=('arial black',20),fg='white',bg='orange').place(x=60,y=50)
        Label(self.win, text='SSP' , font=('arial black',20),fg='white',bg='orange').place(x=260,y=50)

        self.text_box1 = Text(self.win, font=('arial black',13),width=16,height=5,fg='blue', wrap=WORD )
        self.text_box1.place(x=10,y=100)

        self.text_box2 = Text(self.win, font=('arial black',13),width=15,height=5,fg='orange', wrap=WORD)
        self.text_box2.place(x=200,y=100)

        self.search_var = StringVar()

        Entry(self.win, font=('arial black', 14), width=18,textvariable=self.search_var,bd=5).place(x=10,y=250)

        send = Button(self.win, text='Send', font=('arial black',10),bg='blue',fg='white',bd=5,width=10,command=self.send_func).place(x=270,y=250)

        def enter(*args):
            self.send_func()
            
        self.win.bind('<Return>',enter)
        
        self.win.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------------------



root = Widget()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------CODE FINISH------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
