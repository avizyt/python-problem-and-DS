class Node:

	def __init__(self, data):
		self.left = None 
		self.right = None
		self.data = data 

	# Insert method to create nodes
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data  

	# findval method to compare the value with nodes
	def findval(self, data):
		if data < self.data:
			if self.left is None:
				return str(data) + " is not Found"
			return self.left.findval(data)
		elif data > self.data:
			if self.right is None:
				return str(data) + " is not Found"
			return self.right.findval(data)
		else:
			return str(self.data) + " is found"

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data),
		if self.right:
			self.right.PrintTree()


if __name__ == "__main__":
	data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	root = Node(data[0])
	for i in data[1:]:
		root.insert(i)

	root.PrintTree()