import json, math

class dbCalculatorObject:
	def __init__(self, data=None):
		if data:
			with open(data, 'r') as dataFile:
				self.data = json.load(dataFile)
		else:
			self.data = None

	def powerDiff(self, mult):
		mult = float(mult)
		if mult == 0:
			return 0
		else:
			db = 10 * math.log(mult, 10)
			return db

	def deciDiff(self, db):
		db = float(db)
		power = 10 ** (db/10)
		return power

	def processData(self, directData=None):
		if (not self.data) and (not directData):
			return 0

		if directData:
			self.data=directData

		keys = self.data.keys()
		computed = {}
		for key in keys:
			if ("db" in self.data[key]):
				computed[key] = f"{self.deciDiff(self.data[key].replace('db', '')):.4f}x"
			elif (self.data[key][-1] == "x"):
				computed[key] = f"{self.powerDiff(self.data[key].replace('x', '')):.4f}db"
			else:
				computed[key] = f'Invalid input data "{self.data[key]}"'

		with open("ProcessedData.json", 'w') as f:
			json.dump(computed, f, indent=4)

		return 1


def main():
	dbCalculator = dbCalculatorObject(data="data.json")

	dbCalculator.processData()

	# result = dbCalculator.powerDiff(2)
	# print(f"Result: {result:.4f}")

	# result = dbCalculator.deciDiff(3)
	# print(f"Result: {result:.4f}")

if __name__ == '__main__':
	main()