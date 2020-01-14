import random
from tkinter import *
from tkinter import ttk
from string import ascii_uppercase
from tkinter import messagebox

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<9:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman","you guessed it")
                    newGame()
        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses==9:
                messagebox.showwarning("Hangman","game over")
                newGame()
def remove_all_widgets():
    global main_window
    for widget in main_window.winfo_children():
        widget.destroy()

def  game_window():
    global imgLabel
    global photos
    global lblWord
    global word_list
    name=itomadd1.get()
    ch=comboExample.get()
    remove_all_widgets()
    
    main_window.title("Hangman game")
    main_window.geometry("850x600")
    l1=Label(main_window,text="hello {} welcome to hangman".format(name))
    l1.place(x=500, y=20)
    l2=Label(main_window,text="guessed the {} name".format(ch))
    l2.place(x=500, y=40)
    citys_list=["AHMADNAGAR","AMRAVATI","AURANGABAD","DAULATABAD","DHULE","JALGAON","KALYAN","KARLI","KOLHAPUR","MAHABALESHWAR","MALEGAON","MATHERAN","MUMBAI","NAGPUR","NANDED","NASHIK","PUNE","RATNAGIRI","SANGLI","SATARA","SEVAGRAM","SOLAPUR","THANE","VASAI","VIRAR"]
    games_list=["ARCHERY","BADMINTON","CRICKET","BOXING","TENNIS","SURFING","HOCKY","GYMNASTIC","KARATE","VOLLEYBALL","WEIGHTLIFTING","BASKETBALL","BASEBALL","RUGBY","WRESTLING","HIGHJUMPING","CYCLING","RUNNING","TABLETENNIS","FISHING","JUDO","CLIMBING","BILLIARDS","SHOOTING","HORSERIDING","GOLF","SOCCER"] 
    countrys_list=["FRANCE","UNITEDSTATES","CHINA","JAPAN","INDIA","JERMANY","ITALY","TURKEY","MEXICO","THAILAND","UNITEDKINGDOM","AFGANISTAN","POLAND","ICELAND","FINLAND","AUSTRALIA","WESTINDES"]
    if ch=="citys":
        word_list=citys_list
    elif ch=="countrys":
        word_list=countrys_list
    else:
        word_list=games_list
    photos=[PhotoImage(file="img\\img1.png"),PhotoImage(file="img\\img2.png"),
            PhotoImage(file="img\\img3.png"),PhotoImage(file="img\\img4.png"),PhotoImage(file="img\\img5.png"),
            PhotoImage(file="img\\img6.png"),PhotoImage(file="img\\img7.png"),PhotoImage(file="img\\img8.png"),
            PhotoImage(file="img\\img9.png"),PhotoImage(file="img\\img10.png")]
                    
    imgLabel=Label(main_window)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    imgLabel.config(image=photos[0])

    lblWord=StringVar()
    Label(main_window, textvariable=lblWord, font=("consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=20)

    n=0
    for c in ascii_uppercase:
        Button(main_window, text=c, command=lambda c=c:guess(c), font=("Helvetica 18"), width=6).grid(row=1+n//9,column=n%9)
        n+=1
    Button(main_window,text="New\nGame",command=lambda:newGame(),font=("Helvetica 10 bold")).grid(row=3,column=8,sticky="NSWE")
    newGame()


main_window=Tk()
main_window.title("Hangman")
main_window.geometry("850x600")
global itomadd1
itomadd1=StringVar()
l1=Label(main_window,text="Name")
l1.grid(row=0, column=0)
itomadd1 = Entry(main_window)
itomadd1.grid(row=0,column=1,columnspan=3, padx=10, pady=40)
itomadd1.focus()
labelTop = Label(main_window,text = "Choose guessed field")
labelTop.grid(column=0, row=1)
comboExample = ttk.Combobox(main_window, values=["games", "citys", "countrys"])
comboExample.grid(column=1, row=1,columnspan=3, padx=10, pady=40)
comboExample.current(1)
b1=Button(main_window, text="START", command=game_window)
b1.grid(row=2,column=1)
main_window.mainloop()
            
    
