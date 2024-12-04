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
main_width = 680
main_height = int(main_width/aspect_ratio)
root.geometry("{}x{}".format(main_width, main_height))
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
left_frame.pack(expand=True,fill='x', side='left', padx=10, pady=10)
middle_frame.pack(expand=True,fill='x', side='left', padx=10, pady=10)
right_frame.pack(expand=True,fill='x', side='left', padx=10, pady=10)

## Button setup for Left Frame (advantage selection buttons)
adv_button_width = 12
adv_button_height = 8
buttonAdv = Button(left_frame, text="Advantage", command=lambda: advfun("Advantage"),
                   width=adv_button_width, height=adv_button_height, borderwidth=10)
buttonDisAdv = Button(left_frame, text="Disadvantage", command=lambda: advfun("Disadvantage"),
                      width=adv_button_width, height=adv_button_height, borderwidth=10)
buttonNat = Button(left_frame, text="Natural", command=lambda: advfun("Natural"),
                   width=adv_button_width, height=adv_button_height, highlightbackground="purple2",
                   borderwidth=10)
buttonAdv.pack()
buttonDisAdv.pack()
buttonNat.pack()


## Button setup for Middle Frame (dice roll selections)
roll_button_width = 8
roll_button_height = 5
button4 = Button(middle_frame, text="d4", command=lambda: buttonpushed(4),
                 width=roll_button_width, height=roll_button_height)
button6 = Button(middle_frame, text="d6", command=lambda: buttonpushed(6),
                 width=roll_button_width, height=roll_button_height)
button8 = Button(middle_frame, text="d8", command=lambda: buttonpushed(8),
                 width=roll_button_width, height=roll_button_height)
button12 = Button(middle_frame, text="d12", command=lambda: buttonpushed(12),
                 width=roll_button_width, height=roll_button_height)
button20 = Button(middle_frame, text="d20", command=lambda: buttonpushed(20),
                 width=roll_button_width, height=roll_button_height)
button4.pack()
button6.pack()
button8.pack()
button12.pack()
button20.pack()


## Right Frame setup (grid pack 3x2 text labels and roll result displays)
result1_label = Label(right_frame, text="Adv/Dis Roll 1")
result2_label = Label(right_frame, text="Adv/Dis Roll 2")
result_label = Label(right_frame, text="Final Result")
result1_label.grid(row=0, column=0)
result2_label.grid(row=1, column=0)
result_label.grid(row=2, column=0)

outputlabel1 = Label(right_frame, textvariable=currentResult1, width=8, height=3, bg='light sea green')
outputlabel2 = Label(right_frame, textvariable=currentResult2, width=8, height=3, bg='cadet blue')
outputlabel = Label(right_frame, textvariable=currentResult, width=8, height=3, bg='light slate blue')
outputlabel1.grid(row=0, column=1, sticky='E')
outputlabel2.grid(row=1, column=1, sticky='E')
outputlabel.grid(row=2, column=1, sticky='E')

## Run main event window loop
root.mainloop()
