'''
Project : Desktop Assistant JARVIS
Author : Arghadip Biswas
Date of Creation : 24th April, 2024
Last Update : 25th April, 2024
Other Info : Check the Project Log
'''
import time

import pyautogui
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
from newsapi.newsapi_client import NewsApiClient
import pycountry
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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


def news():
    try:
        # you have to get your api key from newapi.com and then paste it below
        newsapi = NewsApiClient(api_key='8ccb07280f5842a19048567717c2776a')

        # now we will take name of country from user as input
        speak("Which Country News You want to hear?? Kindly, type it...")
        input_country = input("Country: ")
        input_countries = [f'{input_country.strip()}']
        countries = {}

        # iterate over all the countries in
        # the world using pycountry module
        for country in pycountry.countries:
            # and store the unique code of each country
            # in the dictionary along with it's full name
            countries[country.name] = country.alpha_2

        # now we will check that the entered country name is
        # valid or invalid using the unique code
        codes = [countries.get(country.title(), 'Unknown code')
                 for country in input_countries]

        # now we have to display all the categories from which user will
        # decide and enter the name of that category
        speak("Which Category are you interested in ??")
        option = input(
            "Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")

        # now we will fetch the new according to the choice of the user
        top_headlines = newsapi.get_top_headlines(

            # getting top headlines from all the news channels
            category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

        # fetch the top news under that category
        Headlines = top_headlines['articles']

        # now we will display the that news with a good readability for user
        if Headlines:
            for articles in Headlines:
                b = articles['title'][::-1].index("-")
                if "news" in (articles['title'][-b + 1:]).lower():
                    speak(f"{articles['title'][-b + 1:]}: {articles['title'][:-b - 2]}.")
                    print(
                        f"{articles['title'][-b + 1:]}: {articles['title'][:-b - 2]}.")
                else:
                    print(
                        f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
                    speak(f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
        else:
            print(
                f"Sorry no articles found for {input_country}, Something Wrong!!!")
            speak(f"Sorry no articles found for {input_country}, Something Wrong!!!")
        speak("Do you want to search again??")
        option = input("Do you want to search again [Yes/No] ?")
        if option.lower() == 'yes':
            news()
        else:
            run()
    except Exception as e:
        print("Something Went Wrong Sir, Try Again")
        speak("Something Went Wrong Sir, Try Again")
        news()


# Main Application
def run():
    while True:
        querry = takecommand().lower()

        # Logic Building for tasks :-

        # System :

        if "open notepad" in querry:
            speak("Sure")
            speak("Openning Notepad")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe photoshop" in querry:
            speak("Sure")
            speak("Openning Adobe Photoshop")
            npath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(npath)

        elif "open adobe premiere pro" in querry:
            speak("Sure")
            speak("Openning Adobe Premiere Pro")
            adbprpath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2021\\Adobe Premiere Pro.exe"
            os.startfile(adbprpath)

        elif "open figma" in querry:
            speak("Sure")
            speak("Openning Figma")
            adbprpath = "C:\\Users\\ASUS\\AppData\\Local\\Figma\\app-116.15.4\\Figma.exe"
            os.startfile(adbprpath)

        elif "open command prompt" in querry or "open cmd" in querry:
            speak("Sure")
            speak("Openning Command Prompt")
            cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdpath)

        elif "play music" in querry or "open music" in querry:
            speak("Sure")
            speak("Playing Music")
            music_dir = "C:\\Users\\ASUS\\Music\\Hindi Bhajans"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

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

        elif "switch windows" in querry or "switch the window" in querry:
            speak("Switching Windows")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        # Online:

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

        elif "customized email" in querry or "customised email" in querry or "customise email" in querry or "customize email" in querry:

            speak("Sure Sir")
            print("Prepairing Customized Email...")
            speak("Prepairing Customized Email")

            try:
                email_list = {
                    "mom": "purnimabiswas0625@gmail.com",
                    "dad": "anupambiswasofficial2023@gmail.com",
                }

                print("is the email saved in your contacts?? [yes/no] ")
                speak("Whom you want to send the mail?? is this in your contacts??")
                comment = input("answer : ")
                if comment.lower() == "yes":
                    print("Say the name of the receipient")
                    speak("Say the name of the receipient")
                    name = takecommand().lower()
                    receiver = email_list[name]
                else:
                    name = input("Enter the receiver's name : ")
                    receiver = input("Enter the email Id : ")


                print("What is the Subject of this Email")
                speak("Ok Sir, What is the Subject of this Email")
                subject = takecommand().lower()
                print("What is the Message for this email??")
                speak("and Sir, What is the Message??")
                message = takecommand().lower()
                speak("Please Enter the Path of the File")
                path = input("Enter the path of the file : ")

                print("Please Wait, I am Sending Email now.....")
                speak("Sending Email")

                msg = MIMEMultipart()
                msg["From"] = "arghadipmath@gmail.com"
                msg["To"] = receiver
                msg["Subject"] = subject

                msg.attach(MIMEText(message, "plain"))

            #   Setup the attachment
                filename = os.path.basename(path)
                attachment = open(path,"rb")
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment; filename= %s" % filename)

            #   Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                # Sending the Email
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("arghadipmath@gmail.com", "xped wwxb ecdw xffv")
                text = msg.as_string()
                server.sendmail("arghadipmath@gmail.com", receiver, text)
                server.quit()

                print(f"Email has been sent to {name}")
                speak(f"Email has been sent to {name}")

            except Exception as e:
                print("Something Went Wrong")
                speak("Something Went Wrong, Try again")
                run()

        elif "tell me news" in querry or "whats the news" in querry or "news" in querry:
            print("Fetching News...")
            speak("Wait a Moment, Fetching News")
            news()



        # Good Bye and Other Salutations:

        elif "thank" in querry or "thanks" in querry or "thank you" in querry:
            statement = ["Its a Pleasure Sir", "Welcome Sir"]
            number = random.randint(0,1)
            speak(statement[number])

        elif "no jarvis" in querry or "no work" in querry or "no other work" in querry:
            speak("Thank You Sir, for using Me.")
            speak("Call me Whenever you need.")

            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<4:
                speak("Bye Boss, Have a Good Night")
            else:
                speak("Bye Boss, Have a Good Day")
            sys.exit()

        else:
            speak("Application Not Available")

        speak("Do You have any other work Sir??")


if __name__ == "__main__":
    wish()
    run()
