import random
import webbrowser as web
import os
import datetime
import time
hello = input("What's Your Name?")
print(f"Hello {hello}. I'm your personal assistant.")


def bye():
    goodbye = ["Have a Good Day", "Good Bye", "See You Soon"]
    print(random.choice(goodbye))

while True:
    user = input("How can I help you? ")
    userlow = user.lower()
    if ("quit" in userlow):
        bye()

    elif ('website' in userlow):
        #open website
        web.get()
        choice = input("Enter name of website that you want to open")
        a = "https:\\www."
        c = ".com"
        d = a + choice + c
        web.open(d)
        print("Opening", choice)

    elif ('google' in userlow):
        #open google
        web.get()
        web.open('google.com')
        print('Opening Google')

    elif ('time' in userlow):
        #show time
        print(datetime.datetime.now().strftime("%H:%M"))

    elif ('app' in userlow):
        # open application
        try:
            codePathhalf = "C:\\Users\\Admin\\Documents\\11th commerce 2023-24\\Divyanshu Ahuja 11Com\\apps\\"
            appname = input('App Name ')
            applow = appname.lower()
            appcap = appname.capitalize()
            codePath = codePathhalf + applow
            if ('chrome' in applow):
                codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            print("Opening", appcap)
            messagebox.showinfo('', f'Opening {appcap}')
            time.sleep(0.1)
            os.startfile(codePath)
        except Exception as e:
            #if error comes in opening app
            print('Sorry. Currently Your pc dont have this application.')

    else:
        #command entered by user is not defined
        print("Sorry. I'm still under development. Currently I'm unable to complete the task provided")