import numpy as np 

def function(x):

	y6 = 5
	v8 = 0
	paths = []
	try:
		if v8 <= 1:
			y6 = 4/y6
			paths.append(1)
		else:
			x = 4+4
			y6 = x+y6
			paths.append(2)
		if v8 <= 2:
			v8 = 6*v8
			paths.append(3)
		else:
			v8 = 0*v8
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