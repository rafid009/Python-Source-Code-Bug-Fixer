import numpy as np 

def function(x):

	v2 = 0
	f3 = 3
	paths = []
	try:
		if v2 > 1:
			x = v2/4
			f3 = f3-3
			paths.append(1)
		else:
			v2 = v2/6
			paths.append(2)
		if v2 >= 6:
			x = 3*x
			x = x-6
			paths.append(3)
		else:
			f3 = 9*f3
			f3 = f3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))