from PyQt5.QtWidgets import QMainWindow, QTabWidget, QAction, QLabel, QMenu
from PyQt5 import uic
from View.ViewConsole import ViewConsole
from View.ViewApp import ViewApp
from Control.Application import App
from Model.ZenControl import Zen
from Model.Motor import Motor
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}MainWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.createsComponentsAndPointers()
		self.setupWindowTabs()

	def setupWindowTabs(self):
		self.tabWidget = QTabWidget()
		self.setCentralWidget(self.tabWidget)
		self.tabWidget.addTab(self.appView, "App")
		self.tabWidget.addTab(self.consoleView, "Console")

	def createsComponentsAndPointers(self):
		zen = Zen()
		motor = Motor()

		# Components
		self.appView = ViewApp()
		self.consoleView = ViewConsole()
		self.app = App(zen, motor)

		# Pointers
		self.appView.consoleView = self.consoleView
		self.appView.app = self.app
		self.app.consoleView = self.consoleView
		self.app.appView = self.appView

		self.consoleView.showOnConsole("motor initialized", "green")
		self.consoleView.showOnConsole("successfully connected to ZEN", "green")
