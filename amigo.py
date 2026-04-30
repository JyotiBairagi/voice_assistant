import pyttsx3
import speech_recognition as sr
import wikipedia

# Fix: wikipedia library uses http:// but Wikipedia now requires https://
wikipedia.set_lang("en")
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    print(f"Amigo: {audio}")
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"[Speech Error]: {e}")


def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, phrase_time_limit=5)
    except Exception as e:
        print(f"[Microphone Error]: {e}")
        return "None"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except sr.UnknownValueError:
        speak("I didnt understand")
        return "None"
    except sr.RequestError as e:
        print(f"[Network Error]: {e}")
        speak("Network error, please check your internet")
        return "None"
    except Exception as e:
        print(f"[Error]: {e}")
        speak("Something went wrong, try again")
        return "None"
    return query


if __name__ == '__main__':

    speak("Amigo assistance activated ")
    speak("How can i help you")
    while True:
        try:
            query = take_command().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia ...")
                search_query = query.replace("wikipedia", '').replace("open", '').replace("search", '').strip()
                if not search_query:
                    speak("Please tell me what to search on Wikipedia")
                    continue
                try:
                    results = wikipedia.summary(search_query, sentences=2)
                    speak("According to wikipedia")
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("There are multiple results. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I could not find anything on Wikipedia.")
                except Exception as e:
                    print(e)
                    speak("Sorry, something went wrong while searching Wikipedia.")
            elif 'are you' in query:
                speak("I am amigo developed by Jaspreet Singh")
            elif 'youtube' in query:
                speak("opening youtube")
                webbrowser.open("https://youtube.com")
            elif 'google' in query:
                speak("opening google")
                webbrowser.open("https://google.com")
            elif 'github' in query:
                speak("opening github")
                webbrowser.open("https://github.com")
            elif 'stackoverflow' in query or 'stack overflow' in query:
                speak("opening stackoverflow")
                webbrowser.open("https://stackoverflow.com")
            elif 'spotify' in query:
                speak("opening spotify")
                webbrowser.open("https://spotify.com")
            elif 'whatsapp' in query:
                speak("opening whatsapp")
                try:
                    os.system("start whatsapp:")
                except Exception as e:
                    print(f"[Error]: Could not open WhatsApp: {e}")
                    speak("Sorry, could not open WhatsApp")
            elif 'play music' in query or 'music' in query:
                speak("opening music")
                webbrowser.open("https://spotify.com")
            elif 'local disk d' in query or 'disk d' in query:
                speak("opening local disk D")
                webbrowser.open("D://")
            elif 'local disk c' in query or 'disk c' in query:
                speak("opening local disk C")
                webbrowser.open("C://")
            elif 'local disk e' in query or 'disk e' in query:
                speak("opening local disk E")
                webbrowser.open("E://")
            elif 'sleep' in query or 'bye' in query or 'exit' in query:
                speak("Goodbye! Going to sleep.")
                exit(0)
        except KeyboardInterrupt:
            print("\nAmigo stopped by user.")
            exit(0)
        except Exception as e:
            print(f"[Error]: {e}")
            speak("Something went wrong, let me try again")
            continue

