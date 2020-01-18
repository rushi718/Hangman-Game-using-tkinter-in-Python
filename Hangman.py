
#Importing Required Libraries

from tkinter import *
import random
from tkinter import messagebox

#Initializing Empty List 
mywords=[]
file1 = open(r"commonword.txt","r")

#Appending words from file to the list
for x in file1:
    mywords.append(x.replace('\n', ''))

word=random.choice(mywords)
random_word=list(word)
p=[]
s='_ '*len(random_word)
p=s.split(' ')
p.pop(len(random_word))
actual=random_word.copy()

class Hangman:
    def __init__(self,master):
        self.count=0
        self.structure(master)
        self.rr=master
        
    def structure(self,master):
 
        """ Instruction Label """
 
        # Create instruction label for Program
        self.inst_lbl = Label(master, text = "Welcome to Hangman Game!")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        """ Guess Input """ 
 
        # Create label for entering Guess  
        self.guess_lbl = Label(master, text = "Enter your Guess:")
        self.guess_lbl.grid(row = 1, column = 0, sticky = W)
 
        # Create entry widget to accept Guess  
        self.guess_ent = Entry(master)
        self.guess_ent.grid(row = 1, column = 1, sticky = W)

        
        # Create a space  
        self.gap2_lbl = Label(master, text = " ")
        self.gap2_lbl.grid(row = 2, column = 0, sticky = W)

        # Creating a submit button
        self.submit_bttn = Button(master, text = "Submit",command=self.submit,height=1, width=20)
        self.submit_bttn.grid(row = 3, column =1, sticky = W)
 
        master.bind('<Return>',self.submit)   
        
        # Create a space  
        self.gap2_lbl = Label(master, text = " ")
        self.gap2_lbl.grid(row = 4, column = 0, sticky = W)
 
        """ RESET """
         
        # Creating a reset button
        self.reset_bttn = Button(master, text = "Reset",command=self.reset,height=2, width=20)
        self.reset_bttn.grid(row = 9, column = 2, sticky = W)
 
        # Create a space  
        self.gap2_lbl = Label(master, text = " ")
        self.gap2_lbl.grid(row = 5, column = 0, sticky = W)
        
        self.inst_lb2 = Label(master, text ='Life:10')
        self.inst_lb2.grid(row = 1, column = 2, columnspan = 2, sticky = W)

        #Creating Label to Display Message
        self.inst_lb3 = Label(master, text ='')
        self.inst_lb3.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        #CReating label to display current Guessed Status of Word
        self.curr_char1 = Label(master, text =p)
        self.curr_char1.place(x=100,y=130)
        self.curr_char = Label(master, text ="Current Status:")
        self.curr_char.place(x=0,y=130)

        # Create a Hangman's Background
        
        self.c=Canvas(master,height=300,width=200)
        self.c.grid(row=9,column=0,sticky =W)
        self.l=self.c.create_line(70,20,70,250,width=2)
        self.l1=self.c.create_line(70,20,150,20,width=2)
        self.l2=self.c.create_line(150,20,150,50,width=2)
    
        
    def current_status(self,char):
        self.curr_char1 = Label(self.rr, text =char)
        self.curr_char1.place(x=100,y=130)

    def reset(self):
        self.guess_ent.delete(0, 'end')

    def submit(self,*args):

        #Taking Entry From Entry Field
        char=self.guess_ent.get()

        #Checking whether Entry Field is empty or not
        if(len(char)==0):
            messagebox.showwarning("Warning","Entry field is Empty")
        if(len(char)>1):
            messagebox.showwarning("Warning","Enter character of length 1")   

        if char in actual and len(char)==1:
            l=actual.count(char)
            for j in range(l):
                i=actual.index(char)
                
                p.insert(i,char)
                p.pop(i+1)
                actual.insert(i,'_')
                actual.pop(i+1)
            self.inst_lb2.config(text='Life:'+ str(10-self.count))
            self.inst_lb3.config(text='Right Guessed!')
            self.guess_ent.delete(0, 'end')
            self.current_status(p)

        elif(len(char)==1):
            self.count=self.count+1
            self.inst_lb2.config(text='Life:'+str(10-self.count))
            self.inst_lb3.config(text='Wrong Guessed!')
            self.guess_ent.delete(0, 'end')
            
        #Creating Hangman's parts orderwise if wrong character is Guessed
        if(self.count==1):
            self.cir=self.c.create_oval(125,100,175,50,width=2)
        elif(self.count==2):
            self.el=self.c.create_line(135,65,145,65,width=2)
        elif(self.count==3):
            self.er=self.c.create_line(155,65,165,65,width=2)
        elif(self.count==4):
            self.no=self.c.create_line(150,70,150,85,width=2)
        elif(self.count==5):
            self.mo=self.c.create_line(140,90,160,90,width=2)
        elif(self.count==6):
            self.l3=self.c.create_line(150,100,150,200,width=2)
        elif(self.count==7):
            self.hl=self.c.create_line(150,125,100,150,width=2)
        elif(self.count==8):
            self.hr=self.c.create_line(150,125,200,150,width=2)
        elif(self.count==9):
            self.fl=self.c.create_line(150,200,100,225,width=2)
        elif(self.count==10):
            self.fr=self.c.create_line(150,200,200,225,width=2)


        #Condition of Player Won
        if( p==random_word):
            self.inst_lb3.config(text='You perfectly guessed the word!')
            messagebox.showinfo("Hello", "You Won")
            self.rr.destroy()

        #Condition Of player Loose
        elif(self.count>=10):
            self.inst_lb3.config(text='You lost.... the word is '+word)
            messagebox.showinfo("Hello", "You lost please try again!")
            self.rr.destroy()



     
            

        

root = Tk()
root.title("Hangman Game")
root.geometry("580x480")
app = Hangman(root)
print(word)
root.mainloop()
