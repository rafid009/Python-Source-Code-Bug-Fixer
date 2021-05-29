import numpy as np 

def function(x):

	d0 = 6
	i4 = x
	paths = []
	try:
		if x > 1:
			d0 = 0*6
			x = x/3
			x = 6*x
			paths.append(1)
		else:
			x = 1-6
			x = 9+i4
			x = 3/x
			paths.append(2)
		if x > 0:
			x = x-3
			paths.append(3)
		else:
			i4 = x*7
			i4 = i4-d0
			i4 = i4-i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))