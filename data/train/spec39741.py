import numpy as np 

def function(x):

	i0 = x
	d9 = x
	x = 7
	paths = []
	try:
		if i0 > 3:
			i0 = i0-x
			x = i0*x
			d9 = x/5
			paths.append(1)
		else:
			i0 = 7-d9
			i0 = x/x
			d9 = d9+3
			paths.append(2)
		if d9 > 2:
			x = 9/3
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))