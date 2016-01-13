import os
import wx
import platform
from get_text import *

def correct(obj,lst):
    lst.append(obj)


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

#edit_page = resource_path('edit_page.png')
#colour_picker = resource_path('color_picker.png')
#open_file = resource_path('open_file.png')
#door_exit = resource_path('door_exit.png')

edit_page = 'edit_page.png'
colour_picker = 'color_picker.png'
open_file = 'open_file.png'
door_exit = 'door_exit.png'

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,500))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        deckmenu= wx.Menu()


        menuSave = filemenu.Append(wx.ID_SAVE, "&Save\tCtrl+S", "Save file")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open\tCtrl+O","Open a new file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About\tCtrl+A"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit\tCtrl+Q"," Terminate the program")
        menuDeck_Open = deckmenu.Append(wx.ID_ANY,"&Open\tCtrl+L","Open a deck of flashcards")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(deckmenu, "&Deck")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.        

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnDeck_Open, menuDeck_Open)
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        self.Show(False)
        self.dirname = ''

    def OnAbout(self,e):
        """ about program"""
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "It Does Stuff", "About FlashCard Maker", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
    def OnSave(self,e):
        """ Save a file"""
        # Save away the edited text
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            itcontains = self.control.GetValue()

            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename),'w')
            filehandle.write(itcontains)
            filehandle.close()
        dlg.Destroy()
    def OnDeck_Open(self,e):
        """Open Deck"""
        frame2.Show(True)
        self.Show(False)
    def OnExit(self,e):
        """Exit"""
        self.Destroy()
        frame2.Destroy()

class DeckWindow(wx.Frame):
    def __init__(self, parent, id, title):
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(500, 300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE| wx.TE_READONLY, pos = (80,60), size = (320,100))
        self.control.SetBackgroundColour("White")
        self.SetBackgroundColour("White")
        self.quote = wx.StaticText(self, label= "", pos = (60,60))
        vbox = wx.BoxSizer(wx.VERTICAL)
        if platform.system() == "Linux":
            filemenu= wx.Menu()   
            menuEdit = filemenu.Append(wx.ID_SAVE, "&Edit\tCtrl+E", "Edit file")
            menuOpen = filemenu.Append(wx.ID_OPEN, "&Open\tCtrl+O","Open a new file")
            menuColour = filemenu.Append(wx.ID_ABOUT, "&Colour\tCtrl+I"," Change Colour")
            menuExit = filemenu.Append(wx.ID_EXIT,"&Exit\tCtrl+Q"," Terminate the program")

            menuBar = wx.MenuBar()
            menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
            self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content. 

            self.Bind(wx.EVT_MENU, self.Edit, menuEdit)
            self.Bind(wx.EVT_MENU, self.Open, menuOpen)
            self.Bind(wx.EVT_MENU, self.color, menuColour)
            self.Bind(wx.EVT_MENU, self.Exit, menuExit)
            self.Bind(wx.EVT_CLOSE, self.Exit)
            

        else:
            self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
            self.toolbar.AddSimpleTool(1, wx.Image(edit_page, wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Edit', '')
            self.toolbar.AddSimpleTool(2, wx.Image(open_file, wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Open', '')
            self.toolbar.AddSimpleTool(3, wx.Image(colour_picker, wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Change Colour', '')
            self.toolbar.AddSimpleTool(4, wx.Image(door_exit, wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Exit', '')
            self.toolbar.Realize()
            
            self.Bind(wx.EVT_TOOL, self.Edit, id=1)
            self.Bind(wx.EVT_TOOL, self.Open, id=2)
            self.Bind(wx.EVT_TOOL, self.color, id=3)
            self.Bind(wx.EVT_TOOL, self.Exit, id=4)
            self.Bind(wx.EVT_CLOSE, self.Exit)

        self.Centre()


        # A button
        self.button =wx.Button(self, label="Previous", pos=(10, 80), size = (50,50))
        self.Bind(wx.EVT_BUTTON, self.Previous,self.button)
        self.button2 =wx.Button(self, label="Next", pos=(420, 80), size = (50,50))
        self.Bind(wx.EVT_BUTTON, self.Next,self.button2)
        self.button3 =wx.Button(self, label="Flip", pos=(220, 180), size = (50,50))
        self.Bind(wx.EVT_BUTTON, self.Flip,self.button3)

        topSizer        = wx.BoxSizer(wx.VERTICAL)
        gridSizer       = wx.GridSizer(rows=4, cols=2, hgap=5, vgap=5)
        titleSizer      = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer        = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer2       = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer3       = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(self.button, 0, wx.ALL, 0)
        btnSizer3.Add(self.button3, 0, wx.ALL, 0)
        btnSizer2.Add(self.button2, 0, wx.ALL, 0)
        
        self.Show(False)
        self.dirname = ''

        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(self.control, 0, wx.ALL|wx.EXPAND, 50)
        gridSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 0)
        gridSizer.Add(btnSizer2, 0, wx.ALL|wx.CENTER, 0)
        gridSizer.Add(btnSizer3, 0, wx.ALL|wx.CENTER, 0)
        topSizer.Add(gridSizer, 0, wx.ALL|wx.CENTER, 5)



        self.SetSizer(topSizer)
        topSizer.Fit(self)
        
    def Edit(self,event):
        """Open Editing window"""
        frame.Show(True)
        self.Show(False)
    def Open(self,event):
        """ Open a file"""
        try:
            self.dirname = ''
            dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'r')
                get_data(self.filename,self.filename)
                self.new_deck = get_cards(self.filename)
                f.close()
                self.x = 0
                (self.q,self.a) = data_to_display(self.new_deck,self.x)
                self.control.SetValue("Question:\n" +str(self.q))
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog( self, "Error: Selected file is not a valid format", "Error", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            
    def color(self,event):
        dlg = wx.ColourDialog(None)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            Colour = data.GetColour().GetAsString()
            dlg.Destroy()
            self.SetBackgroundColour(Colour)
            self.control.SetBackgroundColour(Colour)
            if platform.system() == "Linux":
                self.toolbar.SetBackgroundColour(Colour)
            self.Refresh()
        
    def Previous(self,event):
        #previous
        try:
            if self.x > 0:
                self.x -= 1
            (self.q,self.a) = data_to_display(self.new_deck,self.x)
            self.control.SetValue("Question:\n" +str(self.q))
        except:
            dlg = wx.MessageDialog( self, "Error: No Deck Selected", "Error", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            
    def Next(self,event):
        #Next
        try:
            if self.x < len(self.new_deck)-1:
                self.x += 1
            (self.q,self.a) = data_to_display(self.new_deck,self.x)
            self.control.SetValue("Question:\n" +str(self.q))
        except:
            dlg = wx.MessageDialog( self, "Error: No Deck Selected", "Error", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            
    def Flip(self,event):
        #Flip
        try:
            if self.control.GetValue() == ("Question:\n" +self.q):
                if type(self.a) == list:
                    temp = "Answer:\n"
                    for i in range(len(self.a)):
                        temp += self.a[i]+"\n"
                    self.control.SetValue(temp)
                else:
                    self.control.SetValue("Answer:\n" +str(self.a))
                self.button.SetLabel("Wrong")
                self.button2.SetLabel("Right")
                self.Refresh()
            else:
                self.control.SetValue("Question:\n" +str(self.q))
                self.button.SetLabel("Previous")
                self.button2.SetLabel("Next")
                self.Refresh()
        except:
            dlg = wx.MessageDialog( self, "Error: No Deck Selected", "Error", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            
    def Exit(self,event):
        """Exit"""
        self.Destroy()
        frame.Destroy()


app = wx.App(False)
frame = MainWindow(None, "Editing Window")
frame2 = DeckWindow(None, -1, "FlashCards")
frame2.Show()
app.MainLoop()
