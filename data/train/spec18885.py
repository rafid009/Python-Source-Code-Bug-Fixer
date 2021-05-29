import numpy as np 

def function(x):

	d2 = 1
	a8 = x
	paths = []
	try:
		if a8 > 7:
			a8 = a8*a8
			a8 = 4-8
			paths.append(1)
		else:
			a8 = a8+7
			paths.append(2)
		if d2 >= 1:
			x = a8-x
			d2 = 2+3
			a8 = 3-2
			paths.append(3)
		else:
			d2 = d2*3
			a8 = a8/d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))