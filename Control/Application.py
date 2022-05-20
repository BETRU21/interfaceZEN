from PyQt5.QtCore import pyqtSignal, QThread, QMutex, QObject
from tools.ThreadWorker import Worker
import os

class App(QObject):
	threadSignalFinished = pyqtSignal(int)
	def __init__(self, zen, motor):
		super().__init__()
		self.connectSignals()
		self.zen = zen
		self.motor = motor
		self.mutex = QMutex()
		self.actionWorker = Worker(self.action)
		self.actionThread = QThread()
		self.createThreads()

	# Public functions

	def initializeExperiment(self):
		params = self.appView.getParams()
		try:
			if params.path == "":
				raise ValueError("folder path is empty")
			if params.name == "":
				raise ValueError("file name is empty")
			self.experiment = self.zen.getExperiment(params.exp)
			self.startThread()
		except Exception as error:
			self.appView.createErrorDialogs(error)
			self.consoleView.showOnConsole(str(error), "red")

	def action(self):
		params = self.appView.getParams()
		self.setMotorParams(params.acc, params.speed)
		self.zen.setFolder(params.path)
		self.zen.setFileType(params.ext)
		if params.nbImage == 1:
			img = self.zen.getImage(params.exp)
			self.zen.saveImage(img, params.name)
		else:
			for rank in range(params.nbImage):
				img = self.zen.getImage(params.exp)
				name = params.name + str(rank)
				self.zen.saveImage(img, name)
				self.motor.moveBy(params.step)
		self.threadSignalFinished.emit(0)

	def setMotorParams(self, acc, speed):
		parameter = self.motor.getVelocityParamsLimits()
		acceleration = (acc/100)*parameter.acc
		speed = (speed/100)*parameter.speed
		self.motor.setVelocityParams(acceleration, speed)


	# Non-Public functions

	def connectSignals(self):
		self.threadSignalFinished.connect(self.killThread)

	# Thread Section

	def createThreads(self):
		self.actionWorker.moveToThread(self.actionThread)
		self.actionThread.started.connect(self.actionWorker.run)

	def startThread(self):
		threadRunning = self.actionThread.isRunning()
		if threadRunning == False:
				self.consoleView.showOnConsole("Begin the acquisition", "green")
				self.actionThread.start()
		else:
			self.consoleView.showOnConsole("Acquisition already in progress", "red")
			self.appView.createErrorDialogs("Acquisition already in progress, please wait")

	def killThread(self, ID):
		if ID == 0:
			self.actionThread.quit()
			self.consoleView.showOnConsole("Acquisition finished", "green")
		else:
			pass
