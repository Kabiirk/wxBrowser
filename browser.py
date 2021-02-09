import wx

class MyApp(wx.App):
    def __init__(self):
        super().__init__()
        self.InitBrowser()

    def InitBrowser(self):
        pass

class WebFrame(wx.Frame):
    def __init__(self, title, parent, pos):
        super().__init__(parent, title=title, pos=pos)

class NavBar(wx.Panel):
    def __init__(self, parent, browser):
        super().__init__(parent)

    def OnEnter(self, event):
        pass

    def GoBack(self, event):
        pass

    def GoFwd(self, event):
        pass

if __name__=="main":
    app = MyApp()
    app.MainLoop()