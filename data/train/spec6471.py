import numpy as np 

def function(x):

	v1 = x
	v2 = 8
	paths = []
	try:
		if x < 3:
			v1 = v1-3
			x = x+x
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if v2 < 0:
			v1 = v1*v1
			v2 = 0-7
			paths.append(3)
		else:
			v1 = v1*2
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