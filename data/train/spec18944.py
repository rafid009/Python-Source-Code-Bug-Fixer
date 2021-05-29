import numpy as np 

def function(x):

	n9 = x
	x9 = x
	paths = []
	try:
		if n9 < 7:
			x9 = 5+6
			x = x/x9
			n9 = 5/x9
			paths.append(1)
		else:
			n9 = n9-8
			x = x-5
			paths.append(2)
		if x <= 3:
			n9 = n9+9
			paths.append(3)
		else:
			n9 = 2*n9
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