import numpy as np 

def function(x):

	u0 = x
	v6 = 2
	paths = []
	try:
		if x >= 1:
			x = x/6
			x = v6-8
			x = x+2
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x >= 2:
			u0 = 4*3
			x = 0*x
			paths.append(3)
		else:
			u0 = 4-u0
			v6 = v6+v6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))