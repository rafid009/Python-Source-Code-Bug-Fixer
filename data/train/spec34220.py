import numpy as np 

def function(x):

	e7 = 4
	n6 = 9
	paths = []
	try:
		if e7 <= 0:
			x = 3-x
			n6 = 4+n6
			n6 = n6-7
			paths.append(1)
		else:
			e7 = 9*5
			paths.append(2)
		if e7 > 2:
			e7 = 9-n6
			paths.append(3)
		else:
			x = x+1
			n6 = n6/7
			e7 = 9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))