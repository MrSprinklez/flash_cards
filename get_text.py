#http://stackoverflow.com/questions/7559397/python-read-file-from-and-to-specific-lines-of-text

#import re
#import csv 
import pickle
from document_import import * 
import re
#import json

#flash_cards = [] 

#SHOULD WORK WITH DOC AND TXT

class FlashCard(): #Defines what attributes flash cards have
    def __init__(self,question,answer,colour,image):
        self.question = question #Question on Card
        self.answer = answer #Answer on Card
        #self.colour = colour
        self.image = image #Image on card 



def get_file_type(fl): #Determines file type 
    if fl.endswith(".txt"): #If .txt
        #num_lines = sum(1 for line in open(fl))#if line.rstrip('\n')
        if isinstance(fl, unicode): #check if string is unicode
            fl = fl.encode('utf-8') #Changes to utf 
        filename = open(fl) #open file
        text = filename.readlines()     # creates a list using the text from the file
        for i in range(len(text)):      # for every new line in the list
            text[i] = text[i].rstrip('\r\n')    # remove the newline indicator
        text = filter(None, text)   # filter the empty strings out of the list
        return(text, len(text))     # return the final list and it's length
        
    elif fl.endswith(".docx"): #if Docx
        #num_lines = sum(1 for line in get_docx_text(fl)) #make new function for it
        #print(get_docx_text(fl))
        return(get_docx_text(fl),len(get_docx_text(fl))) #returns list and len

def get_data(fl,stack_name): #Organize data into Question and answer and turn into .obj
    count = 0 
    flash_cards = []  #List which flash card objects are contained 
    is_list = False #If its a list of answers then this bool becomes true 

    (data_file,num_lines) = get_file_type(fl)#Use Function That gets Number of lines and File Type

    q = "" #Create Variables for Question
    a = [] #Create Variable for Answer

    for line in data_file:   #For every line in the file, look through it
        if "\n" in line: #FInds new line symbol 
            line.replace("\n","") #Gets rid of new line symbol 
            
        count+=1 

        if is_list == True: #If the definition is a list, then use this if statement 
            if "-" in line:
                a.append(line[0:].rstrip("\n"))#Append 1 answer to answer list
                if count==num_lines: #if line number has been reached
                    flash_cards.append(FlashCard(q,a,"grey","none")) #APPEND to list of classes with class of that flash card
                    #writer.writerow({'Question':q, "Answer": a})
                    q = "" #Clear list
                    a = [] #Clear list 
                    #is_list = False
                    is_list = False #bool 
                    #break #Consider deleting **
                #break #consider deleting **
            
            else:
                #writer.writerow({'Question':q, "Answer": a})
                #print("Else:", l)
                flash_cards.append(FlashCard(q,a,"grey","none"))
                q = ""
                a = []
                is_list = False 
                #break
            
        #if l == ":":
        if ":" in line: 
            q = line[0:line.index(":")]
            ##Consider changing this and using in range in for loop instead
            #**print(line)
            #print("end",line[len(line)-1])
            if line.rstrip("\n")[len(line.rstrip("\n"))-1]==line[line.index(":")]: #stip /n from file 
                ###IT NEEDS TO BE A TEXT FILE FOR THIS TO WORK! CHANGE TO GE RID OF SPACES AND CHECK END OF LIST
                #line[len(line)-2]==line[line.index(":")                  
                #print("its a list")
                #q = line[0:line.index(":")]
                a = [] #Refresh a list 
                is_list=True #is list 
                #a = line[line.index(":")+1:]
                #flash_cards.append(FlashCard(q,a,"grey","none"))
                #break
                #count+=1##Consider changing this and using in range in for loop instead
                #break
            else: 
                #print("Not A List") 
                #q = line[0:line.index(":")]
                a = line[line.index(":")+1:len(line)].rstrip("\n") #strip \n 
                #got rid of -1
                #print("A", a)
                #print("a:",a)
                flash_cards.append(FlashCard(q,a,"grey","none")) #Append Question and answer to flash card 
                #writer.writerow({'Question':line[0:line.index(":")], "Answer": line[line.index(":")+1:]})
                #break
    #if fl.endswith(".txt"):
        #data_file.close() 
    with open(stack_name+".obj", "wb") as fp: #Open .obj or create new one if doesn't exist 
        pickle.dump(flash_cards, fp) #dump contents into .obj



def get_cards(fl):
    with open(fl+'.obj', 'rb') as fp:   
        deck = pickle.load(fp)
        return(deck) 
        #for x in range(len(deck)):
         #   print(deck[x].question,deck[x].answer)


def data_to_display(deck,num):
    return(deck[num].question,deck[num].answer)


