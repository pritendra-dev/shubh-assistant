import os
import socket
import datetime

def log_event(event_name, status):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{time_stamp}] {event_name}: {status}\n"
    with open("tech_log.txt", "a") as f:
        f.write(log_message)

def run_assistant():
        # Network Scan Feature
    print("\n[ Scanning Local Network...press ctrl+c  ]")
    # यह आपके नेटवर्क के अन्य डिवाइसेस को खोजेगा
    os.system("nmap -sn 192.168.1.0/24 | grep 'Nmap scan report'")

    print("-" * 35)
    print("    SHUBH TECH ASSISTANT (PRO)   ")
    print("-" * 35)

    # यहाँ ध्यान दें: इन लाइनों के आगे 4 खाली जगह (spaces) होनी चाहिए
    print("[ Storage Analysis: Top 5 Files ]")
    os.system("du -ah ~ 2>/dev/null | sort -rh | head -n 5")
    print("-" * 35)

    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"IP Addr:  {ip}")
        log_event("IP_CHECK", f"Success ({ip})")
    except:
        print("IP Addr:  Error")
        log_event("IP_CHECK", "FAILED")

    res = os.system("ping -c 1 google.com > /dev/null 2>&1")
    print(f"Internet: {'ONLINE' if res == 0 else 'OFFLINE'}")
    log_event("INTERNET", "ONLINE" if res == 0 else "OFFLINE")

    print("\n[ RAM Usage ]")
    os.system("free -h | grep Mem")
    print("-" * 35)

if __name__ == "__main__":
    run_assistant()

