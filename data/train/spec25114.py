import numpy as np 

def function(x):

	p3 = x
	h6 = 1
	paths = []
	try:
		if x < 2:
			h6 = 1+h6
			p3 = 3/p3
			paths.append(1)
		else:
			p3 = 8*p3
			h6 = h6-8
			paths.append(2)
		if p3 < 3:
			x = 3+x
			paths.append(3)
		else:
			h6 = 3-h6
			x = 7-x
			h6 = p3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))