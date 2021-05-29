import numpy as np 

def function(x):

	p7 = 1
	h7 = 8
	paths = []
	try:
		if x <= 3:
			h7 = h7-h7
			paths.append(1)
		else:
			p7 = p7/4
			paths.append(2)
		if p7 > 1:
			h7 = 0*5
			p7 = 5*x
			paths.append(3)
		else:
			h7 = h7/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))