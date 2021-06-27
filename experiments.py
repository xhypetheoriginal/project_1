# experiments in python (for now)
import webbrowser
import requests
import bs4
import pickle
import os
import platform
import psutil
import tkinter as tk


def bye():
    print("goodbye for now!")


def urls():
    print("please enter the name of the site")
    url = input()
    webbrowser.open_new('www.' + url + '.com')
    print("anything else?")
    j = input()
    if j == "yes":
        start()
    elif j == "no":
        print("goodbye for now!")


def googlescrape():
    print("this program will take the code from a website and deliver it to you!")
    text = input()
    url = 'https://' + text + '.com'
    request_result = requests.get(url)

    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")
    print(soup)
    print("anything else?")
    j = input()
    if j == "yes":
        start()
    elif j == "no":
        print("goodbye for now!")


def lists():
    ml = []
    print("please name your list\n do not use names that you have already used")
    k = input()
    sf = k + '.txt'

    def listf():
        print("if you want to stop the list: type stop.")
        print("anything except 'stop' will be added to the list")
        print("this text will appear after every word you write. i am very sorry for the inconvenience")
        f = input()
        if f == "stop":
            print("if you want to return to the menu: type yes. if you want to close the program: typr no"
                  "if you want to make another list: type list.")
            j = input()
            if j == "yes":
                start()
            elif j == "no":
                os.close()
            elif j == "list":
                list()

        ml.append(f)
        open_file = open(sf, "wb")
        pickle.dump(ml, open_file)
        open_file.close()

        open_file = open(sf, "rb")
        loaded_list = pickle.load(open_file)
        open_file.close()
        print(loaded_list)
        listf()

    listf()


def math():
    print("i can add, subtract, divide, multiply and power - (n^j)\n tell me what do you want me to do")
    a = input()
    if a == "power":
        print("alright! give me the numbers!")
        print("press enter after each number")
        print("keep in mind: (first input)^(second input)")
        g = int(input())
        h = int(input())
        print("alright! there you go!")
        print(g ** h)
    elif a == "multiply":
        print("alright! give me the numbers!")
        print("press enter after each number")
        print("keep in mind: (first input)*(second input)")
        g = int(input())
        h = int(input())
        print("alright! there you go!")
        print(g * h)
    elif a == "divide":
        print("alright! give me the numbers!")
        print("press enter after each number")
        print("keep in mind: (first input)/(second input)")
        g = int(input())
        h = int(input())
        print("alright! there you go!")
        print(g / h)
    elif a == "add":
        print("alright! give me the numbers!")
        print("press enter after each number")
        print("keep in mind: (first input)+(second input)")
        g = int(input())
        h = int(input())
        print("alright! there you go!")
        print(g + h)
    elif a == "subtract":
        print("alright! give me the numbers!")
        print("press enter after each number")
        print("keep in mind: (first input)-(second input)")
        g = int(input())
        h = int(input())
        print("alright! there you go!")
        print(g - h)
    else:
        print("if it was a mistype, type: mt. if it wasn't: type: no")
        a = input()
        if a == "mt":
            math()
        elif a == "no":
            print("okay")
            print("do you want to close the program?")
            p = input()
            if p == "yes":
                os.close()
            elif p == "no":
                start()


def mt():
    print("this program will print the multiplication table")
    print("please choose a number")
    x = int(input())
    i: int = 0
    j: int = 0
    s: str = "|"
    res: int = 0
    while i < x:
        i = i + 1
        j = 0
        s: str = "|"
        while j < x:
            j = j + 1
            res = str(i * j)
            s = s + res + "|"
        print(s)

    print("do you want to go back to the menu? (type: menu). or close the program? (type: close)")
    j = input()
    if j == "menu":
        start()
    elif j == "close":
        os.close()


def sysdata():
    ml = []
    sf = 'sysdata.txt'
    my_system = platform.uname()

    ml.append(f"System: {my_system.system}")
    ml.append(f"Node Name: {my_system.node}")
    ml.append(f"Release: {my_system.release}")
    ml.append(f"Version: {my_system.version}")
    ml.append(f"Machine: {my_system.machine}")
    ml.append(f"Processor: {my_system.processor}")
    ml.append(f"Memory :{psutil.virtual_memory()}")
    open_file = open(sf, "wb")
    pickle.dump(ml, open_file)
    open_file.close()

    open_file = open(sf, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    print("i have stored the data in your computer. the file name is: 'sysdata.txt'. it will appear after the program"
          "was closed")
    print("anything else?")
    u = input()
    if u == "yes":
        start()
    if u == "no":
        print("goodbye for now!")


def rc():
    print("this program will create a simple app with 1 button. once you will click it it will print what you will "
          "write now." + " this code is just for fun. but maybe you can find a use to it!"
          "\nusing this will stop the program. it is not really a problem. just annoying. so ill give you a chance to"
          "go back now. type 'go back' or 'continue'")
    u = input()
    if u == "go back":
        start()
    if u == "continue":
        f = input()

        root = tk.Tk()

        canvas1 = tk.Canvas(root, width=300, height=300)
        canvas1.pack()

        def hello():
            label1 = tk.Label(root, text=f, fg='red', font=('helvetica', 12, 'bold'))
            canvas1.create_window(150, 200, window=label1)

            button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')
            canvas1.create_window(150, 150, window=button1)

            root.mainloop()
        print("anything else?")
        u = input()
        if u == "yes":
            start()
        if u == "no":
            print("goodbye for now!")


def powpr():
    day = 24
    month = 30
    year = 365
    print("what is the price per kilowatt in your country?")
    price_per_kw = float(input())
    print("how many watts do you consume per hour?")
    wph = float(input())
    killowatt = 1000
    print("how many hours per day?")
    h = float(input())
    if h > day:
        print("there are only 24 hours in a day.")
        powpr()
    elif h <= day:
        price = ((wph * h) / killowatt) * price_per_kw
        print("you pay ")
        print(price)
        print("dollars per day")
        price_month = ((wph * (h * month)) / killowatt) * price_per_kw
        price_year = ((wph * (h * year)) / killowatt) * price_per_kw
        print("that is ")
        print(price_month)
        print("dollars per month")
        print("and ")
        print(price_year)
        print("dollars per year")
        print("anything else?")
        u = input()
        if u == "yes":
            start()
        if u == "no":
            print("goodbye for now!")


def start():
    print("what do you want to do?\nhere are the options:\nsearch google (type: urls\ngoogle-scrape (type: gs)\n"
          "storing data in files (type: lists)\nsimple math problems (type: smp).\nprint the multiplication table "
          "(type:mt).\nprint your systems data (type: sysdata).\nwrite things on an app (just for fun) (type: jff)\n"
          "calculate how much you are paying for electricity (type:ppw)")
    f = input()
    if f == "urls":
        urls()
    elif f == "gs":
        googlescrape()
    elif f == "lists":
        lists()
    elif f == "smp":
        math()
    elif f == "mt":
        mt()
    elif f == "sysdata":
        sysdata()
    elif f == "jff":
        rc()
    elif f == "ppw":
        powpr()


start()
