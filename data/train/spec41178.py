import numpy as np 

def function(x):

	d8 = 6
	x6 = x
	paths = []
	try:
		if d8 < 2:
			x6 = x6-9
			x = 1-7
			paths.append(1)
		else:
			x = x-x6
			d8 = d8*d8
			d8 = d8-1
			paths.append(2)
		if x >= 4:
			d8 = x6-1
			paths.append(3)
		else:
			x = x-x6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))