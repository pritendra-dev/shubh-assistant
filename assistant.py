import os
import json
import time

def speak(text):
    os.system(f"termux-tts-speak '{text}' &")

def get_battery():
    raw = os.popen("termux-battery-status").read()
    data = json.loads(raw)
    percent = data['percentage']
    speak(f"Your battery is at {percent} percent")
    print(f"\n[ Battery: {percent}% ]")

def sys_info():
    speak("Fetching system information")
    print("\n[ RAM Usage ]")
    os.system("free -h")
    print("\n[ Storage Analysis ]")
    os.system("du -ah /data/data/com.termux/files/home | sort -rh | head -n 5")

def main_menu():
    speak("Welcome back, Pritendra")
    while True:
        print("\n" + "="*30)
        print("  SHUBH ASSISTANT CONTROL  ")
        print("="*30)
        print("1. Check Battery")
        print("2. System & Storage Info")
        print("3. Say Hello")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            get_battery()
        elif choice == '2':
            sys_info()
        elif choice == '3':
            speak("I am Shubh Assistant, created by the legend Pritendra dev.")
        elif choice == '4':
            speak("Goodbye Pritendra, see you soon!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main_menu()

