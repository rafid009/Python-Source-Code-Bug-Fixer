import numpy as np 

def function(x):

	x5 = x
	n2 = 9
	paths = []
	try:
		if n2 >= 9:
			n2 = 9+n2
			x5 = n2/x5
			paths.append(1)
		else:
			x5 = 3*x5
			x5 = x5+x
			paths.append(2)
		if n2 > 2:
			n2 = 1-n2
			x = 3/x5
			paths.append(3)
		else:
			n2 = n2-9
			x = x-1
			x = x+x
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