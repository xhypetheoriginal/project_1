import webbrowser


def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + ' by ofek szmulevitz.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def done():
    print("done!")


def mt():
    print("now i will prove to you that i can print the multiplication table!")
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
            print("okay!")


def pl():
    print("now i will prove you that i can search google!")
    print("give me the name of the site please!")
    j = input()
    webbrowser.open("http://" + j + ".com", new=1)


def theend():
    print("press enter to close the window")
    L = input()


greet('john', '2021')
remind_name()
guess_age()
count()
done()
mt()
math()
pl()
theend()
