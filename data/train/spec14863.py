import numpy as np 

def function(x):

	d8 = 3
	i9 = x
	paths = []
	try:
		if i9 > 6:
			x = i9/x
			d8 = d8/i9
			paths.append(1)
		else:
			x = i9/9
			d8 = x*d8
			d8 = 6-3
			paths.append(2)
		if d8 <= 0:
			i9 = i9*4
			x = x-d8
			i9 = 5-i9
			paths.append(3)
		else:
			i9 = 0-i9
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