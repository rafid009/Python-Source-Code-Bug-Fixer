import numpy as np 

def function(x):

	n1 = x
	n4 = x
	paths = []
	try:
		if n4 < 0:
			x = 1/x
			x = x/x
			paths.append(1)
		else:
			n1 = n1-9
			paths.append(2)
		if x >= 0:
			x = x*x
			x = x-9
			paths.append(3)
		else:
			x = x+x
			n4 = n4-7
			n4 = n4-5
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