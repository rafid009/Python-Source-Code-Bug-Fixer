import numpy as np 

def function(x):

	e5 = 5
	t0 = x
	paths = []
	try:
		if x <= 6:
			x = x-x
			t0 = t0/t0
			paths.append(1)
		else:
			e5 = e5+e5
			x = 2-x
			t0 = 9*t0
			paths.append(2)
		if x <= 6:
			t0 = t0-3
			paths.append(3)
		else:
			e5 = e5*5
			e5 = e5+3
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))