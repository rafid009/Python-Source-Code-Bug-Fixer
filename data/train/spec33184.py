import numpy as np 

def function(x):

	d8 = x
	e0 = 3
	paths = []
	try:
		if d8 < 3:
			e0 = 3-1
			paths.append(1)
		else:
			d8 = e0*x
			paths.append(2)
		if e0 > 7:
			d8 = d8*3
			e0 = e0-e0
			paths.append(3)
		else:
			e0 = 8-e0
			d8 = 0*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))