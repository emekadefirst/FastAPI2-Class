import requests

def load_api():
    response = requests.get("https://ol-etest.onrender.com/api/questions/")
    if response.status_code == 200:
        data = response.json()
        for  q in data:
            i = 0
            print(f"{q['text']}")
            answer = str(input(": "))
        





print("Hello welcome to ozark questionair")
reply = str(input("Would you like to take the available quiz?\nYes\nNo ")).lower()
if reply == "yes":
    load_api()
elif reply == "no":
    print("Thank you for stopping by!")
else:
    print("Invalid response")
