# __author__ = Aditya Soni

class Node:
	'''
	Simple Node Class Equivalent to C's struct node
	'''
	def __init__(self, value , next):
		
		self.value = value
		self.next = next

	def __str__(self):
		return 'Node\'s Value [' + str(self.value) + ']'

class linkedList(object):
	'''
	Simple Linked List Class Implementing Basic functionalities	
	'''
	#__size = 0 # error it's common for all linked lists instances... Fixed That

	def __init__(self, inputs = []):
		
		self.first = None
		self.last = None
		self.insert_items = inputs
		self.__size = 0

	def search(self, x, return_prev = False):

		node, prev = self.first, Node(None, None)
		while node and node.value is not x :
			
			prev = node
			node = node.next
		
		if return_prev:
			return node, prev
		return node

	def insert_at_once(self):

		for i in self.insert_items:
			self.insert(i)

	def insert(self, x):

		self.__size += 1
		if self.first is None:
			# 1st Insertion
			self.first = Node(x, None)
			self.last = self.first

		elif self.last == self.first:
			#2nd Insertion, but we already have first(head) and the last check(else one) similar..(kind of redundant and can be merged with 3rd check)
			self.last = Node(x,None)
			self.first.next = self.last

		else:
			#After 2nd its not an edge cae any more
			current = Node(x,None)
			self.last.next = current
			self.last = current

	def delete(self, x):

		assert self.__size is not 0, 'Can\'t Delete, Linked List is Empty, Try Inserting Nodes...'
		node, prev = self.search(x, True)
		# print('In Delete')
		# print(node,prev)

		if node is None:
			#print('Node with Value {} Not Found\t'.format(x))
			return 'Not Found';

		else:

			self.__size -= 1

			if prev.value is None:
				temp = node.next
				self.first = temp
				del temp
				return 'Deleting Head Node'

			elif node.value is self.last.value:
				prev.next, self.last = None, prev
				del prev
				return 'Deleting Last Node'
			else:
				prev.next = node.next
				del node
				return 'Deleting Any Intermediate Node'

	def reverse(self):

		#print('Reversing The Linked List')
		self.last = self.first
		currNode, nextNode, prevNode = self.first, None, None
		
		while currNode is not None:

			nextNode = currNode.next
			currNode.next = prevNode
			prevNode = currNode # in this specific order the last 2 statements should be; think abt it..
			currNode = nextNode

		self.first = prevNode

	def reverse_order(self, head = None):

		if head is None:
			return
		
		self.reverse_order(head.next)
		print(head.value, end = " ")

	def detect_loops(self, index = False):

		#Floyds Detection Method or use a hash table(dict()) nd check for re-entry of the same memory (collisions)...

		slow_ptr, fast_ptr, temp_last = self.first, self.first, self.last
		temp_last.next, length = self.first.next.next, 0
		
		while(slow_ptr and fast_ptr and fast_ptr.next):

			slow_ptr = slow_ptr.next
			fast_ptr = fast_ptr.next.next

			if slow_ptr is fast_ptr:
				if index:
					index = True
					break
				else:
					return 'Loop Exists'
		if index:
			slow_ptr = self.first
			while slow_ptr != fast_ptr:
				fast_ptr = fast_ptr.next
				slow_ptr = slow_ptr.next
				length += 1
			print('Looping at {} and length of loop {}'.format(slow_ptr, length+1))
			return 'Loop Detected'

		return 'No Loop Detected'

	def remove_dups(self):

		# Well it's easy as we can easily skip the connections via node.next.next like thing
		s = set() # buffer
		#s.add(self.first.value)
		head, prev = self.first, None

		while head is not None:
			if head.value not in s:
				s.add(head.value)
				prev = head
				head = head.next
			else:
				prev.next = head.next
				head = head.next
		return s

	def delete_middle_element(self):

		mid = self.__size // 2
		temp, prev = self.first, None
		for _ in range(mid):
			prev = temp
			temp = temp.next
		prev.next = temp.next
		
	def __add__(self, l2):

		#code duplicates, better to create a sample func...
		#dender func's Awesome pYthon!!
		
		temp_1, temp_2 = self.first, l2.first
		num_1, num_2 = 0, 0
		for i in range(self.__size):
			 num_1 += temp_1.value*(10**i)
			 num_2 += temp_2.value*(10**i)
			 temp_1 = temp_1.next
			 temp_2 = temp_2.next

		print('In Reverse Order', num_1+num_2)
		self.reverse()
		l2.reverse()
		temp_1, temp_2 = self.first, l2.first
		num_1, num_2 = 0, 0
		for i in range(self.__size):
			num_1 += temp_1.value*(10**(self.__size - i - 1))
			num_2 += temp_2.value*(10**(self.__size - i - 1))
			temp_1 = temp_1.next
			temp_2 = temp_2.next
		print('In Forward Order', num_1+num_2)
		self.reverse()
		l2.reverse()
	
	def __str__(self):
		## Controllig print(l)
		
		if self.first is not None:
			current = self.first
			out = 'Linked List[' + str(current.value) + '-->'
			while current.next is not None:
				current = current.next
				out += str(current.value) +'-->'
			return out +']'
		return 'LinkedList ()'

	@property
	def top(self):
		return 'Current Top Node\'s Value is ' + str(self.last.value)
	
	@property
	def size(self):
		return '#### Current Size is ' + str(self.__size)

	@property
	def clear(self):

		print('Deleting Everything')
		self.__init__()
		self.__size = 0

if __name__ == '__main__':

	l, l2 = linkedList([7,1,6]), linkedList([5,9,2])
	l.insert_at_once()
	l2.insert_at_once()
	print(l,l2)
	l + l2
	l.reverse()
	print(l)
	l2.reverse()
	print(l2)
# 	#l.clear
	print(l.size)
# 	l.delete_middle_element()
	print(l.remove_dups())
	print(l.delete(4))
	print(l2.delete(2))
	print(l2)
	#l.reverse_order(l.first)
	#l.reverse_order(l.first)
	# print(l.search(1, True))
	# print(l.search(2, True))	
	# l.reverse()
	# print(l)
	# print(l.search(1, True))
	# print(l.search(2, True))
	#print(l.detect_loops(index = True))


def outer():

	x = 10
	def inner():
		print(x)
	return inner

foo = outer()
foo()
