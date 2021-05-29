import numpy as np 

def function(x):

	p2 = 1
	x3 = 1
	paths = []
	try:
		if p2 < 0:
			x3 = 2*x3
			paths.append(1)
		else:
			x = 7/x
			x = x-2
			p2 = x-p2
			paths.append(2)
		if x < 2:
			x3 = x3/x
			paths.append(3)
		else:
			x3 = 1+3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))