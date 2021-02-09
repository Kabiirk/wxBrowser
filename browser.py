import wx
from wx import html2

class MyApp(wx.App):
    def __init__(self):
        super().__init__()
        self.InitBrowser()

    def InitBrowser(self):
        webbrowser = WebFrame(None, "WxBrowser", pos=(100, 100))
        webbrowser.Show()

class WebFrame(wx.Frame):
    def __init__(self, title, parent, pos):
        super().__init__(parent, title=title, pos=pos)

        # Create Variables
        # Browser
        self._browser = html2.WebView.New(self)
        self._browser.LoadURL("https://kabiirk.github.io/")

        # Navbar
        self._navbar = NavBar(self, self._browser)

        # Sizers to define layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._navbar, 0, wx.EXPAND)
        sizer.Add(self._browser, 1, wx.EXPAND)
        self.SetSizer(sizer)
        # The Above lines define layout as
        #  _________________________________________
        # | (<-) (->) | https://kabiirk.github.io   |
        # |___________|_____________________________|
        # |              THE WEBPAGE                |
        # |                                         |
        # |                                         |
        # |                                         |
        # |_________________________________________|


class NavBar(wx.Panel):
    # added browser Parameter so that Navbar could communcate with the Browser
    def __init__(self, parent, browser):
        super().__init__(parent)

        self._browser = browser
        self._url = wx.TextCtrl(parent=self, style=wx.TE_PROCESS_ENTER)
        self._url.SetHint("Enter URL to load Page")

        # Buttons
        back = wx.Button(self, style=wx.BU_EXACTFIT)
        back.Bitmap = wx.ArtProvider.BetBitmap(wx.ART_GO_BACK, wx.ART_TOOLBAR)

        fwd = wx.Button(self, style=wx.BU_EXACTFIT)
        fwd.Bitmap = wx.ArtProvider.BetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.add(back, 0, wx.ALL, 5)
        sizer.add(fwd, 0, wx.ALL, 5)
        sizer.add(self._url, 0, wx.ALL, 5)

        self.SetSizer(sizer)

    def OnEnter(self, event):
        self.browser.LoadURL(self._url.Value)

    def GoBack(self, event):
        event.Enable(self.browser.CanGoBack())
        self._browser.GoBack()

    def GoFwd(self, event):
        event.Enable(self.browser.CanGoForward())
        self._browser.GoForward()

if __name__=="main":
    app = MyApp()
    app.MainLoop()