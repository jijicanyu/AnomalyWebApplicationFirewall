class Record(object):
	""" Record in profile """

	def __init__(self, expected_method, url, expected_code, expected_size):
		self.url = url
		self.expected_method = expected_method
		self.expected_code = expected_code
		self.expected_size = expected_size
		self.connection = []
		self.location = {}
		self.param = {}
		self.accessDay = {}
		self.accessTime = {}
		self.accessAgent = {}
		self.requestURL = {}


	def __eq__(self, other):
		""" Test if records are equal """
		return self.url == other.url

	def getIP(self):
		""" Get IP-Address """
		return self.ip

	def getURL(self):
		""" Get URL """
		return self.url