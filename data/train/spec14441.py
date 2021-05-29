import numpy as np 

def function(x):

	v3 = 9
	d9 = x
	paths = []
	try:
		if v3 < 6:
			d9 = d9+d9
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x >= 8:
			v3 = 7/d9
			paths.append(3)
		else:
			d9 = v3+d9
			x = x-1
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