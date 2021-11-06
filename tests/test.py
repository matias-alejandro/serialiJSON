import unittest

class TestsSerialiJSON(unittest.TestCase):

	def setUp(self):
		from serialiJSON import BaseSerializable

		class Item(BaseSerializable):
			def __init__(self, itemName, isAlive):
				self.itemName = itemName
				self.isAliva = isAlive

		class Pet(BaseSerializable):
			def __init__(self, name, age, favItems):
				self.name = name
				self.age = age
				self.favItems = favItems

		class Human(BaseSerializable):
			def __init__(self, name, age, pets):
				self.name = name
				self.age = age
				self.pets = pets

		self.item = Item("snow ball", False)
		self.pet = Pet("Cat", 12, [Item("snow ball", False),Item("tree", True)])
		self.pets = [
			Pet("Cat", 12, [Item("snow ball", False),Item("tree", True)]), 
			Pet("Dog", 4, [Item("snow ball", False),Item("tree", True)])
		]
		self.human = Human("name", 90, self.pets)

	def testOneLevelObject(self):
		json = '{"itemName": "snow ball", "isAliva": false}'
		self.assertEqual(self.item.toJson(), json)

	def testTwoLevelObject(self):
		json = '{"name": "Cat", "age": 12, "favItems": [{"itemName": "snow ball", "isAliva": false}, {"itemName": "tree", "isAliva": true}]}'
		self.assertEqual(self.pet.toJson(), json)

	def testThreeLevelObject(self):
		json = '{"name": "name", "age": 90, "pets": [{"name": "Cat", "age": 12, "favItems": [{"itemName": "snow ball", "isAliva": false}, {"itemName": "tree", "isAliva": true}]}, {"name": "Dog", "age": 4, "favItems": [{"itemName": "snow ball", "isAliva": false}, {"itemName": "tree", "isAliva": true}]}]}'
		self.assertEqual(self.human.toJson(), json)

if __name__ == '__main__':
	unittest.main()
