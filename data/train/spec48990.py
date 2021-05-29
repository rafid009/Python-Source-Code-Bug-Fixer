import numpy as np 

def function(x):

	d1 = x
	d6 = x
	paths = []
	try:
		if x >= 6:
			x = 1/x
			paths.append(1)
		else:
			d6 = 7-d6
			paths.append(2)
		if d6 < 3:
			d1 = 2+x
			paths.append(3)
		else:
			d6 = 5-d6
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