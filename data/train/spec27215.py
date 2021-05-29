import numpy as np 

def function(x):

	x9 = x
	b8 = x
	paths = []
	try:
		if b8 >= 7:
			x9 = 9-x
			b8 = b8/9
			paths.append(1)
		else:
			x = 2/x
			b8 = x9-x9
			paths.append(2)
		if b8 < 9:
			x9 = x9-x9
			b8 = 7+b8
			x = x-3
			paths.append(3)
		else:
			x9 = x9*x9
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