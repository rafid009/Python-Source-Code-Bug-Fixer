import numpy as np 

def function(x):

	e4 = x
	n0 = x
	x = 4
	paths = []
	try:
		if n0 > 9:
			n0 = n0+3
			e4 = e4/2
			paths.append(1)
		else:
			x = n0*e4
			n0 = n0*4
			paths.append(2)
		if n0 >= 3:
			e4 = e4+e4
			x = x/3
			paths.append(3)
		else:
			n0 = n0*e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		n0 = e4**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))