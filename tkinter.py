from Tkinter import *
import tkFont

#main
root = Tk()
root.title("Tkinter project")
root.configure(background="#2b2b2b")
customFont = tkFont.Font(family="Monospaced", size=11)
btnFont = tkFont.Font(family="Monospaced", size=9)

#global counter
lineString = []
count = 0

def click():
    global count
    global lineString

    #delete contents of line box
    outputLine.delete('1.0', END)

    #put text into output box
    entered_text = textentry.get("1.0", END).splitlines()

    if count == 0:
        for line in entered_text:
            line = line + "\n"
            lineString.append(line)

    if count < len(lineString):
        outputMain.insert(END, lineString[count])
        count += 1
        outputLine.insert(END, str(count))

    else:
        outputLine.insert(END, str(count))


#size of the window
root.geometry("800x600")

#create label
Label(root, text="Source Code Input:", bg="#2b2b2b", fg="#299999", font=customFont) .place(x=50, y=30, width=200, height=20)
Label(root, text="Lexical Analyzed Result:", bg="#2b2b2b", fg="#299999", font=customFont) .place(x=450, y=30, width=200, height=20)
Label(root, text="Current Processing Line:", bg="#2b2b2b", fg="#299999", font=customFont) .place(x=82, y=270)

#text box

textentry = Text(root, bg="#3C3F41", highlightbackground="#ABC023", highlightthickness=1, fg="#BBBBBB", relief=SUNKEN)
textentry.place(x=86, y=55, width=250, height=200)

vscroll = Scrollbar(root, orient=VERTICAL, command=textentry.yview)
textentry['yscroll'] = vscroll.set
vscroll.place(in_=textentry, relx=1.0, relheight=1.0, bordermode="outside")

#insert line numbers

#output box
outputMain = Text(root, width=100, height=200, wrap=WORD, background="#3C3F41", highlightbackground="#ABC023", fg="#BBBBBB", highlightthickness=1)
outputLine = Text(root, width=20, height=10, wrap=WORD, background="#3C3F41", highlightbackground="#ABC023", fg="#FF99FF", highlightthickness=1)

outputMain.place(x=472, y=55, width=250, height=200)
outputLine.place(x=286, y=270, width=50, height=20)

vscroll2 = Scrollbar(root, orient=VERTICAL, command=outputMain.yview)
outputMain['yscroll'] = vscroll2.set
vscroll2.place(in_=outputMain, relx=1.0, relheight=1.0, bordermode="outside")

#Buttons
Button(root, text="Next Line", width=9, command=click, bg="#dd7d4d", font=btnFont) .place(x=264, y=320)
Button(root, text="Quit", width=9, command=root.destroy, bg="#dd7d4d", font=btnFont) .place(x=648, y=320)




root.mainloop()
