class animal(object):
	def __init__(self, numberOfLegs, color, presenceOfFur, weight, length, species, name):
		self.numberOfLegs = numberOfLegs
		self.color = color
		self.presenceOfFur = presenceOfFur
		self.weight= weight
		self.length = length
		self.species = species
		self.name = name

	def sleep(self):
		print self.name + ", the " + self.species + ", is sleeping"

	def breathe(self):
		print self.name + ", the " + self.species + ", is breathing"

	def walk(self):
		print self.name + ", the " + self.species + ", is walking"

dog = animal(4,"brown","true",24,36,"canine","Roofus")
cat = animal(4,"grey","true",7,27,"feline","Mischief")

dog.sleep()
dog.breathe()
dog.walk()

cat.sleep()
cat.breathe()
cat.walk()