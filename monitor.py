import requests
import time

url = 'https://api.github.com'

print("Monitoring started... Press CTRL+C to stop.")

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[{time.ctime()}] Website is UP! (200)")
        else:
            print(f"[{time.ctime()}] ALERT: Status Code {response.status_code}")
    except:
        print(f"[{time.ctime()}] ALERT: Network is DOWN!")
    
    time.sleep(10) # हर 10 सेकंड में चेक करेगा
