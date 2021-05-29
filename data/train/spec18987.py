import numpy as np 

def function(x):

	v0 = 3
	z5 = 6
	paths = []
	try:
		if z5 > 4:
			x = z5+x
			v0 = x+v0
			v0 = 1+z5
			paths.append(1)
		else:
			x = z5*2
			v0 = 4/v0
			paths.append(2)
		if v0 <= 7:
			v0 = v0-v0
			paths.append(3)
		else:
			v0 = z5/v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))