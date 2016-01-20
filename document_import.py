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


#def get_docx_image(path):
    #"""
    #Take the path of a docx file as argument, return the image in pygame.
    #"""
    #import zipfile
    #import os
    ##import pygame
    ##images = []
    #zip_file = zipfile.ZipFile(path, 'r')
    #for files in zip_file.namelist():
        #zip_file.extract(files, 'my_dir')
    
    #zip_file.close()
    #file_counter = sum([len(files) for r, d, files in os.walk('./my_dir/word/media/')])
    ##print file_counter
    ##for i in range(file_counter):
        ##images.append([i, pygame.image.load('./my_dir/word/media/image' + str(i+1) + '.png')])
    ##return images
    
