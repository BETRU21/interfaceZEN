import win32com.client
import os

class Zen:
	def __init__(self):
		self.zenObject = getZenObject()
		self.extention = ".tif"
		self.path = None

	def getZenObject(self):
		try:
			return win32com.client.GetActiveObject("Zeiss.Micro.Scripting.ZenWrapperLM")
		except Exception as e:
			raise RuntimeError(str(e))
	def getExperiment(self, name):
		if type(name) is not str:
			raise
		experiment = name + ".czexp"
		try:
			exp = Zen.Acquisition.Experiments.GetByName(experiment)
			return exp
		except Exception as e:
			raise ValueError(str(e))

	def getImage(self, experiment):
		img = Zen.Acquisition.Execute(experiment)
		return img

	def saveImage(self, image, name):
		try:
			path = self.path + name + self.extention
			image.Save_2(path)
		except Exception as e:
			raise ValueError(str(e))

	def setFolder(self, path):
		if type(path) is not str:
			raise TypeError("path parameter must be str")
		self.path = path

	def setFileType(self, extention):
		if type(extention) is not str:
			raise TypeError("extention parameter must be str")
		self.extention = extention
