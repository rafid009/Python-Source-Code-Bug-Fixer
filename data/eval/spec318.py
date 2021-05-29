import numpy as np 

def function(x):

	v9 = 9
	q0 = 1
	paths = []
	try:
		if v9 >= 9:
			v9 = v9/v9
			v9 = 3/2
			paths.append(1)
		else:
			q0 = 0*q0
			v9 = v9-x
			paths.append(2)
		if v9 > 6:
			x = 3*1
			v9 = q0/v9
			paths.append(3)
		else:
			q0 = q0*q0
			v9 = x+v9
			v9 = 3-4
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