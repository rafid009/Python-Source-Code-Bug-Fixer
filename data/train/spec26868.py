import numpy as np 

def function(x):

	e6 = x
	e4 = 3
	paths = []
	try:
		if x >= 7:
			e4 = e4-5
			paths.append(1)
		else:
			e4 = e4+e6
			paths.append(2)
		if e4 >= 4:
			x = e6/3
			e6 = e6-2
			e6 = 2*5
			paths.append(3)
		else:
			e4 = e4*e6
			x = 5-x
			e6 = 0-x
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