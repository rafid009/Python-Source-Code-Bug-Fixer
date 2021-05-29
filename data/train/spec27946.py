import numpy as np 

def function(x):

	d6 = x
	k4 = 4
	paths = []
	try:
		if x >= 9:
			d6 = d6-2
			paths.append(1)
		else:
			d6 = 5*d6
			k4 = k4+4
			paths.append(2)
		if x >= 1:
			x = 0-x
			d6 = x*d6
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))