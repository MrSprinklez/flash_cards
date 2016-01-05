try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
import pickle

"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""

class FlashCard():
    def __init__(self,question,answer,colour,image):
        self.question = question
        self.answer = answer
        self.image = image 
        



def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    PARA = WORD_NAMESPACE + 'p'
    TEXT = WORD_NAMESPACE + 't'
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    #return('\n\n'.join(paragraphs))
    return(paragraphs)

#print(get_docx_text("geography_study_ note.docx"))
##    count = 0 
##    flash_cards = []    
##    is_list = False #If its a list of answers then this bool becomes true 
##    num_lines = sum(1 for line in paragraphs)
##    q = ""
##    a = []
##    #return '\n\n'.join(paragraphs)
##    for line in paragraphs:
##        for l in range(len(line)): #Goes through every part of the line
##            #l = l.replace('  ', ' ') #Change large spaces to single spaces 
##            
##            if is_list == True: #If the definition is a list, then use this if statement 
##                if l == "-":
##                    a.append(line[0:].rstrip("\n"))
##                    if count==num_lines:
##                        flash_cards.append(FlashCard(q,a,"grey","none"))
##                        q = ""
##                        a = []
##                        is_list = False 
##                        break
##                    break
##                
##                else:
##                    #writer.writerow({'Question':q, "Answer": a})
##            
##                    flash_cards.append(FlashCard(q,a,"grey","none"))
##                    q = ""
##                    a = []
##                    is_list = False 
##                    break
##                
##
##            if l == ":":
##                q = line[0:line.index(":")]
##                ##Consider changing this and using in range in for loop instead
##                if line[len(line)-2]==line[line.index(":")]:
##                    a = [] 
##                    is_list=True 
##                    break
##                else: 
##                    a = line[line.index(":")+1:len(line)].rstrip("\n") #got rid of -1
##                    #print("a:",a)
##                    flash_cards.append(FlashCard(q,a,"grey","none"))
##                    break
##            with open(stack_name+".obj", "wb") as fp:
##                pickle.dump(flash_cards, fp)
##         
##        
##        
##    #return(paragraphs)
##

def get_docx_image(path):
    """
    Take the path of a docx file as argument, return the image in pygame.
    """
    import zipfile
    import os
    #import pygame
    #images = []
    zip_file = zipfile.ZipFile(path, 'r')
    for files in zip_file.namelist():
        zip_file.extract(files, 'my_dir')
    
    zip_file.close()
    file_counter = sum([len(files) for r, d, files in os.walk('./my_dir/word/media/')])
    #print file_counter
    #for i in range(file_counter):
        #images.append([i, pygame.image.load('./my_dir/word/media/image' + str(i+1) + '.png')])
    #return images
    
#def get_docx_location(path):
   # """
   # Take the path of a docx file as argument, return the location of parts of text.
   # """
    #for i in 
    
#def get_cards(fl):
 #   with open(fl+'.obj', 'rb') as fp:   
##        deck = pickle.load(fp)
 #       return(deck) 
#doc = 'geography_study_ note.docx'

#get_docx_text(doc,"Test.obj")
#get_cards("Test.obj")

#for x in doc_list:
 #   print(x)
#print(get_docx_image(doc)) 
#import pygame
#pygame.init()
#game_window = pygame.display.set_mode((640,480))

#def redraw_game_window(image):
    #game_window.fill((0, 0, 0))
    #game_window.blit(image, (0,0))
    #pygame.display.update()

#images = get_docx_image('This_question.docx')
#image = images[0]
#exit_flag = False

#while not exit_flag:                    #
    #for event in pygame.event.get():    # check for any events
        #if event.type == pygame.QUIT:   # If user clicked close
            #exit_flag = True            # Flag that we are done so we exit this loop

    ##if event.type == pygame.mouse
    #redraw_game_window(image)                # window must be constantly redrawn - animation
    #pygame.time.delay(20)           
    
#pygame.quit()
