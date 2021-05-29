import numpy as np 

def function(x):

	h9 = x
	p1 = 4
	paths = []
	try:
		if h9 <= 2:
			p1 = p1*p1
			x = p1-h9
			paths.append(1)
		else:
			h9 = 4*p1
			h9 = h9-x
			p1 = p1+8
			paths.append(2)
		if p1 <= 1:
			x = p1+0
			p1 = h9+p1
			h9 = 5-6
			paths.append(3)
		else:
			x = x*9
			p1 = h9+8
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))