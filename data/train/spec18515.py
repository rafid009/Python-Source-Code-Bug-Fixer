import numpy as np 

def function(x):

	n4 = x
	x9 = x
	x = x
	paths = []
	try:
		if x > 2:
			x = 7/x
			n4 = x9+9
			paths.append(1)
		else:
			n4 = 3+x
			paths.append(2)
		if x9 <= 8:
			x9 = x9+8
			x9 = x9/5
			paths.append(3)
		else:
			n4 = n4*6
			x = 6*x
			x = x/n4
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