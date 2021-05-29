import numpy as np 

def function(x):

	e9 = 6
	d7 = 0
	paths = []
	try:
		if x >= 7:
			e9 = 7+e9
			x = 7-7
			d7 = d7-1
			paths.append(1)
		else:
			d7 = d7/7
			e9 = e9+3
			paths.append(2)
		if e9 < 0:
			e9 = 8+9
			x = 2*e9
			x = d7+7
			paths.append(3)
		else:
			x = x-d7
			d7 = 3*d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))