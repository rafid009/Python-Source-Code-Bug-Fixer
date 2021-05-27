import numpy as np 

def function(x):

	u1 = x
	v1 = 9
	paths = []
	try:
		if x < 6:
			x = x-7
			paths.append(1)
		else:
			v1 = 7/v1
			u1 = v1-v1
			paths.append(2)
		if v1 < 3:
			v1 = 8+v1
			paths.append(3)
		else:
			u1 = u1-0
			v1 = v1-1
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