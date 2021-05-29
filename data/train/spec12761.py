import numpy as np 

def function(x):

	e4 = x
	b1 = 8
	paths = []
	try:
		if x > 8:
			x = x-4
			paths.append(1)
		else:
			b1 = b1/9
			paths.append(2)
		if x < 2:
			x = 7*x
			e4 = b1/e4
			paths.append(3)
		else:
			x = x+4
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