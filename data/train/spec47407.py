import numpy as np 

def function(x):

	v0 = 1
	x5 = 3
	paths = []
	try:
		if x < 4:
			v0 = v0+4
			paths.append(1)
		else:
			x5 = v0/1
			x = v0/x
			x5 = 0-x
			paths.append(2)
		if x5 <= 4:
			x5 = 7+x5
			v0 = v0*4
			paths.append(3)
		else:
			v0 = v0/x5
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