import numpy as np 

def function(x):

	b1 = x
	h9 = 8
	paths = []
	try:
		if b1 < 1:
			x = x+1
			x = x+6
			paths.append(1)
		else:
			b1 = b1/b1
			x = x+4
			paths.append(2)
		if x >= 1:
			h9 = x*b1
			h9 = 1+1
			h9 = h9-4
			paths.append(3)
		else:
			h9 = 6*b1
			x = 7*x
			x = x-5
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		b1 = h9**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))