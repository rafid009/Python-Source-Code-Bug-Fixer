import numpy as np 

def function(x):

	x0 = x
	v1 = x
	paths = []
	try:
		if x <= 2:
			v1 = 5*v1
			x0 = x0*8
			paths.append(1)
		else:
			x0 = 5-x0
			paths.append(2)
		if x >= 9:
			x = 4-9
			x0 = 4/7
			x = x-4
			paths.append(3)
		else:
			x = v1/x0
			v1 = 1-3
			x0 = 6+x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))