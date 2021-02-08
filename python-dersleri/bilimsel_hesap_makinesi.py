from tkinter import *
import math

answerVariableGlobal = ""
answerLabelForSquareRoot = ""
root = Tk()
root.title("Hesap Makinesi")
answerEntryLabel = StringVar()
Label(root, font=('Arial',25, 'bold'), textvariable=answerEntryLabel, justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
answerFinalLabel = StringVar()
Label(root, font=('Arial', 25, 'bold'), textvariable=answerFinalLabel, justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)

def changeAnswerLabel(entry):
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerVariableGlobal = answerVariableGlobal + str(entry)
    answerLabelForSquareRoot = answerVariableGlobal
    answerEntryLabel.set(answerVariableGlobal)

def clearAnswerEntryLabel():
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerLabelForSquareRoot = answerVariableGlobal
    answerVariableGlobal = ""
    answerEntryLabel.set(answerVariableGlobal)

def allClear():
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerVariableGlobal = ""
    answerLabelForSquareRoot = ""
    answerEntryLabel.set("")
    answerFinalLabel.set("")

def evaluateSquareRoot():
    global answerVariableGlobal
    global answerLabelForSquareRoot
    try:
        sqrtAnswer = math.sqrt(eval(str(answerLabelForSquareRoot)))
        clearAnswerEntryLabel()
        answerFinalLabel.set(sqrtAnswer)
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
        clearAnswerEntryLabel()
        answerFinalLabel.set("Error!")

def evaluateAnswer():
    global answerVariableGlobal
    try:
        eval(answerVariableGlobal)
        evaluatedValueAnswerLabelGlobal = str(eval(answerVariableGlobal))
        clearAnswerEntryLabel()
        answerFinalLabel.set(evaluatedValueAnswerLabelGlobal)
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
        clearAnswerEntryLabel()
        answerFinalLabel.set("Error!")

def createButton(txt, x, y):
    Button(root, font=('Arial', 15, 'bold'),
           padx=16, pady=16,
           text=str(txt),
           heigh=2, width=9,
           command=lambda: changeAnswerLabel(txt)).grid(row=x, column=y, sticky=E)


buttons = ['AC', '√', '%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '', '', '.', '']
buttonsListTraversalCounter = 0

for i in range(3, 8):
    for j in range(0, 4):
        createButton(buttons[buttonsListTraversalCounter], i, j)
        buttonsListTraversalCounter = buttonsListTraversalCounter + 1

Button(root, font= ('Arial', 15, 'bold'),
       padx=16, pady=16, text="√", height=2, width=9, command=lambda: evaluateSquareRoot()).grid(row=3, column=1, sticky=E)
Button(root, font= ('Arial', 15, 'bold'),
       padx=16, pady=16, text="AC", height=2, width=9, command=lambda: allClear()).grid(row=3, column=0, sticky=E)
Button(root, font= ('Arial', 15, 'bold'),
       padx=16, pady=16, text="0", height=2, width=9, command=lambda: changeAnswerLabel(0)).grid(row=7, column=0, sticky=E)
Button(root, font= ('Arial', 15, 'bold'),
       padx=16, pady=16, text="=", height=2, width=9, command=lambda: evaluateAnswer()).grid(row=7, column=3, sticky=E)

root.mainloop()
