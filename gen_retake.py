from random import randint 
import names

#variables
global family_tree, creatures_lis, gender, opposable_thum, hair_colour, eye_colour, max_number_of_generations, ready_dad, ready_mom
eye_colour = ['blue', 'brown', 'green', 'yellow']
hair_colour = ['blond', 'ginger', 'brunette']
opposable_thum = ['yes', 'no']
gender = ['male', 'female']
creatures_lis = []
family_tree = []
max_number_of_generations = 10
ready_dad = []
ready_mom = []

#functions
class Node:
	def __init__(self, first_name, last_name):
		self.father = None
		self.mother = None
		self.child_1 = None
		self.child_2 = None
		self.name = last_name
		self.first_name = first_name
		self.eye_colour = None
		self.hair_colour = None
		self.number_legs = None
		self.opposable_thumbs = None
		self.height = None
		self.strength = None
		self.intelligence = None
		self.sex_appeal = None
		self.agility = None
		self.stamina = None
		self.agression = None
		self.gender = gender[randint(0,1)]
		self.number_of_children = 0
		self.gen = 0


class sebs_tree:
	def __init__(self):
		self.root = None

	@staticmethod
	def add_root_creature():
		creature = Node(names.get_first_name(), names.get_last_name())
		creature.eye_colour = eye_colour[randint(0,3)]
		creature.hair_colour = hair_colour[randint(0,2)]
		creature.number_legs = randint(0,6)
		creature.opposable_thumbs = opposable_thum[randint(0,1)]
		creature.height = randint(0, 10)
		creature.strength = randint(0, 10)
		creature.intelligence = randint(0, 10)
		creature.sex_appeal = randint(0, 10)
		creature.agility = randint(0, 10)
		creature.stamina = randint(0, 10)
		creature.agression = randint(0, 10)
		creature.gender = gender[randint(0,1)]
		creature.gen = 0
		creatures_lis.append(creature)

	@staticmethod
	def add_baby(father, mother):

		eye_colours = [father.eye_colour, mother.eye_colour]
		hair_colours = [father.hair_colour, mother.hair_colour]
		opposable_thumb = [father.opposable_thumbs, mother.opposable_thumbs]

		child = Node(names.get_first_name(), father.name) 
		child.father = father
		child.mother = mother
		child.eye_colour = eye_colours[randint(0, 1)]
		child.hair_colour = hair_colours[randint(0, 1)]
		child.opposable_thumbs = opposable_thumb[randint(0, 1)]
		child.gender = gender[randint(0, 1)]
		child.number_legs = round((father.number_legs + mother.number_legs)/2)
		child.height = round((father.height + mother.height)/2)
		child.strength = round((father.strength + mother.strength)/2)
		child.intelligence = round((father.intelligence + mother.intelligence)/2)
		child.sex_appeal = round((father.sex_appeal + mother.sex_appeal)/2)
		child.agility = round((father.agility + mother.agility)/2)
		child.stamina = round((father.stamina + mother.stamina)/2)
		child.agression = round((father.agression + mother.agression)/2)
		child.number_of_children = 0
		child.gen = father.gen + 1
		creatures_lis.append(child)

		if father.number_of_children == 0:
			father.child_1 = child
		else:
			father.child_2 = child

		if mother.number_of_children == 0:
			mother.child_1 = child
		else:
			mother.child_2 = child

		father.number_of_children += 1
		mother.number_of_children += 1
	
	@staticmethod
	def find_family_tree(creature):
		family_tree = []
		if creature.father != None:
			sebs_tree.find_family_tree(creature.father)
		else:
			sebs_tree.find_family(creature)
	
	@staticmethod
	def find_family(creature):
		if creature.mother != None:
			family_tree.append(creature.mother)
		family_tree.append(creature)
		if creature.child_1 != None and creature.child_2 != None:
			if creature.child_1.gender == 'male' and creature.child_2.gender == 'male':
				sebs_tree.find_family(creature.child_1)
				sebs_tree.find_family(creature.child_2)
			elif creature.child_1.gender == 'male' and creature.child_2.gender == 'female':
				family_tree.append(creature.child_2)
				sebs_tree.find_family(creature.child_1)
			elif creature.child_1.gender == 'female' and creature.child_2.gender == 'male':
				family_tree.append(creature.child_1)
				sebs_tree.find_family(creature.child_2)
			else:
				family_tree.append(creature.child_1)
				family_tree.append(creature.child_2)
				sebs_tree.print_tree(family_tree)
		elif creature.child_1 != None and creature.child_2 == None:
			if creature.child_1.gender == 'male':
				sebs_tree.find_family(creature.child_1)
			else:
				family_tree.append(creature.child_1)
				sebs_tree.print_tree(family_tree)
		elif creature.child_1 == None and creature.child_2 != None:
			if creature.child_2.gender == 'male':
				sebs_tree.find_family(creature.child_2)
			else:
				family_tree.append(creature.child_2)
				sebs_tree.print_tree(family_tree)
		else:
			sebs_tree.print_tree(family_tree)

	@staticmethod
	def print_tree(tree):	
		for creatures in tree:
			print('name: %s %s' %(creatures.first_name, creatures.name))
			print('generation: %s' %(creatures.gen))
			print('gender: %s' %(creatures.gender))
			if creatures.father != None and creatures.mother != None:
				print('father gen: %s' %(creatures.father.gen))
				print('mother gen: %s' %(creatures.mother.gen))
				print('father, mother: %s, %s' %(creatures.father.first_name, creatures.mother.first_name))
			else:
				print('root creature, has no parents')
			if creatures.child_1 != None and creatures.child_2 != None:
				print('childrens names: %s, %s' %(creatures.child_1.first_name, creatures.child_2.first_name))
			elif creatures.child_1 != None:
				print('child name: %s' %(creatures.child_1.first_name))
			elif creatures.child_2 != None:
				print('child name: %s' %(creatures.child_2.first_name))
			else:
				print('has no children')
			print('__________')
		print('length of family tree: %s creatures' %(len(family_tree)))
		    
	@staticmethod
	def get_attributes(creature):
		print('name: %s %s' %(creature.first_name, creature.name))
		print('gender: %s' %(creature.gender))
		print('eye colour: %s' %(creature.eye_colour))
		print('hair colour: %s' %(creature.hair_colour))
		print('opposable thumbs: %s' %(creature.opposable_thumbs))
		print('number of legs: %s' %(creature.number_legs))
		print('generation: %s' %(creature.gen))
		print('height: %s' %(creature.height))
		print('strength: %s' %(creature.strength))
		print('intelligence: %s' %(creature.intelligence))
		print('sex_appeal: %s' %(creature.sex_appeal))
		print('agility: %s' %(creature.agility))
		print('stamina: %s' %(creature.stamina))
		if creature.child_1 != None and creature.child_2 != None:
			print('childrens names: %s, %s' %(creature.child_1.first_name, creature.child_2.first_name))
		elif creature.child_1 != None:
			print('child name: %s' %(creature.child_1.first_name))
		elif creature.child_2 != None:
			print('child name: %s' %(creature.child_2.first_name))
		else:
			print('has no children')

	
#initiate 
for i in range(50):
	sebs_tree.add_root_creature()
for j in range(10):
	ready_dad = []
	ready_mom = []
	for creatures in creatures_lis:
			if creatures.gender == 'male' and creatures.gen == j and creatures.number_of_children < 2:
				ready_dad.append(creatures)
			elif creatures.gender == 'female' and creatures.gen == j and creatures.number_of_children < 2:
				ready_mom.append(creatures)
			else:
				continue
	while True:
		if len(ready_dad) == 0 or len(ready_mom) == 0:
			break
		
		else:
			dad = ready_dad[randint(0, len(ready_dad)-1)]
			mom = ready_mom[randint(0, len(ready_mom)-1)]
			sebs_tree.add_baby(dad, mom)
			if dad.number_of_children == 2:				
				ready_dad_1 = []
				for creature in ready_dad:
					if creature == dad:
						continue
					else:
						ready_dad_1.append(creature)
				ready_dad = []
				ready_dad = ready_dad_1
			
			if mom.number_of_children == 2:
				ready_mom_1 = []
				for creature in ready_mom:
					if creature == mom:
						continue
					else:
						ready_mom_1.append(creature)
				ready_mom = []
				ready_mom = ready_mom_1

cret = creatures_lis[randint(0, len(creatures_lis)-1)]
sebs_tree.find_family_tree(cret)
