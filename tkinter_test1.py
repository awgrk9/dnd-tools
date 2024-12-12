from tkinter import *
import random

# Declare Global Variables to Handle Disadvantage States (could implement much better in the future)
advantage = False
disadvantage = False

# Function "advfun(adv_selection)"
## Input: string choice
##      "Advantage"
##      "Disadvantage"
##      "Natural"
##
## Output: returns nothing, but modifies button colors and global variable states for disadvantage
##

def advfun(adv_selection):
    global advantage
    global disadvantage
    if adv_selection == "Advantage":
        advantage = True
        disadvantage = False
        buttonAdv.config(highlightbackground="green2")
        buttonDisAdv.config(highlightbackground="gray")
        buttonNat.config(highlightbackground="gray")
    elif adv_selection == "Disadvantage":
        advantage = False
        disadvantage = True
        buttonAdv.config(highlightbackground="gray")
        buttonDisAdv.config(highlightbackground="red2")
        buttonNat.config(highlightbackground="gray")
    else:
        advantage = False
        disadvantage = False
        buttonAdv.config(highlightbackground="gray")
        buttonDisAdv.config(highlightbackground="gray")
        buttonNat.config(highlightbackground="purple2")

    return

# Function "buttonpushed(numba)"
## Input: Positive Integer > 1
##
## Output: returns nothing
## Behavior: calculates random integer based on dice roll choice
##          takes disadvantage or advantage, rolls again, makes correct choice
##          sets all tkinter variables (currentResult1 is first roll, 2 is second roll, currentResult is final result)
##          prints text to console as debugging option
##
def buttonpushed(numba):
    global currentResult
    global currentResult1
    global currentResult2
    currentResult1.set(0)
    currentResult2.set(0)
    result = random.randint(1, numba)
    if advantage or disadvantage == True:
        result2 = random.randint(1, numba)
        if advantage:
            print("Advantage is enabled. ({}, {})".format(result, result2))
            currentResult1.set(result)
            currentResult2.set(result2)
            result = max(result, result2)
        if disadvantage:
            print("Disadvantage is enabled. ({}, {})".format(result, result2))
            currentResult1.set(result)
            currentResult2.set(result2)
            result = min(result, result2)
    print("Result is {}".format(result))
    print("The button has been pushed.")
    currentResult.set(result)
    print(currentResult.get())
    return


## Setup Block for main GUI window (root)
root = Tk()
aspect_ratio = 4/3
main_width = 320
#main_height = int(main_width/aspect_ratio)
main_height = 240
xoffset = 640+main_width
root.geometry("{}x{}+{}+0".format(main_width, main_height, xoffset))
#root.attributes('-fullscreen', True)
root.title("DnD Roller")
root.config(bg="skyblue")

## Initialize tkinter variables for roll storage
currentResult1 = IntVar()
currentResult2 = IntVar()
currentResult = IntVar()

## Initialize three columns of frames left to right
left_frame = Frame(root)
middle_frame = Frame(root)
right_frame = Frame(root)
right_frame.columnconfigure(1,weight=1)

## Pack in said columns of three frames left to right
left_frame.pack(expand=True,fill='x', side='left', padx=5, pady=5)
middle_frame.pack(expand=True,fill='x', side='left', padx=5, pady=5)
right_frame.pack(expand=True,fill='x', side='left', padx=5, pady=5)

## Button setup for Left Frame (advantage selection buttons)
adv_button_width = 12
adv_button_height = 8
buttonAdv = Button(left_frame, text="Adv", command=lambda: advfun("Advantage"))
buttonDisAdv = Button(left_frame, text="Dis", command=lambda: advfun("Disadvantage"))
buttonNat = Button(left_frame, text="Nat", command=lambda: advfun("Natural"))
buttonAdv.pack()
buttonDisAdv.pack()
buttonNat.pack()


## Button setup for Middle Frame (dice roll selections)
roll_button_width = 8
roll_button_height = 5
button4 = Button(middle_frame, text="d4", command=lambda: buttonpushed(4))
button6 = Button(middle_frame, text="d6", command=lambda: buttonpushed(6))
button8 = Button(middle_frame, text="d8", command=lambda: buttonpushed(8))
button12 = Button(middle_frame, text="d12", command=lambda: buttonpushed(12))
button20 = Button(middle_frame, text="d20", command=lambda: buttonpushed(20))
button4.pack()
button6.pack()
button8.pack()
button12.pack()
button20.pack()


## Right Frame setup (grid pack 3x2 text labels and roll result displays)
result1_label = Label(right_frame, text="Roll 1")
result2_label = Label(right_frame, text="Roll 2")
result_label = Label(right_frame, text="Final Roll")
result1_label.grid(row=0, column=0)
result2_label.grid(row=1, column=0)
result_label.grid(row=2, column=0)

outputlabel1 = Label(right_frame, textvariable=currentResult1, bg='light sea green')
outputlabel2 = Label(right_frame, textvariable=currentResult2, bg='cadet blue')
outputlabel = Label(right_frame, textvariable=currentResult, bg='light slate blue')
outputlabel1.grid(row=0, column=1, sticky='E')
outputlabel2.grid(row=1, column=1, sticky='E')
outputlabel.grid(row=2, column=1, sticky='E')

## Run main event window loop
root.mainloop()
