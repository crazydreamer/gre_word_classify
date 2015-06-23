#coding: utf8

import wx
import random

wordlist = []

class wordListManager:
    def __init__(self, filename = 'list_in.txt'):
        self.filename = filename
        self.wordlist = []
        self.readFile()
    def readFile(self):
        print self.filename
        f = open(self.filename, 'r')
        # 想用dict，考虑内存，用list
        dlist = []
        while 1:
            s = f.readline()
            if not s: break
            s = s.split('\t')
            if len(s) < 3: continue
            word, wordmeaning = s[1], s[2]
            dlist.append([word, wordmeaning])
        self.wordlist = dlist
        print 'read %d words finished' % len(dlist)
    def getWordMean(self, word):
        for k in self.wordlist:
            if k[0]==word: return k[1]
        

class CommonFrame(wx.Frame):
    def __init__(self):
        self.initFrameControls();
        self.wordListManager = wordListManager()
        self.curWords = []
        self.unusedWords = self.wordListManager.wordlist[:]
        self.usedWords = []
    def initFrameControls(self):
        wx.Frame.__init__(self, None, -1, 'commframe', 
                size=(1200, 800),
                style = wx.MINIMIZE_BOX  |wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        (70,50, 640, 720)
        
        text1 = wx.TextCtrl(panel, -1, 
                                size=(400, 600), pos = (30,30), style=wx.TE_MULTILINE)
        self.stext1 = wx.StaticText(panel, -1, '_hahahaha',
                                size=(800, 600), pos = (440, 30), style=wx.TE_MULTILINE)
        #switch
        btn1 = wx.Button(panel, -1, 'switch words', pos = (30, 640), size=(100,40))
        btn2 = wx.Button(panel, -1, 'save to file', pos = (150, 640), size=(100,40))
        btn3 = wx.Button(panel, -1, 'load file', pos = (270, 640), size=(100,40))
        
        btn1.Bind(wx.EVT_BUTTON, self.switchWords)
        btn2.Bind(wx.EVT_BUTTON, self.saveFile)
        btn3.Bind(wx.EVT_BUTTON, self.loadFile)    
        
        self.Bind(wx.EVT_CHAR, self.fastKeyDown)

    def switchWords(self, event):
        pass
        dlist = []
        self.curWords = []
        for k in range(30):
            u = random.randint(0, len(self.unusedWords))
            uw = self.unusedWords[u]
            #self.unusedWords.remove(uw)
            self.curWords.append(uw)
        sstr = ""
        for k in self.curWords:
            sstr += (k[0]+' '+k[1])
        self.stext1.SetLabel(sstr)
    def saveFile(self, event):
        pass
    def loadFile(self, event):
        print 'load file'
    def fastKeyDown(self, event):
        print 'keydown', event.KeyCode
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    CommonFrame().Show()
    app.MainLoop()  