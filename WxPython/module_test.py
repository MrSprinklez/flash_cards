######################
#Programmer: Ari Perz
#Flash Card Test using Functions
###########################

from get_text import *




text_file = raw_input("Enter File Name With Extention: ")
new_stack = raw_input("What Would you Like to Call Your Stack: ")   
    
get_data(text_file,new_stack)
new_deck = get_cards(new_stack)

for x in range(len(new_deck)):
    (q,a) = data_to_display(new_deck,x)
    print("Define: ",q)
    #input("")
    print("Answer: ",a)
    print("")
    #input("") 
    
    




