import random
from tkinter import *
from tkinter.messagebox import askquestion


root = Tk()
root.config(bg='white')
root.title('HangMan')

output_label = Label(font=('Verdana', 16),bg='white',foreground='red')
label = Label(text='Please Enter a Letter.',font=('Verdana', 16),bg='white',foreground='blue')
secret_word_label = Label(font=('Verdana', 16),bg='white',foreground='green')
output_label.grid(row=2, column=0, columnspan=3)
secret_word_label.grid(row=3, column=0)
label.grid(row=4, column=0) 

scale = Scale(from_= 0, to_= 6, length=300, orient='vertical' ,bg='white' )        
scale.grid(row=5, column=1)

HANGMANPICS = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png']

img = []
for i in range(len(HANGMANPICS)):
   img.append(PhotoImage(file = HANGMANPICS[i]))
photoLabel = Label()
photoLabel.grid(row=5, column=0 )

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
button_frame = Frame()
button_frame.grid(row=1, column=0)

buttons = [0]*26
for i in range(26):
      buttons[i] = Button(button_frame, font=('Verdana', 16),bg='yellow', fg='blue', text=alphabet[i],
            command = lambda x=i: callback(x))
      buttons[i].grid(row=1, column=i)

words = 'ali hesam bat code microsoft baby camel cat manchester babel sherek dog friday ralf panda asus city python pogba ram february '.split()
    

def getRandomWord(wordList):
      wordIndex = random.randint(0, len(wordList) - 1)
      return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
      photoLabel.config(image = img[len(missedLetters)])
      scale.set(len(missedLetters))
      
      str = 'Missed letters:';    
      for letter in missedLetters:
          str += letter + ' '
          
      output_label.configure(text =  str)

      blanks = '_' * len(secretWord)

      for i in range(len(secretWord)): 
          if secretWord[i] in correctLetters:
             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

      str = 'Secret word : ';
      for letter in blanks: 
          str += letter + ' '
      secret_word_label.configure(text =  str)

def playAgain():
      answer = askquestion(title='Quit?', message='Do you want to play again? (Yes or No)')
      return answer

def callback(x):
      label.configure(text='Button {} clicked'.format(alphabet[x]))
      keyPressed(alphabet[x].lower())     

def keyPressed(guess):      
     global correctLetters, missedLetters, secretWord, gameOver
     
     
     if guess in (missedLetters + correctLetters):
            label.configure(text = 'You have already guessed that letter. Choose again.') 
            return
     
     if guess in secretWord:
         correctLetters += guess

         foundAllLetters = True

         for i in range(len(secretWord)):
             if secretWord[i] not in correctLetters:
                 foundAllLetters = False
                 break

         if foundAllLetters:
             label.configure(text =  'Yes! The secret word is "' + secretWord + '"! You have won!') 
             gameOver = True

     else:
         missedLetters += guess

         if len(missedLetters) == len(HANGMANPICS) - 1:
  
             label.configure(text = 'You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' Missed guesses and ' + str(len(correctLetters)) + ' Correct guesses, the word was "' + secretWord + '"')
             gameOver = True

     displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
      

     if gameOver:
         if playAgain() == 'yes':
             missedLetters = ''
             correctLetters = ''
             gameOver = False
             secretWord = getRandomWord(words)
             output_label.configure(text =  'Missed Letters :')
             secret_word_label.configure(text =  'Secret word : ')
             label.configure(text = 'Enter a Letter')
             
         else:             
             root.destroy()
             
     displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameOver = False
displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
      
mainloop()
