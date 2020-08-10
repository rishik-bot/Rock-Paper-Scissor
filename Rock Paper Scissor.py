#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Play Rock Paper Scissor vs Computer

import random as rand,sys
print("-----------------------------------Rock Paper Scissor------------------------------------")
counter=0
Tie=0
Win=0
Loose=0
while True:
    counter+=1

    #Generating computer input
    computer_choice=rand.choice(['r','p','s']) #chooses one of the 3 choices

    #Getting user input
    x=True
    while x:
        print("\nRound {}".format(counter))
        user_choice=input("\nPlease enter your choice from either of the four: (r)ock, (p)aper, (s)cissor, (q)uit: ").lower()
        if user_choice in 'rps':
            x=False
        elif user_choice=='q':
            sys.exit()
    
    #Comparing both inputs
    if user_choice==computer_choice:
        print("Match is tied")
        Tie+=1
        print("Status at the end of round %s : WON=%s || LOST=%s || TIED=%s"%(counter,Win,Loose,Tie))
    elif ((user_choice=='p'and computer_choice=='r') or
          (user_choice=='s'and computer_choice=='p') or
          (user_choice=='r'and computer_choice=='s')):
        print("Congrats! You win. Computer chose '%s'"%(computer_choice))
        Win+=1
        print("Status at the end of round %s : WON=%s || LOST=%s || TIED=%s"%(counter,Win,Loose,Tie))
    elif ((user_choice=='p'and computer_choice=='s') or
          (user_choice=='s'and computer_choice=='r') or
          (user_choice=='r'and computer_choice=='p')):
        print("Sorry! You loose. Computer chose '%s'"%(computer_choice))
        Loose+=1
        print("Status at the end of round %s : WON=%s || LOST=%s || TIED=%s"%(counter,Win,Loose,Tie))

