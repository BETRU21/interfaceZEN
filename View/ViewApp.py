from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, QThread, QMutex
from PyQt5 import uic
from tools.ThreadWorker import Worker
from typing import NamedTuple
import os

applicationPath = os.path.abspath("")

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}AppWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class Params(NamedTuple):
	name: str = None
	path: str = None
	ext: str = None
	step: int = None
	acc: int = None
	speed: int = None
	exp: str = None
	nbImage: int = None


class ViewApp(QWidget, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.connectWidgets()

	def connectWidgets(self):
		self.pb_folderPath.clicked.connect(self.setFolderPath)
		self.pb_start.clicked.connect(self.startButtonNotConnectedError)
		self.cmb_step.currentIndexChanged.connect(self.setNbImage)

	def connectExternalFunction(self):
		self.pb_start.clicked.disconnect()
		self.pb_start.clicked.connect(self.app.initializeExperiment)

	def getParams(self):
		name = self.le_name.text()
		path = self.le_path.text()
		ext = self.cmb_ext.currentText()
		step = int(self.cmb_step.currentText())
		acc = self.sb_acc.value()
		speed = self.sb_speed.value()
		exp = self.le_experiment.text()
		nbImage = self.sb_image.value()
		return Params(name, path, ext, step, acc, speed, exp, nbImage)

	def setNbImage(self):
		step = int(self.cmb_step.currentText())
		print(step)
		nbImage = 180/step
		print(nbImage)
		self.sb_image.setValue(nbImage)

	def setFolderPath(self):
		folderPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		if folderPath != "":
			self.le_path.setText(folderPath)
		self.connectExternalFunction()

	def createErrorDialogs(self, error):
		error = str(error)
		self.warningDialog = QMessageBox()
		self.warningDialog.setIcon(QMessageBox.Information)
		self.warningDialog.setText(f"{error}")
		self.warningDialog.setWindowTitle("Warning")
		self.warningDialog.setStandardButtons(QMessageBox.Ok)
		self.warningDialog.exec_()

	def startButtonNotConnectedError(self):
		self.createErrorDialogs("folder path is empty")
