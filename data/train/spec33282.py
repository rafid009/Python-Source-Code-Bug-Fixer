import numpy as np 

def function(x):

	t0 = 3
	x3 = x
	paths = []
	try:
		if x3 <= 6:
			t0 = 0+t0
			paths.append(1)
		else:
			x3 = 9/x3
			x3 = x3-0
			paths.append(2)
		if x <= 2:
			x3 = x3-9
			x3 = x-t0
			x3 = x-2
			paths.append(3)
		else:
			x = x/4
			x = x-0
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