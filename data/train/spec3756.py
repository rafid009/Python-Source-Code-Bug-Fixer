import numpy as np 

def function(x):

	r9 = x
	v7 = x
	paths = []
	try:
		if x < 0:
			r9 = v7*9
			paths.append(1)
		else:
			r9 = 4*r9
			r9 = x/r9
			paths.append(2)
		if x >= 6:
			x = 7*r9
			r9 = r9-6
			x = r9/x
			paths.append(3)
		else:
			v7 = v7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))