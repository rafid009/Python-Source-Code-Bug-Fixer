import numpy as np 

def function(x):

	v1 = x
	x4 = x
	paths = []
	try:
		if v1 >= 4:
			x4 = x4-v1
			v1 = v1*6
			paths.append(1)
		else:
			v1 = 5*v1
			paths.append(2)
		if v1 < 6:
			x4 = x4+2
			paths.append(3)
		else:
			v1 = 0*v1
			x4 = x-v1
			x = v1-8
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))