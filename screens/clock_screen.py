from datetime import datetime, timedelta
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty

import locale

locale.setlocale(locale.LC_ALL, "")

class ClockScreen(Screen):
	time_clock = StringProperty("")
	date_clock = StringProperty("")

	def __init__(self, **kwargs):
		super(ClockScreen, self).__init__(**kwargs)
		self.now = datetime.now()
		Clock.schedule_interval(self.update_clock, 1)
		self.date_clock = str(self.now.strftime("%A %d %B"))
		self.time_clock = str(self.now.strftime("%H:%M:%S"))

	def update_clock(self, *args):
		self.now = self.now + timedelta(seconds = 1)
		self.date_clock = str(self.now.strftime("%A %d %B"))
		self.time_clock = str(self.now.strftime("%H:%M:%S"))
	pass