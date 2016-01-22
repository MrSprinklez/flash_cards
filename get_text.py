#http://stackoverflow.com/questions/7559397/python-read-file-from-and-to-specific-lines-of-text


import pickle
from document_import import * 
import re
import os 

#SHOULD WORK WITH DOC AND TXT

class FlashCard(): #Defines what attributes flash cards have
    def __init__(self,question,answer,colour,image):
        self.question = question #Question on Card
        self.answer = answer #Answer on Card
        #self.colour = colour
        self.image = image #Image on card 

def get_file_type(fl): #Determines file type 
    """(str)->(str,int) 
    Returns file type and number of lines in while when given file (with dir if required) as input 
    """
    if fl.endswith(".txt"): #If .txt
        #if isinstance(fl, unicode): #check if string is unicode
            #fl = fl.encode('utf-8') #Changes to utf 
        filename = open(fl) #open file
        text = filename.readlines()     # creates a list using the text from the file
        for i in range(len(text)):      # for every new line in the list
            text[i] = text[i].rstrip('\r\n')    # remove the newline indicator
        text = filter(None, text)   # filter the empty strings out of the list
        return(text, len(text))     # return the final list and it's length
        
    elif fl.endswith(".docx"): #if file is Docx
        if isinstance(fl, unicode): #check if string is unicode
            fl = fl.encode('utf-8') #Changes to utf 
        return(get_docx_text(fl),len(get_docx_text(fl))) #returns list and len

def get_data(fl,stack_name): #Organize data into Question and answer and turn into .obj
    """(str,str)->(str)
    Organizes data in given file into questions and answers and saves info as a flash card object
    A list of all flash card objects is dumped into a .obj file
    function returns path of file created 
    """
    count = 0 #Make count 0 
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
            if "-" in line:#if there is a - 
                a.append(line[0:].rstrip("\n"))#Append 1 answer to answer list
                if count==num_lines: #if line number has been reached
                    flash_cards.append(FlashCard(q,a,"grey","none")) #APPEND to list of classes with class of that flash card
                  
                    q = "" #Clear list
                    a = [] #Clear list 
        
                    is_list = False #bool 

            
            else: #If flash card is not a list, only one answer
           
                flash_cards.append(FlashCard(q,a,"grey","none")) #append question and answer
                q = "" #clear question var
                a = [] #Clear answer var 
                is_list = False #reset is_list bool 
                
        if ":" in line: #if colon in line (is definition)
            q = line[0:line.index(":")] #Line equals question 
            if line.rstrip("\n")[len(line.rstrip("\n"))-1]==line[line.index(":")]: #stip /n from file 
            
                a = [] #Refresh a list 
                is_list=True #is list 
         
            else: 
             
                a = line[line.index(":")+1:len(line)].rstrip("\n") #strip \n 
          
                flash_cards.append(FlashCard(q,a,"grey","none")) #Append Question and answer to flash card 
    full_path = os.path.realpath(fl)
    (path,filename) = os.path.split(full_path)
    stack_name = os.path.splitext(stack_name)[0]
    print stack_name
    with open(path+"/"+stack_name+".obj", "wb") as fp: #Open .obj or create new one if doesn't exist 
        pickle.dump(flash_cards, fp) #dump contents into .obj
    
    #return (os.getcwd()+"/"+stack_name+".obj")
    #path, filename = 
    #full_path = os.path.realpath(fl)
    #return os.path.split(full_path)
    return (path+"/"+stack_name+".obj") #(os.path.realpath(fl)+stack_name+".obj")

def get_cards(fl): #Function returns flash card lists from object
    """(str)->(lst) 
    opens .obj file, returns list of objects
    
    """
    if '.obj' not in fl:
        with open(os.path.splitext(fl)[0]+'.obj', 'rb') as fp:   
            deck = pickle.load(fp)
            return(deck)
    else:
        with open(fl, 'rb') as fp:   
            deck = pickle.load(fp)
            return(deck)
        
def dump_to_obj(path, stack_name, ls):
    with open(path+"/"+os.path.splitext(stack_name)[0]+" wrong.obj", "wb") as fp:     #Open .obj or create new one if doesn't exist 
        pickle.dump(ls, fp)                                     #dump contents of wrong list into new .obj

def data_to_display(deck,num): #Takes data from lists 
    """(lst,int)->(str,str)
    input deck (list of objects) and the question number
    program outputs the question and answer 
    """
    return(deck[num].question,deck[num].answer) 
