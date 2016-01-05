#http://stackoverflow.com/questions/7559397/python-read-file-from-and-to-specific-lines-of-text

#import re
#import csv 
import pickle 
#import json

#flash_cards = [] 

class FlashCard():
    def __init__(self,question,answer,colour,image):
        self.question = question
        self.answer = answer 
        self.colour = colour
        self.image = image 
        

def get_data(fl,stack_name): #fl is file 
    count = 0 
    flash_cards = []    
    is_list = False #If its a list of answers then this bool becomes true 
    #data_file = open(file)
    #sep =  "#" 
    num_lines = sum(1 for line in open(fl))#if line.rstrip('\n')
    with open(fl) as data_file:#Get User Data for Flash Cards
        q = ""
        a = []
        #num_lines =  8#sum(1 for line in data_file)#if line.rstrip('\n')
        
        #with open('data.csv', 'w') as fp:#Open JSON file to dump Flash Card Info
            #fieldnames = ['Question', 'Answer']
            #writer = csv.DictWriter(fp, fieldnames=fieldnames)
            #writer.writeheader() #Write Header 
            
        for line in data_file:   #For every line in the file, look through it 
            count+=1 
            for l in line: #Every character in lin e
                l = l.replace('  ', ' ') #Change large spaces to single spaces 
                #l = l.replace('  ', ' ')  
                if is_list == True: #If the definition is a list, then use this if statement 
                    if l == "-":
                        #print(line[0:])
                        a.append(line[0:].rstrip("\n"))
                        if count==num_lines:
                            flash_cards.append(FlashCard(q,a,"grey","none"))
                            #writer.writerow({'Question':q, "Answer": a})
                            q = ""
                            a = []
                            is_list = False 
                            break
                        break
                    
                    else:
                        #writer.writerow({'Question':q, "Answer": a})
                
                        flash_cards.append(FlashCard(q,a,"grey","none"))
                        q = ""
                        a = []
                        is_list = False 
                        break
                    

                if l == ":":
                    q = line[0:line.index(":")]
                    ##Consider changing this and using in range in for loop instead
                    if line[len(line)-2]==line[line.index(":")]:
                        #print("its a list")
                        #q = line[0:line.index(":")]
                        a = [] 
                        is_list=True 
                        #a = line[line.index(":")+1:]
                        #flash_cards.append(FlashCard(q,a,"grey","none"))
                        #break
                        #count+=1##Consider changing this and using in range in for loop instead
                        break
                    else: 
                        #print("Not A List") 
                        #q = line[0:line.index(":")]
                        a = line[line.index(":")+1:len(line)].rstrip("\n") #got rid of -1
                        #print("a:",a)
                        flash_cards.append(FlashCard(q,a,"grey","none"))
                        #writer.writerow({'Question':line[0:line.index(":")], "Answer": line[line.index(":")+1:]})
                        break
    with open(stack_name+".obj", "wb") as fp:
        pickle.dump(flash_cards, fp)



#def pull_data(file,stack_name):
#    flash_cards = []     
#    lstbool = False 
#    spamReader = csv.reader(open(file), delimiter=' ', quotechar='|')
#    for row in spamReader:
#    
#        for x in range(len(row)):
#            try:
#                #print(row)
#                if row[x].count(":") == 1:
#                    #print(row)
#                    q = (", ".join(row[0:x+1])).replace(",", "")
#                    
#                    a = (", ".join(row[x+1:len(row)-1])).replace(",", "")
#                    
#                    if a != []:
#                        flash_cards.append(FlashCard(q,a,"grey","none"))
#                    
#                    #y=y.replace(",", "")
#                    print(q)
#                    print(a)
#                
#                if row[x].count("-")==1: # and lstbool == False:
#                    #print("Row X",row[x])
#                    #print("List Stuff: ",row[0:len(row)-1])
#                    if len(row) > 1:
#                        a = (", ".join(row[0:len(row)-1])).replace(",", "")
#                        print(a)
#                    else:
#                        a = row[x]
#                        print(a)
#                    lstbool = True 
#                #elif row[x].count("-")==1 and lstbool == True:
#                        
#                        
#                else:
#                    #print(row) 
#                    pass      
#            except:
#                pass 
#            
#    with open(stack_name+".obj", "wb") as fp:
#        pickle.dump(flash_cards, fp)
#         

    #http://stackoverflow.com/questions/2409330/how-to-get-data-from-csv-file-in-python

def get_cards(fl):
    with open(fl+'.obj', 'rb') as fp:   
        deck = pickle.load(fp)
        return(deck) 
        #for x in range(len(deck)):
         #   print(deck[x].question,deck[x].answer)


def data_to_display(deck,num):
    return(deck[num].question,deck[num].answer)


