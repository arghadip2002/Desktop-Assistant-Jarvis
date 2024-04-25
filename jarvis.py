import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 4:
        speak("Hello Sir, Why are you still Awake??")
    elif hour >= 4 and hour <= 11:
        speak("Good Morning Sir")
    elif hour > 11 and hour < 13:
        speak("Good noon Sir")
    elif hour >= 13 and hour <= 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    string = ["I am Jarvis, How can I help You Sir?", "Boss You are here, Say what help do you need??"]
    wish_statement = string[random.randint(0, 1)]
    speak(wish_statement)


# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=15, phrase_time_limit=60)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : {query}")

    except Exception as e:
        speak("Say that again Please...")
        run()
    return query

# Sending Email
def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("arghadipmath@gmail.com", "xped wwxb ecdw xffv")
    server.sendmail("arghadipmath@gmail.com", to, content)
    server.close()

# Main Application
def run():
    while True:
        querry = takecommand().lower()

        # Logic Building for tasks

        # System

        if "open notepad" in querry:
            speak("Sure")
            speak("Openning Notepad")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            print(querry)

        elif "open adobe photoshop" in querry:
            speak("Sure")
            speak("Openning Adobe Photoshop")
            npath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(npath)
            print(querry)

        elif "open adobe premiere pro" in querry:
            speak("Sure")
            speak("Openning Adobe Premiere Pro")
            adbprpath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2021\\Adobe Premiere Pro.exe"
            os.startfile(adbprpath)
            print(querry)

        elif "open figma" in querry:
            speak("Sure")
            speak("Openning Figma")
            adbprpath = "C:\\Users\\ASUS\\AppData\\Local\\Figma\\app-116.15.4\\Figma.exe"
            os.startfile(adbprpath)
            print(querry)

        elif "open command prompt" in querry or "open cmd" in querry:
            speak("Sure")
            speak("Openning Command Prompt")
            cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdpath)
            print(querry)



        elif "play music" in querry or "open music" in querry:
            speak("Sure")
            speak("Playing Music")
            music_dir = "C:\\Users\\ASUS\\Music\\Hindi Bhajans"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            print(querry)


        elif "open camera" in querry or "open webcam" in querry:
            speak("Sure")
            speak("Openning Webcam")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            print(querry)

        # Online

        elif "ip address" in querry:
            ip = get("https://api.ipify.org").text
            print(f"Your IP address is {ip}")
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in querry:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=5)
            print(results)
            speak(results)

        elif "open youtube" in querry:
            speak("Sure")
            speak("Openning Youtube")
            webbrowser.open("https://www.youtube.com/")

        elif "play song on youtube" in querry:
            speak("Sure")
            print("Openning Youtube...")
            speak("Openning Youtube")
            speak("What song do you want to play??")
            song_name = takecommand().lower()
            speak("Wow Boss, Your Music Taste is good")
            print("Playing your song on Youtube...")
            kit.playonyt(song_name)

        elif "open facebook" in querry:
            speak("Sure")
            speak("Openning Facebook")
            webbrowser.open("https://www.facebook.com/")

        elif "open instagram" in querry:
            speak("Sure")
            speak("Openning Instagram")
            webbrowser.open("https://www.instagram.com/")

        elif "open google" in querry:
            speak("Sure")
            speak("Openning Goocle Chrome Browser")
            webbrowser.open("https://www.google.com/")
            speak("Sir, What should i Search for in Googel!?")
            search = takecommand().lower()
            webbrowser.open(f"{search}")
            content = wikipedia.summary(search,sentences=5)
            print(content)
            speak(content)

        elif "send message" in querry:
            speak("Would you like to type it or you will provide the voice??")
            decision = takecommand().lower()

            if "type" in decision:
                speak("Whom you want to send message?? write the name below :")
                print("Write the name to which you want to send message")

                name = input()
                name = name.lower()
                contacts = {
                    "mom": "+918101540326",
                    "dad": "+918001075264",
                }
                phone_number = contacts[name]

                speak("What is the Message??")

                print("What is the Message?? Write it Below")
                message = input()

                speak("Openning Whatsapp")
                print(
                    f"Message will be delivered at {int(datetime.datetime.now().hour)}:{int(datetime.datetime.now().minute) + 2}")
                kit.sendwhatmsg(phone_number, message, int(datetime.datetime.now().hour),
                                int((datetime.datetime.now().minute) + 2))
                speak(f"Message Send to {name}")
                print(f"Message Send to {name}")


            elif "voice" in decision:
                speak("Whom you want to send message??")

                name = takecommand().lower()
                contacts = {
                    "mom": "+918101540326",
                    "dad": "+918001075264",
                }
                phone_number = contacts[name]

                speak("What is the Message??")

                message = takecommand()

                speak("Openning Whatsapp")
                print(
                    f"Message will be delivered at {int(datetime.datetime.now().hour)}:{int(datetime.datetime.now().minute) + 2}")
                kit.sendwhatmsg(phone_number, message, int(datetime.datetime.now().hour),
                                int((datetime.datetime.now().minute) + 2))
                speak(f"Message Send to {name}")
                print(f"Message Send to {name}")

            else:
                print("try again, Something went wrong!!")
                speak("try again, Something went wrong!!")


        elif "send email" in querry:
            speak("Would you like to type it or you will provide the voice??")
            decision = takecommand().lower()

            if "type" in decision:
                print("Write the name to which you want to send email")
                speak("Whom you want to send email?? write the name below :")

                name = input()
                name = name.lower()
                email_list = {
                    "mom": "purnimabiswas0625@gmail.com",
                    "dad": "anupambiswasofficial2023@gmail.com",
                }
                email_id = email_list[name]

                print("What is the Message?? Write it Below")
                speak("What is the Message??")

                message = input()

                speak("Openning Gmail")

                sendemail(email_id, message)

                speak(f"Email Send to {name}")
                print(f"Email Send to {name}")


            elif "voice" in decision:
                speak("Whom you want to send the email??")

                name = takecommand().lower()
                email_list = {
                    "mom": "purnimabiswas0625@gmail.com",
                    "dad": "anupambiswasofficial2023@gmail.com",
                }
                email_id = email_list[name]

                speak("What is the Message??")

                message = takecommand()

                speak("Openning Gmail")

                sendemail(email_id, message)

                speak(f"Email Send to {name}")
                print(f"Email Send to {name}")

            else:
                print("try again, Something went wrong!!")
                speak("try again, Something went wrong!!")


        elif "thank" in querry or "thanks" in querry or "thank you" in querry:
            statement = ["Its a Pleasure Sir", "Welcome Sir"]
            number = random.randint(0,1)
            speak(statement[number])

        elif "no jarvis" in querry or "no work" in querry or "no other work" in querry:
            speak("Thank You Sir, for using Me.")
            speak("Call me Whenever you need.")
            sys.exit()

            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<4:
                speak("Bye Boss, Have a Good Night")
            else:
                speak("Bye Boss, Have a Good Day")
        else:
            speak("Application Not Available")

        speak("Do You have any other work Sir??")


if __name__ == "__main__":
    # speak("Hello Sir")
    # speak("This is Advanced jarvis")
    # takecommand()
    wish()
    run()
