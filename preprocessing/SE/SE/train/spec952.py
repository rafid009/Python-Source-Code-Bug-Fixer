import numpy as np 

def function(x):

	h9 = 2
	p0 = x
	paths = []
	try:
		if p0 >= 3:
			p0 = h9*p0
			h9 = h9/p0
			x = x-6
			paths.append(1)
		else:
			x = p0/2
			p0 = p0+5
			h9 = h9*6
			paths.append(2)
		if h9 >= 5:
			x = p0+x
			x = h9/4
			paths.append(3)
		else:
			h9 = 1+h9
			p0 = 3-7
			h9 = x/5
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		h9 = p0**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))