try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
import pickle

def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'   # formatting for docx
    PARA = WORD_NAMESPACE + 'p'                                                         # formatting for paragraphs
    TEXT = WORD_NAMESPACE + 't'                                                         # formatting for text
    document = zipfile.ZipFile(path)                                                    # the unzipped document path
    xml_content = document.read('word/document.xml')                                    # location of the primary xml document
    document.close()                                                                    # closes the document
    tree = XML(xml_content)                                                             # splits the xl into a tree

    paragraphs = []                                                                     # a list of the paragraphs
    for paragraph in tree.getiterator(PARA):                                            # for every new paragraph in the tree
        texts = [node.text                                                              # the text is the text node in the tree
                 for node in paragraph.getiterator(TEXT)                                # 
                 if node.text]                                                          # if the node is text, add it to the text list
        if texts:                                                                       # if a text is found,
            paragraphs.append(''.join(texts))                                           # add it to the paragraphs list
    #return('\n\n'.join(paragraphs))
    return(paragraphs)                                                                  # return the paragra
