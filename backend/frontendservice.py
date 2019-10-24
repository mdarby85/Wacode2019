from model import DB

class frontendservice:

	def __init__(self):
		self.db = DB()

	def checkIfValidUser(self, number, password):
		user = self.db.getUser(number)
		if user == None:
			return False
		print(user)
		if user["password"] == password:
			return user
		return False

	def getUser(self, number):
		return self.db.getUser(number)

	def saveUser(self, number, firstname, lastname, password, currentBalance, paymentinfo=None):
		self.db.insertUser(number, firstname, lastname, password, currentBalance, paymentinfo)







m = frontendservice()

m.saveUser("********", "****", "*****", "Andy", 0)

print(m.checkIfValidUser("********", "11"))
