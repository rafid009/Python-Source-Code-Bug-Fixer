import numpy as np 

def function(x):

	p2 = x
	b3 = 4
	paths = []
	try:
		if x < 2:
			b3 = b3-2
			x = b3*x
			b3 = b3+p2
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x >= 6:
			x = 9+x
			paths.append(3)
		else:
			b3 = b3*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))