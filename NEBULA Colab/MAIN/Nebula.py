import pyautogui, struct, pyaudio, cv2, pvporcupine, pyttsx3, winsound, pyjokes, psutil, winshell, datetime, time, calendar, os
import speech_recognition as sr
from vosk import KaldiRecognizer, Model
import google.generativeai as genai
try:
    import requests, wolframalpha,wikipedia, pywhatkit
    from pywikihow import search_wikihow
    from bs4 import BeautifulSoup
    from requests import get
except:
    pass

access_key = '5mLOpx/ci8CdIns0Ug53C4BfUC8/TPzc+5SaXxDznLs9tnhX9BdRUQ=='

porcupine = None
pa = None
audio_stream = None

executed_q = False
# mouse = False

def task_executed():
    global executed_q
    executed_q = True

genai.configure(api_key="AIzaSyDVDA8FLlosD6JwJ6yteOO-GjLX6l5PgG0")

# Set up the model
generation_config = {
  "temperature": 0.7,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 1000,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",  
                            generation_config=generation_config,
                            safety_settings=safety_settings)

class hotword:
    def setup(self):
        global audio_stream,porcupine,pa
        porcupine = None
        pa = None
        audio_stream = None

        porcupine = pvporcupine.create(access_key=access_key, keywords=['jarvis'])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        print("JARVIS at your service")

    def hotword_detection(self):
        global porcupine, pa, audio_stream
        try:
            self.setup()
            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h"*porcupine.frame_length, pcm)
                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0:
                    return True
                    
        finally:
            if porcupine is not None:
                porcupine.delete()

class offline:
    # import mediapipe as mp
    # cam = cv2.VideoCapture(0) 
    # face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) 
    # screen_w, screen_h = pyautogui.size() 
    def beep(self,pitch, duration):
        winsound.Beep(pitch, duration)

    def speak(self,text):
        engine = pyttsx3.init()
        print(text)
        engine.say(text)
        engine.runAndWait()

    def time_now(self):
        task_executed()
        return str(datetime.datetime.now().strftime("%I:%M %p"))
    
    def mousemove(self):
        global cam, face_mesh, screen_w, screen_h
        _, frame = cam.read() 
        frame = cv2.flip(frame, 1) 
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        output = face_mesh.process(rgb_frame) 
        landmark_points = output.multi_face_landmarks 
        frame_h, frame_w, _ = frame.shape 

        

        
        if landmark_points: 
            landmarks = landmark_points[0].landmark 
            for id, landmark in enumerate(landmarks[474:478]): 
                x = int(landmark.x * frame_w) 
                y = int(landmark.y * frame_h) 
                cv2.circle(frame, (x, y), 3, (0, 255, 0)) 




                if id == 1: 
                    screen_x = screen_w * landmark.x 
                    screen_y = screen_h * landmark.y 
                    pyautogui.moveTo(screen_x, screen_y) 



            left = [landmarks[145], landmarks[159]] 
            for landmark in left: 
                x = int(landmark.x * frame_w) 
                y = int(landmark.y * frame_h) 
                cv2.circle(frame, (x, y), 3, (0, 255, 255))



            
            if (left[0].y - left[1].y) < 0.004: 
                print("Left clicked performed")
                pyautogui.click() 
                pyautogui.sleep(1) 


            
            right = [landmarks[145], landmarks[159]] 
            for landmark in right: 
                x = int(landmark.x * frame_w) 
                y = int(landmark.y * frame_h) 
                cv2.circle(frame, (x, y), 3, (0, 255, 255)) 



            
            if (right[0].y - right[1].y) < 0.004:
                print("Right clicked performed")
                pyautogui.rightClick() 
                pyautogui.sleep(1) 



            
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)

    def wishme(self,greetings):
        hour = int(datetime.datetime.now().hour)
        self.speak(f"It is {time()}.")

        if hour>=0 and hour<=12:
            self.speak(f"Good Morning sir.")
        elif hour>=12 and hour<=18:
            self.speak(f"Good Afternoon sir.")
        else:
            self.speak(f"Good Evening sir.")

        if greetings is True:
            self.speak("How can I help you?")
        task_executed()

    def date(self):
        now = datetime.datetime.now()
        date_now = datetime.datetime.today()
        week_now = calendar.day_name[date_now.weekday()]
        month_now = now.month
        day_now = now.day

        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

        ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

        self.speak(f"Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.")
        task_executed()

    def new_desktop(self):    
        pyautogui.hotkey('ctrl', 'win', 'd')
        task_executed()

    def switch_desktop(self,direction):    
        pyautogui.hotkey('ctrl', 'win', direction)
        task_executed()

    def switch_window(self):
        pyautogui.hotkey('alt', 'tab')
        task_executed()
    def maximise_window(self):
        pyautogui.hotkey('win', 'up')
        task_executed()
    def open(self,query):
        if "paint" in query: os.system("start mspaint"); task_executed()
        if "notepad" in query: os.system("start Notepad");task_executed()
        if "chrome" in query: os.system("start chrome");task_executed()
        if "edge" in query: os.system("start msedge");task_executed()
        if "firefox" in query: os.system("start firefox");task_executed()
        if "cmd" in query or "command prompt" in query: os.system("start cmd");task_executed()
        if "blender" in query: os.system('start "C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender-launcher.exe"');task_executed()
        if "file" in query and "explorer" in query: pyautogui.hotkey("win", "e");task_executed()
        if "setting" in query: pyautogui.hotkey("win", "i");task_executed()
        if "word" in query: os.system("start winword");task_executed()
        if "excel" in query: os.system("start excel");task_executed()
        if "powerpoint" in query: os.system("start powerpnt");task_executed()
        if "calculator" in query: os.system("start calc");task_executed()
        if "youtube" in query: os.system("start https://www.youtube.com/");task_executed()
        if "google" in query: os.system("start https://www.google.com/");task_executed()
        if "scratch" in query: os.system("start https://scratch.mit.edu/");task_executed()
        if "wikipedia" in query: os.system("start https://en.wikipedia.org/wiki/Main_Page");task_executed()
        if "github" in query: os.system("start https://www.github.com/");task_executed()
        if "stack" and "over" and "flow" in query: os.system("start https://stackoverflow.com/");task_executed()
        if "amazon" in query: os.system("start https://www.amazon.com");task_executed()
        if "facebook" in query: os.system("start https://www.facebook.com");task_executed()
        if "instagram" in query: os.system("start https://instagram.com");task_executed()
        if "twitter" in query: os.system("start https://twitter.com");task_executed()
        if "linked in" in query: os.system("start https://linkedin.com");task_executed()
        if "mail" in query: os.system("start https://mail.google.com");task_executed()
        if "outlook" in query: os.system("start https://outlook.office365.com");task_executed()
        if executed_q is False:
            pyautogui.press("win")
            time.sleep(1)
            pyautogui.typewrite(str(query).replace("open",''))
            time.sleep(1)
            pyautogui.press("enter")
            task_executed()
        
    def typewrite(self,query):
        pyautogui.typewrite(str(query).replace('type', ''))
        task_executed()
      
    def press(self,query:str):
        query = query.replace('press', '')
        if 'full' in query and 'stop' in query: pyautogui.press('.'); task_executed()
        elif 'period' in query: pyautogui.press('.'); task_executed()
        elif "enter" in query: pyautogui.press('enter'); task_executed()
        elif "tab" in query: pyautogui.press('tab'); task_executed()
        elif "escape" in query: pyautogui.press('esc'); task_executed()
        elif "space" in query: pyautogui.press('space'); task_executed()
        elif "right" in query or "light" in query or "write" in query: pyautogui.press('right'); task_executed()
        elif "left" in query: pyautogui.press('left'); task_executed()
        elif "up" in query: pyautogui.press('up'); task_executed()
        elif "down" in query: pyautogui.press('down'); task_executed()
        elif 'one' in query or '1' in query: pyautogui.press('1'); task_executed()
        elif 'two' in query or '2' in query: pyautogui.press('2'); task_executed()
        elif 'three' in query or '3' in query: pyautogui.press('3'); task_executed()
        elif 'four' in query or '4' in query: pyautogui.press('4');   task_executed()
        elif 'five' in query or '5' in query: pyautogui.press('5'); task_executed()
        elif 'six' in query or '6' in query: pyautogui.press('6'); task_executed()
        elif 'seven' in query or '7' in query: pyautogui.press('7'); task_executed()
        elif 'eight' in query or '8' in query: pyautogui.press('8'); task_executed()
        elif 'nine' in query or '9' in query: pyautogui.press('9'); task_executed()
        elif 'zero' in query or '0' in query: pyautogui.press('0'); task_executed()
        elif 'a' in query: pyautogui.press('a'); task_executed()
        elif 'b' in query: pyautogui.press('b'); task_executed()
        elif 'c' in query: pyautogui.press('c'); task_executed()
        elif 'd' in query: pyautogui.press('d'); task_executed()
        elif 'e' in query: pyautogui.press('e'); task_executed()
        elif 'f' in query: pyautogui.press('f'); task_executed()
        elif 'g' in query: pyautogui.press('g'); task_executed()
        elif 'h' in query: pyautogui.press('h'); task_executed()
        elif 'i' in query: pyautogui.press('i'); task_executed()
        elif 'j' in query: pyautogui.press('j'); task_executed()
        elif 'k' in query: pyautogui.press('k'); task_executed()
        elif 'l' in query: pyautogui.press('l'); task_executed()
        elif 'm' in query: pyautogui.press('m'); task_executed()
        elif 'n' in query: pyautogui.press('n'); task_executed()
        elif 'o' in query: pyautogui.press('o'); task_executed()
        elif 'p' in query: pyautogui.press('p'); task_executed()
        elif 'q' in query: pyautogui.press('q'); task_executed()
        elif 'r' in query: pyautogui.press('r'); task_executed()
        elif 's' in query: pyautogui.press('s'); task_executed()
        elif 't' in query: pyautogui.press('t'); task_executed()
        elif 'u' in query: pyautogui.press('u'); task_executed()
        elif 'v' in query: pyautogui.press('v'); task_executed()
        elif 'w' in query: pyautogui.press('w'); task_executed()
        elif 'x' in query: pyautogui.press('x'); task_executed()
        elif 'y' in query: pyautogui.press('y'); task_executed()
        elif 'z' in query: pyautogui.press('z'); task_executed()

    def minimise(self):
        pyautogui.keyDown('win')
        pyautogui.press('down')
        pyautogui.press('down')
        task_executed()
        
    def screenshot(self):
        self.speak("Sir, please tell me name of screenshot file.")
        while len(name) <= 0: name = takeCommand()
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.beep(10000, beep_modes[beep_mode-1])
        task_executed()
        
    def volume(self,dir):
        if any(["up" in dir,"raise" in dir,"increase" in dir]):
            for x in range(5):
                pyautogui.press("volumeup")
        elif any(["down" in dir,"decrease" in dir,"increase" in dir]):
            for x in range(5):
                pyautogui.press("volumedown")
        elif any(["off" in dir,"mute" in dir]): pyautogui.press("volumemute")
        else: self.speak("Sorry sir. I don't understand that. Please try again.")
        task_executed()
        
    def empty_recycle_bin(self):
        try:
            winshell.recycle_bin().empty(
                confirm=False, show_progress=False, sound=True
            )
            self.speak("Recycle Bin Emptied")
        except:
            self.speak("Your Recycle Bin was already empty.")
        task_executed()
        
    def joke(self):
        self.speak(pyjokes.get_joke())
        task_executed()
        
    def alarm(self,query):
        timehere = open("Alarm.txt", "a")
        timehere.write(query)
        timehere.close()
        task_executed()

class online:
    def study_bot(self):
        offline.speak(offline,"Starting Study Bot")
        offline.speak(offline,'3')
        offline.speak(offline,'2')
        offline.speak(offline,'1')
        while True:
            query = takeCommand()
            if query:
                if "exit" in query or "quit" in query:
                    if "study" and "bot" in query:
                        offline.speak(offline,"Exiting Study Bot.")
                        break
                app_id = 'LYR3K9-XQ9YJAW95V'
                req = wolframalpha.Client(app_id)
                requ = req.query(query)
                try:
                    result = next(requ.results).text
                    offline.speak(offline,result)
                except:
                    offline.speak(offline,"Sorry. I don't know that one.")
        task_executed()

    def google_search(self,query):
        search = str(query).split()
        search[0] = ''
        search = ' '.join(search)
        offline.speak(offline,f'Searching for {search}')
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        result = data.find("div", class_="BNeawe").text
        task_executed()
        return result

    def weather(self,city:str, weather_true:bool):
        api_key = '30d4741c779ba94c470ca1f63045390a'
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
        if weather_data.json()['cod'] == '404':
            return f'Sorry. {city} city was not found.'
        else:
            weather = str(weather_data.json()['weather'][0]['main'])
            temp = round(weather_data.json()['main']['temp'])
            temp_celsius = round((temp - 32) * 5 / 9)
            if weather_true is True: 
                task_executed()
                return(f"The weather in {city} is {weather.lower()} and the temperature is {temp_celsius} degrees Celsius.")
            else: 
                task_executed()
                return(f"The temperature in {city} is {temp_celsius} degree celsius.")

    def search_engine(self):
        offline.speak(offline,"Starting Search Engine")
        while True:
            offline.speak(offline,"What do you want to search?")
            how = takeCommand()
            if "search" in how:
                how_list = how.split(' ')
                
                if "exit" in how or "close" in how:
                    if "search engine" in how:
                        offline.speak(offline,"shutting down search engine")
                        break
                offline.speak(offline,"Please wait, fetching the best article from google for you.")
                try:
                    max_result = 1
                    how_to = search_wikihow(how, max_result)
                    assert len(how_to) == 1
                    offline.speak(offline,'Do you want me to make a new speak file for this article?')
                    speak_file_bool = takeCommand()
                    if "yes" in speak_file_bool or "yeah" in speak_file_bool or "yep" in speak_file_bool:
                        text_file_name = input('File name: ')
                        text_file = open(f'{text_file_name}.txt', 'a')
                        text_file.write(how_to[0].summary)
                        print(how_to[0].summary)
                        text_file.close()
                        offline.speak(offline,'Done')
                    else:
                        offline.speak(offline,how_to[0].summary)
                except:
                    offline.speak(offline,"Sorry sir, I am not able to find this")
        task_executed()

    def news(self):
        main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=61f1f891a2bd44aab7d01ddc21e3b3e9'

        main_page = requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day=["first" , "second", "third", "fourth", "fifth", "sixth" , "seventh" , "eighth" , "ninth" , "tenth"]
        for ar in articles:
            head.append(ar["title"])

        for i in range(len(day)):
            offline.speak(offline,f"Today's {day[i]} news is: {head[i]}")
        task_executed()

    def play_on_yt(self,query):
        query = str(query)
        if query.split()[0] == 'play': query = query.replace('play ', '')
        if 'on youtube' in query: query = query.replace('on youtube', '')
        elif 'in youtube' in query: query = query.replace('in youtube', '')
        pywhatkit.playonyt(query)
        task_executed()

    def wikipedia_func(self,query:str):
        offline.speak(offline,"searching wikipedia...")
        query = query.replace("wikipedia" ,"")
        results = wikipedia.summary(query, sentences=2)
        offline.speak(offline,"According to wikipedia:")
        offline.speak(offline,results)
        task_executed()

    def ai(self, prompt):
        try:
            response = model.generate_content([str(prompt)])
            task_executed()
            return response.text
        except Exception as e:
            task_executed()
            print(e)
            print(response.prompt_feedback)
            return "Sorry. Due to some issue, I couldn't help you with that."
    

phrases = ["Internet is required for this function."]

on = online()
off = offline()
hot = hotword()
beep_modes = [100,1000]
beep_mode = 1



def takeCommand():
    try:
        recognizer_online = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print("Listening...")
                off.beep(1000,beep_modes[beep_mode-1])
                recognizer_online.adjust_for_ambient_noise(source)
                audio = recognizer_online.listen(source)
                print("Recognising...")
                off.beep(1000,beep_modes[beep_mode-1])
                text = recognizer_online.recognize_google(audio)
                if len(text) > 0: print(text)
                return text.lower()
            except Exception as e:
                print(e)
                return ''
    except Exception as e:
        print(e)
        return ''

def TaskExicution():
    global executed_q, mouse
    query = ''
    query = takeCommand()
    executed_q = False
    if "system" in query:
        if "shut" in query: os.system("shutdown /s /t 5"); task_executed()
        elif "restart system" in query: os.system("shutdown /r /t 5");task_executed()
        elif "sleep the system" in query: os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0");task_executed()
  
    elif "study" in query and "bot" in query:
        try:    
            on.study_bot()
        except:
            off.speak(phrases[0])

   
            
    elif "close" in query:
        if "tab" in query:
            pyautogui.hotkey("ctrl","w")
            task_executed()
            
        if "window" in query:
            pyautogui.hotkey("alt", "f4")
            task_executed()
            
    elif "search" in query and "engine" in query:
        if "start" in query or "open" in query or "initialise" in query or "initialize" in query:
            try:
                on.search_engine()
            except:
                off.speak(phrases[0])
                       
    elif "type" in query:
        off.typewrite(query)
                

   
    elif "press" in query:
        off.press(query)

    elif "note" in query:
        with open("notes.txt", "a+") as f:
            var = (query.split()[1:(len(query.split()))])
            text = ''
            for x in var: text = text + x + ' '
            off.speak(f"I have noted {text}.")
            f.write(text +"\n")
        f.close()
        
    else:
        if "jarvis" in query or "you" in query:
            if "hello" in query or "hi" in query or "hey" in query:
                off.speak('Hey there!')
                task_executed()
                
            elif "how" in query:
                off.speak("I\'m doing great! Hope you are doing great as well.")
                task_executed()
            elif "stop" in query or "exit" in query:
                off.speak("Exiting JARVIS.")
                task_executed()
                exit()
        
        if "click" in query:
            if "left" in query:
                pyautogui.leftClick()
            elif "right" in query:
                pyautogui.rightClick()
            else:
                pyautogui.leftClick()

        if "eye" in query and "control" in query:
            if "on" in query:
                mouse = True
            elif "off" in query:
                mouse = False
            else:
                if mouse is True:
                    mouse = False
                else:
                    mouse = True
        
        if "date" in query:
            off.date()
            
        if "time" in query:
            off.speak(f'It is {off.time_now()} right now.')

        if "clear" in query:
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            task_executed()
            
        if "new" in query or "make" in query or "create" in query:
            if "desktop" in query:
                off.speak('Making a new desktop')
                off.new_desktop()
                
            if "tab" in query:
                pyautogui.hotkey("ctrl", "t")
                task_executed()
                
            if "square" in query or "rectangle" in query: 
                try:
                    pyautogui.locateCenterOnScreen("MAIN\\Images\\Paint - Rectangle.png")
                    pyautogui.click()
                    pyautogui.moveTo(x=440, y=281, duration = 2)
                    pyautogui.dragRel(xOffset=100, yOffset=100, duration = 2)
                    pyautogui.press('enter')
                except: 
                    off.speak("Sorry, I couldn't execute this function currently.")
                task_executed()
                
            if "circle" in query:
                try:
                    pyautogui.click(pyautogui.locateCenterOnScreen("MAIN\\Images\\Screenshot 2024-01-23 140735.png"))
                    pyautogui.moveTo(x=450, y=450, duration = 2)
                    pyautogui.leftClick()
                    pyautogui.dragRel(xOffset=100, yOffset=100, duration = 2)
                    pyautogui.press('enter')
                except:
                    off.speak("Sorry, I couldn't execute this function currently.")
                task_executed()
                
            if "triangle" in query:
                try:
                    pyautogui.locateCenterOnScreen("MAIN\\Images\\Paint - Triangle.png")
                    pyautogui.click()
                    pyautogui.moveTo(x=965, y=270, duration = 2)
                    pyautogui.dragRel(xOffset=100, yOffset=100, duration = 2)
                    pyautogui.press('enter')
                except: 
                    off.speak("Sorry, I couldn't execute this function currently.")
                task_executed()
                
        if "joke" in query:
            off.joke()

        
        if "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            off.speak(f"our sustem has {percentage} percent")
            
        if all(["recycle" in query, "bin" in query, "empty" in query]):
            off.empty_recycle_bin()
        
        if "close" in query:
            if "tab" in query:
                pyautogui.hotkey("ctrl","w")
                task_executed()
                
            if "window" in query:
                pyautogui.hotkey("alt", "f4")
                task_executed()
            
        if "switch" in query:
            if "desktop" in query:
                if "right" in query or "write" in query or "light" in query:
                    off.switch_desktop('right')
                    
                elif "left" in query:
                    off.switch_desktop('left')
                    
            if "window" in query:
                off.switch_window()
                
        if any(["minimise" in query, "minimize" in query]):
            off.minimise()
            
        if "play" in query:
            try:
                on.play_on_yt(query)
            except:
                off.speak(phrases[0])
            
        if "search" in query:
            try:
                off.speak(on.google_search(query))
            except:
                off.speak(offline,phrases[0])
            
        if "weather" in query or "whether" in query:
            try:
                off.speak(on.weather(query.split()[(query.split().index("in"))+1], True))
            except:
                off.speak(phrases[0])
            
        if "temperature" in query:
            off.speak(on.weather(query.split()[(query.split().index("in"))+1], False))
            
        if "ip address" in query:
            ip = get('https://api.ipify.org')
            off.speak(f"Your IP adress is->{ip}")
            task_executed()
            
        if "news" in query:
            try:
                on.news()
            except:
                off.speak(phrases[0])
                task_executed()
             
        if "volume" in query:
            off.volume(query)
            
        if "mute" in query:
            off.volume(query)
            
        if "start" in query or "open" in query:
            off.open(query)

        if "screenshot" in query:
            off.screenshot()
            
        if "wikipedia" in query:
            try:
                on.wikipedia_func(query)
            except:
                off.speak(phrases[0])
        if executed_q is False:
            pass
            off.speak(on.ai(query))




