import plugin
from .screens.clock_screen import ClockScreen

class ClockPlugin(plugin.PluginObject):

	def get_main_screen():
		return ClockScreen()

	def get_screens():
		return [ClockScreen()]