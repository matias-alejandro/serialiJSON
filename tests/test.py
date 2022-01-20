import unittest
import json

class TestsSerialiJSON(unittest.TestCase):

	def setUp(self):
		from serialiJSON import BaseSerializable

		class Item(BaseSerializable):
			def __init__(self, itemName, isAlive):
				self.itemName = itemName
				self.isAlive = isAlive

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
		jsonResult = '{"itemName": "snow ball", "isAlive": false}'
		self.assertEqual(json.loads(self.item.toJson()), json.loads(jsonResult))

	def testTwoLevelObject(self):
		jsonResult = '{"name": "Cat", "age": 12, "favItems": [{"itemName": "snow ball", "isAlive": false}, {"itemName": "tree", "isAlive": true}]}'
		self.assertEqual(json.loads(self.pet.toJson()), json.loads(jsonResult))

	def testThreeLevelObject(self):
		jsonResult = '{"name": "name", "age": 90, "pets": [{"name": "Cat", "age": 12, "favItems": [{"itemName": "snow ball", "isAlive": false}, {"itemName": "tree", "isAlive": true}]}, {"name": "Dog", "age": 4, "favItems": [{"itemName": "snow ball", "isAlive": false}, {"itemName": "tree", "isAlive": true}]}]}'
		self.assertEqual(json.loads(self.human.toJson()), json.loads(jsonResult))

if __name__ == '__main__':
	unittest.main()
