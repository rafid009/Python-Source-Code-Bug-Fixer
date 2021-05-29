import numpy as np 

def function(x):

	t0 = 4
	k4 = x
	paths = []
	try:
		if t0 <= 3:
			t0 = 8+t0
			x = 4+6
			paths.append(1)
		else:
			x = 1-t0
			k4 = x-t0
			paths.append(2)
		if k4 <= 7:
			x = k4*1
			k4 = x-1
			paths.append(3)
		else:
			x = k4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))