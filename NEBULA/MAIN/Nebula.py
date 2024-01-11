import pyautogui, struct, pyaudio, pvporcupine, pyttsx3, winsound, pyjokes, winshell, datetime, time, calendar, os
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

genai.configure(api_key="AIzaSyD6rRT40PH1eUyCM7FW4ZDtR2bPUpNjKJQ")

# Set up the model
generation_config = {
  "temperature": 0.7,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 200,
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
    def beep(self,pitch, duration):
        winsound.Beep(pitch, duration)

    def speak(self,text):
        engine = pyttsx3.init()
        print(text)
        engine.say(text)
        engine.runAndWait()

    def time_now(self):
        return str(datetime.datetime.now().strftime("%I:%M %p"))

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

    def date(self):
        now = datetime.datetime.now()
        date_now = datetime.datetime.today()
        week_now = calendar.day_name[date_now.weekday()]
        month_now = now.month
        day_now = now.day

        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

        ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

        self.speak(f"Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.")

    def new_desktop(self):    
        pyautogui.hotkey('ctrl', 'win', 'd')

    def switch_desktop(self,direction):    
        pyautogui.hotkey('ctrl', 'win', direction)

    def switch_window(self):
        pyautogui.hotkey('alt', 'tab')

    def maximise_window(self):
        pyautogui.hotkey('win', 'up')

    def open(self,query):
        if "paint" in query: os.system("start mspaint")
        if "notepad" in query: os.system("start Notepad")
        if "chrome" in query: os.system("start chrome")
        if "edge" in query: os.system("start msedge")
        if "firefox" in query: os.system("start firefox")
        if "cmd" in query or "command prompt" in query: os.system("start cmd")
        if "blender" in query: os.system('start "C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender-launcher.exe"')
        if "file" in query and "explorer" in query: pyautogui.hotkey("win", "e")
        if "setting" in query: pyautogui.hotkey("win", "i")
        if "word" in query: os.system("start winword")
        if "excel" in query: os.system("start excel")
        if "powerpoint" in query: os.system("start powerpnt")
        if "calculator" in query: os.system("start calc")
        if "youtube" in query: os.system("start https://www.youtube.com/")
        if "google" in query: os.system("start https://www.google.com/")
        if "scratch" in query: os.system("start https://scratch.mit.edu/")
        if "wikipedia" in query: os.system("start https://en.wikipedia.org/wiki/Main_Page")
        if "github" in query: os.system("start https://www.github.com/")
        if "stack" and "over" and "flow" in query: os.system("start https://stackoverflow.com/")
        if "amazon" in query: os.system("start https://www.amazon.com")
        if "facebook" in query: os.system("start https://www.facebook.com")
        if "instagram" in query: os.system("start https://instagram.com")
        if "twitter" in query: os.system("start https://twitter.com")
        if "linked in" in query: os.system("start https://linkedin.com")
        if "mail" in query: os.system("start https://mail.google.com")
        if "outlook" in query: os.system("start https://outlook.office365.com")

    def typewrite(self,query):
        pyautogui.typewrite(str(query).replace('type', ''))
        

    def press(self,query:str):
        query = query.replace('press', '')
        if 'full' in query and 'stop' in query: pyautogui.press('.'); 
        elif 'period' in query: pyautogui.press('.'); 
        elif "enter" in query: pyautogui.press('enter'); 
        elif "tab" in query: pyautogui.press('tab'); 
        elif "escape" in query: pyautogui.press('esc'); 
        elif "space" in query: pyautogui.press('space'); 
        elif "right" in query or "light" in query or "write" in query: pyautogui.press('right'); 
        elif "left" in query: pyautogui.press('left'); 
        elif "up" in query: pyautogui.press('up'); 
        elif "down" in query: pyautogui.press('down'); 
        elif 'one' in query or '1' in query: pyautogui.press('1'); 
        elif 'two' in query or '2' in query: pyautogui.press('2'); 
        elif 'three' in query or '3' in query: pyautogui.press('3'); 
        elif 'four' in query or '4' in query: pyautogui.press('4');   
        elif 'five' in query or '5' in query: pyautogui.press('5'); 
        elif 'six' in query or '6' in query: pyautogui.press('6'); 
        elif 'seven' in query or '7' in query: pyautogui.press('7'); 
        elif 'eight' in query or '8' in query: pyautogui.press('8'); 
        elif 'nine' in query or '9' in query: pyautogui.press('9'); 
        elif 'zero' in query or '0' in query: pyautogui.press('0'); 
        elif 'a' in query: pyautogui.press('a'); 
        elif 'b' in query: pyautogui.press('b'); 
        elif 'c' in query: pyautogui.press('c'); 
        elif 'd' in query: pyautogui.press('d'); 
        elif 'e' in query: pyautogui.press('e'); 
        elif 'f' in query: pyautogui.press('f'); 
        elif 'g' in query: pyautogui.press('g'); 
        elif 'h' in query: pyautogui.press('h'); 
        elif 'i' in query: pyautogui.press('i'); 
        elif 'j' in query: pyautogui.press('j'); 
        elif 'k' in query: pyautogui.press('k'); 
        elif 'l' in query: pyautogui.press('l'); 
        elif 'm' in query: pyautogui.press('m'); 
        elif 'n' in query: pyautogui.press('n'); 
        elif 'o' in query: pyautogui.press('o'); 
        elif 'p' in query: pyautogui.press('p'); 
        elif 'q' in query: pyautogui.press('q'); 
        elif 'r' in query: pyautogui.press('r'); 
        elif 's' in query: pyautogui.press('s'); 
        elif 't' in query: pyautogui.press('t'); 
        elif 'u' in query: pyautogui.press('u'); 
        elif 'v' in query: pyautogui.press('v'); 
        elif 'w' in query: pyautogui.press('w'); 
        elif 'x' in query: pyautogui.press('x'); 
        elif 'y' in query: pyautogui.press('y'); 
        elif 'z' in query: pyautogui.press('z'); 

    def minimise(self):
        pyautogui.keyDown('win')
        pyautogui.press('down')
        pyautogui.press('down')
        

    def screenshot(self):
        self.speak("Sir, please tell me name of screenshot file.")
        while len(name) <= 0: name = takeCommand()
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.beep(10000, beep_modes[beep_mode-1])
        

    def volume(self,dir):
        if any(["up" in dir,"raise" in dir,"increase" in dir]):
            for x in range(5):
                pyautogui.press("volumeup")
        elif any(["down" in dir,"decrease" in dir,"increase" in dir]):
            for x in range(5):
                pyautogui.press("volumedown")
        elif any(["off" in dir,"mute" in dir]): pyautogui.press("volumemute")
        else: self.speak("Sorry sir. I don't understand that. Please try again.")
        

    def empty_recycle_bin(self):
        try:
            winshell.recycle_bin().empty(
                confirm=False, show_progress=False, sound=True
            )
            self.speak("Recycle Bin Emptied")
        except:
            self.speak("Your Recycle Bin was already empty.")
        

    def joke(self):
        self.speak(pyjokes.get_joke())
        
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

    def google_search(self,query):
        search = str(query).split()
        search[0] = ''
        search = ' '.join(search)
        offline.speak(offline,f'Searching for {search}')
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        result = data.find("div", class_="BNeawe").text
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
            if weather_true is True: return(f"The weather in {city} is {weather.lower()} and the temperature is {temp_celsius} degrees Celsius.")
            else: return(f"The temperature in {city} is {temp_celsius} degree celsius.")

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

    def play_on_yt(self,query):
        query = str(query)
        if query.split()[0] == 'play': query = query.replace('play ', '')
        if 'on youtube' in query: query.replace('on youtube', '')
        elif 'in youtube' in query: query.replace('in youtube', '')
        pywhatkit.playonyt(query)

    def wikipedia_func(self,query:str):
        offline.speak(offline,"searching wikipedia...")
        query = query.replace("wikipedia" ,"")
        results = wikipedia.summary(query, sentences=2)
        offline.speak(offline,"According to wikipedia:")
        offline.speak(offline,results)

    def ai(self, prompt):
        try:
            response = model.generate_content([str(prompt)])
            return response.text
        except:
            return response.prompt_feedback
    

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
    query = ''
    query = takeCommand()
    
    if "system" in query:
        if "shut" in query: os.system("shutdown /s /t 5"); 
        elif "restart system" in query: os.system("shutdown /r /t 5");
        elif "sleep the system" in query: os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0");
  
    elif "study" in query and "bot" in query:
        try:    
            on.study_bot()
        except:
            off.speak(phrases[0])
            
    elif "close" in query:
        if "tab" in query:
            pyautogui.hotkey("ctrl","w")
            
        if "window" in query:
            pyautogui.hotkey("alt", "f4")
            
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
                
            elif "how" in query:
                off.speak("I\'m doing great! Hope you are doing great as well.")
            elif "stop" in query or "exit" in query:
                off.speak("Exiting JARVIS.")
                exit()
        
        if "date" in query:
            off.date()
            
        if "time" in query:
            off.speak(f'It is {off.time_now()} right now.')
            
        if "new" in query or "make" in query or "create" in query:
            if "desktop" in query:
                off.speak('Making a new desktop')
                off.new_desktop()
                
            if "tab" in query:
                pyautogui.hotkey("ctrl", "t")
                
            if "square" in query: 
                pyautogui.moveTo(x=440, y=63, duration = 2)
                pyautogui.click()
                pyautogui.moveTo(x=440, y=281, duration = 2)
                pyautogui.dragRel(xOffset=100, yOffset=100, duration = 2)
                pyautogui.press('enter')
                
            if "circle" in query:
                pyautogui.moveTo(x=420, y=60, duration = 2)
                pyautogui.click()
                pyautogui.moveTo(x=450, y=450, duration = 2)
                pyautogui.dragRel(xOffset=100, yOffset=100, duration = 2)
                pyautogui.press('enter')
                
            if "triangle" in query:
                pyautogui.moveTo(x=500, y=60, duration = 2)
                pyautogui.click()
                pyautogui.moveTo(x=965, y=270, duration = 2)
                pyautogui.dragRel(xOffset=100, yOffset=100, duration = 2)
                pyautogui.press('enter')
                
        if "joke" in query:
            off.joke()
            
        if all(["recycle" in query, "bin" in query, "empty" in query]):
            off.empty_recycle_bin()
        
        if "close" in query:
            if "tab" in query:
                pyautogui.hotkey("ctrl","w")
                
            if "window" in query:
                pyautogui.hotkey("alt", "f4")
            
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
            
        if "news" in query:
            try:
                on.news()
            except:
                off.speak(phrases[0])
             
        if "volume" in query:
            off.volume(query)
            
        if "mute" in query:
            off.volume(query)
            
        if "start" in query or "open" in query:
            if "paint" in query: os.system("start mspaint"); 
            if "notepad" in query: os.system("start Notepad"); 
            if "chrome" in query: os.system("start chrome"); 
            if "edge" in query: os.system("start msedge"); 
            if "firefox" in query: os.system("start firefox"); 
            if "cmd" in query or "command prompt" in query: os.system("start cmd"); 
            if "file" in query and "explorer" in query: pyautogui.hotkey("win", "e"); 
            if "setting" in query: pyautogui.hotkey("win", "i"); 
            if "word" in query: os.system("start winword"); 
            if "excel" in query: os.system("start excel"); 
            if "powerpoint" in query: os.system("start powerpnt"); 
            if "calculator" in query: os.system("start calc"); 
            if "youtube" in query: os.system("start https://www.youtube.com/"); 
            if "google" in query: os.system("start https://www.google.com/"); 
            if "scratch" in query: os.system("start https://scratch.mit.edu/"); 
            if "wikipedia" in query: os.system("start https://en.wikipedia.org/wiki/Main_Page"); 
            if "github" in query: os.system("start https://www.github.com/"); 
            if "stack" and "over" and "flow" in query: os.system("start https://stackoverflow.com/"); 
            if "amazon" in query: os.system("start https://www.amazon.com"); 
            if "facebook" in query: os.system("start https://www.facebook.com"); 
            if "instagram" in query: os.system("start https://instagram.com"); 
            if "twitter" in query: os.system("start https://twitter.com"); 
            if "linked in" in query: os.system("start https://linkedin.com"); 
            if "mail" in query: os.system("start https://mail.google.com"); 
            if "outlook" in query: os.system("start https://outlook.office365.com"); 
     
        if "screenshot" in query:
            off.screenshot()
            
        if "wikipedia" in query:
            try:
                on.wikipedia_func(query)
            except:
                off.speak(phrases[0])


while True:
    if hot.hotword_detection():
        print("Hotword detected")
        TaskExicution()