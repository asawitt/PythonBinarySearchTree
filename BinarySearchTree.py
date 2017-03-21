from queue import Queue

class BSTNode:
	def __init__(self,value):
		self.value = value
		self.left = self.right = None
class BST:
	def __init__(self):
		self.root = None
	def insert(self,value):
		if not self.root:
			self.root = BSTNode(value)
		else:
			cur = self.root
			prev = None
			while cur is not None:
				prev = cur
				if value > cur.value:
					cur = cur.right
					if cur is None:
						prev.right = BSTNode(value)
				else:
					cur = cur.left
					if cur is None:
						prev.left = BSTNode(value)
	def find(self,value):
		cur = self.root
		while cur is not None and cur.value != value:
			if value > cur.value:
				cur = cur.right
			else:
				cur = cur.left
			if cur is None:
				return False
		return True
	def delete(self,value):
		cur = self.root
		prev = None
		right_child = False
		left_child = False
		while cur is not None and cur.value != value:
			if value > cur.value:
				prev = cur
				cur = cur.right
				right_child = True; left_child = False
			elif value < cur.value:
				prev = cur
				cur = cur.left
				right_child = False; left_child = True

		if cur is not None:
		#3 cases for the found Node (could be slightly optimized with nested if-statements, but this reduces readability)
			#CASE 1: No children
			if cur.right is None and cur.left is None:
				if prev is not None:
					if right_child:
						prev.right = None
					else:
						prev.left = None
				#Deleting root node with no children
				else:
					self.root = None
			#CASE 2: 1 Child 
			elif bool(cur.right) != bool(cur.left):
				child_node = cur.right if cur.right is not None else cur.left
				if prev is not None:
					if right_child:
						prev.right = child_node
					else:
						prev.left = child_node
				#Deleting root node with 1 child
				else: 
					self.root = child_node
			#CASE 3: 2 Children
			elif cur.left is not None and cur.right is not None:
				#find minimum value in right subtree
				cur2 = cur.right
				while cur2.left is not None:
					cur2 = cur2.left
				if prev is not None:
					prev.left = cur2
				#Deleting root node with 2 children
				else:
					self.root = cur2
				cur2.left = cur.left
	#returns a list of values sorted from least to greatest. Can be used as BST-Sort O(n log n) avg, O(n^2) worst-case
	def flatten(self):
		a = []
		prev = None
		cur = self.root
		if cur is None:
			return []
		def traverse(node):
			if node.left is not None:
				traverse(node.left)
			a.append(node.value)
			if node.right is not None:
				traverse(node.right)
		traverse(self.root)
		return a
	#Using Breadth-First traversal prints out a list of lists in which each sublist represents a layer of the tree
	def printTree(self):
		a = []
		q = Queue()
		q.put(self.root)
		num_at_depth = 1
		num_so_far = 0
		found_at_depth = False
		while not q.empty():
			node = q.get()
			if node is None:
				num_so_far += 1
			else:
				print(" " + str(node.value),end="")
				num_so_far += 1
				found_at_depth = True
			if num_so_far == num_at_depth:
				if not found_at_depth:
					break
				num_so_far = 0
				num_at_depth *= 2
				found_at_depth = False
				print("")
			if node == None:
				q.put(None)
				q.put(None)
				continue
			q.put(node.left)
			q.put(node.right)
		print("")