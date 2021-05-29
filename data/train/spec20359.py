import numpy as np 

def function(x):

	d1 = 1
	e7 = x
	paths = []
	try:
		if x >= 9:
			x = x*x
			paths.append(1)
		else:
			e7 = 8/x
			paths.append(2)
		if e7 > 2:
			e7 = d1+5
			paths.append(3)
		else:
			x = x-8
			e7 = e7-3
			d1 = d1+e7
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))