import csv
from datetime import datetime
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

def record_text():
    while True:
        try:
            with sr.Microphone() as source1:
                r.adjust_for_ambient_noise(source1, duration=0.2)
                audio2 = r.listen(source1)
                Mytext = r.recognize_google(audio2)
                print(Mytext)
                return Mytext
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            speak("Could not request results")
        except sr.UnknownValueError:
            print("Sorry,say again")
            speak("Sorry,say again")

def speak(text):
    engine.say(text)
    engine.runAndWait()



def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    
    print("\nSpeak the category (e.g.-Food/Rent/Transport/etc)")
    speak("Speak the category")
    category = record_text()
    
    print("\nSpeak the number of your amount (e.g., '100'):")
    speak("Speak the number of your amount")
    amount = record_text()
    
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        speak("Invalid amount. Please enter a number.")
        return
    
    print("\nSpeak a description (optional):")
    speak("describe or else say no description")
    description = record_text() or "No description"
    
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully! Thank you")
    speak("Expense added successfully! Thank you")

    print("Do you want to continue?if no close or say 'New Expenses', 'Show My Expenses',")
    speak("Do you want to continue?if no close or say 'New Expenses', 'Show My Expenses',")
    

def view_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
            print("Do you want to continue?if no close or say 'New Expenses', 'Show My Expenses',")
            speak("Do you want to continue?if no close or say 'New Expenses', 'Show My Expenses',")
    except FileNotFoundError:
        print("No expenses recorded yet.")
        speak("No expenses recorded yet.")

# Main loop
print("\nStudent Budget Tracker (Voice Input)")
print("1. New Expenses")
print("2. Show My Expenses")
print("3. close")
speak("say New expenses , say show to view all expenses , say close to exit the tracker")

while True:

    print("Now listening.....")
    speak("Now listening.....")

    print(record_text,end=' ')

    text = record_text()

    print(type(record_text))
    if "new" in text.lower():
        add_expense()
    elif "show" in text.lower():
        view_expenses()
    elif "close" in text.lower():
        print("Exiting...")
        speak("Have a good day")
        break
    else:
        print("Invalid command. Please say 'New Expenses', 'Show My Expenses', or 'close'.")
        speak("Invalid command. Please say 'New Expenses', 'Show My Expenses', or 'close'.")
