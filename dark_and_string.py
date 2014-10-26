class Stack:
	'''This is the Stack datastructure with the basic operetions.'''

	def __init__(self):
		#Initializes a empty stack
		self.items = []

	def isEmpty(self):
		#Return True if the stack is empty
		return self.items == []

	def push(self,item):
		#Inserts the item into the stack
		self.items.append(item)

	def pop(self):
		#Retruns the top item i.e the last item from the stack after removing it
		return self.items.pop(0)
	def size(self):
		#Returns the size
		return len(self.items)

	def insert(self,item,i=0):
		#insert item at ith position.
		return self.items.insert(i,item)

def evaluate(infix):
	"Perform the postfix evaluation."
	operandStack = Stack()	
	opstack = Stack()
	infix = list(infix)
	print infix
	operand = "0123456789"
	operator = "-+*/%"
	for token in infix:
		if token in operand:
			operandStack.push(int(token))
		elif token in operator :
			opstack.push(token)
	if operandStack.size()>1:
		while not opstack.isEmpty():
			op = opstack.pop()
			op1 = operandStack.pop()
			op2 = operandStack.pop()
			result = doMath(op,op1,op2)
			operandStack.insert(result)
	if operandStack.isEmpty():
		return '-1'
	else:
		return operandStack.pop()

def doMath(op,op1,op2):
	"Return the result of the operation between operand1 and operand2."
	if op == '%':
		return op1 % op2
	elif op == '*':
		return op1 * op2
	elif op == '/':
		return op1/op2
	elif op == '+':
		return op1 + op2
	else:
		return op1 - op2
t = input()
for i in xrange(t):
	string = raw_input()
	print evaluate(string)
	print "\n"