import requests

# GitHub API से डेटा मांगना
url = 'https://api.github.com'
response = requests.get(url)

# डेटा को एक फाइल में सेव करना
with open("result.txt", "w") as f:
    f.write(f"Status: {response.status_code}\n")
    f.write(f"Data: {response.text[:100]}") # सिर्फ शुरुआती 100 अक्षर

print("Data saved to result.txt successfully!")

