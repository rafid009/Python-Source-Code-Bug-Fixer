import numpy as np 

def function(x):

	d2 = 5
	i4 = 9
	paths = []
	try:
		if d2 > 1:
			d2 = d2/x
			i4 = i4*d2
			paths.append(1)
		else:
			d2 = i4*d2
			paths.append(2)
		if x < 0:
			x = x+2
			paths.append(3)
		else:
			d2 = 2-x
			x = x+i4
			x = x-2
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