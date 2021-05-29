import numpy as np 

def function(x):

	x1 = 5
	b6 = 2
	paths = []
	try:
		if x < 5:
			x1 = 9*x1
			paths.append(1)
		else:
			x = b6+x
			paths.append(2)
		if x1 > 9:
			x1 = x/4
			x1 = b6/x1
			paths.append(3)
		else:
			b6 = 1/b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))