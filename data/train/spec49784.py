import numpy as np 

def function(x):

	d7 = 7
	i0 = 2
	paths = []
	try:
		if x <= 0:
			d7 = 8/d7
			paths.append(1)
		else:
			x = 9-i0
			d7 = d7-x
			paths.append(2)
		if x > 4:
			d7 = 0-i0
			x = 3*i0
			paths.append(3)
		else:
			d7 = d7*i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))