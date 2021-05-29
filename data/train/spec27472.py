import numpy as np 

def function(x):

	n4 = 4
	v6 = 6
	paths = []
	try:
		if n4 > 2:
			v6 = x-v6
			x = x-0
			paths.append(1)
		else:
			n4 = 6/6
			paths.append(2)
		if n4 > 3:
			v6 = v6+8
			paths.append(3)
		else:
			x = n4-x
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