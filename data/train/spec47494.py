import numpy as np 

def function(x):

	d9 = 6
	i4 = 7
	paths = []
	try:
		if i4 >= 6:
			x = i4*x
			d9 = d9-d9
			x = x+8
			paths.append(1)
		else:
			i4 = 0*6
			d9 = 3-4
			paths.append(2)
		if d9 > 1:
			d9 = d9/7
			paths.append(3)
		else:
			i4 = d9*6
			d9 = d9+3
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