import numpy as np 

def function(x):

	x0 = x
	t8 = x
	paths = []
	try:
		if t8 < 9:
			x = x-7
			x0 = 2/1
			x0 = x0/x0
			paths.append(1)
		else:
			x0 = t8*t8
			paths.append(2)
		if x0 <= 0:
			t8 = t8/8
			x = t8*6
			paths.append(3)
		else:
			x0 = 3*x0
			x0 = t8+6
			x0 = 9+x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))