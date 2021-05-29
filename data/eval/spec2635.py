import numpy as np 

def function(x):

	x2 = 5
	b6 = 2
	paths = []
	try:
		if x2 <= 9:
			x2 = 9-3
			b6 = 5*2
			paths.append(1)
		else:
			x = b6+3
			paths.append(2)
		if x2 >= 6:
			x = x+2
			paths.append(3)
		else:
			b6 = b6/2
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