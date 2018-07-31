import  wx
isok = False
global _global_dict
_global_dict = 0
cancelClick = 0
okclick = 0
class myFrame(wx.Frame):
    tmpClick = cancelClick
    def __init__(self,parent,id=wx.ID_ANY,title="",pos=wx.DefaultPosition,size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name='My Frame'):
        super(myFrame,self).__init__(parent,id,title,pos,size,style,name)
        self.Panel = wx.Panel(self)
        self.Panel.SetBackgroundColour(wx.WHITE)
        self.Button = wx.Button(self.Panel,label='好',pos=[100,100])
        self.ButtonId = self.Button.GetId()
        self.Button.Bind(wx.EVT_BUTTON,self.ShowMessage,self.Button)
        self.Button.Bind(wx.EVT_CLOSE, self.ShowMessage, self.Button)
        self.Button = wx.Button(self.Panel, label='不好', pos=[260, 100])
        self.ButtonId = self.Button.GetId()
        self.Bind(wx.EVT_BUTTON,self.NoShowMessage,self.Button)
        self.Text =  wx.StaticText(self.Panel,-1,"小姐姐,已经观察你很久了\r\n做我女朋友好不好",pos=[100,20])
        font = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.Text.SetFont(font)
    def ShowMessage(self,event):
        global okclick
        if okclick == 0:
            msg = wx.MessageBox('三号目标已拿下','提示',wx.OK|wx.ICON_INFORMATION)
            okclick = okclick + 1
            self.Close()
    def NoShowMessage(self,event):
        global _global_dict
        _global_dict=_global_dict+1
        if _global_dict == 1:
         msg = wx.MessageBox('车子给你','提示',wx.OK|wx.ICON_INFORMATION)
        elif _global_dict == 2:
            msg = wx.MessageBox('房子给你', '提示', wx.OK | wx.ICON_INFORMATION)
        elif _global_dict == 3:
            msg = wx.MessageBox('票子给你', '提示', wx.OK | wx.ICON_INFORMATION)
        elif _global_dict == 4:
            msg = wx.MessageBox('我长的帅', '提示', wx.OK | wx.ICON_INFORMATION)
        elif _global_dict == 4:
            msg = wx.MessageBox('会吹牛逼', '提示', wx.OK | wx.ICON_INFORMATION)
        else:
            _global_dict = 0;
            msg = wx.MessageBox('别点了快约起来', '提示', wx.OK | wx.ICON_INFORMATION)
    def OnClose(self,event):
        if okclick == 1:
            myFrame.Destroy(self)
        else:
            r = wx.MessageBox('关闭就等于默认同意了', '提示', wx.OK | wx.ICON_INFORMATION)
class MyApp(wx.App):
    def OnInit(self):
        self.Frame = myFrame(None,title="Hello,Kitty",pos=wx.DefaultPosition,size=[500,300])
        self.Frame.SetMaxSize([500,300])
        self.Frame.Center()
        self.Frame.Bind(wx.EVT_CLOSE, self.Frame.OnClose)
        self.SetTopWindow(self.Frame)
        self.Frame.Show()
        return True
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

