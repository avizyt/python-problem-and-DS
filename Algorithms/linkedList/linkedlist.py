class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None 

	def __repr__(self):
		return self.data



class LinkedList:
	def __init__(self, nodes=None):
		self.head = None
		if nodes is not None:
			node = Node(data=nodes.pop(0))
			self.head = node
			for ele in nodes:
				node.next = Node(data=ele)
				node = node.next

	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def __len__(self):
		if self.head is None:
			return Exception("List is empty")
		count = 0
		for node in self:
			count += 1
			node.next
		return count

	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		return "-> ".join(nodes)

	
	# add beginning of the linked list			
	def add_begin(self, node):
		node.next = self.head
		self.head = node

	# add end of the linked list	
	def add_end(self, node):
		if self.head in None:
			self.head = node
			return
		for curr_node in self:
			pass
		curr_node.next = node 


	def add_after(self, target_node_data, new_node):
		if self.head is None:
			raise Exception("List is empty")

		for node in self:
			if node.data == target_node_data:
				new_node.next = node.next
				node.next = new_node
				return
		raise Exception(f"Node with data {target_node_data} not found")



	def add_before(self, target_node_data, new_node):
		if self.head is None:
			raise Exception("List is Empty")

		if self.head.data == target_node_data:
			return self.add_begin(new_node)

		prev_node = self.head
		for node in self:
			if node.data == target_node_data:
				prev_node.next = new_node
				new_node.next = node
				return
			prev_node = node
		raise Exception(f"Node with data {target_node_data} not found")

	def remove_node(self, target_node_data):
		if self.head is None:
			raise Exception("List is empty")

		if self.head.data == target_node_data:
			self.head = self.head.next
			return

		prev_node = self.head
		for node in self:
			if node.data == target_node_data:
				prev_node.next = node.next
				return
			prev_node = node 

		raise Exception(f"Node with data {target_node_data} not found")

	def get_node(self, idx):
		if self.head is None:
			return Exception("List is empty")

		for num, node in enumerate(self):
			if num == idx:
				return node

		raise Exception(f"Node with data {idx} not found")

	def reverse(self):
		arr = []
		for node in self:
			arr.append(node)
			self.next
		return LinkedList(arr)

	



if __name__ == "__main__":
	str1 = "abcdef"
	arr = list(str1)
	llist = LinkedList(arr)
	print(llist)

	# llist.add_after("b", Node("B"))
	# print(llist)

	llist.add_before("b", Node("B"))
	print(llist)
	print(len(llist))

	llist.remove_node("B")
	print(llist)
	print(len(llist))

	print(llist.get_node(5))

	print(llist.reverse())

	# for num, node in enumerate(llist):
	# 	print(f"{num} : {node}")