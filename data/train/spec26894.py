import numpy as np 

def function(x):

	p6 = x
	h1 = 6
	paths = []
	try:
		if h1 > 6:
			p6 = p6+7
			paths.append(1)
		else:
			h1 = 8/x
			p6 = 8/p6
			paths.append(2)
		if x >= 0:
			h1 = 4+0
			p6 = 1+7
			x = p6/x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))