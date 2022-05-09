import tkinter as tk
import tkinter.font as font
import random
from tkinter import END

test_words = ["all", "and", "any", "are", "bad", "bet", "big", "box", "boy", "bye", "bye",
              "can", "car", "cat", "cup", "cut", "dad", "day", "did", "dog", "dry", "eat",
              "eve", "fly", "for", "fun", "get", "had", "has", "her", "him", "his", "hot",
              "how", "hum", "let", "lot", "man", "may", "mom", "new", "not", "off", "old",
              "one", "our", "out", "pet", "put", "red", "run", "saw", "say", "see", "she",
              "sit", "the", "too", "top", "try", "two", "use", "was", "way", "who", "why",
              "yes", "yet", "you"
              ]
test = ""


def initial():
    global test_words, test
    test = random.choice(test_words)
    testWord.configure(text=test)


def check():
    global test_words, test
    user_input = entry.get()
    if user_input == test:
        mark.configure(text="Correct!")
        reset()
    else:
        mark.configure(text="Try Again!")
        entry.delete(0, END)


def check2(event):
    global test_words, test
    user_input = entry.get()
    if user_input == test:
        mark.configure(text="Correct!")
        reset()
    else:
        mark.configure(text="Try Again!")
        entry.delete(0, END)



def reset():
    global test_words, test
    test = random.choice(test_words)
    testWord.configure(text=test)
    entry.delete(0, END)


def restart():
    global test_words, test
    test = random.choice(test_words)
    testWord.configure(text=test)
    entry.delete(0, END)
    mark.configure(text="")


# build the root frame
root = tk.Tk()
root.title("Spell It Out!")

# change window icon
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(True, icon)

# specify size and background colour
canvas = tk.Canvas(root, height=600, width=900, bg="#00B0f0")
canvas.pack()

frame = tk.Frame(root, bg="#92D050")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

frame2 = tk.Frame(frame, bg="white")
frame2.place(relwidth=0.33, relheight=0.15, relx=0.35, rely=0.33)

# title
titleFont = font.Font(size=46, family="Ink Free")
title = tk.Label(frame, text="Spell It Out!", bg="#92D050", font=titleFont)
title.place(relx=0.28, rely=0.09)

# testWord
testFont = font.Font(size=46, family="Calibri")
testWord = tk.Label(frame2, fg="red", bg="white", font=testFont)
testWord.pack()

# start and exit buttons
smFont = font.Font(size=12, family="Calibri")
start = tk.Button(frame, text="START", padx=10, pady=5, bd=6, fg="white", bg="#7030A0", font=smFont,
                  command=restart)
start.place(relx=0.04, rely=0.04)

close = tk.Button(frame, text="EXIT", padx=16, pady=5, bd=6, fg="white", bg="#7030A0", font=smFont,
                  command=root.destroy)
close.place(relx=0.87, rely=0.04)

# wrong or right
markFont = font.Font(size=35, family="Calibri")
mark = tk.Label(frame, bg="#92D050", font=markFont, fg="red")
mark.place(relx=0.65, rely=0.62)

# user entry label
label = tk.Label(frame, text="Spell the word here:", bg="#92D050", font=smFont)
label.place(relx=0.418, rely=0.58)

# user entry
entry = tk.Entry(frame, bg="#92D050")
entry.place(relx=0.47, rely=0.65)
entry.config(font=('Calibri', 20))
entry.config(width=4)

# submit button
submitFont = font.Font(size=28, family="Calibri")
submit = tk.Button(frame, text="SUBMIT", fg="white", bg="#7030A0", bd=7, font=submitFont,
                   command=check)
submit.place(relx=0.4, rely=0.78)


initial()

root.bind('<Return>', check2)
root.mainloop()
