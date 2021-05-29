import numpy as np 

def function(x):

	h7 = x
	n0 = x
	paths = []
	try:
		if x > 4:
			h7 = n0+9
			paths.append(1)
		else:
			x = 5/4
			n0 = 5/n0
			paths.append(2)
		if x <= 7:
			n0 = n0+5
			h7 = 4*7
			paths.append(3)
		else:
			h7 = 3+5
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))