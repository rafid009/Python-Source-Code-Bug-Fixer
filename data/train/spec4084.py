import numpy as np 

def function(x):

	v7 = x
	x0 = x
	paths = []
	try:
		if x <= 3:
			x = x*x0
			x0 = x0*3
			paths.append(1)
		else:
			v7 = x*9
			x0 = x0*8
			paths.append(2)
		if x0 > 8:
			x = v7-x
			x0 = 9-x0
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		v7 = x0**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))