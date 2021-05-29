import numpy as np 

def function(x):

	d4 = x
	u6 = 9
	paths = []
	try:
		if d4 >= 5:
			d4 = d4*d4
			paths.append(1)
		else:
			x = 8-0
			paths.append(2)
		if x >= 4:
			x = 2/x
			u6 = 5+u6
			paths.append(3)
		else:
			d4 = 9-d4
			d4 = 2*d4
			d4 = d4-u6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))