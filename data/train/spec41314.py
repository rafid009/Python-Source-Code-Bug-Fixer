import numpy as np 

def function(x):

	x9 = x
	p3 = x
	paths = []
	try:
		if x >= 8:
			p3 = x+p3
			x = x9*8
			x = x-3
			paths.append(1)
		else:
			x9 = p3*x9
			paths.append(2)
		if x < 3:
			x9 = x9+x
			paths.append(3)
		else:
			x = 3-x
			p3 = 2+p3
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))