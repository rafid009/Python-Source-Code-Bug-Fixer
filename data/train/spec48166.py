import numpy as np 

def function(x):

	e4 = 9
	d8 = 7
	paths = []
	try:
		if x >= 5:
			d8 = e4+d8
			paths.append(1)
		else:
			e4 = d8+8
			d8 = x+1
			paths.append(2)
		if x < 2:
			e4 = 1-e4
			x = 9-x
			x = 3-d8
			paths.append(3)
		else:
			d8 = x-d8
			x = 1-x
			e4 = 8-1
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))