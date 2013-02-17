import wx
import re
import time
import datetime
class Frame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title="SimpleReminder", size=(200,100))
		self.tc = wx.TextCtrl(self)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnPress, self.tc)
		self.Centre()
		self.Show(True)
		self.Raise()
	def OnPress(self, evt):
		data = self.tc.GetValue()
		currentdate = datetime.date.today()
		currentdatetime = datetime.datetime.now()
		currenttime = currentdatetime.time()
		m = re.match('(\d\d):(\d\d) (.+)', data)
		if m:
			destime = datetime.time(hour=int(m.group(1)), minute=int(m.group(2)))
			if destime>currenttime:
				seconds = (datetime.datetime.combine(currentdate,destime)-currentdatetime).seconds
			else:
				seconds = (datetime.datetime.combine(currentdate,destime)-currentdatetime+datetime.timedelta(days=1)).seconds
			self.Hide()
			time.sleep(seconds)
			notice = Notice(self)
			notice.setText(m.group(3))
			notice.Centre()
			notice.Show(True)
			notice.Raise()
		m = re.match('(\d+h)*(\d+m)*(\d+s)* (.+)', data)
		if m:
			self.Hide()
			seconds = 0
			if m.group(1):
				seconds += int(re.match('(\d+)', m.group(1)).group(1))*3600
			if m.group(2):
				seconds += int(re.match('(\d+)', m.group(2)).group(1))*60
			if m.group(3):
				seconds += int(re.match('(\d+)', m.group(3)).group(1))
			time.sleep(seconds)
			notice = Notice(self)
			notice.setText(m.group(4))
			notice.Centre()
			notice.Show(True)
			notice.Raise()

class Notice(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title="Notice", size=(200,100))
		self.st = wx.StaticText(self, wx.ID_ANY, label = "A", style=wx.ALIGN_CENTER)
		self.Bind(wx.EVT_CLOSE, self.OnClose, self)
	def setText(self, text):
		font = wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.ITALIC, wx.NORMAL)
		self.st.SetFont(font)
		self.st.SetLabel(text)
	def OnClose(self, evt):
		frame.Destroy()

app = wx.App(False)
frame = Frame(None)
app.MainLoop()