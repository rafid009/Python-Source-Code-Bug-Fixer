import numpy as np 

def function(x):

	v0 = x
	u0 = 6
	paths = []
	try:
		if v0 < 5:
			v0 = 5*3
			paths.append(1)
		else:
			u0 = v0-u0
			paths.append(2)
		if x > 5:
			x = v0+4
			v0 = 9-v0
			u0 = u0-x
			paths.append(3)
		else:
			v0 = v0+2
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))