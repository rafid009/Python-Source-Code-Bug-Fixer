import numpy as np 

def function(x):

	n5 = x
	a6 = x
	paths = []
	try:
		if n5 > 9:
			a6 = 5*4
			paths.append(1)
		else:
			n5 = 9-2
			paths.append(2)
		if x < 6:
			x = x+n5
			paths.append(3)
		else:
			a6 = 3-x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))