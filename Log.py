import os
import sys
import logging

class Log(object):

	logInstance = None
	formatter = None
	fileHandler = None
	streamHandler = None

	@staticmethod
	def initLogConf():
		Log.formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
		#Log.fileHandler = logging.FileHandler(logFile)
		#Log.fileHandler.setFormatter(Log.formatter)
		Log.streamHandler = logging.StreamHandler(sys.stdout)
		Log.streamHandler.setFormatter(Log.formatter)


	@staticmethod
	def getLogger():
		if Log.logInstance is None:
			Log.logInstance = logging.getLogger()
			Log.initLogConf()
			Log.logInstance.setLevel(logging.NOTSET)
			#Log.logInstance.addHandler(Log.fileHandler)
			Log.logInstance.addHandler(Log.streamHandler)
		return Log.logInstance

	@staticmethod
	def d(msg):
		f = sys._getframe(1)
		filename = os.path.split(f.f_code.co_filename)[-1]
		lineno = f.f_lineno
		Log.getLogger().debug("[%s:%d] : %s" % (filename, lineno, msg))

	@staticmethod
	def i(msg):
		f = sys._getframe(1)
		filename = os.path.split(f.f_code.co_filename)[-1]
		lineno = f.f_lineno
		Log.getLogger().info("[%s:%d] : %s" % (filename, lineno, msg))

	@staticmethod
	def w(msg):
		f = sys._getframe(1)
		filename = os.path.split(f.f_code.co_filename)[-1]
		lineno = f.f_lineno
		Log.getLogger().warn("[%s:%d] : %s" % (filename, lineno, msg))

	@staticmethod
	def e(msg):
		f = sys._getframe(1)
		filename = os.path.split(f.f_code.co_filename)[-1]
		lineno = f.f_lineno
		Log.getLogger().error("[%s:%d] : %s" % (filename, lineno, msg))




